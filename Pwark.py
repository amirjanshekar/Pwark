from tkinter import *
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from PIL import ImageTk, Image
import csv

win = Tk()
years = ['1400', '1401']

win.resizable(False, False)
win.title('Pwark')
picon = ImageTk.PhotoImage(Image.open("Images/123.png"))
win.iconphoto(False, picon)
title = Frame(win, bg='coral4')
win.configure(bg='black')
win.geometry('800x480')

img = ImageTk.PhotoImage(Image.open("Images/pwarklogo2.png"))
label = Label(win, image=img)
label.config(bg='black')
label.place(relx=0.28, rely=0.075)


img1 = ImageTk.PhotoImage(Image.open("Images/1.jpg"))
l1 = Label(win, image=img1)
l1.place(relx=0.43, rely=0.88)

img2 = ImageTk.PhotoImage(Image.open("Images/2.jpg"))
l2 = Label(win, image=img2)
l2.place(relx=0.52, rely=0.88)

img3 = ImageTk.PhotoImage(Image.open("Images/line.png"))
l3 = Label(win, image=img3)
l3.place(relx=0.25, rely=0.71)
l3.config(bg='black')

menubar = Menu(win)
win.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="ويرايش", menu=file_menu)

sub_menu2 = Menu(file_menu, tearoff=0)
sub_menu2.add_command(label='اضافه', command=lambda: add_year(False, years, year_list))
sub_menu2.add_command(label='حذف', command=lambda: add_year(True, years, year_list))
file_menu.add_cascade(label="سال", menu=sub_menu2)

year_label = Label(win, text='سال مورد نظر را انتخاب کنيد', fg='white', bg='black')
year_label.place(relx=0.7, rely=0.4)

selected_year = tk.StringVar()
year_list = ttk.Combobox(win, textvariable=selected_year, values=years, state="reandomly", width=15)
year_list.place(relx=0.72, rely=0.46)

label_month = Label(win, text='ماه مورد نظر را انتخاب کنيد', fg='white', bg='black')
label_month.place(relx=0.42, rely=0.4)

selected_month = tk.StringVar()
month_list = ttk.Combobox(win, textvariable=selected_month,
                          values=['فروردين', 'ارديبهشت', 'خرداد', 'تير', 'مرداد', 'شهريور', 'مهر', 'آبان', 'آذر', 'دي',
                                  'بهمن', 'اسفند'], state="reandomly", width=15)
month_list.place(relx=0.44, rely=0.46)

day_label = Label(win, text='روز مورد نظر را انتخاب کنيد', fg='white', bg='black')
day_label.place(relx=0.13, rely=0.4)

selected_day = tk.StringVar()
day_list = ttk.Combobox(win, textvariable=selected_day,
                        values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                                '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                '31'], state="reandomly", width=15)
day_list.place(relx=0.15, rely=0.46)


def sec_page():
    second_page = Toplevel()
    second_page.geometry('1360x768')
    second_page.resizable(False, False)
    second_page.configure(bg='gray5')
    second_page.title('Pwark')

    icon = ImageTk.PhotoImage(Image.open("Images/123.png"))
    second_page.iconphoto(False, icon)

    img4 = ImageTk.PhotoImage(Image.open("Images/pwarklogo1.png"))
    l4 = tk.Label(second_page, image=img4)
    l4.config(bg='gray5')
    l4.place(relx=0.001, rely=0.001)

    #img5 = ImageTk.PhotoImage(Image.open("../images/line2.png"))
    #l4 = tk.Label(second_page, image=img5)
    #l4.config(bg='gray5')
    #l4.place(relx=0.65, rely=0.27)

    style_combobox = ttk.Style()
    style_combobox.configure('TCombobox', background='blue', foreground='gray5')
    style_combobox.map('TCombobox', background=[('hover', 'darkorange')], foreground=[('hover', 'darkorange')])

    type_label = Label(second_page, text='نوع داده ', fg='saddle brown', bg='gray5', font=("Arial", 12, 'bold'))
    type_label.place(relx=0.79, rely=0.23)

    selected_type = tk.StringVar()
    type_list = ttk.Combobox(second_page, textvariable=selected_type, values=['ضايعات', 'دوباره کاري'],
                             state="reandomly", width=45)
    type_list.place(relx=0.71, rely=0.28)

    product_label = Label(second_page, text='انتخاب محصول ', fg='saddle brown', bg='gray5', font=("Arial", 12, 'bold'))
    product_label.place(relx=0.78, rely=0.33)

    with open("Data/ListOfProduct.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)

    selected_listofproduct = tk.StringVar()
    product_list = ttk.Combobox(second_page, textvariable=selected_listofproduct, values=data, state="reandomly",
                                width=45)
    product_list.place(relx=0.71, rely=0.38)

    label_ppm_rework = Label(second_page, text='انتخاب نوع ضايعات يا دوباره کاري', fg='saddle brown', bg='gray5',
                             font=("Arial", 12, 'bold'))
    label_ppm_rework.place(relx=0.73, rely=0.57)

    label_ppm_rework_list = tk.Listbox(second_page, width=50)
    label_ppm_rework_list.place(relx=0.71, rely=0.63)

    selected_number = tk.StringVar()
    number_spin = ttk.Spinbox(second_page, from_=0, to=10000, width=37, textvariable=selected_number, wrap=True)
    number_spin.place(relx=0.18, rely=0.64)

    label_number = Label(second_page, text='مقدار خرابی را وارد کنید', fg='saddle brown', bg='gray5', font=("Arial", 12,
                                                                                                            'bold'))
    label_number.place(relx=0.38, rely=0.63)

    label_explanation = Label(second_page, bg='grey3', width=109, height=16)
    label_explanation.place(relx=0.05, rely=0.26)

    style = ttk.Style()
    style.configure('TButton', background='blue', foreground='black')
    style.map('TButton', background=[('active', 'darkorange')], foreground=[('active', 'darkorange')])
    save_button = ttk.Button(second_page, text='ذخیره', width=20)
    save_button.place(relx=0.40, rely=0.8)

    bar_menu2 = Menu(second_page)
    second_page.config(menu=bar_menu2)
    menu_file2 = Menu(bar_menu2, tearoff=0)
    bar_menu2.add_cascade(label="گزارش", menu=menu_file2)

    sub_menu_output = Menu(menu_file2, tearoff=0)
    sub_menu_output.add_cascade(label='دوباره کاری')
    sub_menu_rework = Menu(menu_file2, tearoff=0)
    sub_menu_rework.add_command(label='گزارش ماهانه')
    sub_menu_rework.add_command(label='گزارش سه ماه')
    sub_menu_rework.add_command(label='گزارش شش ماهه')
    sub_menu_rework.add_command(label='گزارش سالانه')

    sub_menu_output.add_cascade(label='ضایعات')
    sub_menu_unconforting = Menu(menu_file2, tearoff=0)
    sub_menu_unconforting.add_command(label='گزارش ماهانه')
    sub_menu_unconforting.add_command(label='گزارش سه ماه')
    sub_menu_unconforting.add_command(label='گزارش شش ماهه')
    sub_menu_unconforting.add_command(label='گزارش سالانه')
    sub_menu_unconforting.add_command(label='لیست RPN')

    bar_menu = Menu(second_page)
    second_page.config(menu=bar_menu)
    menu_file = Menu(bar_menu, tearoff=0)
    bar_menu.add_cascade(label="ويرايش", menu=menu_file)

    sub_menu1 = Menu(menu_file, tearoff=0)
    sub_menu1.add_command(label='اضافه', command=lambda: add_product(False, data, product_list))
    sub_menu1.add_command(label='حذف', command=lambda: add_product(True, data, product_list))
    menu_file.add_cascade(label="محصول", menu=sub_menu1)

    def add_product(state, d_list, combo_box):
        if state:
            remove_product = Toplevel()
            remove_product.geometry("400x200")
            remove_product.configure(bg='white')
            remove_product.resizable(False, False)
            remove_product.title('ويرايش محصولات')
            label1 = Label(remove_product, text='محصول جديد را وارد کنيد', bg='white', fg='black')
            label1.place(relx=0.34, rely=0.25)
            entry1 = Entry(remove_product, width=18)
            entry1.place(relx=0.34, rely=0.4)

            b_product = ttk.Button(remove_product, text='اضافه',
                                   command=lambda: insert_value(entry1, d_list, combo_box, remove_product))
            b_product.place(relx=0.38, rely=0.6)
        else:
            remove_product = Toplevel()
            remove_product.geometry("400x200")
            remove_product.configure(bg='white')
            remove_product.resizable(False, False)
            remove_product.title('ويرايش محصولات')
            label1 = Label(remove_product, text='محصول جديد را وارد کنيد', bg='white', fg='black')
            label1.place(relx=0.34, rely=0.25)
            entry1 = Entry(remove_product, width=18)
            entry1.place(relx=0.34, rely=0.4)

            b_product = ttk.Button(remove_product, text='اضافه',
                                   command=lambda: insert_value(entry1, d_list, combo_box, remove_product))
            b_product.place(relx=0.38, rely=0.6)

    sub_menu_2 = Menu(menu_file, tearoff=0)
    sub_menu_2.add_command(label='اضافه', command=lambda: add_failur_product(False, years, year_list))
    sub_menu_2.add_command(label='حذف', command=lambda: add_failur_product(True, data, product_list))
    menu_file.add_cascade(label="لیست خرابی", menu=sub_menu_2)

    def add_failur_product(state, d_list, combo_box):
        if state:
            remove_failur_product = Toplevel()
            remove_failur_product.geometry("400x200")
            remove_failur_product.configure(bg='white')
            remove_failur_product.resizable(False, False)
            remove_failur_product.title('ويرايش محصولات')
            label1 = Label(remove_failur_product, text='محصول جديد را وارد کنيد', bg='white', fg='black')
            label1.place(relx=0.34, rely=0.25)
            entry1 = Entry(remove_failur_product, width=18)
            entry1.place(relx=0.34, rely=0.4)

            b_product = ttk.Button(remove_failur_product, text='اضافه',
                                   command=lambda: insert_value(entry1, d_list, combo_box, remove_failur_product))
            b_product.place(relx=0.38, rely=0.6)
        else:
            remove_failur_product = Toplevel()
            remove_failur_product.geometry("400x200")
            remove_failur_product.configure(bg='white')
            remove_failur_product.resizable(False, False)
            remove_failur_product.title('ويرايش محصولات')
            label1 = Label(remove_failur_product, text='محصول جديد را وارد کنيد', bg='white', fg='black')
            label1.place(relx=0.34, rely=0.25)
            entry1 = Entry(remove_failur_product, width=18)
            entry1.place(relx=0.34, rely=0.4)

            b_product = ttk.Button(remove_failur_product, text='اضافه',
                                   command=lambda: insert_value(entry1, d_list, combo_box, remove_failur_product))
            b_product.place(relx=0.38, rely=0.6)

    sub_menu_2 = Menu(menu_file, tearoff=0)
    sub_menu_2.add_command(label='اضافه', command=lambda: add_info_product(False, years, year_list))
    sub_menu_2.add_command(label='حذف', command=lambda: add_info_product(True, data, product_list))
    menu_file.add_cascade(label="تصویر یا نوشته", menu=sub_menu_2)

    def add_info_product(state, d_list, combo_box):
        if state:
            remove_info_product = Toplevel()
            remove_info_product.geometry("400x200")
            remove_info_product.configure(bg='white')
            remove_info_product.resizable(False, False)
            remove_info_product.title('ويرايش محصولات')
            label1 = Label(remove_info_product, text='محصول جديد را وارد کنيد', bg='white', fg='black')
            label1.place(relx=0.34, rely=0.25)
            entry1 = Entry(remove_info_product, width=18)
            entry1.place(relx=0.34, rely=0.4)

            b_product = ttk.Button(remove_info_product, text='اضافه',
                                   command=lambda: insert_value(entry1, d_list, combo_box, remove_info_product))
            b_product.place(relx=0.38, rely=0.6)
        else:
            remove_info_product = Toplevel()
            remove_info_product.geometry("400x200")
            remove_info_product.configure(bg='white')
            remove_info_product.resizable(False, False)
            remove_info_product.title('ويرايش محصولات')
            label1 = Label(remove_info_product, text='محصول جديد را وارد کنيد', bg='white', fg='black')
            label1.place(relx=0.34, rely=0.25)
            entry1 = Entry(remove_info_product, width=18)
            entry1.place(relx=0.34, rely=0.4)

            b_product = ttk.Button(remove_info_product, text='اضافه',
                                   command=lambda: insert_value(entry1, d_list, combo_box, remove_info_product))
            b_product.place(relx=0.38, rely=0.6)
    second_page.mainloop()


style = ttk.Style()
style.configure('TButton', background='blue', foreground='black')
style.map('TButton', background=[('active', 'darkorange')], foreground=[('active', 'darkorange')])
open_button = ttk.Button(win, text='ورود', command=sec_page)
open_button.place(relx=0.46, rely=0.61)


def insert_value(entry, data_list, combo_box, modal):
    if entry.get() not in data_list:
        data_list.append(entry.get())
        combo_box['values'] = data_list
    modal.destroy()


def add_year(state, years_list, combo_box):
    if state:
        remove_year = Toplevel()
        remove_year.geometry("400x200")
        remove_year.configure(bg='white')
        remove_year.resizable(False, False)
        remove_year.title('ويرايش سال')
        label_2 = Label(remove_year, text='سال جديد را وارد کنيد', bg='white', fg='black')
        label_2.place(relx=0.34, rely=0.25)
        entry1 = Entry(remove_year, width=18)
        entry1.place(relx=0.34, rely=0.4)

        b_product = ttk.Button(remove_year, text='اضافه',
                               command=lambda: insert_value(entry1, years_list, combo_box, remove_year))
        b_product.place(relx=0.38, rely=0.6)
    else:
        remove_year = Toplevel()
        remove_year.geometry("400x200")
        remove_year.configure(bg='white')
        remove_year.resizable(False, False)
        remove_year.title('ويرايش سال')
        label_2 = Label(remove_year, text='سال جديد را وارد کنيد', bg='white', fg='black')
        label_2.place(relx=0.34, rely=0.25)
        entry1 = Entry(remove_year, width=18)
        entry1.place(relx=0.34, rely=0.4)

        b_product = ttk.Button(remove_year, text='اضافه',
                               command=lambda: insert_value(entry1, years_list, combo_box, remove_year))
        b_product.place(relx=0.38, rely=0.6)


win.mainloop()