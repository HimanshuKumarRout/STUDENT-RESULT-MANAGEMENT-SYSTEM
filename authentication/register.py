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



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.state('zoomed')
        self.root.config(bg="white")
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        #===bg_new Image===
        try:
            self.bg_new=Image.open("image/bg.jpg")
        except FileNotFoundError:
            self.bg_new=Image.open("../image/bg.jpg")
        self.bg_new=self.bg_new.resize((screen_width, screen_height), Image.LANCZOS if hasattr(Image, 'LANCZOS') else Image.ANTIALIAS)
        self.bg_new=ImageTk.PhotoImage(self.bg_new)
        bg_new=Label(self.root,image=self.bg_new).place(x=0,y=0,relwidth=1,relheight=1)

        #===LEFT Image===
        try:
            self.left=ImageTk.PhotoImage(file="image/side.png")
        except Exception:
            self.left=ImageTk.PhotoImage(file="../image/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #===Register Frame===
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #----------------------------------------------
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #----------------------------------------------
        
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #----------------------------------------------
        
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        
        #----------------------------------------------
        
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        #-------Terms-----------------------------------
        self.var_chk=IntVar(value=0)
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12),command=self.toggle_register).place(x=50,y=380)

        # Create a text-based Register button (disabled until terms are checked)
        self.btn_register=Button(frame1,text="Register",font=("Arial Rounded MT Bold",15),bg="#00B0F0",fg="white",bd=0,cursor="hand2",command=self.register_data,state=DISABLED)
        self.btn_register.place(x=50,y=420,width=250,height=40)

        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460) 
        
    def login_window(self):
        self.root.destroy()
        try:
            from login import Login_Window
        except ModuleNotFoundError:
            from authentication.login import Login_Window
        root=Tk()
        obj=Login_Window(root)
        root.mainloop()

    def toggle_register(self):
        # Enable register button only when terms checkbox is checked
        if self.var_chk.get()==1:
            self.btn_register.config(state=NORMAL)
        else:
            self.btn_register.config(state=DISABLED)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)
        # Reset terms checkbox and disable register button
        try:
            self.var_chk.set(0)
            self.btn_register.config(state=DISABLED)
        except Exception:
            pass

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
             messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
                cur=con.cursor()
                cur.execute("select * from teacher where email=%s",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","User already Exist,Please try another email",parent=self.root)
                else:
                    cur.execute("insert into teacher (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()
                    self.login_window()

                
            except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
