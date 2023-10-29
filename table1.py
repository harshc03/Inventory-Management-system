from tkinter import *
from tkinter import ttk
import tkinter as tk

class VerticalScrolledFrame:
    """
    ie it needs a master and layout and it can be a master.
    keyword arguments are passed to the underlying Frame
    except the keyword arguments 'width' and 'height', which
    are passed to the underlying Canvas
    note that a widget layed out in this frame will have Canvas as self.master,
    if you subclass this there is no built in way for the children to access it.
    You need to provide the controller separately.
    """

    def __init__(self, master, **kwargs): #master is root passed
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)
        self.outer = tk.Frame(master, **kwargs)
        self.outer.pack()

        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        self.canvas = tk.Canvas(self.outer, highlightthickness=0, width=width+10, height=height)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas['yscrollcommand'] = self.vsb.set
        # mouse scroll does not seem to work with just "bind"; You have
        # to use "bind_all". Therefore to use multiple windows you have
        # to bind_all in the current widget
        self.canvas.bind("<Enter>", self.__bind__mouse)
        self.canvas.bind("<Leave>", self.__unbind__mouse)
        self.vsb['command'] = self.canvas.yview

        self.inner = tk.Frame(self.canvas)
        # pack the inner Frame into the Canvas with the topleft corner 4 pixels offset
        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self.__on__frame__configure)

        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            # geometry attributes etc (eg pack, destroy, tkraise) are passed on to self.outer
            return getattr(self.outer, item)
        else:
            # all other attributes (_w, children, etc) are passed to self.inner
            return getattr(self.inner, item)

    def __on__frame__configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        self.canvas.config(scrollregion=(0, 0, x2, max(y2, height)))

    def __bind__mouse(self, event=None):
        self.canvas.bind_all("<4>", self.__on__mousewheel)
        self.canvas.bind_all("<5>", self.__on__mousewheel)
        self.canvas.bind_all("<MouseWheel>", self.__on__mousewheel)

    def __unbind__mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def __on__mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")

def clicked(x):
    print(f" {x} was clicked")

root =Tk()
root.geometry('1000x1000')
root.title("Buttons methods")

f = Frame(root,width=1500,height=900)
f.pack(expand=0,fill=BOTH)

#top heading
# lbl0 = Label(f, text="List of Donors",width=75,height=2 ,bg="red" , font=("Calibri", 30, "bold", "italic"))
# lbl0.pack(side=TOP)

lbl=Label(f,text="List of Donors",bg="red" , font=("Calibri", 30, "bold", "italic"))
lbl.pack(fill=BOTH)
#Column names
# lbl1 = Label(root, text="Sr no.", font=("Arial", 16), bg="pink")
# lbl1.place(x=50, y=120, height=20, width=100)
#
# lbl2 = Label(root, text="Full Name", font=("Arial", 16), bg="pink")
# lbl2.place(x=300, y=120, height=20, width=100)
#
# lbl3 = Label(root, text="Age", font=("Arial", 16), bg="pink")
# lbl3.place(x=650, y=120, height=20, width=100)
#
# lbl4 = Label(root, text="Blood Group", font=("Arial", 16), bg="pink",)
# lbl4.place(x=950, y=120, height=20, width=150)
#
# lbl2 = Label(root, text="View Details", font=("Arial", 16), bg="pink")
# lbl2.place(x=1300, y=120, height=20, width=150)


class SimpleTable(VerticalScrolledFrame):
    def __init__(self, parent, rows=10, columns=5,**kwargs):
        super().__init__(parent, background="#f2efe6",**kwargs)
        self.header_color="red"
        self.even_color="pink"
        self.odd_color="lightpink1"
        self._widgets = []
        for row in range(rows):
            current_row = []
            if(row==0):
              bg=self.header_color
            elif(row%2==0):
                bg=self.even_color
            else:
                bg=self.odd_color
            for column in range(columns):
                label = Label(self, text="-",borderwidth=0, height=3,bg=bg,wraplength=400)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        # for column in range(columns):
        #     self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value,widget=None,**kwargs):
        widget_ref = self._widgets[row][column]

        if(widget is not None):
            if(row%2==0):
                widget.configure(bg=self.even_color)
            else:
                widget.configure(bg=self.odd_color)
            widget.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            self._widgets[row][column]=widget
            widget_ref.configure(text=str(value), **kwargs)
            widget_ref=widget
        widget_ref.configure(text=str(value),**kwargs)

if __name__ == "__main__":

    t = SimpleTable(root, rows=20, columns=5,width=2000, height=800)
#    t.pack( fill=X)
    t.set(0, 0, "                                      Sr no                                    ")
    t.set(0, 1, "                                         Product Name                                   ")
    t.set(0, 2, "                                      Cost                                   ")
    t.set(0, 3, "                                      Selling P                                      ")
    t.set(0, 4, "                                      Quantity                                     ")


    t.set(1, 0, "")
    t.set(1, 1, "")

    root.mainloop()





f.pack_propagate(0)
root.mainloop()