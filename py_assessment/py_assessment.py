#Tkinter bits
import tkinter as tk
import tkinter.font as font
import tkmacosx as tkm
#from tkinter import messagebox

#Other things
import math
import random

#State variables & Constants


#State Class and subroutines
class Calculator():
    def __init__(self) -> None:
        #Numpad
        one_btn = tk.Button(background, text='1',width=1,height=1,font=("Helvetica",16)).grid(row=4,column=6,sticky='NSEW')
        two_btn = tk.Button(background, text='2',width=1,height=1,font=("Helvetica",16)).grid(row=4,column=7,sticky='NSEW')
        three_btn = tk.Button(background, text='3',width=1,height=1,font=("Helvetica",16)).grid(row=4,column=8,sticky='NSEW')
        four_btn = tk.Button(background, text='4',width=1,height=1,font=("Helvetica",16)).grid(row=3,column=6,sticky='NSEW')
        five_btn = tk.Button(background, text='5',width=1,height=1,font=("Helvetica",16)).grid(row=3,column=7,sticky='NSEW')
        six_btn = tk.Button(background, text='6',width=1,height=1,font=("Helvetica",16)).grid(row=3,column=8,sticky='NSEW')
        seven_btn = tk.Button(background, text='7',width=1,height=1,font=("Helvetica",16)).grid(row=2,column=6,sticky='NSEW')
        eight_btn = tk.Button(background, text='8',width=1,height=1,font=("Helvetica",16)).grid(row=2,column=7,sticky='NSEW')
        nine_btn = tk.Button(background, text='9',width=1,height=1,font=("Helvetica",16)).grid(row=2,column=8,sticky='NSEW')
        zero_btn = tk.Button(background, text='0',width=2,height=1,font=("Helvetica",16)).grid(row=5,column=6,columnspan=2,sticky='NSEW')
        deci_btn = tk.Button(background, text=".",width=1,height=1,font=("Helvetica",16)).grid(row=5,column=8,sticky='NSEW')
        #Operators
        eqal_btn = tk.Button(background, text="=",width=1,height=1,font=("Helvetica",16)).grid(row=5, column=9,sticky='NSEW')
        plus_btn = tk.Button(background,text="+",width=1,height=1,font=("Helvetica",16)).grid(row=4,column=9,sticky='NSEW')
        minus_btn = tk.Button(background,text="-",width=1,height=1,font=("Helvetica",16)).grid(row=3,column=9,sticky='NSEW')
        mult_btn = tk.Button(background,text="×",width=1,height=1,font=("Helvetica",16)).grid(row=2,column=9,sticky='NSEW')
        div_btn = tk.Button(background,text="÷",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=9,sticky='NSEW')
        inv_btn =tk.Button(background, text="{}/x".format(self.get_super('1')),width=1,height=1,font=("Helvetica",16)).grid(row=3,column=0,sticky='NSEW')
        #Suffixes
        perc_btn = tk.Button(background,text="%",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=8,sticky='NSEW')
        pmin_btn = tk.Button(background,text="±",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=7,sticky='NSEW')
        #Misc
        clear_btn = tk.Button(background,text="AC",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=6,sticky='NSEW')
        rand_btn = tk.Button(background,text="Rand",width=1,height=1,font=("Helvetica",16)).grid(row=5,column=5,sticky='NSEW')
        opn_per_btn = tk.Button(background,text="(",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=0,sticky='NSEW')
        cls_per_btn = tk.Button(background,text=")",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=1,sticky='NSEW')
        mem_clr_btn = tk.Button(background,text="mc",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=2,sticky='NSEW')
        mem_add_btn = tk.Button(background,text="m+",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=3,sticky='NSEW')
        mem_sub_btn = tk.Button(background,text="m-",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=4,sticky='NSEW')
        mem_rcl_btn = tk.Button(background,text="mr",width=1,height=1,font=("Helvetica",16)).grid(row=1,column=5,sticky='NSEW')
        fx_2nd_btn = tk.Button(background,text="2{}".format(self.get_super('nd')),width=1,height=1,font=("Helvetica",16)).grid(row=2,column=0,sticky='NSEW')
        #Irrationals
        pi_btn = tk.Button(background,text="π",width=1,height=1,font=("Helvetica",16)).grid(row=5,column=4,sticky='NSEW')
        x2_btn = tk.Button(background,text="x{}".format(self.get_super('2')),width=1,height=1,font=("Helvetica",16)).grid(row=2,column=1,sticky='NSEW')
        x3_btn = tk.Button(background,text="x{}".format(self.get_super('3')),width=1,height=1,font=("Helvetica",16)).grid(row=2,column=2,sticky='NSEW')
        xy_btn = tk.Button(background,text="x{}".format(self.get_super('y')),width=1,height=1,font=("Helvetica",16)).grid(row=2,column=3,sticky='NSEW')
        ex_btn = tk.Button(background,text="e{}".format(self.get_super('x')),width=1,height=1,font=("Helvetica",16)).grid(row=2,column=4,sticky='NSEW')       
        tenx_btn = tk.Button(background,text="10{}".format(self.get_super('x')),width=1,height=1,font=("Helvetica",16)).grid(row=2,column=5,sticky='NSEW')
   
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
root.mainloop()