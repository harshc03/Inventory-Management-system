from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from DatabaseHelper import *
from Components.table import SimpleTable
import datetime

class Distributor:
    def __init__(self, root,s):
        self.s=s
        print("did",s)
        self.root = root
        self.frame = Frame(self.root, height=900, width=750,bg='cadetblue1')

        self.bframe=Frame(self.root, bg="cadetblue1")
        self.b1 = Button(self.bframe, text="Buy Items", width=10, height=2,command=self.buy_items)
        self.b2 = Button(self.bframe, text="View Orders", width=10, height=2,command=self.past_orders)
        self.b3 = Button(self.bframe, text="Logout", width=10, height=2,command=self.login)
        self.header()
        self.frame.grid_propagate(0)
        self.b1.pack(side=LEFT, padx=10, pady=10)
        self.b2.pack(side=LEFT, padx=10, pady=10)
        self.b3.pack(side=RIGHT, padx=10, pady=10)
        self.bframe.pack(fill=BOTH, expand=YES)
        self.bframe.place(x=180, y=150)

        self.frame.pack()
    def login(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()
        import Login
        Login.Login(self.root)
    def past_orders(self):
        self.order_frame = Frame(self.frame, width=600, height=400, bg="white", borderwidth=3, relief='solid')
        self.order_frame.place(x=400, y=500, anchor=CENTER)
        self.order = Label(self.order_frame, text="Order History", font=('Calibri', 25), bg="white")
        self.order.place(x=100, y=25, anchor=CENTER)
        query = "select o.oid as ID,p.pname as Name,o.Orderdate as Date,o.quantity as Quantity from orders o inner join product p on o.pid=p.pid where o.did=%s"
        parameters=(self.s["did"])
        result = DatabaseHelper.get_all_data(query,parameters)
        print(result)
        if (len(result)==1):
            messagebox.showerror("Order History","OOPS!!! you haven't placed any order ,Go & place the Order Hurry Up")
        else:
            self.viewpr_table = SimpleTable(self.order_frame, rows=len(result), columns=len(result[0]), width=500,
                                            height=300)
            self.viewpr_table.place(x=0, y=60)
            for r in range(len(result)):
                for c in range(len(result[0])):
                    self.viewpr_table.set(row=r, column=c, value=result[r][c])
    def bill(self):
        self.items=[]
        print(self.items)
        for item in self.result[1:]:
            if item[-1].get()!=0:
                item[-1]=item[-1].get()
                self.items.append(item)
        self.total_amount = 0

        for item in self.items:
            price = item[2]
            quantity = item[3]
            amount = price * quantity
            self.total_amount += amount

        print(self.total_amount)
        if len(self.items)==0:
            messagebox.showwarning("Warning", "NO item selected")
        else:
            print(self.items)
            self.billing=SimpleTable(self.frame,rows=len(self.items),columns=2,width=530, height=340)
            self.billing.place(x=95, y=350)
            print(len(self.items))
            print(len(self.items[0]))
            for r in range(len(self.items)):
                for c in range(2):
                    # self.billing.set(row=r, column=c, value=items[r][c])
                    if c==0:
                        self.billing.set(row=r, column=c, value=self.items[r][c+1])

                    else:
                        self.billing.set(row=r,column=c,value=self.items[r][c+1]*self.items[r][c+2])
            self.buy.destroy()
            self.confirm_lbl=Label(self.frame, text=f"Total Amount {self.total_amount}", font=('Calibri', 15), bg="white")
            self.confirm_lbl.place(relx=0.4,rely=0.85)
            self.confirm = Button(self.frame, text='Place Order', command=lambda:self.message(self.items))
            self.confirm.place(relx=0.8, rely=0.85)


    def message(self,items):
        self.item1=items
        self.did=self.s

        # self.d=self.did['did']
        # print(self.d)
        # print("did",self.did)
        query="insert into orders(did,pid,quantity,sell_p,Orderdate) values(%s,%s,%s,%s,%s)"
        for item in self.item1:
            parameters=(self.did["did"],item[0],item[-1],item[-2],datetime.datetime.today().date())
            DatabaseHelper.execute_query(query,parameters)
        messagebox.showinfo("Order Placed","Your order is successfully placed")



    def view_pd(self):
            query = "select pid as ID,pname as Name,p_sell as Cost from product"
            result = DatabaseHelper.get_all_data(query)
            self.table = SimpleTable(self.frame, rows=len(result), columns=len(result[0]) + 1, width=530, height=340)
            self.table.place(x=95, y=350)
            self.result = list(list(x) for x in result)


            for r in range(len(result)):
                for c in range(len(result[0])):
                    self.table.set(row=r, column=c, value=result[r][c], width=15)
                else:
                    if r==0:
                        self.table.set(row=r, column=c+1, value="Quantity")
                    else:
                        quantity = IntVar()
                        self.result[r].append(quantity)
                        col = len(result[0])
                        spin = Spinbox(self.table, from_=0, to=10, textvariable=self.result[r][col], width=10)
                        self.table.set(row=r, column=col, widget=spin, value=self.result[r][col])

    def buy_items(self):
        self.buy_frame = Frame(self.frame, width=600, height=400, bg="white", borderwidth=3, relief='solid')
        self.buy_frame.place(x=380, y=500, anchor=CENTER)
        self.product_search = Label(self.buy_frame, text="Product Search:", font=('Calibri', 15), bg="white")
        self.product_search.place(x=100, y=25, anchor=CENTER)
        self.p_search = Entry(self.buy_frame, width=10, font=(('Arial'), 15))
        self.p_search.bind("<Return>", lambda e: self.search_product())
        self.p_search.place(x=180, y=15)
        self.p_image = Image.open("images\search.jpg")
        self.p_image = self.p_image.resize((20, 25))
        self.search_img = ImageTk.PhotoImage(self.p_image)
        self.s_button = Button(self.buy_frame,image=self.search_img)
        self.buy = Button(self.frame, text='Buy', command=self.bill)
        self.buy.place(relx=0.8,rely=0.85)
        # , image=self.search_img, bd=0)
        # self.search_button.image = self.search_img
        self.s_button.place(x=300, y=15)
        self.p_search.focus_set()
        # self.add_btn = Button(self.Show_frame, text="Add Product", font='bold', height=1, width=10,
        #                       command=self.add_products)
        # self.add_btn.place(x=400, y=15)
        self.view_pd()

    def search_product(self):
        s = self.p_search.get()
        if s == "":
            query = "select pid as ID,pname as Name,p_sell as Cost from product "
        else:
            query = f"select pid as ID,pname as Name,p_sell as Cost from product where Pname like '{s}%' "
        result = DatabaseHelper.get_all_data(query)
        self.table = SimpleTable(self.frame, rows=len(result), columns=len(result[0]) + 1, width=530, height=340)
        self.table.place(x=95, y=350)
        self.result = list(list(x) for x in result)

        for r in range(len(result)):
            for c in range(len(result[0])):
                self.table.set(row=r, column=c, value=result[r][c], width=15)
            else:
                if r != 0:
                    quantity = IntVar()
                    self.result[r].append(quantity)
                    col = len(result[0])
                    spin = Spinbox(self.table, from_=0, to=10, textvariable=self.result[r][col], width=10)
                    self.table.set(row=r, column=col, widget=spin, value=self.result[r][col])

    def header(self):
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
        # self.header_f = Frame(self.frame, height=100, width=800)
        # self.header_f.grid(row=0, column=0, sticky="nsew", columnspan=6)
        #
        # self.raw_login_image = Image.open("background.jpg")
        # self.raw_login_image = self.raw_login_image.resize((50, 50))
        # self.login_img = ImageTk.PhotoImage(self.raw_login_image)
        # self.login_l = Label(self.header_f,image=self.login_img)
        # self.login_l.image = self.login_img
        # self.login_l.grid(row=0, column=0, padx=30)
        #
        # self.welcome_l = Label(self.header_f, text=" Manufacturing Process Management", font=("Times", 30))
        # self.welcome_l.grid(row=0, column=1, padx=20, pady=20)

if(__name__=="__main__"):
    root=Tk()
    m=Distributor(root)
    root.mainloop()