import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Objective5:
    def __init__(self, root,model):
        #setting title
        self.model=model
        root.title("Semester wise performance")
        #setting window size
        self.usn=tk.StringVar()
        width=590
        height=348
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_189=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_189["font"] = ft
        GLabel_189["fg"] = "#333333"
        GLabel_189["justify"] = "center"
        GLabel_189["text"] = "Semester-Wise"
        GLabel_189.place(x=0,y=10,width=590,height=39)

        GLabel_637=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_637["font"] = ft
        GLabel_637["fg"] = "#333333"
        GLabel_637["justify"] = "center"
        GLabel_637["text"] = "Performance Analysis"
        GLabel_637.place(x=0,y=60,width=594,height=39)

        GLabel_312=tk.Label(root)
        ft = tkFont.Font(family='Times',size=33)
        GLabel_312["font"] = ft
        GLabel_312["fg"] = "#333333"
        GLabel_312["justify"] = "center"
        GLabel_312["text"] = "Student USN :-"
        GLabel_312.place(x=30,y=130,width=286,height=117)

        GLineEdit_856=ttk.Entry(root,text = "Enter USN",textvariable=self.usn,width=29,font=("Times",22))
        GLineEdit_856.place(x=320,y=170,width=197,height=41)

        GButton_229=tk.Button(root)
        GButton_229["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=33)
        GButton_229["font"] = ft
        GButton_229["fg"] = "#000000"
        GButton_229["justify"] = "center"
        GButton_229["text"] = "Visualize"
        GButton_229.place(x=200,y=260,width=173,height=45)
        GButton_229["command"] = self.GButton_229_command

        

    def GButton_229_command(self):
        self.model.Objective5(str(self.usn.get()).upper())

