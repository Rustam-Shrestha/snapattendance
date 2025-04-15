# Import necessary modules
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry  # For selecting dates easily

# Student class definition
class Student:
    def __init__(self, root):
        """Initializes the student management window"""
        self.root = root
        self.root.geometry("900x500+250+100")  # Set window size and position
        self.root.title("Student Management System")

        # Background Label
        self.bg_label = Label(self.root, text="Student Management", font=("JetBrains Mono", 20, "bold"), bg="#0f4c75", fg="white")
        self.bg_label.pack(fill=X)

        # Label and Entry for Student Name
        name_label = Label(self.root, text="Name:", font=("Arial", 14))
        name_label.place(x=50, y=80)
        self.name_entry = Entry(self.root, font=("Arial", 14))
        self.name_entry.place(x=200, y=80, width=200)

        # Label and Calendar for Date of Birth
        dob_label = Label(self.root, text="Date of Birth:", font=("Arial", 14))
        dob_label.place(x=50, y=130)
        self.dob_entry = DateEntry(self.root, font=("Arial", 14), date_pattern="yyyy-mm-dd")
        self.dob_entry.place(x=200, y=130, width=200)

        # Gender Dropdown
        gender_label = Label(self.root, text="Gender:", font=("Arial", 14))
        gender_label.place(x=50, y=180)
        self.gender_combo = ttk.Combobox(self.root, font=("Arial", 14), state="readonly", values=["Male", "Female", "Other"])
        self.gender_combo.place(x=200, y=180, width=200)
        self.gender_combo.current(0)

        # Save Button
        save_button = Button(self.root, text="Save", font=("Arial", 14, "bold"), bg="green", fg="white", command=self.save_student)
        save_button.place(x=200, y=230, width=100)

    def save_student(self):
        """Handles saving student details (Placeholder function)"""
        name = self.name_entry.get()
        dob = self.dob_entry.get()
        gender = self.gender_combo.get()
        print(f"Student Details: Name: {name}, DOB: {dob}, Gender: {gender}")

# Main Application Class
class Face_Recognition_System:
    def __init__(self, root):
        """Initializes the face recognition system UI"""
        self.root = root
        self.root.geometry('1300x680+10+28')
        self.root.title('Face Recognition System')

        # Load the first header image
        img1 = Image.open("assets/panoramicwallpaper.png").resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)

        # Load the second header image
        img2 = Image.open("assets/panoramicwallpaper.png").resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)

        # Load the third header image
        img3 = Image.open("assets/panoramicwallpaper.png").resize((500, 130))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=500, height=130)

        # Load background image
        bg_img = Image.open("assets/background.png").resize((1380, 680))
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        Label(self.root, image=self.photoimg_bg).place(x=0, y=130, width=1380, height=680)

        # Title Label
        title_label = Label(self.root, text="Snap Attendance", font=("Chomsky", 35, "bold"), bg='#888', fg="black")
        title_label.place(x=0, y=130, width=1380, height=50)

        # Row 1 Buttons
        Button(self.root, text="Add Student", command=self.student_details, font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15).place(x=200, y=200)
        Button(self.root, text="Detect Face", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15).place(x=400, y=200)
        Button(self.root, text="Take Attendance", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15).place(x=600, y=200)
        Button(self.root, text="Need Assistance", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15).place(x=800, y=200)

        # Row 2 Buttons
        Button(self.root, text="Train Model", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15).place(x=200, y=280)
        Button(self.root, text="Trained Photos", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15).place(x=400, y=280)
        Button(self.root, text="Developer", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15).place(x=600, y=280)
        Button(self.root, text="Exit", font=("Jetbrains Mono", 15, "bold"), bg='#dc143c', fg='white', cursor='hand2', width=15, command=self.root.quit).place(x=800, y=280)

    def student_details(self):
        """Opens the Student Management Window"""
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

# Run Application
if __name__ == '__main__':
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
