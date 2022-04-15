import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Objective3:
    def __init__(self, root,model):
        self.model=model
        #setting title
        root.title("Backlog Analysis")
        #setting window size
        width=600
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.usn=tk.StringVar()
        self.passed=tk.StringVar()
        self.failed=tk.StringVar()



        GLabel_785=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_785["font"] = ft
        GLabel_785["fg"] = "#333333"
        GLabel_785["justify"] = "center"
        GLabel_785["text"] = "Backlog Analysis"
        GLabel_785.place(x=10,y=10,width=560,height=100)

        GLabel_663=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_663["font"] = ft
        GLabel_663["fg"] = "#333333"
        GLabel_663["justify"] = "center"
        GLabel_663["text"] = "USN with Backlog:-"
        GLabel_663.place(x=50,y=160,width=200,height=25)

        GLineEdit_427=ttk.Entry(root,text = "Enter USN",textvariable=self.usn,width=29,font=("Times",22))
        GLineEdit_427.place(x=300,y=160,width=200,height=30)

        GButton_640=tk.Button(root)
        GButton_640["bg"] = "#00ced1"
        ft = tkFont.Font(family='Times',size=10)
        GButton_640["font"] = ft
        GButton_640["fg"] = "#000000"
        GButton_640["justify"] = "center"
        GButton_640["text"] = "Analyse"
        GButton_640.place(x=250,y=230,width=90,height=30)
        GButton_640["command"] = self.GButton_640_command

        GLabel_241=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_241["font"] = ft
        GLabel_241["fg"] = "#333333"
        GLabel_241["justify"] = "center"
        GLabel_241["text"] = "Subject with Backlog:-"
        GLabel_241.place(x=50,y=290,width=220,height=25)

        

        GMessage_341=tk.Message(root,textvariable=self.failed,width=500)
        GMessage_341["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=18)
        GMessage_341["font"] = ft
        GMessage_341["fg"] = "#333333"
        GMessage_341["justify"] = "center"
        GMessage_341["text"] = "Subject Fail"
        GMessage_341.place(x=25,y=330,width=550,height=90)

        GLabel_85=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_85["font"] = ft
        GLabel_85["fg"] = "#333333"
        GLabel_85["justify"] = "center"
        GLabel_85["text"] = "Subjects Cleared:-"
        GLabel_85.place(x=30,y=450,width=220,height=25)

        GMessage_679=tk.Message(root,textvariable=self.passed,width=500)
        GMessage_679["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=18)
        GMessage_679["font"] = ft
        GMessage_679["fg"] = "#333333"
        GMessage_679["justify"] = "center"
        GMessage_679["text"] = "Subject Pass"
        GMessage_679.place(x=25,y=480,width=550,height=90)

    def GButton_640_command(self):
        sub,flag=self.model.Objective3(str(self.usn.get()).upper())
        failedsub=""
        passedsub=""
        if len(sub)==0:
            self.failed.set("No Subjects Failed")
        else:
            for i in sub:
                failedsub=failedsub+" "+i
            self.failed.set(failedsub)
        if len(flag)==0:
            self.passed.set("No Subjects Cleared")
        else:
            for i in flag:
                passedsub=passedsub+" "+i
            self.passed.set(passedsub)

