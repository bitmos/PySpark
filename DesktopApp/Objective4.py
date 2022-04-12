import tkinter as tk
from  tkinter import ttk
import tkinter.font as tkFont

class Objective4:
    def __init__(self, root,model):
        self.model=model
        self.subcode=tk.StringVar()
        #setting title
        root.title("Pass/Fail Analysis")
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
        GLabel_189["text"] = "Result Analysis"
        GLabel_189.place(x=0,y=10,width=589,height=87)

        GLabel_312=tk.Label(root)
        ft = tkFont.Font(family='Times',size=33)
        GLabel_312["font"] = ft
        GLabel_312["fg"] = "#333333"
        GLabel_312["justify"] = "center"
        GLabel_312["text"] = "Subject code :-"
        GLabel_312.place(x=30,y=100,width=286,height=117)

        GLineEdit_856=ttk.Entry(root,text = "Enter Subject Code",textvariable=self.subcode,width=29,font=("Times",22))
        GLineEdit_856.place(x=310,y=140,width=197,height=41)

        GButton_229=tk.Button(root)
        GButton_229["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=33)
        GButton_229["font"] = ft
        GButton_229["fg"] = "#000000"
        GButton_229["justify"] = "center"
        GButton_229["text"] = "Visualize"
        GButton_229.place(x=200,y=250,width=173,height=45)
        GButton_229["command"] = self.GButton_229_command

    def GButton_229_command(self):
        self.model.Objective4(str(self.subcode.get()).upper())
        # print(str(self.subcode.get()).upper())

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
