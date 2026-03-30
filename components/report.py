from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
try:
    from db_config import DB_HOST, DB_USER, DB_PASS, DB_NAME
except ModuleNotFoundError:
    import sys
    sys.path.append("..")
    from db_config import DB_HOST, DB_USER, DB_PASS, DB_NAME


class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

    #=====Title========
        title=Label(self.root,text="View Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)


    #======Search======
        self.var_search=StringVar()
        self.var_id=""
        
        lbl_search=Label(self.root,text="Enter Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=300,y=100)
        txt_search=Entry(self.root,font=("goudy old style",15),bg="lightyellow",textvariable=self.var_search).place(x=450,y=100,width=200,height=30)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15),bg="#262626",fg="white",cursor="hand2",command=self.search).place(x=670,y=100,width=120,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=810,y=100,width=120,height=30)


    #=====Results Table========
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks_obtained=Label(self.root,text="Marks Score",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_percentage=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll = Label(self.root, font=("goudy old style",15), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)

        self.name = Label(self.root, font=("goudy old style",15), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)

        self.course = Label(self.root, font=("goudy old style",15), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)

        self.marks_obtained = Label(self.root, font=("goudy old style",15), bg="white", bd=2, relief=GROOVE)
        self.marks_obtained.place(x=600, y=280, width=150, height=50)

        self.full_marks = Label(self.root, font=("goudy old style",15), bg="white", bd=2, relief=GROOVE)
        self.full_marks.place(x=750, y=280, width=150, height=50)

        self.percentage = Label(self.root, font=("goudy old style",15), bg="white", bd=2, relief=GROOVE)
        self.percentage.place(x=900, y=280, width=150, height=50)


    #======Buttons========
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="#f0190a",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=150,height=40)


    #=====Search========
    def search(self):
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        my_cursor = conn.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:  
                my_cursor.execute("select * from result where roll=%s", (self.var_search.get(),))
                row = my_cursor.fetchone()
                if row != None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks_obtained.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
        conn.close()

    def clear(self):
        self.var_id=""
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_obtained.config(text="")
        self.full_marks.config(text="")
        self.percentage.config(text="")

    def delete(self):
        conn= mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        my_cursor=conn.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Please search student result",parent=self.root)
            else:
                my_cursor.execute("select * from result where rid=%s",(self.var_id,))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        my_cursor.execute("delete from result where rid=%s",(self.var_id,))
                        conn.commit()
                        messagebox.showinfo("Delete","Student Result Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()