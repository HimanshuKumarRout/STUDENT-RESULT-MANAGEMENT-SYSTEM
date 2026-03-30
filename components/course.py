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


class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

    #=====Title========
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=50)
    

    #======Variables========
        self.var_courseName=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()


    #=====Widgets========
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=80)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=120)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=160)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=200)


    #=====Entry Fields========
        self.txt_courseName=Entry(self.root,textvariable=self.var_courseName,font=("goudy old style",15),bg="lightyellow")
        self.txt_courseName.place(x=150,y=80,width=300,height=30)
        self.txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15),bg="lightyellow")
        self.txt_duration.place(x=150,y=120,width=300,height=30)
        self.txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15),bg="lightyellow")
        self.txt_charges.place(x=150,y=160,width=300,height=30)
        self.txt_description=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_description.place(x=150,y=200,width=500,height=130)

    #=====Buttons========
        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=150,y=400,width=100,height=40)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=260,y=400,width=100,height=40)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=370,y=400,width=100,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=480,y=400,width=100,height=40)

    #====Search Panel======
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=80)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow").place(x=870,y=80,width=180,height=30)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1070,y=80,width=120,height=30)


    #=====Content Table========
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=120,width=470,height=350)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]="headings"

        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#======Function Declarations========
    def clear(self):
        self.show()
        self.var_courseName.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        if self.var_courseName.get()=="":
            messagebox.showerror("Error","Course Name should be required",parent=self.root)
        else:
            cur.execute("select * from course where name=%s",(self.var_courseName.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Please select course from the list first",parent=self.root)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                    cur.execute("delete from course where name=%s",(self.var_courseName.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Course deleted Successfully",parent=self.root)
                    self.clear()

    def update(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        if self.var_courseName.get()=="":
            messagebox.showerror("Error","Course Name should be required",parent=self.root)
        else:
            cur.execute("select * from course where name=%s",(self.var_courseName.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Select Course from list",parent=self.root)
            else:
                cur.execute("update course set duration=%s,charges=%s,description=%s where name=%s",(
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0",END),
                    self.var_courseName.get()
                ))
                con.commit()
                messagebox.showinfo("Success","Course Updated Successfully",parent=self.root)
                self.show()

    def add(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        if self.var_courseName.get()=="":
            messagebox.showerror("Error","Course Name should be required",parent=self.root)
        else:
            cur.execute("select * from course where name=%s",(self.var_courseName.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Course Name already present",parent=self.root)
            else:
                cur.execute("insert into course (name,duration,charges,description) values(%s,%s,%s,%s)",(
                    self.var_courseName.get(),
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0",END)
                ))
                con.commit()
                messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                self.show()

    def show(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        cur.execute("select * from course")
        rows=cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert('',END,values=row)

    def search(self):
        con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cur=con.cursor()
        cur.execute("select * from course where name LIKE %s",("%"+self.var_search.get()+"%",))
        rows=cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert('',END,values=row)

    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        r=self.CourseTable.focus()
        if r!="":
            content=self.CourseTable.item(r)
            row=content["values"]
            if row:
                self.var_courseName.set(row[1])
                self.var_duration.set(row[2])
                self.var_charges.set(row[3])
                self.txt_description.delete('1.0',END)
                self.txt_description.insert(END,row[4])

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()

