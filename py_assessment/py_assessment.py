#Tkinter bits
import tkinter as tk
import tkinter.font as font
import tkmacosx as tkm
from tkinter import messagebox

#Other things
import math
import numpy as np
import random

#State variables & Constants


#State Class and subroutines
class Calculator():
    def __init__(self) -> None:
        #Variables
        row = 1
        col = 0
        self.is_final = 0
        
        # Buttons
        buttons = [
            "(", ")", "mc", "m+", "m-", "mr", "AC", "±", "%", "÷",
            "2{}".format(self.get_super('nd')), "x{}".format(self.get_super('2')), "x{}".format(self.get_super('3')), "x{}".format(self.get_super('y')), "e{}".format(self.get_super('x')), "10{}".format(self.get_super('x')), "7", "8", "9", "×",
            "{}/x".format(self.get_super('1')), "{}√x".format(self.get_super('2')), "{}√x".format(self.get_super('3')), "{}√x".format(self.get_super('y')), "ln", "log{}".format(self.get_sub('10')), "4", "5", "6", "-",
            "x!", "sin", "cos", "tan", "e", "EE", "1", "2", "3", "+",
            "Rad", "sinh", "cosh", "tanh", "π", "Rand", "0", ".", "="
        ]

        
        for button in buttons:
            btn = tk.Button(background, text=button, font=("Helvetica", 16), width=1, height=1)
            btn.grid(row=row, column=col, sticky="NSEW")
            if button == "0":
                btn.grid_configure(columnspan=2)
                col += 1
            btn.bind("<Button-1>", self.button_click)
            col += 1
            if col > 9:
                col = 0
                row += 1
                
        # Entry Field
        self.entry_field = tk.Entry(root,font=("Helvetica", 20), justify="right")
        self.entry_field.grid(row=0, column=0, columnspan=10,sticky="NSEW")

    def button_click(self, event):
        button = event.widget
        text = button["text"]

        if text == "=":
            try:
                self.is_final = 0
                entry_content = self.entry_field.get()
                entry_content = entry_content.replace('×', '*')
                entry_content = entry_content.replace('÷', '/')
                entry_content = entry_content.replace('%', '/100')
                entry_content = entry_content.replace('±','*(-1)')
                entry_content = entry_content.replace("{}/x".format(self.get_super('1')),'')
                result = eval(entry_content)
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, str(result))
                self.is_final = 1
            except:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            self.entry_field.insert(tk.END,text)
        
        
        if text == "AC":
            try:
                self.entry_field.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Could not Clear")
        operators = ["+", "-", "÷", "×", "±", "%", "=", "x!", "sin", "cos", "tan", "sinh", "cosh", "tanh",
                     "{}/x".format(self.get_super('1')), "{}√x".format(self.get_super('2')), "{}√x".format(self.get_super('3')),
                     "x{}".format(self.get_super('2')), "x{}".format(self.get_super('3')), "x{}".format(self.get_super('y')),
                     "e{}".format(self.get_super('x')), "10{}".format(self.get_super('x'))]
        for operator in operators:
            if text != operator and self.is_final == 1:
                self.entry_field.delete(0,tk.END)
        


    #Text Formatting
    def get_super(self,x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)
    
    def get_sub(self,x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
        res = x.maketrans(''.join(normal), ''.join(sub_s))
        return x.translate(res)
        
        
#Define Window name
root = tk.Tk()
#Create Canvas
background = tk.Canvas(root,)
background.grid(row=1,column=0,columnspan=10,rowspan=5,sticky="NSEW")
#Call class logic and buttons
Calculator()
#Configure window
root.title("Calculator")
root.geometry("575x320")
root.wm_attributes('-alpha', 0.92)
background.configure(background='lightgrey')
root.resizable(False,False)
#Refresh window
root.mainloop()