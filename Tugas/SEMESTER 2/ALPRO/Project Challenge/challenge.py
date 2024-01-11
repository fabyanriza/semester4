import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast

class App():
    root = tk.Tk()
    def __init__(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Aplikasi pencatatan pelanggaran siswa")
        self.root.geometry("670x550")
        self.root.resizable(False,False)
        self.text = ttk.Label(self.root, text="Aplikasi",font=("Courier", 40)).place(x=200, y=10)
        self.text = ttk.Label(self.root, text="Data Pelanggaran Siswa",font=("Courier", 25)).place(x=100, y=70)
        self.text = ttk.Label(self.root, text="Username : ",font=("Arial", 11)).place(x=80, y=180)
        self.text = ttk.Label(self.root, text="Password : ",font=("Arial", 11)).place(x=80, y=210)
        self.code = ttk.Entry(self.root,show="*")
        self.code.pack(pady=210, ipadx=200,ipady=10)
        self.code.place(x=200,y=210,width=300)
        self.user = ttk.Entry(self.root)
        self.user.place(x=200, y=180,width=300)
        
        

        def show_password():
            if self.code.cget("show")=='*':
                self.code.config(show="")
            else:
                self.code.config(show="*")

        tk.Checkbutton(self.root,text="show pasword",command=show_password).place(x=197, y=255)
        

        # login system
        def signin():
            username = self.user.get()
            password = self.code.get()

            file = open("login.txt", "r")
            d = file.read()
            r = ast.literal_eval(d)
            file.close()           

            if username in r.keys() and password == r[username]:
                self.menu()
            elif username in r.keys() and not password == r[username]:
                tk.Label(self.root, text = "*password yang anda masukkan salah", fg='#f00',font=("Courier", 8)).place(x=195, y=240) 
            else:
                tk.Label(self.root, text = "*username atau password yang anda masukkan salah", fg='#f00', font=("Courier", 8)).place(x=195, y=240)




        def register():
            def signup():
                username = self.user.get()
                password = self.code.get()
                confirm_password = confirm_code.get()

                if password == confirm_password:
                    try:
                        file = open('login.txt', 'r+')
                        d = file.read()
                        r = ast.literal_eval(d)

                        dict2 = {username:password}
                        r.update(dict2)
                        file.truncate(0)
                        file.close()

                        file = open('login.txt', 'w')
                        file.write(str(r))

                        messagebox.showinfo('Signup', "succefully signup")
                        self.__init__()
                        

                    except:
                        ValueError
                        
                else:
                    messagebox.showerror('Invalid', 'Both Password shsoul match')




            self.root.destroy()
            self.root = tk.Tk()
            self.root.title("Aplikasi pencatatan pelanggaran siswa")
            self.root.geometry("670x550")
            self.root.resizable(False,False)

            tk.Label(self.root, text="Create new username", font=("Arial", 20)).place(x=100, y=100)
            self.user = tk.Entry(self.root)
            self.user.place(x= 100, y=150)

            tk.Label(self.root, text="Create new password", font=("Arial", 20)).place(x=100, y=200)
            self.code = tk.Entry(self.root)
            self.code.place(x=100, y=250)

            tk.Label(self.root, text="Confirm new password", font=("Arial", 20)).place(x=100, y=300)
            confirm_code = tk.Entry(self.root)
            confirm_code.place(x=100, y=350)

        

            tk.Button(self.root, text="sign up", font=("Arial, 15"), width=30, command=signup).place(x=150,y=450)
            
        
        
        

        ttk.Button(self.root, text="Login", command=signin,width= 49,).place(x=200, y=280)
        ttk.Button(self.root, text="Register", command=register,width= 49,).place(x=200, y=310)

        self.root.mainloop()

    def menu(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title('Aplikasi pencatatan pelanggaran siswa')
        self.root.geometry('670x550')
        self.root.resizable(False,False)
        tk.Label(self.root, text="admin",font=("Arial", 11)).place(x=470, y=10)
        tk.Button(self.root, text="Logout", command=self.__init__ ,height = 1, width = 13,font=("Arial", 11)).place(x=530, y=10)
        tk.Button(self.root, text="Input Data", command=self.input_data ,height = 1, width = 13,font=("Arial", 20)).place(x=100, y=200)
        tk.Button(self.root, text="Cari Data", command=self.cari_data ,height = 1, width = 13,font=("Arial", 20)).place(x=350, y=200)
            
    def input_data(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Aplikasi pencatatan pelanggaran siswa")
        self.root.geometry("670x650")
        var1 = tk.IntVar()
        var2 = tk.IntVar()

        tk.Label(self.root, text="admin",font=("Arial", 11)).place(x=470, y=10)
        tk.Button(self.root, text="Logout", command=self.__init__,width = 13,font=("Arial", 11)).place(x=530, y=10)
        tk.Button(self.root, text="Masukkan foto", command=None, width = 13,font=("Arial", 11)).place(x=200, y=120)
        
        tk.Label(self.root, text="Nama Siswa : ",font=("Arial", 11)).place(x=50, y=210)
        tk.Label(self.root, text="Kelas",font=("Arial", 11)).place(x=50, y=240)
        tk.Label(self.root, text="Nama Orang Tua", font=("Arial", 11)).place(x=50, y=270)
        tk.Label(self.root, text="Telp Orang Tua",font=("Arial", 11)).place(x=50, y=300)
        tk.Label(self.root, text="Data Pelanggaran Siswa",font=("Arial", 25)).place(x=200, y=350)
        tk.Label(self.root, text="Pelanggaran : ",font=("Arial", 11)).place(x=50, y=420)
        tk.Label(self.root, text="Penanganan : ",font=("Arial", 11)).place(x=50, y=450)
        tk.Label(self.root, text="Guru BK", font=("Arial", 11)).place(x=50, y=480)
        tk.Label(self.root, text="Konsultasi", font=("Arial", 11)).place(x=50, y=510)
        tk.Button(self.root, text = "Simpan",command = self.menu,height = 1, width = 13,font=("Arial", 11)).place(x=280, y=580) 
    

        # kotak foto
        e1 = tk.Entry(self.root)
        e1.place(x=40, y=70,height=130,width=130)


        e2 = tk.Entry(self.root)
        e2.place(x=210, y=210,width=300)
        e3 = tk.Entry(self.root)
        e3.place(x=210, y=240,width=300)
        e4 = tk.Entry(self.root)
        e4.place(x=210, y=270,width=300)
        e5 = tk.Entry(self.root)
        e5.place(x=210, y=300,width=300)
        e6 = tk.Entry(self.root)
        e6.place(x=210, y=420,width=300)
        e7 = tk.Entry(self.root)
        e7.place(x=210, y=450,width=300)
        e8 = tk.Entry(self.root)
        e8.place(x=210, y=480,width=300)
        
        
        tk.Checkbutton(self.root, text='Iya',variable=var1, onvalue=1, offvalue=0, command=None).place(x=205, y=510)
        tk.Checkbutton(self.root, text='Tidak',variable=var2, onvalue=1, offvalue=0, command=None).place(x=250, y=510)
            
    def cari_data(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Aplikasi pencatatan pelanggaran siswa")
        self.root.geometry("670x550")
        
        tk.Label(self.root, text="admin",font=("Arial", 11)).place(x=470, y=10)
        tk.Button(self.root, text="Logout", command=self.__init__ ,height = 1, width = 13,font=("Arial", 11)).place(x=530, y=10)
        
        tk.Label(self.root, text="Data Pelanggaran Siswa",font=("Courier", 25)).place(x=100, y=70)
            
        tk.Label(self.root, text="Nama siswa : ",font=("Arial", 11)).place(x=80, y=180)
        tk.Button(self.root, text="Cari", command=self.info_data ,height = 1, width = 13,font=("Arial", 11)).place(x=250, y=260)
        e1 = tk.Entry(self.root)
        e1.place(x=200, y=180,width=300)

    def info_data(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Aplikasi pencatatan pelanggaran siswa")
        self.root.geometry("670x550")

        tk.Label(self.root, text="Data Pelanggaran Siswa",font=("Arial", 25)).place(x=150, y=50)

        tk.Label(self.root, text="admin",font=("Arial", 11)).place(x=470, y=10)
        tk.Button(self.root, text="Logout", command=self.__init__ ,height = 1, width = 13,font=("Arial", 11)).place(x=530, y=10)
        tk.Button(self.root, text = "Kembali",command = self.cari_data,height = 1, width = 13,font=("Arial", 11)).place(x=530, y=50) 
        tk.Label(self.root, text="Nama Siswa      : ",font=("Arial", 11)).place(x=170, y=130)
        tk.Label(self.root, text="Kelas           : ",font=("Arial", 11)).place(x=170, y=160)
        tk.Label(self.root, text="Nama Orang Tua  : ", font=("Arial", 11)).place(x=170, y=190)
        tk.Label(self.root, text="Telp Orang Tua  : ",font=("Arial", 11)).place(x=170, y=220)
        # kotak foto
        e1 = tk.Entry(self.root)
        e1.place(x=20, y=120,height=130,width=130)
                
    
        # Create a Treeview widget
        self.table = ttk.Treeview(self.root, columns=(1, 2, 3, 4, 5, 6), show="headings")
        self.table.pack()
        self.table.grid(sticky='nwes')
        self.table.place(x=20,y=300, width=610)
        
        # headings
        self.table.heading(1, text="No")
        self.table.heading(2, text="Nama")
        self.table.heading(3, text="Pelanggaran")
        self.table.heading(4, text="Penanganan")
        self.table.heading(5, text="Guru BK")
        self.table.heading(6, text="Konsultasi")
        # columns
        self.table.column(1, width=50, stretch=tk.NO)
        self.table.column(2, width=100, stretch=tk.NO)
        self.table.column(3, width=150, stretch=tk.NO)
        self.table.column(4, width=140, stretch=tk.NO)
        self.table.column(5, width=98, stretch=tk.NO)
        self.table.column(6, width=70, stretch=tk.NO)





        

if __name__ == '__main__':
    App()

