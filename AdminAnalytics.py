import tkinter as tk

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DatabaseHelper import *

class Analytics:
    def __init__(self):
        self.temp_root = tk.Toplevel()
        self.temp_root.geometry('1500x700')
        self.add_bar_graph("Total earnings per day")
        self.add_line_graph("Total orders per day")

    def get_manufacturing_total_data(self):
        query = """ Select Orderdate, sell_P 
                    from project.orders
                    order by Orderdate
                """
        result = DatabaseHelper.get_all_data(query)

        df1 = DataFrame(result[1:], columns=result[0]).groupby("Orderdate").sum()
        return df1

    def get_total_orders_data(self):
        query = """ Select Orderdate, sell_p 
                    from project.orders
                    order by Orderdate
                """
        result = DatabaseHelper.get_all_data(query)

        df = DataFrame(result[1:], columns=result[0]).groupby("Orderdate").count()
        return df

    def add_bar_graph(self, title):
        df1 = self.get_manufacturing_total_data()
        figure1 = plt.Figure(figsize=(7, 5), dpi=100)
        ax1 = figure1.subplots()

        bar1 = FigureCanvasTkAgg(figure1, self.temp_root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1.plot(kind='bar', legend=True, ax=ax1, fontsize=10)
        ax1.set_title(title)

    def add_line_graph(self, title):
        df2 = self.get_total_orders_data()

        figure2 = plt.Figure(figsize=(7, 4), dpi=100)
        ax2 = figure2.subplots()

        line2 = FigureCanvasTkAgg(figure2, self.temp_root)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2.plot(kind='line', legend=True, ax=ax2, color='red', marker='o', fontsize=10)
        ax2.set_title(title)

