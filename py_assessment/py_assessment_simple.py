#Tkinter bits
import tkinter as tk
from tkinter import messagebox

#Other things
import math
from py_numeric_parser_class import *
from py_assessment_constants import *

#Create objects / instanses / CONSTANTS
nsp = NumericStringParser()

#State Class and subroutines
class Calculator():
    def __init__(self) -> None:
        #Variables
        text = ''
        row = 0
        col = 0
        self.is_final = 0
        self.text = text
        
        # get screen width and height
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = ((ws/2) - (W/2))
        y = 0-hs
        
        root.geometry('%dx%d' % (W, H))
        
        # Buttons
        buttons = [
            "AC", "(INV)", "%", "÷",
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
        self.entry_field = tk.Entry(root,font=("Helvetica", 20), justify="right",width=-20)
        self.entry_field.grid(row=0, column=0,sticky="NSEW")
        root.rowconfigure(1, weight=3)
        root.rowconfigure(0, weight=1)
        background.rowconfigure(4, weight=1)
        for unit in range(0,3):
            background.rowconfigure(unit, weight=1)
            background.columnconfigure(unit,weight = 1)
                
        #Lists
        self.operators = ["+", "-", "÷", "×", "(INV)", "%", "="]
    
    def round_up(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier

    def button_click(self, event):
        button = event.widget
        self.text = button["text"]

        if self.text == "=":
            self.is_final = 0
            entry_content = self.entry_field.get()
            entry_content = entry_content.replace('×', '*')
            entry_content = entry_content.replace('÷', '/')
            entry_content = entry_content.replace('%', '/100')
            entry_content = entry_content.replace('(INV)','*(-1)')
            result = nsp.eval(entry_content)
            result = str(result)
            
            match len(result) >= 15 and '.' in result:
                case True:
                    result = float(result)
                    result = self.round_up(result,5)
                    result = str(result)
                case _: pass
            
            match result[-1] == '0' and result[-2] == '.':
                case True:
                    result = result.removesuffix('.0')
                case _: pass
                
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, str(result))
            self.is_final = 1
        else:
            self.entry_field.insert(tk.END,self.text)
        
        match self.text == "AC":
            case True:
                try:
                    self.entry_field.delete(0, tk.END)
                except:
                    messagebox.showerror("Error", "Could not Clear")
            case _: pass
        
        match self.text not in self.operators and self.is_final == 1:
            case True:
                self.entry_field.delete(0,tk.END)
                self.is_final = 0
            case _: pass
        match self.text in self.operators:
            case True: self.is_final = 0
            case _: pass
        
        #Quit Button
        match self.text == "Quit":
            case True:
                try:
                    root.destroy()
                except:
                    root.destroy()
            case _: pass

        
        
#Define Window name
root = tk.Tk()
#Create & configure frame
background = tk.Frame(root)
background.grid(row=1,column=0,sticky="NSEW")
background.configure(background='lightgrey')
#Configure window
root.title("Calculator")
root.wm_attributes('-alpha', 0.92)
root.resizable(RESIZE_N,RESIZE_N)
#Call class logic and buttons
Calculator()
#Refresh window
from py_test_page import *
try:
    root.focus()
except:
    TclError
root.mainloop()