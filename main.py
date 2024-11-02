from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x680+10+28')
        self.root.title('Face Recognition System')

        # First image
        img = Image.open(r'C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\panoramicwallpaper.png')
        img = img.resize((500, 130))
        # photo image insertion
        self.photoimg = ImageTk.PhotoImage(img)
        wallpaper_label1 = Label(self.root, image=self.photoimg)
        wallpaper_label1.place(x=0, y=0, width=500, height=130)

        # Second image
        img2 = Image.open(r'C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\panoramicwallpaper.png')
        # resizing image itself to show in window and resampling is compressing image to show in window
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        wallpaper_label2 = Label(self.root, image=self.photoimg2)
        wallpaper_label2.place(x=500, y=0, width=500, height=130)

# Third image
        img3 = Image.open(r'C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\panoramicwallpaper.png')
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        wallpaper_label3 = Label(self.root, image=self.photoimg3)
        wallpaper_label3.place(x=1000, y=0, width=500, height=130)

# Background image
        bg_img = Image.open(r'C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\background.png')
        bg_img = bg_img.resize((1380, 680), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        main_wallpaper_label = Label(self.root, image=self.photoimg_bg)
        main_wallpaper_label.place(x=0, y=130, width=1380, height=680)

        # Title label
        # title_label = Label(main_wallpaper_label, text="Snap Attendance", font=("Chomsky", 35, "bold"), bg='#888', fg="black")
        # title_label.place(x=0, y=0, width=1380, height=50)

#buttons at first row 

         # Add Student button
        add_student_button = Button(main_wallpaper_label, text="Add Student", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        add_student_button.place(x=200, y=100)

         # face recognizer
        detect_face_button = Button(main_wallpaper_label, text="Detect Face", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        detect_face_button.place(x=400, y=100)

         # attencdance
        attendance_button = Button(main_wallpaper_label, text="Take Attendance", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        attendance_button.place(x=600, y=100)

         # Help button
        help_button = Button(main_wallpaper_label, text="Need Assistance", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        help_button.place(x=800, y=100)

#buttons at second row  
        # Train System
        train_button = Button(main_wallpaper_label, text="Train Model", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        train_button.place(x=200, y=240)

        # Train System
        photos_button = Button(main_wallpaper_label, text="Trained Photos", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        photos_button.place(x=400, y=240)

        # Developer
        developer_button = Button(main_wallpaper_label, text="Developer", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        developer_button.place(x=600, y=240)

        # Exit
        exit_button = Button(main_wallpaper_label, text="Exit", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15)
        exit_button.place(x=800, y=240)



if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
