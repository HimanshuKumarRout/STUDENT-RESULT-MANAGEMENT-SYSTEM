from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from components.course import CourseClass
from components.student import StudentClass
from components.result import ResultClass
from components.report import ReportClass


class RMS:
    def __init__(self,root,user=None):
        self.root=root
        self.user = user
        self.root.title("Student Result Management System")
        self.root.state('zoomed')  # Maximize window
        self.root.config(bg="white")


    #======ICONS========
        # Load logo and resize to fit title bar (50px height) while preserving aspect ratio
        img = Image.open("image/logo_p.png")
        target_h = 50
        target_w = int(img.width * (target_h / img.height))
        resample_filter = Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS
        img = img.resize((target_w, target_h), resample_filter)
        self.logo_dash = ImageTk.PhotoImage(img)


    #=======title========
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        # Show logged in user (if provided)
        if self.user:
            Label(self.root, text=f"Logged in as: {self.user}", font=("goudy old style",12), bg="#033054", fg="white").place(relx=0.84, y=10)

    #======Menu========
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1515,height=80)

    #======Buttons========
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(relx=0.014,y=5,relwidth=0.15,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(relx=0.178,y=5,relwidth=0.15,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(relx=0.342,y=5,relwidth=0.15,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.view_report).place(relx=0.506,y=5,relwidth=0.15,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(relx=0.670,y=5,relwidth=0.15,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_app).place(relx=0.834,y=5,relwidth=0.15,height=40)

    #======Content========
        self.bg_img=Image.open("image/bg.jpg")
        self.bg_img=self.bg_img.resize((920,350),)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=600,y=180,width=920,height=350)


    #======Update Details========
        self.lbl_course=Label(self.root,text="Courses",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white").place(x=600,y=560,width=300,height=100)
        self.lbl_student=Label(self.root,text="Students",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white").place(x=910,y=560,width=300,height=100)
        self.lbl_result=Label(self.root,text="Results",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white").place(x=1220,y=560,width=300,height=100)

    #======Footer========
        footer=Label(self.root,text="Student Result Management System\nContact us for any technical Issues: 9876543210",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def view_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)

    def logout(self):
        ans = messagebox.askyesno("Confirm","Are you sure you want to logout?",parent=self.root)
        if ans:
            self.root.destroy()
            from authentication.login import Login_Window
            root = Tk()
            obj = Login_Window(root)
            root.mainloop()

    def exit_app(self):
        ans = messagebox.askyesno("Confirm","Are you sure you want to exit?",parent=self.root)
        if ans:
            self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()