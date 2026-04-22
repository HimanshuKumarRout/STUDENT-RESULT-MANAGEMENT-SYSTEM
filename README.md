
<div align="center">
  <h1>🎓 Student Result Management System</h1>
  <p>
    <strong>A Python Tkinter-based desktop application for managing students, courses, and academic results efficiently.</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" />
    <img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge" />
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&amp;logo=mysql&amp;logoColor=white" />
    <img src="https://img.shields.io/badge/Desktop-App-success?style=for-the-badge" />
  </p>
</div>

<br />

## 🌟 Overview

The **Student Result Management System** is a desktop-based application built using **Python (Tkinter)** and **MySQL** to streamline academic data management.

It enables institutions to efficiently manage **students, courses, and results** through a user-friendly graphical interface, making it ideal for educational projects and real-world small-scale systems.

---

## 🚀 Key Features

- 🔐 **Authentication System** – Secure login & registration for admins  
- 📚 **Course Management** – Add, update, or delete courses  
- 👨‍🎓 **Student Database** – Maintain detailed student records  
- 📝 **Result Processing** – Assign and manage student grades  
- 📊 **Dashboard UI** – Clean and interactive graphical interface  
- 🔍 **Search & View** – Easily access stored records  
- 📋 **Report Generation** – View academic performance  

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** (GUI Framework)
- **Pillow (PIL)** (Image handling)
- **MySQL** (Database)
- **mysql-connector-python**

---

## ⚙️ Prerequisites

Make sure you have:

- Python 3.x  
- MySQL Server  

Install required packages:

```bash id="v4u9d2"
pip install Pillow mysql-connector-python
````

---

## 🗄️ Database Setup

### 1️⃣ Create Database

```sql id="a2l9pq"
CREATE DATABASE `student_result_management_system`;
```

---

### 2️⃣ Configure Database Connection

Create a file named `db_config.py` in the root directory:

```python id="y1n0vx"
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "yourpassword"
DB_NAME = "student_result_management_system"
```

> ⚠️ Keep this file private (do not upload to GitHub)

---

## 💻 Installation & Usage

### 1️⃣ Clone Repository

```bash id="t6p3zo"
git clone https://github.com/your-username/student-result-management-system.git
cd student-result-management-system
```

---

### 2️⃣ Run the Application

```bash id="z9h1qx"
python main.py
```

---

## 📁 Project Structure

```text
STUDENT-RESULT-MANAGEMENT-SYSTEM/
├── main.py                  # Entry point
├── dashboard.py             # Main dashboard UI
├── authentication/
│   ├── login.py             # Login system
│   └── register.py          # Registration system
├── components/
│   ├── course.py            # Course management
│   ├── student.py           # Student management
│   ├── result.py            # Result processing
│   └── report.py            # Reports & performance
└── image/                   # UI assets
```

---

## 🖥️ Application Modules

| Module  | Description                   |
| ------- | ----------------------------- |
| Login   | Secure authentication system  |
| Course  | Manage course records         |
| Student | Store and update student data |
| Result  | Assign and manage marks       |
| Report  | Display performance analytics |

---

## 🔮 Future Enhancements

* 🔐 Role-based access (Admin/Teacher)
* 📊 Graphical analytics (charts)
* 📤 Export results (PDF/Excel)
* 🌐 Web-based version (Django/Flask)
* 📱 Mobile-friendly version

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create a branch (`feature/new-feature`)
3. Commit your changes
4. Push and open a Pull Request

---

## 👨‍💻 Author

**Himanshu Kumar Rout**

* GitHub: [https://github.com/HimanshuKumarRout](https://github.com/HimanshuKumarRout)
* Email: [himanshurout136@gmail.com](mailto:himanshurout136@gmail.com)

---

## ⭐ Support

If you found this project useful, please **star ⭐ the repository** and share it!

---

<p align="center">Built with 🎓 using Python & MySQL</p>
```
