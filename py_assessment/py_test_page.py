from tkinter import *
import time
from tkinter import messagebox
import random

class quizPage():
    def __init__(self) -> None:
        
        #Configure window
        questionWindow.title("Math Quiz")
        questionWindow["padx"] = 40
        questionWindow["pady"] = 20   
        
        #Create a text frame to hold the text Label and the Entry widget
        textFrame = Frame(questionWindow)
        
        #Make objects refrenceable within class
        self.questionWindow = questionWindow
        self.textFrame = textFrame
        
        
        #Create a Label in textFrame
        entryLabel = Label(textFrame)
        entryLabel["text"] = "Answer:"
        entryLabel.pack(side=LEFT)

        # Create an Entry Widget in textFrame
        entryWidget = Entry(textFrame)
        entryWidget["width"] = 50
        entryWidget.pack(side=LEFT)

        textFrame.pack()
        
        #directions     
        directions = ('Click start to begin. You will be asked a series of questions.')
        instructions = Label(self.questionWindow, text=directions, width=len(directions), bg='orange')
        instructions.pack()

        # this will be a global flag
        global count_flag
        count_flag = True


        Sub = lambda: self.Submit(answer, entryWidget)
        
        # create needed widgets
        
        btn_submit = Button(self.questionWindow, text="Submit", command = Sub)
        btn_start = Button(self.questionWindow, text="Start", command = self.start)
        btn_submit.pack()
        btn_start.pack()
        label.pack()
        
    def Questions(self):    
        number1 = random.randrange(1,25)
        number2 = random.randrange(1,50)
        answer = number1 + number2
        prompt = ("Add " + str(number1) + " and " + str(number2))
        self.labelCreation(prompt)
        return answer

    def labelCreation(self,prompt):
        global label1
        label1 = Label(self.questionWindow, text=prompt, width=len(prompt))
        label1.pack()

    def start(self):
        global count_flag 
        global answer
        global count
        answer = self.Questions()
        count_flag = True
        count = 0.0
        while True:
            if count_flag == False:
                break
            count = round(count, 3)
            # put the count value into the label
            label['text'] = str(count)
            # wait for 0.1 seconds
            time.sleep(0.1)
            # needed with time.sleep()
            self.root.update()
            # increase count
            count += 0.1

    def Submit(self,answer, entryWidget):
        """ Display the Entry text value. """
        global count_flag

        count_flag = False
        print(answer)

        if entryWidget.get().strip() == "":
            messagebox.showerror("Tkinter Entry Widget", "Please enter a number.")

        if answer != int(entryWidget.get().strip()):
            messagebox.showinfo("Answer", "INCORRECT!")
        else:
            messagebox.showinfo("Answer", "CORRECT!\nPlease press 'Start' again for a new question")
            self.labelConfig(count, True)
            
    def labelConfig(self,string,append=False):
        if append:
            text = label1.cget("text") + string
            label1.configure(text=text)
        else:
            label1.configure(text=string)

#Call logic
#Create window & Labels refrenced in call
questionWindow = Tk()
label = Label(questionWindow, text='0.0')
quizPage()
questionWindow.mainloop()