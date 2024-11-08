from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
# for this we need to install pip install mysql-connector-python


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768+0+0')
        self.root.title('Student Details System')

# form data variables
        self.dep_data = StringVar()
        self.sem_data = StringVar()
        self.course_data = StringVar()
        self.sid_data = StringVar()
        self.sname_data = StringVar()
        self.sroll_data = StringVar()
        self.sdob_data = StringVar()
        self.sgender_data = StringVar()
        self.sphone_data = StringVar()
        self.saddress_data = StringVar()



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
        title_label = Label(main_wallpaper_label, text="New Student Details Form", font=("Chomsky", 35, "bold"), bg='#888', fg="black")
        title_label.place(x=0, y=0, width=1380, height=50)

        # frame for form input field
        frame = Frame(main_wallpaper_label, bg='#888', bd=2)
        frame.place(x=50,y=70,height=500, width=1280)

        # left side of the window part
        left_frame = LabelFrame(frame, bd=4, relief=RIDGE, fg="black", text="Student Details", font=('consolas', 12, "bold"))
        left_frame.place(x=10, y=10, width=598, height=500)  # Added height for visibility
# image under the left frame
        img_left_panorama = Image.open(r'C:\Users\Rustam Shrestha\OneDrive - Tribhuvan University\Documents\snapattendance\assets\panoramicwallpaper_right.png')
        img_left_panorama = img_left_panorama.resize((600, 90), Image.Resampling.LANCZOS)
        self.panorama_left = ImageTk.PhotoImage(img_left_panorama)
        panorama_left_label = Label(left_frame, image=self.panorama_left)
        panorama_left_label.place(x=0, y=0, width=600, height=90)

        current_course_frame = LabelFrame(left_frame, bd=4, relief=RIDGE, fg="black", text="Current Courses Details", font=('consolas', 12, "bold"))
        current_course_frame.place(x=0, y=100, width=590, height=115)  # Added height for visibility

# department dropdown
        dept_label =Label(current_course_frame,text='Department',font=('consolas', 12, "bold"))
        dept_label.grid(row=0, column=0, padx=10)
        dept_combo = ttk.Combobox(current_course_frame,textvariable=self.dep_data, font=('consolas', 12, "bold"), width=17, state="readonly")
        dept_combo['values']=('Select Department', "Data Science", "IOT", "Actuarial Science","Quantum Computing")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=4, pady=10)

        
# semester dropdown
        semester_label =Label(current_course_frame,textvariable=self.sem_data,text='Semester',font=('consolas', 12, "bold"))
        semester_label.grid(row=0, column=2, padx=4)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.sem_data, font=('consolas', 12, "bold"), width=7, state="readonly")
        semester_combo['values']=('Select', "1st", "2nd", "3rd","4th", '5th', '6th')
        semester_combo.current(0)
        semester_combo.grid(row=0, column=3)
# course dropdown
        course_label =Label(current_course_frame,text='Course',font=('consolas', 12, "bold"))
        course_label.grid(row=1, column=1, padx=4)
        # course dropdown
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.course_data, font=('consolas', 12, "bold"), width=17, state="readonly")
        course_combo['values'] = ('Select Courses', "Bsc. DS", "Bsc. Robotics", "Bsc. Actuary", "Bsc. QC")
        course_combo.current(0)
        course_combo.grid(row=1, column=2, padx=4, pady=4)

        

        
        # right side of window
        right_frame = LabelFrame(frame, bd=4, relief=RIDGE, fg="black", text="Student Details", font=('consolas', 12, "bold"))
        right_frame.place(x=620, y=10, width=600, height=500)  # Added height for visibility

# class student information
        # for sid
        class_student_frame = LabelFrame(left_frame, bd=4, relief=RIDGE, fg="black", text="Class Student", font=('consolas', 12, "bold"))
        class_student_frame.place(x=0, y=214, width=590, height=240)  # Added height for visibility
        sid_label =Label(class_student_frame,text='Student Id',font=('consolas', 12, "bold"))
        sid_label.grid(row=0, column=0, padx=4)
        sid_entry = ttk.Entry(class_student_frame,textvariable=self.sid_data,width=13, font=('consolas', 12, "bold"))
        sid_entry.grid(row=0, column=1, padx=4)
# class student information
        # for name
        sname_label =Label(class_student_frame,text='Student Name',font=('consolas', 12, "bold"))
        sname_label.grid(row=0, column=2, padx=4)
        sname_entry = ttk.Entry(class_student_frame,textvariable=self.sname_data,width=13, font=('consolas', 12, "bold"))
        sname_entry.grid(row=0, column=3, padx=4)

# next row
        # for rollnumber
        sroll_label =Label(class_student_frame,text='Student Rollno',font=('consolas', 12, "bold"))
        sroll_label.grid(row=1, column=0, padx=4)
        sroll_entry = ttk.Entry(class_student_frame,textvariable=self.sroll_data,width=13, font=('consolas', 12, "bold"))
        sroll_entry.grid(row=1, column=1, padx=2)

        # for ddobob
        sdob_label =Label(class_student_frame,text='DOB.', width=10,font=('consolas', 12, "bold"))
        sdob_label.grid(row=1, column=2, padx=4)
        sdob_entry = DateEntry(class_student_frame,textvariable=self.sdob_data, width=11, font=('consolas', 12, "bold"), background='darkblue', foreground='white', borderwidth=2)
        sdob_entry.grid(row=1, column=3, padx=4)

# next row
        # for Gender
        gender_label =Label(class_student_frame,text='Student Gender',font=('consolas', 12, "bold"))
        gender_label.grid(row=3, column=0, padx=4)
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.sgender_data, font=('consolas', 12, "bold"),width=11, state="readonly")
        gender_combo['values']=('Neuter', "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1, padx=4, pady=4)

        # for phone
        sphone_label =Label(class_student_frame,text='Phone',font=('consolas', 12, "bold"))
        sphone_label.grid(row=3, column=2, padx=4)
        sphone_entry = ttk.Entry(class_student_frame,textvariable=self.sphone_data,width=13, font=('consolas', 12, "bold"))
        sphone_entry.grid(row=3, column=3, padx=4)

# next row
        # for address
        sadress_label =Label(class_student_frame,text='Address', width=10,font=('consolas', 12, "bold"))
        sadress_label.grid(row=4, column=0, padx=4)
        sadress_entry = ttk.Entry(class_student_frame,textvariable=self.saddress_data,width=13, font=('consolas', 12, "bold"), background='darkblue', foreground='white')
        sadress_entry.grid(row=4, column=1, padx=4)

        snap_label =Label(class_student_frame,text='Snap photo',width=13,font=('consolas', 12, "bold"))
        snap_label.grid(row=4, column=2, padx=2)
        # Radio Buttons for Photo Sample
        self.yes_photo=StringVar()
        sphoto_yes = ttk.Radiobutton(class_student_frame,variable=self.yes_photo, text='Take Photo Sample', value='Yes')
        sphoto_yes.grid(row=4, column=2, padx=2, sticky='w')

        sphoto_no = ttk.Radiobutton(class_student_frame,variable=self.yes_photo, text='No photos', value='No')
        sphoto_no.grid(row=4, column=3, padx=2, sticky='w')

       
       # cerating a more customizable button
        save_button = Button(class_student_frame, text='Save',command=self.add_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        save_button.grid(row=6, column=0, padx=4,pady=9, sticky='w')
       # update button
        update_button = Button(class_student_frame, text='Update',command=self.update_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        update_button.grid(row=6, column=1, padx=4,pady=9, sticky='w')
       # delete button
        delete_button = Button(class_student_frame, text='Delete',command=self.delete_data, bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        delete_button.grid(row=6, column=2, padx=4,pady=9, sticky='w')
       # reset button
        reset_button = Button(class_student_frame, text='Reset', bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        reset_button.grid(row=6, column=3, padx=4,pady=9, sticky='w')

       #t photo sample takingbutton
        photo_sample_button = Button(class_student_frame, text='Take photo sample', bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        photo_sample_button.grid(row=7, column=1, padx=4,pady=9, sticky='w')
       # photo sample updating buton
        u_photo_sample_button = Button(class_student_frame, text='Update Photo', bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        u_photo_sample_button.grid(row=7, column=2, padx=4,pady=9, sticky='w')

      

# right side of window
        right_frame = LabelFrame(frame, bd=4, relief=RIDGE, fg="black", text="Search Student", font=('consolas', 12, "bold"))
        right_frame.place(x=620, y=10, width=598, height=500)  # Added height for visibility
        
        search_label =Label(right_frame,text='Search By',font=('consolas', 12, "bold"))
        search_label.grid(row=0, column=0, padx=10)
        search_combo = ttk.Combobox(right_frame, font=('consolas', 12, "bold"), width=17, state="readonly")
        search_combo['values']=('select', "Phone no", "Roll no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=4, pady=10)
        
        searchparam_entry = ttk.Entry(right_frame  ,width=13, font=('consolas', 12, "bold"), background='darkblue', foreground='white')
        searchparam_entry.grid(row=0, column=2, padx=4)

        # search button
        search_button = Button(right_frame, text='Search', bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        search_button.grid(row=0, column=3, padx=10,pady=9, sticky='w')
       # show all button
        showAll_button = Button(right_frame, text='Show all', bg="#dc143c", fg="white", font=('consolas', 12, "bold"), cursor="hand2")
        showAll_button.grid(row=1, column=0, padx=10,pady=9, sticky='w')

 # Table frame
        table_frame = Frame(right_frame, bd=4, relief=RIDGE)
        table_frame.place(x=5, y=120, width=598, height=320)  # Added height for visibility

        # Vertical and horizontal scrolling
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Assuming table_frame, scroll_x, and scroll_y are already defined
        self.student_table = ttk.Treeview(
        table_frame,
        columns=("Department", "course", "semester", "id", "name", "roll no", "gender", "dob", "address", "photo"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )

        # Setting up the headings for the Treeview columns
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll no", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Dob")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo")
        self.student_table['show'] = "headings"

        # Adjusting the width of the columns
        self.student_table.column("Department")
        self.student_table.column("course")
        self.student_table.column("semester")
        self.student_table.column("id")
        self.student_table.column("name")
        self.student_table.column("roll no")
        self.student_table.column("gender")
        self.student_table.column("dob")
        self.student_table.column("address")
        self.student_table.column("photo")

        # Adding scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configuring the scrollbars
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Packing the Treeview widget
        self.student_table.pack(fill=BOTH, expand=1)

        # Setting up the headings for the Treeview columns
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll no", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Dob")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo")
        self.student_table['show'] = "headings"

        # Adjusting the width of the columns
        self.student_table.column("Department", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("semester", width=70)
        self.student_table.column("id", width=30)
        self.student_table.column("name", width=100)
        self.student_table.column("roll no", width=70)
        self.student_table.column("gender", width=70)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=150)
        self.student_table.column("photo", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        # binding the parameters with the cursor((data that we have in our databse))
        # binding with input fields from database for making update later 
        self.student_table.bind("<ButtonRelease>", self.get_data)
        self.fetch_data()
        

        # function for taking and adding data
    def add_data(self):
        if ( self.dep_data.get()=="Select Department" or  self.sem_data.get()=="Select" or  self.course_data.get()=="Select Courses" or
                        self.sid_data.get()=="" or  self.sname_data.get()=="" or  self.sroll_data.get()=="" or
                        self.sdob_data.get()=="" or  self.sgender_data.get()=="" or  self.sphone_data.get()== "" or
                        self.saddress_data.get()==""):
                messagebox.showerror("Error", "All fields must be filled out", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="admin", database="snapattendance")
                connection_obj=connection.cursor()
                connection_obj.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.dep_data.get(),self.course_data.get(),self.sem_data.get(),self.sid_data.get(),self.sname_data.get(),self.sroll_data.get(),self.sgender_data.get(),self.sdob_data.get(),self.sphone_data.get(), self.saddress_data.get(), self.yes_photo.get()))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success","Student details have been saved successfully",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)



                # fetching data from the mysql table and 
                # showing in the gui table
    def fetch_data(self):
        # Start the connection
        connection = mysql.connector.connect(
                host="localhost", 
                username="root", 
                password="admin", 
                database="snapattendance"
        )
        connection_obj = connection.cursor()
        
        # Fetch all data
        connection_obj.execute("SELECT * FROM students")
        student_data = connection_obj.fetchall()  # Corrected to fetchall()
        # print("Fetched data:", student_data)  

        # Populate the table with values
        if len(student_data) != 0:
                # Delete previous values and add new ones
                self.student_table.delete(*self.student_table.get_children())
                for row in student_data:
                        # Insert each row as an entry in the table
                        self.student_table.insert("", "end", values=row)
        
        # Close the cursor and connection after inserting data
        connection_obj.close()
        connection.close()
    
#     getr all the data to the input fields 
    def get_data(self,event=""):
        db_data = self.student_table.focus()
        content= self.student_table.item(db_data)
        data=content['values']
        self.dep_data.set(data[0])
        self.course_data.set(data[1])
        self.sem_data.set(data[2])
        self.sid_data.set(data[3])
        self.sname_data.set(data[4])
        self.sroll_data.set(data[5])
        self.sgender_data.set(data[6])
        self.sdob_data.set(data[7])
        self.sphone_data.set(data[8])
        self.saddress_data.set(data[9])
        self.yes_photo.set(data[10])

# updating funciton
    def update_data(self):
        if ( self.dep_data.get()=="Select Department" or  self.sem_data.get()=="Select" or  self.course_data.get()=="Select Courses" or
                self.sid_data.get()=="" or  self.sname_data.get()=="" or  self.sroll_data.get()=="" or
                self.sdob_data.get()=="" or  self.sgender_data.get()=="" or  self.sphone_data.get()== "" or
                self.saddress_data.get()==""):
             messagebox.showerror("Error", "All fields must be filled out", parent=self.root)
        else:
             try:
                update_confirmation = messagebox.askyesno("Update","Do you really want to update student details?",parent=self.root)
                if update_confirmation> 0:
                        connection = mysql.connector.connect(host="localhost", username="root", password="admin", database="snapattendance")
                        connection_obj=connection.cursor()
                        connection_obj.execute(
    "UPDATE students SET dept=%s, course=%s, semester=%s, student_id=%s, sname=%s, roll=%s, gender=%s, dob=%s, phone=%s, address=%s, photo_sample=%s WHERE student_id=%s",
    (
        self.dep_data.get(),
        self.course_data.get(),
        self.sem_data.get(),
        self.sid_data.get(),
        self.sname_data.get(),
        self.sroll_data.get(),
        self.sgender_data.get(),
        self.sdob_data.get(),
        self.sphone_data.get(),
        self.saddress_data.get(),
        self.yes_photo.get(),
        self.sid_data.get()  
        # the student_id is the primary key and used to identify the record to update
        # sow riting it last to be updated
    )
)

                else:
                        if not update_confirmation:
                             return
                messagebox.showinfo("Success","Successfully updated student details",parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()
             except Exception as ex:
                        messagebox.showerror("Error", f"error: {str(ex)}",parent=self.root)

                        connection.commit()


# updating funciton
    def delete_data(self):
        if (self.sid_data.get()==""):
             messagebox.showerror("Error", "Sid required", parent=self.root)
        else:
             try:
                delete_confirmation = messagebox.askyesno("Delete","Do you really want to Delete student details?",parent=self.root)
                
                if delete_confirmation > 0:
                        connection = mysql.connector.connect(host="localhost", username="root", password="admin", database="snapattendance")
                        connection_obj = connection.cursor()
                        value = (self.sid_data.get(),)  # Wrap value in a tuple
                        sql = "DELETE FROM students WHERE student_id=%s"  # Corrected table name
                        connection_obj.execute(sql, value)
                        connection.commit()  # Commit the transaction
                        self.fetch_data()
                else:
                        if not delete_confirmation:
                                return

                        connection.commit()
                        self.fetch_data()
                        connection.close()
                        messagebox.showinfo("Success","Successfully Deleted student details",parent=self.root)
             except Exception as ex:
                        messagebox.showerror("Error", f"error: {str(ex)}",parent=self.root)

                        connection.commit()
                       
                       

if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
