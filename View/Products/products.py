from tkinter import *
from tkinter import ttk, Entry
from PIL import ImageTk, Image
from Controllers.products_controller import ProductsController
from Controllers.wastage_controller import WastageController


class Products(Tk):
    add_product_entry: Entry
    add_un_comforting_entry: Entry
    add_info_entry: Entry

    def __init__(self, connection, data):
        super().__init__()

        self.connection = connection
        self.data = data

        self.add_wastage_entries = []

        self.products = ProductsController.fetch_all_products(connection)

        self.wastage = WastageController.fetch_all_wastage(connection)

        self.geometry('1350x768')
        self.resizable(width=False, height=False)
        self.config(bg='black')

        self.icon = ImageTk.PhotoImage(Image.open("Images/123.png"))
        self.iconphoto(False, self.icon)

        self.img4 = ImageTk.PhotoImage(Image.open("Images/pwarklogo1.png"))
        self.top_image = Label(image=self.img4)
        self.top_image.config(bg='gray5')
        self.top_image.place(relx=0.001, rely=0.001)

        self.type_label = Label(self, text='Data type', fg='saddle brown', bg='gray5', font=("Arial", 12, 'bold'))
        self.type_label.place(relx=0.765, rely=0.23)

        self.type_list = ttk.Combobox(self, textvariable=StringVar(), values=['ضايعات', 'دوباره کاري'],
                                      state="readonly", width=35)
        self.type_list.current(0)
        self.type_list.place(relx=0.71, rely=0.28)

        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        self.main_menu = Menu(self.menubar, tearoff=0)
        self.report_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.main_menu)
        self.menubar.add_cascade(label="Report", menu=self.report_menu)

        self.product_sub_menu = Menu(self.main_menu, tearoff=0)
        self.product_sub_menu.add_command(label='Add', command=self.add_product)
        self.product_sub_menu.add_command(label='Remove')
        self.main_menu.add_cascade(label="Product", menu=self.product_sub_menu)

        self.un_comforting = Menu(self.main_menu, tearoff=0)
        self.un_comforting.add_command(label='Add')
        self.un_comforting.add_command(label='Remove')
        self.main_menu.add_cascade(label="Uncomforting", menu=self.un_comforting)

        self.info_sub_menu = Menu(self.main_menu, tearoff=0)
        self.info_sub_menu.add_command(label='Add')
        self.info_sub_menu.add_command(label='Remove')
        self.main_menu.add_cascade(label="Picture or Text", menu=self.info_sub_menu)

        self.product_sub_menu = Menu(self.main_menu, tearoff=0)
        self.product_sub_menu.add_command(label='Add')
        self.product_sub_menu.add_command(label='Remove')
        self.main_menu.add_cascade(label="Product", menu=self.product_sub_menu)

        self.rework_sub_menu = Menu(self.report_menu, tearoff=0)
        self.rework_sub_menu.add_command(label='گزارش ماهانه')
        self.rework_sub_menu.add_command(label='گزارش سه ماه')
        self.rework_sub_menu.add_command(label='گزارش شش ماهه')
        self.rework_sub_menu.add_command(label='گزارش سالانه')
        self.report_menu.add_cascade(label='دوباره کاری', menu=self.rework_sub_menu)

        self.un_comforting_sub_menu = Menu(self.report_menu, tearoff=0)
        self.un_comforting_sub_menu.add_command(label='گزارش ماهانه')
        self.un_comforting_sub_menu.add_command(label='گزارش سه ماه')
        self.un_comforting_sub_menu.add_command(label='گزارش شش ماهه')
        self.un_comforting_sub_menu.add_command(label='گزارش سالانه')
        self.un_comforting_sub_menu.add_command(label='لیست RPN')
        self.report_menu.add_cascade(label='ضایعات', menu=self.un_comforting_sub_menu)

        self.product_label = Label(self, text='Chose product', fg='saddle brown', bg='gray5',
                                   font=("Arial", 12, 'bold'))
        self.product_label.place(relx=0.75, rely=0.33)

        self.product_list = ttk.Combobox(self, values=self.products, width=35)
        self.product_list.current(0)
        self.product_list.place(relx=0.71, rely=0.38)

        self.label_ppm_rework = Label(self, text='Chose data', fg='saddle brown', bg='gray5',
                                      font=("Arial", 12, 'bold'))
        self.label_ppm_rework.place(relx=0.765, rely=0.57)

        self.label_ppm_rework_list = Listbox(self, width=50)
        self.label_ppm_rework_list.place(relx=0.69, rely=0.63)

        self.number_spin = ttk.Spinbox(self, from_=0, to=10000, width=37, textvariable=StringVar(), wrap=True)
        self.number_spin.place(relx=0.20, rely=0.64)

        self.label_number = Label(self, text='Enter number', fg='saddle brown', bg='gray5',
                                  font=("Arial", 12,
                                        'bold'))
        self.label_number.place(relx=0.40, rely=0.635)

        self.label_explanation = Label(self, bg='grey3', width=109, height=16)
        self.label_explanation.place(relx=0.05, rely=0.26)

        ttk.Style().configure('TButton', background='blue', foreground='black')
        ttk.Style().map('TButton', background=[('active', 'darkorange')], foreground=[('active', 'darkorange')])
        self.save_button = ttk.Button(self, text='Add data', width=20)
        self.save_button.place(relx=0.40, rely=0.8)

    def add_product(self):
        add_product_window = Tk()
        add_product_window.geometry("400x200")
        add_product_window.configure(bg='white')
        add_product_window.resizable(False, False)
        add_product_window.title('Edit Products')

        add_product_entry_frame = Frame(add_product_window)
        add_product_entry_frame.grid(row=0, column=0, padx=10, pady=10)

        add_product_table_frame = Frame(add_product_window, bg='white')
        add_product_table_frame.grid(row=1, column=0, padx=10, pady=10, sticky='')

        add_product_button_frame = Frame(add_product_window, bg='white')
        add_product_button_frame.grid(row=2, column=0, pady=10, padx=10)

        label1 = Label(add_product_entry_frame, text='Enter New Product', bg='white', fg='black')
        label1.grid(row=0, column=0, sticky='')
        self.add_product_entry = Entry(add_product_entry_frame, width=18)
        self.add_product_entry.grid(row=0, column=1, sticky='')
        entries = []

        detection_label = Label(add_product_table_frame, text='Detection', bg='white', fg='black')
        detection_label.grid(row=0, column=0)

        severity_label = Label(add_product_table_frame, text='Severity', bg='white', fg='black')
        severity_label.grid(row=0, column=1)

        wastage_label = Label(add_product_table_frame, text='Wastage', bg='white', fg='black', width=20)
        wastage_label.grid(row=0, column=2)

        for col in range(3):
            if col == 2:
                self.add_wastage_entries.append(Entry(add_product_table_frame, width=20))
            else:
                self.add_wastage_entries.append(Entry(add_product_table_frame, width=10))
            self.add_wastage_entries[col].grid(row=1, column=col, padx=10)

        add_product_button = ttk.Button(add_product_button_frame, text='Add',
                                        command=lambda: self.insert_product_to_list(add_product_window))
        add_product_button.grid(row=0, column=0, sticky='')

    def add_un_comforting(self):
        un_comforting_window = Tk()
        un_comforting_window.geometry("400x200")
        un_comforting_window.configure(bg='white')
        un_comforting_window.resizable(False, False)
        un_comforting_window.title('Edit Uncomfortings')
        label1 = Label(un_comforting_window, text='Enter New Uncomforting', bg='white', fg='black')
        label1.place(relx=0.34, rely=0.25)
        self.add_un_comforting_entry = Entry(un_comforting_window, width=18)
        self.add_un_comforting_entry.place(relx=0.34, rely=0.4)
        add_un_comforting_button = Button(un_comforting_window, text='Add',
                                          command=lambda: self.insert_un_comforting_to_list(un_comforting_window))
        add_un_comforting_button.place(relx=0.38, rely=0.5)

    def add_info(self):
        info_window = Tk()
        info_window.geometry("400x200")
        info_window.configure(bg='white')
        info_window.resizable(False, False)
        info_window.title('Edit Uncomfortings')
        label1 = Label(info_window, text='Enter New Uncomforting', bg='white', fg='black')
        label1.place(relx=0.34, rely=0.25)
        self.add_info_entry = Entry(info_window, width=18)
        self.add_info_entry.place(relx=0.34, rely=0.4)
        add_info_button = Button(info_window, text='Add',
                                 command=lambda: self.insert_info_to_list(info_window))
        add_info_button.place(relx=0.38, rely=0.5)

    def insert_product_to_list(self, modal):
        if self.add_product_entry.get() not in self.products:
            ProductsController.add_product(self.connection, self.add_product_entry.get())
            self.products = ProductsController.fetch_all_products(self.connection)
            self.product_list['values'] = self.products
        product_id = ProductsController.fetch_product_by_name(self.connection, self.add_product_entry.get())[0]
        if self.add_wastage_entries[2].get() not in self.wastage:
            WastageController.add_wastage(self.connection, wastage=self.add_wastage_entries[2].get(),
                                          product_id=product_id, severity=self.add_wastage_entries[1].get(),
                                          detection=self.add_wastage_entries[0].get())
        modal.destroy()

    def insert_un_comforting_to_list(self, modal):
        if self.add_product_entry.get() not in self.data:
            ProductsController.add_product(self.connection, self.add_product_entry.get())
            self.data = ProductsController.fetch_all_products(self.connection)
            self.product_list['values'] = self.data
        modal.destroy()

    def insert_info_to_list(self, modal):
        if self.add_product_entry.get() not in self.data:
            ProductsController.add_product(self.connection, self.add_product_entry.get())
            self.data = ProductsController.fetch_all_products(self.connection)
            self.product_list['values'] = self.data
        modal.destroy()
