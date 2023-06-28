import tkinter as tk
import time
from tkinter import messagebox
import random
import math

class quizPage():
    def __init__(self) -> None:
        
        #Configure window
        questionWindow.title("Math Quiz")
        questionWindow["padx"] = 40
        questionWindow["pady"] = 20   
        
        #Create a text frame to hold the text Label and the Entry widget
        textFrame = tk.Frame(questionWindow)
        
        #Make objects refrenceable within class
        self.questionWindow = questionWindow
        self.textFrame = textFrame
        
        
        #Create a Label in textFrame
        entryLabel = tk.Label(textFrame)
        entryLabel["text"] = "Answer:"
        entryLabel.pack(side=tk.LEFT)

        # Create an Entry Widget in textFrame
        global entryWidget
        entryWidget = tk.Entry(textFrame,state="readonly")
        entryWidget["width"] = 50
        entryWidget.pack(side=tk.LEFT)

        textFrame.pack()
        
        #directions     
        directions = ('Click start to begin. Use the calculator provided to solve the questions.')
        instructions = tk.Label(self.questionWindow, text=directions, width=len(directions), bg='orange')
        instructions.pack()

        # this will be a global flag
        global count_flag
        count_flag = True


        Sub = lambda: self.Submit(answer)
        
        # create needed widgets
        
        btn_submit = tk.Button(self.questionWindow, text="Submit", command = Sub)
        btn_start = tk.Button(self.questionWindow, text="Start", command = self.start)
        btn_submit.pack()
        btn_start.pack()
        label.pack()
        
    def Questions(self):    
        number1 = random.randrange(1,25)
        number2 = random.randrange(1,50)
        
        rando = random.randrange(1,4)
        rando1 = random.randrange(0,1)
        operator = ""
        
        if rando == 1:
            answer = number1 + number2
            operator = 'Add'
            context = 'and'
        elif rando ==2:
            answer = number1 - number2
            operator = 'Subtract'
            context = 'take away'
        elif rando == 3:
            if rando1 == 1:
                number2 = number2 / 1.5
                number2 = round(number2)
            answer = number1 * number2
            operator = 'Multiply'
            context = 'and'
        elif rando == 4:
            if rando1 == 1:
                number2 = number2 / 1.5
                number2 = round(number2)
            operator = 'Divide'
            context = 'by'
            answer = number1 / number2
            
        prompt = (str(operator) , str(number1) , context , str(number2))
        self.labelCreation(prompt)
        return answer

    def labelCreation(self,prompt):
        global label1
        label1 = tk.Label(self.questionWindow, text=prompt)
        label1.pack()

    def start(self):
        global count_flag 
        global answer
        global count
        answer = self.Questions()
        count_flag = True
        count = 0.0
        entryWidget.configure(state='normal')
        print(answer)
        while True:
            if count_flag == False:
                break
            count = round(count, 3)
            # put the count value into the label
            label['text'] = str(count)
            # wait for 0.1 seconds
            time.sleep(0.1)
            # needed with time.sleep()
            questionWindow.update()
            # increase count
            count += 0.1

    def Submit(self,answer):
        """ Display the Entry text value. """
        global count_flag

        count_flag = False

        if entryWidget.get().strip() == "":
            messagebox.showerror("Tkinter Entry Widget", "Please enter a number.")

        if answer != int(entryWidget.get().strip()):
            messagebox.showinfo("Answer", "INCORRECT!")
            labelstr = 'completed in',str(count),', False'
            labelstr = ' '.join(labelstr)
            self.labelConfig(labelstr, append=True)
            entryWidget.delete(0,tk.END)
            entryWidget.configure(state="readonly")
        else:
            messagebox.showinfo("Answer", "CORRECT!\nPlease press 'Start' again for a new question")
            labelstr = 'completed in',str(count),', Correct'
            labelstr = ' '.join(labelstr)
            self.labelConfig(labelstr, append=True)
            entryWidget.delete(0,tk.END)
            entryWidget.configure(state="readonly")
            
    def labelConfig(self,string,append=False):
        if append:
            text = label1.cget('text')
            text = text,string
            text = ', '.join(text)
            
            label1.configure(text=text)
        else:
            label1.configure(text=string)

#Call logic
#Create window & Labels refrenced in call
questionWindow = tk.Tk()
label = tk.Label(questionWindow, text='0.0')
quizPage()
questionWindow.mainloop()