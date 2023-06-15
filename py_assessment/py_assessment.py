#Tkinter bits
import tkinter as tk
import tkinter.font as font
import tkmacosx as tkm
from tkinter import messagebox

#Other things
import math
import random

#State variables & Constants


#State Class and subroutines
class Calculator():
    def __init__(self) -> None:
        # Buttons
        buttons = [
            "(", ")", "mc", "m+", "m-", "mr", "AC", "±", "%", "÷",
            "2{}".format(self.get_super('nd')), "x{}".format(self.get_super('2')), "x{}".format(self.get_super('3')), "x{}".format(self.get_super('y')), "e{}".format(self.get_super('x')), "10{}".format(self.get_super('x')), "7", "8", "9", "×",
            "{}/x".format(self.get_super('1')), "{}√{}".format(self.get_super('2'),self.get_sub('x')), "{}√{}".format(self.get_super('3'),self.get_sub('x')), "{}√{}".format(self.get_super('y'),self.get_sub('x')), "ln", "log{}".format(self.get_sub('10')), "4", "5", "6", "-",
            "x!", "sin", "cos", "tan", "e", "EE", "1", "2", "3", "+",
            "Rad", "sinh", "cosh", "tanh", "π", "Rand", "0", ".", "="
        ]

        row = 1
        col = 0
        for button in buttons:
            btn = tk.Button(root, text=button, font=("Helvetica", 16), width=1, height=1)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="NSEW")
            btn.bind("<Button-1>", self.button_click)
            col += 1
            if col > 10:
                col = 0
                row += 1

    def button_click(self, event):
        button = event.widget
        text = button["text"]

        if text == "=":
            try:
                result = eval(self.entry_field.get())
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, str(result))
            except:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            self.entry_field.insert(tk.END, text)


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
        
        

root = tk.Tk()
background = tk.Canvas(root, width=575,height=270)
background.grid()
Calculator()
root.title("Calculator")
root.geometry("575x320")
root.wm_attributes('-alpha', 0.92)
root.configure(background='lightgrey')
root.resizable(False,False)
root.mainloop()