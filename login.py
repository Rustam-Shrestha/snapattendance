from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import os

class Login_Window:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1366x768+0+0")  # Set the window size and position

        # Load and set the background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\background.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)  # Make the background image cover the entire window

        # Create a frame for the login form
        frame = Frame(self.root, bg="#004747")
        frame.place(x=610, y=170, width=350, height=450)

        # Create a canvas to draw the circle for the user icon
        canvas = Canvas(frame, width=70, height=70, bg="#004747", highlightthickness=0)
        canvas.place(x=140, y=20)  # Position the canvas

        try:
            # Draw a white circle on the canvas
            canvas.create_oval(10, 10, 70, 70, fill="white", outline="")

            # Path to the user icon image
            image_path = r"C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\usericon.jpg"

            if os.path.exists(image_path):
                # Open and resize the image
                img = Image.open(image_path).resize((45,45), Image.Resampling.LANCZOS)

                # Create a mask for rounded corners
                mask = Image.new("L", img.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 70, 70), fill=255)

                # Apply the mask to the image to make it round
                img.putalpha(mask)

                # Convert the image to a format Tkinter can use
                self.user_icon = ImageTk.PhotoImage(img)
                # Place the image on the canvas
                canvas.create_image(40, 40, image=self.user_icon)
            else:
                raise FileNotFoundError(f"File not found: {image_path}")
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            # Optionally, you can use a default placeholder image if the file is not found
            # self.user_icon = ImageTk.PhotoImage(file="path_to_default_image.jpg")
            # canvas.create_image(40, 40, image=self.user_icon)

        # Add a label and entry field for the username
        username_label = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="#004747", fg="white")
        username_label.place(x=50, y=100)

        self.username_entry = ttk.Entry(frame, font=("times new roman", 15))
        self.username_entry.place(x=50, y=130, width=250)

        # Add a label and entry field for the password
        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="#004747", fg="white")
        password_label.place(x=50, y=180)

        self.password_entry = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.password_entry.place(x=50, y=210, width=250)

        login_btn = Button(frame,command=self.login,text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="white", fg="black")
        login_btn.place(x=100, y=280, width=150, height=40)


        # Registration buttons
        register_btn = Button(frame, text="Register", font=("times new roman", 15, "normal"), bd=0, bg=frame.cget("bg"), highlightthickness=0, activebackground=frame.cget("bg"), fg="white")
        register_btn.place(x=-15, y=320, width=170)

        # Forgor passwordf  buttons
        forgot_btn = Button(frame, text="Forgot password", font=("times new roman", 15, "normal"),bd=0, bg=frame.cget("bg"), highlightthickness=0, activebackground=frame.cget("bg"), fg="white")
        forgot_btn.place(x=20, y=360, width=170)

    def login(self):
        if(self.username_entry.get()=="" or self.password_entry.get()==""):
            messagebox.showerror("Error", "Please fill in all fields required")
        elif(self.username_entry.get()=="Rustam" and self.password_entry.get()=="1234"):
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showerror("invalid", "invalid username and password")
                




# Main loop to run the application
if __name__ == '__main__':
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
