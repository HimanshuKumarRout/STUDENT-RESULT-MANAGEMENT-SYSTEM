from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
from db_config import DB_HOST, DB_USER, DB_PASS, DB_NAME

class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

    #=====Title========
        title=Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)


    #======Variables======
        self.var_roll=StringVar()
        self.var_student=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks_obtained=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()


    #=====widgets========
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks_obtained=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")

        btn_search=Button(self.root,text="Search",font=("goudy old style",20),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=100,height=30)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20),bg="lightyellow",state="readonly").place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20),bg="lightyellow",state="readonly").place(x=280,y=220,width=320)
        txt_marks_obtained=Entry(self.root,textvariable=self.var_marks_obtained,font=("goudy old style",20),bg="lightyellow").place(x=280,y=280,width=320)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20),bg="lightyellow").place(x=280,y=340,width=320)


    #=====Buttons========
        btn_add=Button(self.root,text="Submit",font=("goudy old style",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=40)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=40)


    #=====images========
        self.img_right=Image.open("image/result.jpg")
        self.img_right=self.img_right.resize((500,300))
        self.img_right=ImageTk.PhotoImage(self.img_right)

        self.lbl_img=Label(self.root,image=self.img_right,bg="white")
        self.lbl_img.place(x=650,y=100)


    #=====functions========
    def fetch_roll(self):
        try:
            con = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
            cur = con.cursor()
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def search(self):
        try:
            con = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
            cur = con.cursor()
            cur.execute("select name,course from student where roll=%s", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def add(self):
        try:
            # Basic validations
            if self.var_roll.get() == "" or self.var_roll.get() == "Select":
                messagebox.showerror("Error", "Please select a student", parent=self.root)
                return
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please search student record", parent=self.root)
                return
            if self.var_marks_obtained.get() == "" or self.var_full_marks.get() == "":
                messagebox.showerror("Error", "Please enter marks and full marks", parent=self.root)
                return
            # Validate numeric marks
            try:
                marks = int(self.var_marks_obtained.get())
                full_marks = int(self.var_full_marks.get())
            except ValueError:
                messagebox.showerror("Error", "Marks and Full Marks must be integers", parent=self.root)
                return
            if full_marks <= 0:
                messagebox.showerror("Error", "Full Marks must be greater than 0", parent=self.root)
                return
            if marks < 0 or marks > full_marks:
                messagebox.showerror("Error", "Marks must be between 0 and Full Marks", parent=self.root)
                return
            con = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
            cur = con.cursor()
            # Check if result already exists for this roll
            cur.execute("select * from result where roll=%s", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Result already present", parent=self.root)
                con.close()
                return
            # Insert result (excluding course since table has no `course` column)
            percentage = (marks / full_marks) * 100
            cur.execute(
                "insert into result(roll, name, course, marks_obtained, full_marks, percentage) values(%s, %s, %s, %s, %s, %s)",
                (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    marks,
                    full_marks,
                    str(percentage),
                ),
            )
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Result added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks_obtained.set("")
        self.var_full_marks.set("")



if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()