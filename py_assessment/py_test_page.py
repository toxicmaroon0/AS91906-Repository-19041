from tkinter import*
import time
from tkinter import messagebox
import random

def Questions():    
    number1 = random.randrange(1,25)
    number2 = random.randrange(1,50)
    answer = number1 + number2
    prompt = ("Add " + str(number1) + " and " + str(number2))
    labelCreation(prompt)
    return answer

def labelCreation(prompt):
    label1 = Label(root, text=prompt, width=len(prompt))
    label1.pack()

def start():
    global count_flag 
    global answer
    answer = Questions()
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
        root.update()
        # increase count
        count += 0.1

def Submit(answer, entryWidget):
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
         labelConfig()
         
def labelConfig(string,append=False):
    if append:
        text = label.cget("text") + string
        label.configure(text=text)
    else:
        label.configure(text=string)


# create a Tkinter window
root = Tk()

root.title("Math Quiz")
root["padx"] = 40
root["pady"] = 20   

# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(root)

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
instructions = Label(root, text=directions, width=len(directions), bg='orange')
instructions.pack()

# this will be a global flag
count_flag = True


Sub = lambda: Submit(answer, entryWidget)
#stopwatch = lambda: start(answer)

# create needed widgets
label = Label(root, text='0.0')
btn_submit = Button(root, text="Submit", command = Sub)
btn_start = Button(root, text="Start", command = start)
btn_submit.pack()
btn_start.pack()
label.pack()


# start the event loop
root.mainloop()