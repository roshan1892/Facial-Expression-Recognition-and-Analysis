#!/usr/bin/env python

import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def _train():
    print ("\n\n Please Wait. . . .Training.....")
    import classifier.py
    #exec(open('classifier.py').read()) 

   
    # os.system('"Train Classifier.exe"')
    # opencvProcess.communicate()


def _start():
    print("START")
    print("Please Wait ........")
    exec(open('test.py').read()) 


def _quit():
    
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate'''


if __name__ == "__main__":
    # Embedding things in a tkinter plot & Starting tkinter plot
    root = Tk.Tk()
    root.wm_title("Emotion Recognition Using Scikit-Learn & OpenCV")
    root.geometry("300x400")
    root.configure(background='light blue')


    # Declaring Button & Label Instances
    # =======================================



    authorVar = Tk.StringVar()
    authorLabel = Tk.Label(master=root, textvariable=authorVar,bg="White")
    authorString = "\n\n FACIAL EXPRESSION RECOGNITION SYSTEM  " 
    authorVar.set(authorString)
    authorLabel.pack(side=Tk.TOP,pady=40)


    opencvButton = Tk.Button(master=root, text='Train The Classifier', command=_train , bg="cyan")
    opencvButton.pack(side=Tk.TOP,pady=10)

    resetButton = Tk.Button(master=root, text='Start ', command=_start , bg="cyan")
    resetButton.pack(side=Tk.TOP,pady=10)

    quitButton = Tk.Button(master=root, text='Quit Application', command=_quit ,bg="cyan")
    quitButton.pack(side=Tk.TOP,pady=10)

    authorVar = Tk.StringVar()
    authorLabel = Tk.Label(master=root, textvariable=authorVar)
    authorString = "\n\n Developed By: " \
                   "\n Sujan Koju,Sabin Lama,Roshan Bhandari,Ranjan Shrestha " \
                
    authorVar.set(authorString)
    authorLabel.pack(side=Tk.BOTTOM)

    root.iconbitmap(r'icon\happy-sad.ico')
    Tk.mainloop()                               # Starts mainloop required by Tk 
