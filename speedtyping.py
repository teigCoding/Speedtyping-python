import tkinter as tk
from threading import Timer
import datetime
import random
from tkinter import *

def start_game():
    randomNum = random.randint(1,10)
    fileName = 'text'+str(randomNum)+'.txt'
    with open(fileName, 'r') as file:
        text = file.read()
    
    lbl_showText["text"] = text
    orgTime = datetime.datetime.now()
    global shouldItRun
    shouldItRun = True
    start_timer(orgTime)
    

def check_correct():
    text = lbl_showText["text"]
    userText = txt_edit.get("1.0",'end-1c')
    listeTekst = text.split()
    listeBrukerTekst = userText.split()
    counter = 0
    for index in range(min(len(listeTekst), len(listeBrukerTekst))):
        if listeTekst[index] == listeBrukerTekst[index]:
            counter += 1
    global shouldItRun
    shouldItRun = False
    if counter != 0:
        wordsPerMinute = counter/(lbl_showTimer["text"]/60)
        lbl_showText["text"] = "You had " + str(counter) + " correct words!" + "\n" + "\n" + "Your time was " + str(lbl_showTimer["text"]) + " seconds!" + "\n" + "That is " + str(round(wordsPerMinute,2)) + " WPM!"
    else: 
        lbl_showText["text"] = "You had 0 correct words!" + "\n" + "\n" + "Your time was 0 seconds!" + "\n" + "That is 0.00 WPM!"
    lbl_showTimer["text"] = "0"

def check_correct_return(event):
    text = lbl_showText["text"]
    userText = txt_edit.get("1.0",'end-1c')
    listeTekst = text.split()
    listeBrukerTekst = userText.split()
    counter = 0
    for index in range(min(len(listeTekst), len(listeBrukerTekst))):
        if listeTekst[index] == listeBrukerTekst[index]:
            counter += 1
    global shouldItRun
    shouldItRun = False
    wordsPerMinute = counter/(lbl_showTimer["text"]/60)
    lbl_showText["text"] = "You had " + str(counter) + " correct words!" + "\n" + "\n" + "Your time was " + str(lbl_showTimer["text"]) + " seconds!" + "\n" + "That is " + str(round(wordsPerMinute,2)) + " WPM!"
    lbl_showTimer["text"] = "0"



def start_timer(orgTime):
    if shouldItRun == True:
        t = Timer(0.1, start_timer,[orgTime])
        newTime = datetime.datetime.now() - orgTime
        lbl_showTimer["text"] = round(newTime.total_seconds(),1)
        t.start()



def stop_game():
    global shouldItRun
    shouldItRun = False
    lbl_showTimer["text"] = "0"
    lbl_showText["text"] = "You've stopped the game!" + "\n" + "\n" + "Click the start button to start the game again!"
    
window = tk.Tk()
window.title("Speed Type")

window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=400, weight=1)
txt_edit = tk.Text(window)
lbl_showText = tk.Label(window,wraplength=550,font=("Arial", 10))


frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
lbl_showTimer = tk.Label(frm_buttons,text="0")
btn_open = tk.Button(frm_buttons, text="Start",command=start_game)
btn_save = tk.Button(frm_buttons, text="Stop",command=stop_game)
btn_done = tk.Button(frm_buttons, text="Done",command=check_correct)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_done.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

lbl_showTimer.grid(row=3, column=0)
frm_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.bind('<Return>', check_correct_return)

txt_edit.grid(row=1, column=1,sticky="ns")
lbl_showText.grid(row=0, column=1,sticky="ew")




window.mainloop()
