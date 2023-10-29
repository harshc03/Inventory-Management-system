from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from DatabaseHelper import *



# root.title('Inventory Management System')
class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("750x900")
        self.var=IntVar()
        self.f1=Frame(self.root, width=750, height=900,bg='MediumPurple2')
        self.f1.pack()
        self.f1.pack_propagate(0)
        self.heading=Label(self.f1,text='Manufacturing Process Management',font=('Times',20,'bold italic underline'),bg='MediumPurple2')
        self.heading.pack(pady=15)
        self.l_frame=Frame(self.f1,width=600,height=300,bg='MediumPurple2')
        self.l_frame.pack()
        self.l_frame.pack_propagate(0)
        self.lbl=Label(self.l_frame,text='Login page',font=('Arial',15,'bold'),bg='MediumPurple2')
        self.lbl.pack()
        self.option1=Radiobutton(self.l_frame,text='Admin',variable=self.var,value=1,bg='MediumPurple2')
        self.option1.place(x=200,y=40)
        self.option2 = Radiobutton(self.l_frame, text='Distributor', variable=self.var,value=2,bg='MediumPurple2')
        self.option2.place(x=300, y=40)
        self.username=Label(self.l_frame,text='Username',font=('',15,''),bg='MediumPurple2')
        self.pwd=Label(self.l_frame,text='Password',font=('',15,''),bg='MediumPurple2')
        self.username.place(x=100,y=80)
        self.pwd.place(x=100,y=140)
        self.e_user = Entry(self.l_frame, width=30)
        self.e_pwd = Entry(self.l_frame, width=30, show='*')
        self.e_user.place(x=250,y=83)
        self.e_user.focus_set()
        self.e_pwd.place(x=250,y=143)
        self.login=Button(self.l_frame,text='Login',width=15,command=self.validate)
        self.login.place(x=190,y=190)
        self.acc = Label(self.l_frame, text="Don't have an account?", font=('Arial', 11, 'bold'),bg='MediumPurple2')
        self.acc.place(x=100,y=230)
        self.signup=Button(self.l_frame,text='Sign Up',width=15,command=self.registration)
        self.signup.place(x=300,y=230)
        self.open_eye = Image.open("images\open.png").resize((10, 10))
        self.close_eye = Image.open("images\close.png").resize((10, 10))
        self.open_tk = ImageTk.PhotoImage(self.open_eye)
        self.close_tk = ImageTk.PhotoImage(self.close_eye)
        self.display_pwd = IntVar()
        self.display =Checkbutton(self.l_frame,text='Show',bg='MediumPurple2',command=self.flip,variable=self.display_pwd)
        self.display.place(x=450,y=138)


    def validate(self):
        if self.e_user.get()=='' or self.e_pwd.get()=='':
            messagebox.showwarning("Warning", "Empty fields")
        else:
            self.username = self.e_user.get()
            self.pwd = self.e_pwd.get()
            if self.var.get()==1:
                query = "Select * from Admin where username= %s and password=%s"
            else:
                query = "Select * from distributors where username= %s and password=%s"
            parameters = (self.username, self.pwd)
            result = DatabaseHelper.get_data(query, parameters)
            if (result is None):
                messagebox.showerror("Login Failed", "Incorrect credentials")
            # elif (self.var.get()==1 == "admin"):
            #     self.root.destroy()
            #     print("Login Done")
            #     import main
            #     main.HomePage(self.root)
            elif self.var.get()==1:

                messagebox.showinfo('Login Success', "Login successfuly completed")
                self.f1.destroy()
                import main
                main.HomePage(self.root)
            else:
                query = "Select did from distributors where username= %s"
                parameters = (self.username)
                result = DatabaseHelper.get_data(query, parameters)

                self.d_id=result
                print(self.d_id)
                # self.store(self.d_id)
                messagebox.showinfo('Login Success', "Login successfuly completed")
                self.f1.destroy()
                import distrib
                distrib.Distributor(self.root,self.d_id)

    # def store(self,d_id):
    #     self.f1.destroy()
    #     self.dd=d_id


    def registration(self):
            self.f1.destroy()
            self.register=Frame(self.root,width=600, height=600,bg='MediumPurple2')
            self.register.pack()
            self.register.pack_propagate(0)
            self.l1=Label(self.register,text='Sign Up',bg='MediumPurple2',font=('Times',20,'bold italic underline'))
            self.l1.pack(padx=30,pady=20)
            self.name=Label(self.register,text='Name',font=('',15,''),bg='MediumPurple2')
            self.Phone=Label(self.register,text='Phone Number',font=('',15,''),bg='MediumPurple2')
            self.address=Label(self.register,text='Address',font=('',15,''),bg='MediumPurple2')
            self.user = Label(self.register, text='Username', font=('', 15, ''), bg='MediumPurple2')
            self.password = Label(self.register, text='Password', font=('', 15, ''), bg='MediumPurple2')
            self.name.pack(padx=50,pady=20,anchor=W)
            self.Phone.pack(padx=50,pady=20,anchor=W)
            self.address.pack(padx=50,pady=20,anchor=W)
            self.user.pack(padx=50,pady=20,anchor=W)
            self.password.pack(padx=50,pady=20,anchor=W)
            self.e_name=Entry(self.register,width=30)
            self.e_phone=Entry(self.register,width=30)
            self.e_address=Entry(self.register,width=30)
            self.e_usrname=Entry(self.register,width=30)
            self.e_password=Entry(self.register,width=30,show='*')
            self.e_name.place(x=270,y=100)
            self.e_name.focus_set()
            self.e_phone.place(x=270, y=170)
            self.e_address.place(x=270, y=240)
            self.e_usrname.place(x=270, y=310)
            self.e_password.place(x=270, y=380)
            self.reg=Button(self.register,text='Register',command=self.distributor)
            self.reg.pack(padx=200,pady=20,anchor=W)
            self.show_password=IntVar()
            self.show_password_check=Checkbutton(self.register,text='Show',bg='MediumPurple2',command=self.show_hide,variable=self.show_password)
            self.show_password_check.place(x=470,y=377)

    def distributor(self):
        if self.e_name.get()=='' or self.e_phone.get()=='' or self.e_address.get()=='' or self.e_usrname.get()=='' or self.e_password.get()=='':
            messagebox.showwarning("Warning", "Empty fields")
        else:
            Dname=self.e_name.get()
            location=self.e_address.get()
            Dphone=self.e_phone.get()
            username=self.e_usrname.get()
            password=self.e_password.get()
            query="insert into distributors(Dname,location,Dphone,username,password) values(%s,%s,%s,%s,%s)"
            parameters=(Dname,location,Dphone,username,password)
            DatabaseHelper.execute_query(query, parameters)
            messagebox.showinfo("Success", "User registered successfully. Please login")


    def show_hide(self):
        if self.show_password.get()==1:
            self.e_password.configure(show="")
        else:
            self.e_password.configure(show="*")


    def flip(self):
        if self.display_pwd.get() == 1:
            self.e_pwd.configure(show='')

        else:
            self.e_pwd.configure(show='*')



if __name__=="__main__":
    root=Tk()
    root.title("Login")
    h = Login(root)
    root.mainloop()
