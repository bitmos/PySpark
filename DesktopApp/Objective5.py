import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=590
        height=348
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_189=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_189["font"] = ft
        GLabel_189["fg"] = "#333333"
        GLabel_189["justify"] = "center"
        GLabel_189["text"] = "Semester-Wise"
        GLabel_189.place(x=0,y=10,width=590,height=59)

        GLabel_312=tk.Label(root)
        ft = tkFont.Font(family='Times',size=33)
        GLabel_312["font"] = ft
        GLabel_312["fg"] = "#333333"
        GLabel_312["justify"] = "center"
        GLabel_312["text"] = "Subject code :-"
        GLabel_312.place(x=30,y=130,width=286,height=117)

        GLineEdit_856=tk.Entry(root)
        GLineEdit_856["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=33)
        GLineEdit_856["font"] = ft
        GLineEdit_856["fg"] = "#333333"
        GLineEdit_856["justify"] = "center"
        GLineEdit_856["text"] = "Enter code"
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

        GLabel_637=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_637["font"] = ft
        GLabel_637["fg"] = "#333333"
        GLabel_637["justify"] = "center"
        GLabel_637["text"] = "Performance Analysis"
        GLabel_637.place(x=0,y=30,width=594,height=129)

    def GButton_229_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
