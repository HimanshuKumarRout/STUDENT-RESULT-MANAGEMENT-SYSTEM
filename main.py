from tkinter import Tk
from authentication.login import Login_Window

def main():
    root = Tk()
    app = Login_Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
