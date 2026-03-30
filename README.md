# Student Result Management System

A comprehensive desktop-based Python application built with Tkinter for schools and educational institutions to manage courses, students, and their academic results.

## 🚀 Features

- **Secure Authentication System**: Separate login and registration panels for teachers/administrators.
- **Course Management**: Easily add, edit, or delete various courses offered by the institution.
- **Student Database**: Register students and maintain a detailed, searchable database of their personal and academic profiles.
- **Result Processing**: Compute, publish, and manage grades matching specific student IDs to their enrolled subjects.
- **Graphical Dashboard**: An intuitive, visually appealing user interface utilizing clean layouts and sidebar navigations.

## 🛠️ Technology Stack

- **Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Image Processing:** Pillow (PIL)
- **Database:** MySQL

## ⚙️ Prerequisites

Before you get started, ensure you have the following installed on your machine:
- Python 3.x
- MySQL Server

Additionally, you need to install the required Python dependencies:
```bash
pip install Pillow mysql-connector-python
```

## 🗄️ Database Setup

1. Open your MySQL client (e.g., MySQL Workbench, phpMyAdmin, or terminal).
2. Create a fresh database named `student-result-management-system`:
   ```sql
   CREATE DATABASE `student-result-management-system`;
   ```
3. Since database credentials are kept private and excluded from this repository for security, right before running the application you need to create a new file named `db_config.py` in the root directory.
4. Add the following Python configuration variables into your `db_config.py`, filling in your local MySQL settings:
   ```python
   DB_HOST = "localhost"
   DB_USER = "root"
   DB_PASS = "YourPassword123!"
   DB_NAME = "student-result-management-system"
   ```
*Note: Ensure your `teacher` and other corresponding tables are properly initialized!*


## 💻 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/student-result-management-system.git
   cd student-result-management-system
   ```

2. **Run the application:**
   Launch the system via the provided entry point script situated in the root directory:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
STUDENT RESULT MANAGEMENT SYSTEM/
│
├── main.py                     # Primary entry point for launching the app
├── dashboard.py                # Main administrative dashboard
├── authentication/             # User authentication logic
│   ├── login.py                # Login interface & verification
│   └── register.py             # Administrator registration interface
├── components/                 # Core modular dashboard sections
│   ├── course.py               # Course management
│   ├── student.py              # Student data management
│   ├── result.py               # Exam results processing
│   └── report.py               # View student performance
└── image/                      # Application icons and background assets
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page and open a pull request.
