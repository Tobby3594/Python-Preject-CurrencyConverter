import tkinter as tk
from tkinter import *
from tkinter import ttk
import urllib.request, urllib.parse , urllib.error
import json


class CurrencyConverter():
    def __init__(self):
        self.f = Tk()
        self.f.title(" Currency Converter in Python")
        self.f.geometry("350x250+400+300")

        # tv result
        self.tv_result = StringVar()
        self.tv_result.set("")
        # create label to
        self.lbl_to_resulr = Label(self.f, text=self.tv_result.get(), anchor="w")
        self.lbl_to_resulr.config(fg="red")

        # tv title
        self.tv_title = StringVar()
        _json = self.convertToServer()
        self.tv_title.set(_json["date"])

        # tv error
        self.tv_error = StringVar()
        self.tv_error.set("pleas enter all values")
        self.lbl_error = Label(self.f, text=self.tv_error.get(), anchor="w")
        # lbl_error = Label(f, text="pleas enter all values", anchor="w")

        # list of cons
        data = self.convertToServer()
        arr_cons = list(data["rates"].keys())

        self.lbl_hand = Label(self.f, text="Today is " + self.tv_title.get(), anchor="w")
        self.lbl_hand.config(fg="red")
        self.lbl_hand.pack(side="top", padx=80, pady=15)

        # label from
        self.lbl_from = Label(self.f, text="From: ", anchor="w")
        self.lbl_from.pack(fill="y")

        # select cons from
        self._from_n = tk.StringVar()
        self._select_from = ttk.Combobox(self.f, width=27, textvariable=self._from_n)
        self._select_from['values'] = arr_cons
        self._select_from.pack()

        # input from
        self.inp_from = Entry(self.f)
        self.inp_from.pack()

        # label to
        self.lbl_to = Label(self.f, text="To", anchor="w")
        self.lbl_to.pack(fill="y")

        # select cons to
        self._to_n = tk.StringVar()
        self._select_to = ttk.Combobox(self.f, width=27, textvariable=self._to_n)
        self._select_to['values'] = arr_cons
        self._select_to.pack(expand=YES)

        # button to convert
        self.btn = Button(self.f, text="Convert", command=self.convert)
        self.btn.config(bg="red")
        self.btn.pack(side="bottom", padx=80, pady=12)

    # connect to derver
    def convertToServer(self):
        fhand = urllib.request.urlopen("https://api.exchangerate-api.com/v4/latest/USD").read()
        data = json.loads(fhand)
        return data

    # func to convert
    def convert(self):
        try:
            #Conversion calculation
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
            self.tv_error.set("")
            self.lbl_error.config(text=self.tv_error.get())
            print(currency_value_to)
        except:
            #reset the lbl_to_result
            self.tv_result.set("")
            self.lbl_to_resulr.config(text=self.tv_result.get())
            self.lbl_to_resulr.pack(fill="y")
            # lbl error
            self.tv_error.set("pleas enter all values")
            self.lbl_error.config(text=self.tv_error.get())
            self.lbl_error.pack(fill="y")

    #Launch the app
    def run(self):
        self.f.mainloop()






