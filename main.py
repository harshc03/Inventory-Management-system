from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from DatabaseHelper import *
from Components.table import SimpleTable
from AdminAnalytics import Analytics


class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Page Manufacturing Process Management")
        self.frame = Frame(self.root, height=900, width=750, bg="cadetblue1")
        self.add_header_section()
        self.btn_frame = Frame(self.root, bg="cadetblue1")
        self.btn_frame.pack(fill=BOTH, expand=YES)
        self.product_btn = Button(self.btn_frame, text="View Products", width=15, height=3, command=self.Show_products)
        self.distribution_btn = Button(self.btn_frame, text="View Distributors", width=15, height=3,
                                       command=self.show_distributors)
        self.sales_btn = Button(self.btn_frame, text="Sales Growth", width=15, height=3,command=self.analytics)
        self.logout_btn = Button(self.btn_frame, text="Logout", width=15, height=3,command=self.login)

        self.product_btn.pack(side=LEFT, padx=10, pady=10)
        self.distribution_btn.pack(side=LEFT, padx=10, pady=10)
        self.sales_btn.pack(side=LEFT, padx=10, pady=10)
        self.logout_btn.pack(side=RIGHT, padx=10, pady=10)

        self.btn_frame.place(x=180, y=150)
        self.frame.grid_propagate(0)
        self.frame.pack()
    def login(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()
        import Login
        Login.Login(self.root)
    def analytics(self):
        import AdminAnalytics as a
        a.Analytics()


    def Show_products(self):
        self.Show_frame = Frame(self.frame, width=600, height=400, bg="white", borderwidth=3, relief='solid')
        self.Show_frame.place(x=380, y=500, anchor=CENTER)
        self.lb_search = Label(self.Show_frame, text="Product Search:", font=('Calibri', 15), bg="white")
        self.lb_search.place(x=100, y=25, anchor=CENTER)
        self.e_search = Entry(self.Show_frame, width=10, font=(('Arial'), 15))
        self.e_search.bind("<Return>", lambda e: self.search_product())
        self.e_search.place(x=180, y=15)
        self.se_image = Image.open("images\search.jpg")
        self.se_image = self.se_image.resize((20, 25))
        self.search_img = ImageTk.PhotoImage(self.se_image)
        self.search_button = Button(self.Show_frame, image=self.search_img, bd=0, command=self.search_product)
        self.search_button.image = self.search_img
        self.search_button.place(x=300, y=15)
        self.e_search.focus_set()
        self.add_btn = Button(self.Show_frame, text="Add Product", font='bold', height=1, width=10,
                              command=self.add_products)
        self.add_btn.place(x=400, y=15)
        self.view_products()

    def search_product(self):
        s = self.e_search.get()
        if s == "":
            query = "select * from product "
        else:
            query = f"select * from product where Pname like '{s}%' "
        result = DatabaseHelper.get_all_data(query)

        self.viewpr_table = SimpleTable(self.Show_frame, rows=len(result), columns=len(result[0]), width=550,
                                        height=300)
        self.viewpr_table.place(x=0, y=60)
        for r in range(len(result)):
            for c in range(len(result[0])):
                self.viewpr_table.set(row=r, column=c, value=result[r][c])

    def view_products(self):
        query = "select pid as ID,Pname as Name,p_cost as 'Actual Cost',p_sell as 'Selling Price',quantity as Quantity from product"
        result = DatabaseHelper.get_all_data(query)

        self.viewpr_table = SimpleTable(self.Show_frame, rows=len(result), columns=len(result[0]), width=550,
                                        height=300)
        self.viewpr_table.place(x=0, y=60)
        for r in range(len(result)):
            for c in range(len(result[0])):
                self.viewpr_table.set(row=r, column=c, value=result[r][c])

    def show_distributors(self):
        self.Show_frame = Frame(self.frame, width=600, height=400, bg="white", borderwidth=3, relief='solid')
        self.Show_frame.place(x=380, y=500, anchor=CENTER)
        self.lb_search = Label(self.Show_frame, text="Search Distributors:", font=('Calibri', 16), bg="white", width=30)
        self.lb_search.place(x=190, y=25, anchor=CENTER)
        self.e_search = Entry(self.Show_frame, width=12, font=(('Arial'), 15))
        self.e_search.bind("<Return>", lambda e: self.search_distributor())
        self.e_search.place(x=280, y=15)
        self.se_image = Image.open("images\search.jpg")
        self.se_image = self.se_image.resize((20, 25))
        self.search_img = ImageTk.PhotoImage(self.se_image)
        self.search_button = Button(self.Show_frame, image=self.search_img, bd=0, command=self.search_distributor)
        self.search_button.image = self.search_img
        self.search_button.place(x=420, y=15)
        self.e_search.focus_set()
        self.view_Distributors()

    def search_distributor(self):
        s = self.e_search.get()
        if s == "":
            query = "select did as DistributorID,dname as Name,dphone as Contact,location as Location from distributors"
        else:
            query = f"select did,dname,dphone,location from distributors where Dname like '{s}%' "
        result = DatabaseHelper.get_all_data(query)

        self.viewpr_table = SimpleTable(self.Show_frame, rows=len(result), columns=len(result[0]), width=450,
                                        height=300)
        self.viewpr_table.place(x=50, y=60)
        for r in range(len(result)):
            for c in range(len(result[0])):
                self.viewpr_table.set(row=r, column=c, value=result[r][c])

    def view_Distributors(self):
        query = "select did as DistributorID,dname as Name,dphone as Contact,location as Location from distributors"
        result = DatabaseHelper.get_all_data(query)

        self.viewpr_table = SimpleTable(self.Show_frame, rows=len(result), columns=len(result[0]), width=450,
                                        height=300)
        self.viewpr_table.place(x=50, y=60)
        for r in range(len(result)):
            for c in range(len(result[0])):
                self.viewpr_table.set(row=r, column=c, value=result[r][c])

    def add_header_section(self):
        self.header_frame = Frame(self.frame, height=100, width=800)
        self.header_frame.grid(row=0, column=0, sticky="nsew", columnspan=6)

        self.raw_login_image = Image.open("background.jpg")
        self.raw_login_image = self.raw_login_image.resize((50, 50))
        self.login_img = ImageTk.PhotoImage(self.raw_login_image)
        self.login_label = Label(self.header_frame, image=self.login_img)
        self.login_label.image = self.login_img
        self.login_label.grid(row=0, column=0, padx=30)

        self.welcome_label = Label(self.header_frame, text=" Manufacturing Process Management", font=("Times", 30))
        self.welcome_label.grid(row=0, column=1, padx=20, pady=20)

    def add_products(self):
        self.add_product_frame = Frame(self.frame, width=600, height=400, bg="white", borderwidth=3, relief='solid')
        self.add_product_frame.place(x=380, y=500, anchor=CENTER)

        self.head_lbl = Label(self.add_product_frame, text="Enter Product Details", font=('Calibri', 20, 'bold'),
                              bg="white")
        self.head_lbl.place(x=300, y=30, anchor=CENTER)

        self.lb1 = Label(self.add_product_frame, text="Product name:", font=('Calibri', 20), bg="white")
        self.lb1.place(x=100, y=75, anchor=CENTER)
        self.e1 = Entry(self.add_product_frame, width=20, font=(('Arial'), 15))
        self.e1.place(x=220, y=65)

        self.lb2 = Label(self.add_product_frame, text="Cost:", font=('Calibri', 20), bg="white")
        self.lb2.place(x=45, y=125, anchor=CENTER)
        self.e2 = Entry(self.add_product_frame, width=20, font=(('Arial'), 15))
        self.e2.place(x=220, y=115)

        self.lb3 = Label(self.add_product_frame, text="Sell Price:", font=('Calibri', 20), bg="white")
        self.lb3.place(x=70, y=175, anchor=CENTER)
        self.e3 = Entry(self.add_product_frame, width=20, font=(('Arial'), 15))
        self.e3.place(x=220, y=165)

        self.lb4 = Label(self.add_product_frame, text="Quantity:", font=('Calibri', 20), bg="white")
        self.lb4.place(x=70, y=225, anchor=CENTER)
        self.e4 = Entry(self.add_product_frame, width=20, font=(('Arial'), 15))
        self.e4.place(x=220, y=215)

        self.e1.focus_set()

        self.update_var = IntVar()
        self.update_var.set("New")
        self.update_rb = Radiobutton(self.add_product_frame, text="Update Product",width=15,height=2, variable=self.update_var, value=1)
        self.update_rb.place(x=160, y=265)

        self.new_rb = Radiobutton(self.add_product_frame, text="New Product",width=15,height=2, variable=self.update_var, value=2)
        self.new_rb.place(x=290, y=265)

        self.b1 = Button(self.add_product_frame, text="Submit", height=2, width=10, command=self.submit)
        self.b1.place(x=220, y=315)

        self.b2 = Button(self.add_product_frame, text="Reset", height=2, width=10, command=self.reset)
        self.b2.place(x=330, y=315)

        self.e1.focus_set()

    def submit(self):
        update=self.update_var.get()
        print(update)
        name = self.e1.get()
        cost = self.e2.get()
        selling_price = self.e3.get()
        quantity = self.e4.get()

        if name == "" or cost == "" or quantity == "" or selling_price == "":
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            if update==1:
                query="""UPDATE product SET p_cost=%s,p_sell=%s,quantity=%s
                WHERE pname=%s"""
                parameters=(cost,selling_price,quantity,name)
                DatabaseHelper.execute_query(query,parameters)
                messagebox.showinfo("Entry Done", "Product Upadted Successfully")
            else:
                query = "insert into product(pname,p_cost,p_sell,quantity) values(%s,%s,%s,%s)"
                parameters = (name, cost, selling_price, quantity)
                DatabaseHelper.execute_query(query, parameters)
                messagebox.showinfo("Entry Done", "Product Successfully added")




    def authenticate(self, name, cost):
        pass

    # authentication code here

    def reset(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e1.focus_set()


if __name__ == '__main__':
    root = Tk()
    h = HomePage(root)
    root.mainloop()
