import tkinter as tk
from tkinter import *
from tkinter import ttk
import urllib.request, urllib.parse , urllib.error
import json


class CurrencyConverter():
    def __init__(self):
        pass

    # connect to derver
    def convertToServer(self):
        fhand = urllib.request.urlopen("https://api.exchangerate-api.com/v4/latest/USD").read()
        data = json.loads(fhand)
        return data

    # func to convert
    def convert(self):
        try:
            _from = self._select_from.get()
            _from_count = int(self.inp_from.get())
            _to = self._select_to.get()
            _json = self.convertToServer()
            currency_value_from = _json["rates"][_from]
            USD_value = (1 / currency_value_from) * _from_count
            currency_value_to = _json["rates"][_to] * USD_value
            self.tv_result.set(str(currency_value_to))
            # show label to
            self.lbl_to_resulr.config(text=self.tv_result.get())
            self.lbl_to_resulr.pack(fill="y")
            # lbl error
            self.tv_result.set("")
            self.lbl_error.config(text=self.tv_result.get())
            print(currency_value_to)
        except:
            # lbl error
            # lbl_error.config(text="pleas enter all values")
            self.tv_result.set("pleas enter all values")
            self.lbl_error.config(text=self.tv_result.get())
            self.lbl_error.pack(fill="y")
    def run(self):
        f = Tk()
        f.title(" Currency Converter in Python")
        f.geometry("350x250+400+300")

        # tv result
        tv_result = StringVar()
        tv_result.set("")
        # create label to
        lbl_to_resulr = Label(f, text=tv_result.get(), anchor="w")
        lbl_to_resulr.config(fg="red")

        # tv title
        tv_title = StringVar()
        _json = self.convertToServer()
        tv_title.set(_json["date"])

        # tv error
        tv_error = StringVar()
        tv_error.set("pleas enter all values")
        lbl_error = Label(f, text=tv_error.get(), anchor="w")
        # lbl_error = Label(f, text="pleas enter all values", anchor="w")

        # list of cons
        data = self.convertToServer()
        arr_cons = list(data["rates"].keys())

        lbl_hand = Label(f, text="Today is " + tv_title.get(), anchor="w")
        lbl_hand.config(fg="red")
        lbl_hand.pack(side="top", padx=80, pady=15)

        # label from
        lbl_from = Label(f, text="From: ", anchor="w")
        lbl_from.pack(fill="y")

        # select cons from
        _from_n = tk.StringVar()
        _select_from = ttk.Combobox(f, width=27, textvariable=_from_n)
        _select_from['values'] = arr_cons
        _select_from.pack()

        # input from
        inp_from = Entry(f)
        inp_from.pack()

        # label to
        lbl_to = Label(f, text="To", anchor="w")
        lbl_to.pack(fill="y")

        # select cons to
        _to_n = tk.StringVar()
        _select_to = ttk.Combobox(f, width=27, textvariable=_to_n)
        _select_to['values'] = arr_cons
        _select_to.pack(expand=YES)

        # button to convert
        btn = Button(f, text="Convert", command=self.convert)
        btn.config(bg="red")
        btn.pack(side="bottom", padx=80, pady=12)

        f.mainloop()






