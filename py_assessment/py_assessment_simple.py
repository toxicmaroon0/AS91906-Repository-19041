#Tkinter bits
import tkinter as tk
#import tkinter.font as font
#import tkmacosx as tkm
from tkinter import messagebox

#Other things
import math
import numpy as np
from py_tooltip import *
from py_numeric_parser_class import *

#Create objects / instanses / CONSTANTS
nsp = NumericStringParser()
RESIZE_YN = 0

#State Class and subroutines
class Calculator():
    def __init__(self) -> None:
        #Variables
        row = 1
        col = 0
        self.is_final = 0
        
        # Buttons
        buttons = [
            "AC", "±", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "Quit", "0", ".", "="
        ]

        
        for button in buttons:
            btn = tk.Button(background, text=button, font=("Helvetica", 16), width=1, height=1)
            btn.grid(row=row, column=col, sticky="NSEW")
            btn.bind("<Button-1>", self.button_click)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
                
        # Entry Field
        self.entry_field = tk.Entry(root,font=("Helvetica", 20), justify="right",width=20)
        self.entry_field.grid(row=0, column=0,sticky="NSEW")
        
        for x in range(0,4):
            if x <= 1:
                root.rowconfigure(x, weight=1)
                continue
            if x == 0:
                root.columnconfigure(x, weight=1)
                continue
            if x <= 4:
                background.rowconfigure(x, weight=1)
                continue
            if x <= 3:
                background.columnconfigure(x, weight=1)
                continue

        #Button Tooltips
        #CreateToolTip(,'Exponential notation')
        
        #Lists
        self.operators = ["+", "-", "÷", "×", "±", "%", "="]

    def button_click(self, event):
        button = event.widget
        text = button["text"]
        res_str = ''

        if text == "=":
            self.is_final = 0
            entry_content = self.entry_field.get()
            entry_content = entry_content.replace('×', '*')
            entry_content = entry_content.replace('÷', '/')
            entry_content = entry_content.replace('%', '/100')
            entry_content = entry_content.replace('±','*(-1)')
            result = nsp.eval(entry_content)
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, str(result))
            self.is_final = 1
        else:
            self.entry_field.insert(tk.END,text)
        
        if text == "AC":
            try:
                self.entry_field.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Could not Clear")
        
        if text not in self.operators and self.is_final == 1:
            self.entry_field.delete(0,tk.END)
            self.is_final = 0
        if text in self.operators:
            self.is_final = 0
        
        #Quit Button
        if text == "Quit":
            try:
                root.destroy()
            except:
                root.destroy()

        
        
#Define Window name
root = tk.Tk()
#Create & configure frame
background = tk.Frame(root)
background.grid(row=1,column=0,sticky="NSEW")
background.configure(background='lightgrey')
#Call class logic and buttons
Calculator()
#Configure window
root.title("Calculator")
root.geometry("250x320")
root.wm_attributes('-alpha', 0.92)
root.resizable(RESIZE_YN,RESIZE_YN)
#Refresh window
root.mainloop()