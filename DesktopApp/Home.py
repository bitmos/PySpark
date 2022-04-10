import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_653=tk.Label(root)
        GLabel_653["activebackground"] = "#a75454"
        GLabel_653["activeforeground"] = "#954747"
        ft = tkFont.Font(family='Times',size=54)
        GLabel_653["font"] = ft
        GLabel_653["fg"] = "#040404"
        GLabel_653["justify"] = "center"
        GLabel_653["text"] = "Result Analysis"
        GLabel_653["relief"] = "flat"
        GLabel_653.place(x=80,y=20,width=424,height=52)

        GButton_887=tk.Button(root)
        GButton_887["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_887["font"] = ft
        GButton_887["fg"] = "#000000"
        GButton_887["justify"] = "center"
        GButton_887["text"] = "Performance in a subject"
        GButton_887.place(x=30,y=110,width=124,height=41)
        GButton_887["command"] = self.GButton_887_command

        GButton_637=tk.Button(root)
        GButton_637["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_637["font"] = ft
        GButton_637["fg"] = "#000000"
        GButton_637["justify"] = "center"
        GButton_637["text"] = "Performance prediction of a subject"
        GButton_637.place(x=30,y=170,width=124,height=41)
        GButton_637["command"] = self.GButton_637_command

        GButton_932=tk.Button(root)
        GButton_932["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#000000"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "Backlog Analysis"
        GButton_932.place(x=30,y=230,width=124,height=41)
        GButton_932["command"] = self.GButton_932_command

        GButton_513=tk.Button(root)
        GButton_513["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_513["font"] = ft
        GButton_513["fg"] = "#000000"
        GButton_513["justify"] = "center"
        GButton_513["text"] = "Pass/Fail Analysis "
        GButton_513.place(x=30,y=290,width=124,height=41)
        GButton_513["command"] = self.GButton_513_command

        GButton_84=tk.Button(root)
        GButton_84["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_84["font"] = ft
        GButton_84["fg"] = "#000000"
        GButton_84["justify"] = "center"
        GButton_84["text"] = "Semester wise performance"
        GButton_84.place(x=30,y=350,width=124,height=41)
        GButton_84["command"] = self.GButton_84_command

        GButton_180=tk.Button(root)
        GButton_180["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_180["font"] = ft
        GButton_180["fg"] = "#000000"
        GButton_180["justify"] = "center"
        GButton_180["text"] = "Consecutive  Year Score Prediction "
        GButton_180.place(x=30,y=410,width=124,height=41)
        GButton_180["command"] = self.GButton_180_command

    def GButton_887_command(self):
        print("command")


    def GButton_637_command(self):
        print("command")


    def GButton_932_command(self):
        print("command")


    def GButton_513_command(self):
        print("command")


    def GButton_84_command(self):
        print("command")


    def GButton_180_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
