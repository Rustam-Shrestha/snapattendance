from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import os

class Register_Window:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Register Window")
        self.root.geometry("1360x768+0+0")  # Set the window size and position

        # Load and set the background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\bg2.jpeg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)  # Make the background image cover the entire window
        
       
    
        




# Main loop to run the application
if __name__ == '__main__':
    root = Tk()
    obj = Register_Window(root)
    root.mainloop()
