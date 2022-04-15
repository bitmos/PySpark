import tkinter as tk
import tkinter.font as tkFont
from Model import Model
from Objective1 import Objective1
from Objective2 import Objective2
from Objective3 import Objective3
from Objective4 import Objective4
from Objective5 import Objective5
from Objective6 import Objective6




class Home:
    def __init__(self,root):
        self.root=root
        self.model=Model()
        #setting title
        self.root.title("Home")
        #setting window size
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_653=tk.Label(self.root)
        GLabel_653["activebackground"] = "#a75454"
        GLabel_653["activeforeground"] = "#954747"
        ft = tkFont.Font(family='Times',size=54)
        GLabel_653["font"] = ft
        GLabel_653["fg"] = "#040404"
        GLabel_653["justify"] = "center"
        GLabel_653["text"] = "Result Analysis"
        GLabel_653["relief"] = "flat"
        GLabel_653.place(x=120,y=30,width=524,height=72)

        GLabel_654=tk.Message(self.root,width=320)
        ft = tkFont.Font(family='Times',size=29)
        GLabel_654["font"] = ft
        GLabel_654["fg"] = "#040404"
        GLabel_654["justify"] = "left"
        GLabel_654["text"] = "Select From the options given on the left navigation bar to obtain desired results."
        GLabel_654.place(x=320,y=120,width=320,height=302)

        GButton_887=tk.Button(self.root)
        GButton_887["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_887["font"] = ft
        GButton_887["fg"] = "#000000"
        GButton_887["justify"] = "center"
        GButton_887["text"] = "Performance in a subject"
        GButton_887.place(x=30,y=110,width=224,height=41)
        GButton_887["command"] = self.Performance_subject

        GButton_637=tk.Button(self.root)
        GButton_637["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_637["font"] = ft
        GButton_637["fg"] = "#000000"
        GButton_637["justify"] = "center"
        GButton_637["text"] = "Performance prediction of a subject"
        GButton_637.place(x=30,y=170,width=224,height=41)
        GButton_637["command"] = self.prediction_subject

        GButton_932=tk.Button(self.root)
        GButton_932["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#000000"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "Backlog Analysis"
        GButton_932.place(x=30,y=230,width=224,height=41)
        GButton_932["command"] = self.Backlog

        GButton_513=tk.Button(self.root)
        GButton_513["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_513["font"] = ft
        GButton_513["fg"] = "#000000"
        GButton_513["justify"] = "center"
        GButton_513["text"] = "Pass/Fail Analysis "
        GButton_513.place(x=30,y=290,width=224,height=41)
        GButton_513["command"] = self.Pass_Fail

        GButton_84=tk.Button(self.root)
        GButton_84["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_84["font"] = ft
        GButton_84["fg"] = "#000000"
        GButton_84["justify"] = "center"
        GButton_84["text"] = "Semester wise performance"
        GButton_84.place(x=30,y=350,width=224,height=41)
        GButton_84["command"] = self.Semester_performance

        GButton_180=tk.Button(self.root)
        GButton_180["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_180["font"] = ft
        GButton_180["fg"] = "#000000"
        GButton_180["justify"] = "center"
        GButton_180["text"] = "Consecutive Year Score Prediction"
        GButton_180.place(x=30,y=410,width=224,height=41)
        GButton_180["command"] = self.Consecutive_Prediction


    def Performance_subject(self):
        newWindow = tk.Toplevel(self.root)
        Objective1(newWindow,self.model)


    def prediction_subject(self):
        newWindow = tk.Toplevel(self.root)
        Objective2(newWindow,self.model)


    def Backlog(self):
        newWindow = tk.Toplevel(self.root)
        Objective3(newWindow,self.model)


    def Pass_Fail(self):
        newWindow = tk.Toplevel(self.root)
        Objective4(newWindow,self.model)


    def Semester_performance(self):
        newWindow = tk.Toplevel(self.root)
        Objective5(newWindow,self.model)


    def Consecutive_Prediction(self):
        newWindow = tk.Toplevel(self.root)
        Objective6(newWindow,self.model)

if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    root.mainloop()
