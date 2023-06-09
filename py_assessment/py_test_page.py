import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
import random
from py_assessment_constants import *

class quizPage():
    def __init__(self) -> None:
        answer = 0
        questionsAsked = 0
        count = 0.0
        bindsHelpAsked = 0
        self.answer = answer
        self.questionsAsked = questionsAsked
        self.count = count
        self.bindsHelpAsked = bindsHelpAsked
        
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
        while self.questionsAsked > 10:
            entryWidget.configure(state='readonly')

        textFrame.pack()
        
        #directions     
        directions = ('Click start to begin. Use the calculator provided to solve the questions.')
        instructions = tk.Label(self.questionWindow, text=directions, width=len(directions), bg='orange')
        instructions.pack()

        # this will be a global flag
        count_flag = True
        self.count_flag = count_flag

        # create needed widgets
        
        btn_submit = tk.Button(self.questionWindow, text="Submit", command = lambda: [self.Submit(self.answer)])
        questionWindow.bind('<Return>',lambda: [self.Submit(self.answer), questionWindow.focus()])
        btn_start = tk.Button(self.questionWindow, text="Start", command = lambda: [self.start(), entryWidget.focus_set()])
        questionWindow.bind('<\>',lambda x: [self.start(), questionWindow.focus_set(), entryWidget.focus_set()])
        questionWindow.bind('<Escape>',lambda x:[self.quitQuestion()])
        if self.questionsAsked > 10:
            questionWindow.unbind_all('<\>')
            questionWindow.unbind_all('<Return>')
        btn_submit.pack()
        btn_start.pack()
        label.pack()
        self.label = label
        
        # get screen width and height
        ws = questionWindow.winfo_screenwidth() # width of the screen
        hs = questionWindow.winfo_screenheight() # height of the screen
        x = ((ws/2) - (W/2))
        y = 0-hs
        
        questionWindow.geometry('%dx%d+%d+%d' % ((4*W),(H*1.28),x,y))
        
        questionWindow.resizable(RESIZE_N,RESIZE_N)
        
    def Questions(self):    
        number1 = random.randrange(1,25)
        number2 = random.randrange(1,50)
        
        rando = random.randrange(1,4)
        rando1 = random.randrange(0,1)
        operator = ""
        if self.questionsAsked < 10:
            if rando == 1:
                self.answer = number1 + number2
                operator = 'Add'
                context = 'and'
            elif rando ==2:
                self.answer = number1 - number2
                operator = 'Subtract'
                context = 'from'
            elif rando == 3:
                if rando1 == 1:
                    number2 = number2 / 1.5
                    number2 = round(number2)
                self.answer = number1 * number2
                operator = 'Multiply'
                context = 'and'
            elif rando == 4:
                if rando1 == 1:
                    number2 = number2 / 1.5
                    number2 = round(number2)
                operator = 'Divide'
                context = 'by'
                self.answer = number1 / number2
                
            if rando ==2:    
                prompt = (str(operator) , str(number2) , str(context) , str(number1))
            else:
                prompt = (str(operator) , str(number1) , str(context) , str(number2))
            self.labelCreation(prompt)
            self.questionsAsked += 1
            return self.answer
        else:
            self.labelCreation('You have finished the questionare, restart to try again.')


    def labelCreation(self,prompt):
        global label1
        label1 = tk.Label(self.questionWindow, text=prompt)
        label1.pack()

    def start(self):
        self.keyBindings()
        self.answer = self.Questions()
        self.count = 0.0    
        self.count_flag = True    
        entryWidget.configure(state='normal')
        match self.answer == None:
            case True: print('----\nQuiz finished\nNo new questions')
            case _: print('----\nNew Question\n Answer = '+str(self.answer))
        while self.questionsAsked <= 10:
            match self.count_flag == False:
                case True: break
            self.count = round(self.count, 3)
            # put the count value into the label
            self.label['text'] = str(self.count)
            # wait for 0.1 seconds
            time.sleep(0.1)
            # needed with time.sleep()
            questionWindow.update()
            # increase count
            self.count += 0.1
        entryWidget.configure(state='readonly')

    def Submit(self,answer):
        """ Display the Entry text value. """

        self.count_flag = False

        if entryWidget.get().strip() == "":
            messagebox.showerror("Tkinter Entry Widget", "Please enter a number.")
            self.count_flag = True
            questionWindow.focus_set()
            self.start()

        match self.answer != int(entryWidget.get().strip()):
            case True: 
                messagebox.showinfo("Answer", "INCORRECT!")
                labelstr = 'completed in ',str(self.count),' seconds, False'
                labelstr = ''.join(labelstr)
                self.labelConfig(labelstr, append=True)
                entryWidget.delete(0,tk.END)
                entryWidget.configure(state="readonly")
                questionWindow.focus()
                questionWindow.focus_set()
            case _:
                messagebox.showinfo("Answer", "CORRECT!\nPlease press 'Start' again for a new question")
                labelstr = 'completed in ',str(self.count),' seconds, Correct'
                labelstr = ''.join(labelstr)
                self.labelConfig(labelstr, append=True)
                entryWidget.delete(0,tk.END)
                entryWidget.configure(state="readonly")
                questionWindow.focus()
                questionWindow.focus_set()
            
    def labelConfig(self,string,append=False):
        match append == True:
            case True:
                text = label1.cget('text')
                text = text,string
                text = ', '.join(text)
                label1.configure(text=text)
            case _:
                label1.configure(text=string)
    
    def quitQuestion(self):
        match bool(messagebox.askquestion('Quit?','Are you sure you want to close the question window?')) == True:
            case True:
                questionWindow.destroy()
            case _:
                return
    
    def keyBindings(self):
        match self.bindsHelpAsked == 1:
            case True:
                messagebox.showinfo("Keybind information","Keybind Information;\n[Return]: Submit Answer\n[\]: Generate new question\n[Esc]: Opme window cloase dialogue")
                self.bindsHelpAsked = 1
            case _: pass

#Call logic
#Create window & Labels refrenced in call
questionWindow = tk.Tk()
label = tk.Label(questionWindow, text='0.0')
quizPage()
questionWindow.mainloop()