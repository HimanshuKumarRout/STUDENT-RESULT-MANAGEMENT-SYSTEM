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



class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x600+80+100")
        self.root.config(bg="white")
        self.root.focus_force()


    #=====Title========
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=50)
    

    #======Variables========
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()


    #=====Widgets========
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=80)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=120)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=160)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=200)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=240)
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=300)
        lbl_contact=Label(self.root,text="Contact No.",font=("goudy old style",15,"bold"),bg="white").place(x=345,y=80)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=345,y=120)
        lbl_a_date=Label(self.root,text="Admission Date",font=("goudy old style",15,"bold"),bg="white").place(x=345,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=345,y=200)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=255,y=240)
        lbl_pin=Label(self.root,text="Pincode",font=("goudy old style",15,"bold"),bg="white").place(x=480,y=240)


    #=====Entry Fields========
        self.txt_roll=Entry(self.root, textvariable=self.var_roll, font=("goudy old style",15), bg="lightyellow")
        self.txt_roll.place(x=130,y=80,width=200,height=30)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=130,y=120,width=200,height=30)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=130,y=160,width=200,height=30)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_gender.place(x=130,y=200,width=200,height=30)
        self.txt_gender.current(0)
        self.txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15),bg="lightyellow").place(x=80,y=240,width=150,height=30)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=130,y=300,width=550,height=150)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=500,y=80,width=200,height=30)
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=120,width=200,height=30)
        self.txt_a_date=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15),bg="lightyellow").place(x=500,y=160,width=200,height=30)
        
        self.course_list=[]
        
        self.fetch_course()
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_course.place(x=500,y=200,width=200,height=30)   
        self.txt_course.set("Select")
        self.txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15),bg="lightyellow").place(x=300,y=240,width=150,height=30)
        self.txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15),bg="lightyellow").place(x=565,y=240,width=150,height=30)
        

    #=====Buttons========
        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=150,y=500,width=100,height=40)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=260,y=500,width=100,height=40)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=370,y=500,width=100,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=480,y=500,width=100,height=40)


    #====Search Panel======
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=80)
        self.txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow")
        self.txt_search_roll.place(x=870,y=80,width=180,height=30)
        self.txt_search_roll.bind("<Return>", self.search)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1070,y=80,width=120,height=30)


    #=====Content Table========
        self.S_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.S_Frame.place(x=720,y=120,width=470,height=450)

        scrolly=Scrollbar(self.S_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.S_Frame,orient=HORIZONTAL)

        self.StudentTable=ttk.Treeview(self.S_Frame,columns=("roll","name","email","gender","contact","dob","course"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        self.StudentTable.heading("roll",text="Roll No.")  
        self.StudentTable.heading("name",text="Name")
        self.StudentTable.heading("email",text="Email")
        self.StudentTable.heading("gender",text="Gender")
        self.StudentTable.heading("contact",text="Contact No.")
        self.StudentTable.heading("dob",text="D.O.B")
        self.StudentTable.heading("course",text="Course")

        self.StudentTable["show"]="headings"
        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("email",width=150)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("contact",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("course",width=150)

        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<<TreeviewSelect>>",self.get_data)
        self.show()

#========Functions========
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_course.set("Select")
        self.var_a_date.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Roll No. should be required",parent=self.root)
        else:
            cur.execute("select * from student where roll=%s",(self.var_roll.get(),))
            row=cur.fetchone()
            if row is None:
                messagebox.showerror("Error","Please select student from the list first",parent=self.root)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                if op:
                    cur.execute("delete from student where roll=%s",(self.var_roll.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                    self.clear()
        con.close()

    def get_data(self,ev):
        # use the current selection (more reliable than focus)
        selected = self.StudentTable.selection()
        if not selected:
            return
        r = selected[0]
        content = self.StudentTable.item(r)
        row_data = content.get("values", [])
        if not row_data:
            return
        roll = row_data[0]

        # make the roll entry readonly if available
        if hasattr(self, 'txt_roll') and getattr(self.txt_roll, 'config', None):
            self.txt_roll.config(state='readonly')

        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        cur.execute("select * from student where roll=%s",(roll,))
        row=cur.fetchone()

        if row:
            self.var_roll.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_a_date.set(row[6])
            self.var_course.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])
            self.txt_address.delete("1.0",END)
            self.txt_address.insert(END,row[11])
        con.close()

    def add(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Roll No. should be required",parent=self.root)
        else:
            cur.execute("select * from student where roll=%s",(self.var_roll.get(),))
            row=cur.fetchone()
            if row is not None:
                messagebox.showerror("Error","Roll No. already present",parent=self.root)
            else:
                cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0",END)
                ))
                con.commit()
                messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                self.show()
        con.close()

    def update(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Roll No. should be required",parent=self.root)
        else:
            cur.execute("select * from student where roll=%s",(self.var_roll.get(),))
            row=cur.fetchone()
            if row is None:
                messagebox.showerror("Error","Select Student from list",parent=self.root)
            else:
                cur.execute("update student set name=%s,email=%s,gender=%s,dob=%s,contact=%s,admission=%s,course=%s,state=%s,city=%s,pin=%s,address=%s where roll=%s",(
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0",END),
                    self.var_roll.get()
                ))
                con.commit()
                messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
                self.show()
        con.close()
    
    def show(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        self.StudentTable.delete(*self.StudentTable.get_children())
        for row in rows:
            self.StudentTable.insert('',END,values=row)
        
    def fetch_course(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        cur.execute("select name from course")
        rows=cur.fetchall()
        for row in rows:
            self.course_list.append(row[0])
        con.close()

    def search(self, ev=None):
        key = self.var_search.get().strip()
        # Treat empty search as 'show all'
        if key == "":
            try:
                self.show()
            except Exception as e:
                messagebox.showerror("Error", f"Error showing records: {e}", parent=self.root)
            return

        try:
            con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
            cur=con.cursor()

            # If the key is purely digits, search exact roll first for faster/precise match
            if key.isdigit():
                cur.execute("select * from student where roll=%s", (key,))
            else:
                pattern = "%" + key + "%"
                cur.execute("select * from student where CAST(roll AS CHAR) LIKE %s OR name LIKE %s", (pattern, pattern))

            rows = cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())

            if not rows:
                messagebox.showinfo("Info", "No records found", parent=self.root)
            else:
                for row in rows:
                    self.StudentTable.insert('',END,values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error searching records: {e}", parent=self.root)
        finally:
            try:
                con.close()
            except Exception:
                pass



if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()