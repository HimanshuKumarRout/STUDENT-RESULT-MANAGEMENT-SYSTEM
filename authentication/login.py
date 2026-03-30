from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
try:
    from db_config import DB_HOST, DB_USER, DB_PASS, DB_NAME
except ModuleNotFoundError:
    import sys
    sys.path.append("..")
    from db_config import DB_HOST, DB_USER, DB_PASS, DB_NAME



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.state('zoomed')
        self.root.config(bg="white")
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        #===Background Image===
        try:
            self.bg_new=Image.open("image/bg.jpg")
        except FileNotFoundError:
            self.bg_new=Image.open("../image/bg.jpg")
        self.bg_new=self.bg_new.resize((screen_width, screen_height), Image.LANCZOS if hasattr(Image, 'LANCZOS') else Image.ANTIALIAS)
        self.bg_new=ImageTk.PhotoImage(self.bg_new)
        lbl_bg_new=Label(self.root,image=self.bg_new).place(x=0,y=0,relwidth=1,relheight=1)

        
        #===Login Frame===
        self.teacher_id=StringVar()
        self.password=StringVar()
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
        
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        
        lbl_user=Label(login_frame,text="Email Address",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_user=Entry(login_frame,textvariable=self.teacher_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        
        btn_login=Button(login_frame,command=self.login,text="Login",font=("Arial Rounded MT Bold",15),bg="#00B0F0",fg="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)
        
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_password_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0,highlightthickness=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=100,y=390)
        
        #===Register Frame===
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        
        lbl_reg=Label(register_frame,text="Don't have an account?",font=("times new roman",13),bg="white").place(x=40,y=20)
        btn_reg=Button(register_frame,text="Sign Up",command=self.register_window,font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,cursor="hand2").place(x=200,y=18)
        
    def register_window(self):
        self.root.destroy()
        try:
            from register import Register
        except ModuleNotFoundError:
            from authentication.register import Register
        root=Tk()
        obj=Register(root)
        root.mainloop()

        
    def login(self):
        if self.teacher_id.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
                cur=con.cursor()
                cur.execute("select * from teacher where email=%s and password=%s",(self.teacher_id.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    teacher_email = self.teacher_id.get()
                    self.root.destroy()
                    import importlib.util
                    try:
                        spec = importlib.util.spec_from_file_location("dashboard", "dashboard.py")
                        if spec is None or spec.loader is None: raise FileNotFoundError
                        dashboard = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(dashboard)
                    except (FileNotFoundError, Exception):
                        spec = importlib.util.spec_from_file_location("dashboard", "../dashboard.py")
                        dashboard = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(dashboard)
                    root=Tk()
                    obj=dashboard.RMS(root, teacher_email)
                    root.mainloop()
                if con.is_connected():
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}")

    def forget_password_window(self):
        if self.teacher_id.get()=="":
            messagebox.showerror("Error","Please enter the Email Address to reset password",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
                cur=con.cursor()
                cur.execute("select * from teacher where email=%s",(self.teacher_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid Email Address to reset password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    #===Security Question===
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
                    
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)
                    
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)
                    
                    btn_change=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
                cur=con.cursor()
                cur.execute("select * from teacher where email=%s and question=%s and answer=%s",(self.teacher_id.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Correct Security Question / Answer",parent=self.root2)
                else:
                    cur.execute("update teacher set password=%s where email=%s",(self.txt_new_pass.get(),self.teacher_id.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","password has been reset,Please login with new password",parent=self.root2)
                    self.root2.destroy()
                    
            except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root2)

if __name__=="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()
