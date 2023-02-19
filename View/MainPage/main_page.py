from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Controllers.years_controller import YearsController
from View.Products.products import Products


class MainMenu(Tk):

    def __init__(self, connection):
        super().__init__()

        self.connection = connection
        self.title('Pwark')
        self.geometry('800x480')
        self.resizable(width=False, height=False)
        self.config(bg='black')
        self.picon = ImageTk.PhotoImage(Image.open("Images/123.png"))
        self.iconphoto(False, self.picon)

        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        self.main_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.main_menu)

        self.year_sub_menu = Menu(self.main_menu, tearoff=0)
        self.year_sub_menu.add_command(label='Add')
        self.year_sub_menu.add_command(label='Remove')
        self.main_menu.add_cascade(label="Year", menu=self.year_sub_menu)

        self.title_img = ImageTk.PhotoImage(Image.open("Images/pwarklogo2.png"))
        self.title = Label(image=self.title_img)
        self.title.config(bg='black')
        self.title.place(relx=0.28, rely=0.075)

        self.right_logo_img = ImageTk.PhotoImage(Image.open("Images/1.jpg"))
        self.right_logo = Label(image=self.right_logo_img)
        self.right_logo.place(relx=0.43, rely=0.88)

        self.left_logo_img = ImageTk.PhotoImage(Image.open("Images/2.jpg"))
        self.left_logo = Label(image=self.left_logo_img)
        self.left_logo.place(relx=0.52, rely=0.88)

        self.divider_img = ImageTk.PhotoImage(Image.open("Images/line.png"))
        self.divider = Label(image=self.divider_img)
        self.divider.config(bg='black')
        self.divider.place(relx=0.25, rely=0.71)

        self.year_label = Label(self, text='Choose the year', bg='black', fg='white')
        self.year_label.place(relx=0.715, rely=0.4)

        self.year_data = YearsController.fetch_all_years(self.connection)
        self.years = [year_row['year'] for year_row in self.year_data]

        self.year_list = ttk.Combobox(self, textvariable=StringVar(), values=self.years, state="readonly", width=10)
        self.year_list.current(0)
        self.year_list.place(relx=0.72, rely=0.46)

        self.label_month = Label(self, text='Choose the month', bg='black', fg='white')
        self.label_month.place(relx=0.44, rely=0.4)

        self.months = [
            {'id': 1, 'value': 'فروردين'},
            {'id': 2, 'value': 'ارديبهشت'},
            {'id': 3, 'value': 'خرداد'},
            {'id': 4, 'value': 'تير'},
            {'id': 5, 'value': 'مرداد'},
            {'id': 6, 'value': 'شهريور'},
            {'id': 7, 'value': 'مهر'},
            {'id': 8, 'value': 'آبان'},
            {'id': 9, 'value': 'آذر'},
            {'id': 10, 'value': 'دي'},
            {'id': 11, 'value': 'بهمن'},
            {'id': 12, 'value': 'اسفند'},
        ]
        self.month_list = ttk.Combobox(self, textvariable=StringVar(), values=[month['value'] for month in self.months],
                                       state="readonly", width=15)
        self.month_list.current(0)
        self.month_list.place(relx=0.44, rely=0.46)

        self.day_label = Label(self, text='Chose the day', bg='black', fg='white')
        self.day_label.place(relx=0.15, rely=0.4)

        self.day_list = ttk.Combobox(self, textvariable=StringVar(),
                                     values=[f"{i}" for i in range(1, 32)], state="readonly", width=10)
        self.day_list.current(0)
        self.day_list.place(relx=0.15, rely=0.46)

        ttk.Style().configure('TButton', background='blue', foreground='black')
        ttk.Style().map('TButton', background=[('active', 'darkorange')], foreground=[('active', 'darkorange')])
        self.next_button = ttk.Button(self, text='Next Page', command=self.go_to_second_page)
        self.next_button.place(relx=0.46, rely=0.61)

    def go_to_second_page(self):
        month = (month['id'] for month in self.months if month['value'] == self.month_list.get()).__next__()
        data = {"year": self.year_list.get, 'month': month, 'day': self.day_list.get()}
        self.destroy()
        products = Products(self.connection, data)
        products.mainloop()
