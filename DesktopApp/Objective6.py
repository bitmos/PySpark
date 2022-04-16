import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Objective6:
    def __init__(self, root,model):
        #setting title
        self.model=model
        root.title("Consecutive Year Score Prediction")
        #setting window size
        width=605
        height=441
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.usn=tk.StringVar()
        self.code=tk.StringVar()
        self.year=tk.StringVar()
        self.result=tk.StringVar()


        GLabel_768=tk.Label(root)
        ft = tkFont.Font(family='Times',size=31)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "Consecutive Score Prediction"
        GLabel_768.place(x=0,y=10,width=602,height=85)

        GLabel_749=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_749["font"] = ft
        GLabel_749["fg"] = "#333333"
        GLabel_749["justify"] = "center"
        GLabel_749["text"] = "USN :-"
        GLabel_749.place(x=70,y=120,width=107,height=45)

        GLabel_373=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_373["font"] = ft
        GLabel_373["fg"] = "#333333"
        GLabel_373["justify"] = "center"
        GLabel_373["text"] = "Subject Code :-"
        GLabel_373.place(x=80,y=190,width=196,height=37)

        GLabel_491=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_491["font"] = ft
        GLabel_491["fg"] = "#333333"
        GLabel_491["justify"] = "center"
        GLabel_491["text"] = "Year :-"
        GLabel_491.place(x=80,y=260,width=86,height=30)

        GLineEdit_211=ttk.Entry(root,text = "Enter USN",textvariable=self.usn,width=29,font=("Times",18))
        GLineEdit_211.place(x=300,y=130,width=148,height=35)

        GLineEdit_368=ttk.Entry(root,text = "Enter Code",textvariable=self.code,width=29,font=("Times",18))
        GLineEdit_368.place(x=300,y=190,width=148,height=35)

        GLineEdit_750=ttk.Entry(root,text = "Enter Year",textvariable=self.year,width=29,font=("Times",18))
        GLineEdit_750.place(x=300,y=260,width=148,height=35)

        GButton_225=tk.Button(root)
        GButton_225["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=22)
        GButton_225["font"] = ft
        GButton_225["fg"] = "#000000"
        GButton_225["justify"] = "center"
        GButton_225["text"] = "Predict"
        GButton_225.place(x=90,y=340,width=140,height=38)
        GButton_225["command"] = self.GButton_225_command

        GLabel_957=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_957["font"] = ft
        GLabel_957["fg"] = "#333333"
        GLabel_957["justify"] = "center"
        GLabel_957["text"] = "Total Score :-"
        GLabel_957.place(x=270,y=330,width=167,height=59)

        GMessage_114=tk.Message(root,textvariable=self.result)
        GMessage_114["bg"] = "#1be8d5"
        ft = tkFont.Font(family='Times',size=22)
        GMessage_114["font"] = ft
        GMessage_114["fg"] = "#333333"
        GMessage_114["justify"] = "center"
        GMessage_114["text"] = ""
        GMessage_114.place(x=450,y=340,width=109,height=39)

    def GButton_225_command(self):
        a=str(self.usn.get().upper())
        b=int(str(self.code.get().upper())[-1])
        c=int(str(self.year.get().upper()))
        data=self.model.encode(a,b,c)
        self.result.set(int(self.model.Objective6(data)))

