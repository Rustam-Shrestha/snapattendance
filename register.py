from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import cv2
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768+0+0')
        self.root.title('Student Details System')

        # Form data variables
        self.dep_data = StringVar()
        self.sem_data = StringVar()
        self.course_data = StringVar()
        self.name_data = StringVar()
        self.sroll_data = StringVar()
        self.sdob_data = StringVar()
        self.sgender_data = StringVar()
        self.sphone_data = StringVar()
        self.saddress_data = StringVar()
        self.yes_photo = StringVar(value="No")

        # Header images
        img = Image.open(r'D:\old documents\snapattendance\assets\panoramicwallpaper.png')
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        wallpaper_label1 = Label(self.root, image=self.photoimg)
        wallpaper_label1.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r'D:\old documents\snapattendance\assets\panoramicwallpaper.png')
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        wallpaper_label2 = Label(self.root, image=self.photoimg2)
        wallpaper_label2.place(x=500, y=0, width=500, height=130)

        img3 = Image.open(r'D:\old documents\snapattendance\assets\panoramicwallpaper.png')
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        wallpaper_label3 = Label(self.root, image=self.photoimg3)
        wallpaper_label3.place(x=1000, y=0, width=500, height=130)

        # Background image
        bg_img = Image.open(r'D:\old documents\snapattendance\assets\background.png')
        bg_img = bg_img.resize((1380, 680), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        main_wallpaper_label = Label(self.root, image=self.photoimg_bg)
        main_wallpaper_label.place(x=0, y=130, width=1380, height=680)

        # Title label
        title_label = Label(main_wallpaper_label, text="New Student Details Form", font=("Chomsky", 35, "bold"), bg='#888', fg="black")
        title_label.place(x=0, y=0, width=1380, height=50)

        # Main frame
        frame = Frame(main_wallpaper_label, bg='#888', bd=2)
        frame.place(x=50, y=70, height=500, width=1280)

        # Left frame
        left_frame = LabelFrame(frame, bd=4, relief=RIDGE, fg="black", text="Student Details", font=('consolas', 12, "bold"))
        left_frame.place(x=10, y=10, width=598, height=480)

        img_left_panorama = Image.open(r'D:\old documents\snapattendance\assets\panoramicwallpaper_right.png')
        img_left_panorama = img_left_panorama.resize((600, 90), Image.Resampling.LANCZOS)
        self.panorama_left = ImageTk.PhotoImage(img_left_panorama)
        panorama_left_label = Label(left_frame, image=self.panorama_left)
        panorama_left_label.place(x=0, y=0, width=600, height=90)

        # Current course frame
        current_course_frame = LabelFrame(left_frame, bd=4, relief=RIDGE, fg="black", text="Current Courses Details", font=('consolas', 12, "bold"))
        current_course_frame.place(x=0, y=100, width=590, height=115)

        # Department dropdown
        department_label = Label(current_course_frame, text='Department', font=('consolas', 12, "bold"))
        department_label.grid(row=0, column=0, padx=10)
        department_combo = ttk.Combobox(current_course_frame, textvariable=self.dep_data, font=('consolas', 12, "bold"), width=17, state="readonly")
        department_combo['values'] = ('Select Department', "Data Science", "IOT", "Actuarial Science", "Quantum Computing")
        department_combo.current(0)
        department_combo.grid(row=0, column=1, padx=4, pady=10)

        # Semester dropdown
        semester_label = Label(current_course_frame, text='Semester', font=('consolas', 12, "bold"))
        semester_label.grid(row=0, column=2, padx=4)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.sem_data, font=('consolas', 12, "bold"), width=7, state="readonly")
        semester_combo['values'] = ('Select', "1st", "2nd", "3rd", "4th", '5th', '6th')
        semester_combo.current(0)
        semester_combo.grid(row=0, column=3)

        # Course dropdown
        course_label = Label(current_course_frame, text='Course', font=('consolas', 12, "bold"))
        course_label.grid(row=1, column=1, padx=4)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.course_data, font=('consolas', 12, "bold"), width=17, state="readonly")
        course_combo['values'] = ('Select Courses', "Bsc. DS", "Bsc. Robotics", "Bsc. Actuary", "Bsc. QC")
        course_combo.current(0)
        course_combo.grid(row=1, column=2, padx=4, pady=4)

        # Class student frame
        class_student_frame = LabelFrame(left_frame, bd=4, relief=RIDGE, fg="black", text="Class Student", font=('consolas', 12, "bold"))
        class_student_frame.place(x=0, y=214, width=590, height=240)

        # Name
        name_label = Label(class_student_frame, text='Student Name', font=('consolas', 12, "bold"))
        name_label.grid(row=0, column=0, padx=4)
        name_entry = ttk.Entry(class_student_frame, textvariable=self.name_data, width=20, font=('consolas', 12, "bold"))
        name_entry.grid(row=0, column=1, padx=4)

        # Roll number
        sroll_label = Label(class_student_frame, text='Student Rollno', font=('consolas', 12, "bold"))
        sroll_label.grid(row=0, column=2, padx=4)
        sroll_entry = ttk.Entry(class_student_frame, textvariable=self.sroll_data, width=20, font=('consolas', 12, "bold"))
        sroll_entry.grid(row=0, column=3, padx=2)

        # DOB
        sdob_label = Label(class_student_frame, text='DOB', width=10, font=('consolas', 12, "bold"))
        sdob_label.grid(row=1, column=0, padx=4)
        sdob_entry = DateEntry(class_student_frame, textvariable=self.sdob_data, width=18, font=('consolas', 12, "bold"), background='darkblue', foreground='white', borderwidth=2)
        sdob_entry.grid(row=1, column=1, padx=4)

        # Gender
        gender_label = Label(class_student_frame, text='Student Gender', font=('consolas', 12, "bold"))
        gender_label.grid(row=1, column=2, padx=4)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.sgender_data, font=('consolas', 12, "bold"), width=17, state="readonly")
        gender_combo['values'] = ('Neuter', "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=4, pady=4)

        # Phone
        sphone_label = Label(class_student_frame, text='Phone', font=('consolas', 12, "bold"))
        sphone_label.grid(row=2, column=0, padx=4)
        sphone_entry = ttk.Entry(class_student_frame, textvariable=self.sphone_data, width=20, font=('consolas', 12, "bold"))
        sphone_entry.grid(row=2, column=1, padx=4)

        # Address
        sadress_label = Label(class_student_frame, text='Address', width=10, font=('consolas', 12, "bold"))
        sadress_label.grid(row=2, column=2, padx=4)
        sadress_entry = Entry(class_student_frame, textvariable=self.saddress_data, width=20, font=('consolas', 12, "bold"), bg='white', fg='black', insertbackground='black')
        sadress_entry.grid(row=2, column=3, padx=4)

        # Photo sample
        snap_label = Label(class_student_frame, text='Snap photo', width=13, font=('consolas', 12, "bold"))
        snap_label.grid(row=3, column=0, padx=2)
        sphoto_yes = ttk.Radiobutton(class_student_frame, variable=self.yes_photo, text='Take Photo Sample', value='Yes')
        sphoto_yes.grid(row=3, column=1, padx=2, sticky='w')
        sphoto_no = ttk.Radiobutton(class_student_frame, variable=self.yes_photo, text='No photos', value='No')
        sphoto_no.grid(row=3, column=2, padx=2, sticky='w')

        # Buttons
        save_button = Button(class_student_frame, text='Save', command=self.add_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        save_button.grid(row=4, column=0, padx=4, pady=9, sticky='w')
        update_button = Button(class_student_frame, text='Update', command=self.update_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        update_button.grid(row=4, column=1, padx=4, pady=9, sticky='w')
        delete_button = Button(class_student_frame, text='Delete', command=self.delete_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        delete_button.grid(row=4, column=2, padx=4, pady=9, sticky='w')
        reset_button = Button(class_student_frame, text='Reset', command=self.reset_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        reset_button.grid(row=4, column=3, padx=4, pady=9, sticky='w')

        # Placeholder for photo buttons (disabled since cv2 is not used)
        photo_sample_button = Button(class_student_frame,command=self.generate_dataset, text='Take photo sample', bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        photo_sample_button.grid(row=5, column=1, padx=4, pady=9, sticky='w')
        u_photo_sample_button = Button(class_student_frame, text='Update Photo', bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2", state=DISABLED)
        u_photo_sample_button.grid(row=5, column=2, padx=4, pady=9, sticky='w')

        # Right frame
        right_frame = LabelFrame(frame, bd=4, relief=RIDGE, fg="black", text="Search Student", font=('consolas', 12, "bold"))
        right_frame.place(x=620, y=10, width=598, height=480)

        # Search section
        self.search_var = StringVar()
        self.search_value = StringVar()
        search_label = Label(right_frame, text='Search By', font=('consolas', 12, "bold"))
        search_label.grid(row=0, column=0, padx=10)
        search_combo = ttk.Combobox(right_frame, textvariable=self.search_var, font=('consolas', 12, "bold"), width=17, state="readonly")
        search_combo['values'] = ('select', "Phone", "Roll_no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=4, pady=10)

        searchparam_entry = ttk.Entry(right_frame, textvariable=self.search_value, width=20, font=('consolas', 12, "bold"))
        searchparam_entry.grid(row=0, column=2, padx=4)

        search_button = Button(right_frame, text='Search', command=self.search_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        search_button.grid(row=0, column=3, padx=10, pady=9, sticky='w')
        showAll_button = Button(right_frame, text='Show all', command=self.fetch_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        showAll_button.grid(row=1, column=0, padx=10, pady=9, sticky='w')

        # Table frame
        table_frame = Frame(right_frame, bd=4, relief=RIDGE)
        table_frame.place(x=5, y=120, width=580, height=320)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=("Department", "Course", "Semester", "Name", "Roll_no", "Gender", "Dob", "Phone", "Address", "Photo"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Headings
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll_no", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Dob", text="DOB")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Photo", text="Photo")
        self.student_table['show'] = "headings"

        # Column widths
        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Semester", width=70)
        self.student_table.column("Name", width=100)
        self.student_table.column("Roll_no", width=70)
        self.student_table.column("Gender", width=70)
        self.student_table.column("Dob", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=150)
        self.student_table.column("Photo", width=70)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_data)
        self.fetch_data()

    def add_data(self):
        if (self.dep_data.get() == "Select Department" or self.sem_data.get() == "Select" or
            self.course_data.get() == "Select Courses" or self.name_data.get() == "" or
            self.sroll_data.get() == "" or self.sdob_data.get() == "" or
            self.sgender_data.get() == "" or self.sphone_data.get() == "" or
            self.saddress_data.get() == ""):
            messagebox.showerror("Error", "All fields must be filled out", parent=self.root)
        elif not self.sphone_data.get().isdigit() or len(self.sphone_data.get()) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits", parent=self.root)
        else:
            try:
                with mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="",
                    database="snapattendance"
                ) as connection:
                    cursor = connection.cursor()
                    cursor.execute(
                        """
                        INSERT INTO students (department, course, semester, name, roll_no, gender, dob, phone, address, photo_sample)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            self.dep_data.get(),
                            self.course_data.get(),
                            self.sem_data.get(),
                            self.name_data.get(),
                            self.sroll_data.get(),
                            self.sgender_data.get(),
                            self.sdob_data.get(),
                            self.sphone_data.get(),
                            self.saddress_data.get(),
                            self.yes_photo.get()
                        )
                    )
                    connection.commit()
                    self.fetch_data()
                    self.reset_data()
                messagebox.showinfo("Success", "Student details saved successfully", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)

    def fetch_data(self):
        try:
            with mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="snapattendance"
            ) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT department, course, semester, name, roll_no, gender, dob, phone, address, photo_sample FROM students")
                rows = cursor.fetchall()
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", "end", values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)

    def get_data(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content.get('values', [])
        if data:
            self.dep_data.set(data[0])
            self.course_data.set(data[1])
            self.sem_data.set(data[2])
            self.name_data.set(data[3])
            self.sroll_data.set(data[4])
            self.sgender_data.set(data[5])
            self.sdob_data.set(data[6])
            self.sphone_data.set(data[7])
            self.saddress_data.set(data[8])
            self.yes_photo.set(data[9])

    def update_data(self):
        if (self.dep_data.get() == "Select Department" or self.sem_data.get() == "Select" or
            self.course_data.get() == "Select Courses" or self.name_data.get() == "" or
            self.sroll_data.get() == "" or self.sdob_data.get() == "" or
            self.sgender_data.get() == "" or self.sphone_data.get() == "" or
            self.saddress_data.get() == ""):
            messagebox.showerror("Error", "All fields must be filled out", parent=self.root)
        elif not self.sphone_data.get().isdigit() or len(self.sphone_data.get()) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits", parent=self.root)
        else:
            try:
                update_confirmation = messagebox.askyesno("Update", "Do you want to update student details?", parent=self.root)
                if update_confirmation:
                    with mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="",
                        database="snapattendance"
                    ) as connection:
                        cursor = connection.cursor()
                        cursor.execute(
                            """
                            UPDATE students
                            SET department=%s, course=%s, semester=%s, name=%s, gender=%s, dob=%s, phone=%s, address=%s, photo_sample=%s
                            WHERE roll_no=%s
                            """,
                            (
                                self.dep_data.get(),
                                self.course_data.get(),
                                self.sem_data.get(),
                                self.name_data.get(),
                                self.sgender_data.get(),
                                self.sdob_data.get(),
                                self.sphone_data.get(),
                                self.saddress_data.get(),
                                self.yes_photo.get(),
                                self.sroll_data.get()==id+1
                            )
                        )
                        connection.commit()
                        self.fetch_data()
                        self.reset_data()
                        messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)

    def delete_data(self):
        if self.sroll_data.get() == "":
            messagebox.showerror("Error", "Roll number required", parent=self.root)
        else:
            try:
                delete_confirmation = messagebox.askyesno("Delete", "Do you want to delete student details?", parent=self.root)
                if delete_confirmation:
                    with mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="",
                        database="snapattendance"
                    ) as connection:
                        cursor = connection.cursor()
                        cursor.execute("DELETE FROM students WHERE roll_no=%s", (self.sroll_data.get(),))
                        connection.commit()
                        self.fetch_data()
                        self.reset_data()
                        messagebox.showinfo("Success", "Student details deleted successfully", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)

    def reset_data(self):
        self.dep_data.set("Select Department")
        self.course_data.set("Select Courses")
        self.sem_data.set("Select")
        self.name_data.set("")
        self.sroll_data.set("")
        self.sgender_data.set("Neuter")
        self.sdob_data.set("")
        self.sphone_data.set("")
        self.saddress_data.set("")
        self.yes_photo.set("No")

    # generating dataset or taking photo samples
    def generate_dataset(self):
        if (self.dep_data.get() == "Select Department" or self.sem_data.get() == "Select" or
            self.course_data.get() == "Select Courses" or self.name_data.get() == "" or
            self.sroll_data.get() == "" or self.sdob_data.get() == "" or
            self.sgender_data.get() == "" or self.sphone_data.get() == "" or
            self.saddress_data.get() == ""):
            messagebox.showerror("Error", "All fields must be filled out", parent=self.root)
        elif not self.sphone_data.get().isdigit() or len(self.sphone_data.get()) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="",
                        database="snapattendance"
                    )
                cursor = conn.cursor()
                cursor.execute("select * from students")
                result=cursor.fetchall()
                id=0
                for x in result:
                    id+=1
                    cursor.execute(
                            """
                            UPDATE students
                            SET department=%s, course=%s, semester=%s, name=%s, gender=%s, dob=%s, phone=%s, address=%s, photo_sample=%s
                            WHERE roll_no=%s
                            """,
                            (
                                self.dep_data.get(),
                                self.course_data.get(),
                                self.sem_data.get(),
                                self.name_data.get(),
                                self.sgender_data.get(),
                                self.sdob_data.get(),
                                self.sphone_data.get(),
                                self.saddress_data.get(),
                                self.yes_photo.get(),
                                self.sroll_data.get()
                            )
                        )
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                    # losing predefined face data of frontal face fromopencv
                    face_classifier = cv2.CascadeClassifier("./assets/haarcascade_frontalface_default.xml")
                    def face_cropped(img):
                        # converting to grayscale 
                        grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        # scaling facotor 1.3  and minimum neighbor 5
                        faces = face_classifier.detectMultiScale(grayscale,1.3,5)
                        for(x,y,w,h) in faces:
                            # cropping the face from the image
                            face_cropped = img[y:y+h,x:x+w]
                            return face_cropped
                        # 0 IS FOR WEB CAMERS
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    # infinitely capture photos
                    while True:
                        # reading the frame
                        ret, my_frame = cap.read()
                        # converting to grayscale
                        ret, my_frame = cap.read()
                        cropped_face = face_cropped(my_frame)
                        if cropped_face is not None:
                            img_id += 1
                            face = cv2.resize(cropped_face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_path = f"dataset/user.{id}.{img_id}.jpg"
                            cv2.imwrite(file_path, face)  # Fixed typo: inwrite → imwrite
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()   
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating dataset completed!!", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)




    def search_data(self):
        if self.search_var.get() == "select" or self.search_value.get() == "":
            messagebox.showerror("Error", "Select search criteria and enter a value", parent=self.root)
        else:
            try:
                with mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="",
                    database="snapattendance"
                ) as connection:
                    cursor = connection.cursor()
                    column = "phone" if self.search_var.get() == "Phone" else "roll_no"
                    query = f"SELECT department, course, semester, name, roll_no, gender, dob, phone, address, photo_sample FROM students WHERE {column}=%s"
                    cursor.execute(query, (self.search_value.get(),))
                    rows = cursor.fetchall()
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", "end", values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)

if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()