from tkinter import *
from tkinter import messagebox
import ast

win = Tk()
win.title("signup")
win.geometry("920x500")
win.resizable(False,False)

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open('logininfo.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('logininfo.txt', 'w')
            file.write(str(r))

            messagebox.showinfo('Signup', "succefully signup")

        except:
            file = open("logininfo.txt", 'w')
            pp = str({"Username" : "password"})
            file.write(pp)
            file.close
            
    else:
        messagebox.showerror('Invalid', 'Both Password shsoul match')


Label(win, text="Create new username", font=("Arial", 20)).place(x=100, y=100)
user = Entry(win)
user.place(x= 100, y=150)

Label(win, text="Create new password", font=("Arial", 20)).place(x=100, y=200)
code = Entry(win)
code.place(x=100, y=250)

Label(win, text="Confirm new password", font=("Arial", 20)).place(x=100, y=300)
confirm_code = Entry(win)
confirm_code.place(x=100, y=350)

Button(win, text="sign up", font=("Arial, 15"), width=50, command=signup).place(x=150,y=450)



win.mainloop()