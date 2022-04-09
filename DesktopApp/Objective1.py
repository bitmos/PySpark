from tkinter import *
from PIL import ImageTk, Image

from Model import Model
root=Tk()
root.title("Graph")
root.geometry("400x200")
model=Model("Results_Data.csv")
model.Objective2("18ELE13")
root.mainloop()