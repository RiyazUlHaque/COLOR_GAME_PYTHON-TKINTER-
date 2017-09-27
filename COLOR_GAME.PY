
import tkinter
import random


colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']

score=0
timeleft=30


def startGame(event):

    
    if timeleft == 30:
 
        countdown()
        

    nextColour()


def nextColour():


    global score
    global timeleft

    #if a game is currently in play...
    if timeleft > 0:

        #...make the text entry box active.
        e.focus_set()

        #if the colour typed is equal to the colour of the text...
        if e.get().lower() == colours[1].lower():
            #...add one to the score.
            score += 1

        #clear the text entry box.
        e.delete(0, tkinter.END)
        #shuffle the list of colours.
        random.shuffle(colours)
        #change the colour to type, by changing the text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))
        #update the score.
        scoreLabel.config(text="Score: " + str(score))

 
def countdown():

    
    global timeleft

    #if a game is in play...
    if timeleft > 0:

        #decrement the timer.
        timeleft -= 1
        #update the time left label.
        timeLabel.config(text="Time left: " + str(timeleft))
        #run the function again after 1 second.
        timeLabel.after(1000, countdown)
    

root = tkinter.Tk()

root.title("COLOR GAME")

root.geometry("600x400")


instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()


scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()


timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()


label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()


e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()


root.mainloop()