import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


class Objective1:
    def __init__(self, root,model):
        #setting title
        root.title("Performance in a subject")
        #setting window size
        width=590
        height=348
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        self.model=model

        self.subcode=tk.StringVar()

        GLabel_189=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_189["font"] = ft
        GLabel_189["fg"] = "#333333"
        GLabel_189["justify"] = "center"
        GLabel_189["text"] = "Student Performance in "
        GLabel_189.place(x=0,y=0,width=589,height=87)

        GLabel_635=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_635["font"] = ft
        GLabel_635["fg"] = "#333333"
        GLabel_635["justify"] = "center"
        GLabel_635["text"] = "a Subject"
        GLabel_635.place(x=150,y=80,width=274,height=59)

        GLabel_312=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_312["font"] = ft
        GLabel_312["fg"] = "#333333"
        GLabel_312["justify"] = "center"
        GLabel_312["text"] = "Subject code :-"
        GLabel_312.place(x=20,y=150,width=286,height=117)

        GLineEdit_856=ttk.Entry(root,text = "Enter Subject Code",textvariable=self.subcode,width=29,font=("Times",22))
        GLineEdit_856.place(x=310,y=190,width=197,height=41)

        GButton_229=tk.Button(root)
        GButton_229["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=23)
        GButton_229["font"] = ft
        GButton_229["fg"] = "#000000"
        GButton_229["justify"] = "center"
        GButton_229["text"] = "Visualize"
        GButton_229.place(x=200,y=270,width=173,height=45)
        GButton_229["command"] = self.GButton_229_command

    def GButton_229_command(self):
        self.model.Objective1(str(self.subcode.get()).upper())
        

