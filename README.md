"# snapattendance" 

## Installed Dependencies

- `pip install opencv-python`
- `pip install tkinter`
- `pip install mysql`
- `pip install mysql-connector-python`
- `pip install tkcalendar`
- `pip install pillow`
- `pip install opencv-python`

---

## Features

- GUI
- Add student
- Delete student
- View student
- Update student
- Reset form


#database code
CREATE DATABASE snapattendance;
USE snapattendance;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    roll_no VARCHAR(70),
    gender VARCHAR(70),
    dob DATE,
    phone VARCHAR(15), -- Added missing phone number field
    address VARCHAR(150),
    department VARCHAR(100),
    course VARCHAR(100),
    semester VARCHAR(70),
    photo_sample VARCHAR(10) -- Stores 'Yes' or 'No' from radio buttons
);