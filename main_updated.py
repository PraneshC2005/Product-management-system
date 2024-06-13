import sqlite3
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class Product:
    # Database file name
    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.bg = Image.open("images/5153829.jpg")
        self.bg = self.bg.resize((1918, 1080))
        self.bg_img = ImageTk.PhotoImage(self.bg)
        self.bg_label = Label(window, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.wind.title('Products Application')
        self.wind.attributes('-fullscreen', True)
        self.wind.configure(bg='lightgray')

        # Close button to exit fullscreen mode
        close_button = Button(self.wind, text='Exit', font=('Arial', 18), bg='red', fg='white', command=self.wind.quit)
        close_button.grid(row=0, column=0, pady=10, padx=10, sticky='nw')

        # Configuring grid layout to expand with window size
        self.wind.grid_rowconfigure(1, weight=1)
        self.wind.grid_rowconfigure(2, weight=1)
        self.wind.grid_rowconfigure(3, weight=10)
        self.wind.grid_rowconfigure(4, weight=1)
        self.wind.grid_columnconfigure(0, weight=1)
        self.wind.grid_columnconfigure(1, weight=1)

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Register new Product', bg='#e0f7fa', padx=20, pady=20, bd=2, relief=RIDGE, font=('Arial', 16, 'bold'))
        frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20, sticky='n')
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Name Input Frame
        name_frame = Frame(frame, bg='#e0f7fa', bd=0, relief=FLAT)
        name_frame.grid(row=0, column=0, columnspan=2, pady=10, padx=150)
        name_frame.grid_columnconfigure(0, weight=1)
        name_frame.grid_columnconfigure(1, weight=2)
        Label(name_frame, text='Name: ', bg='#e0f7fa', font=('Arial', 14)).grid(row=0, column=0, sticky='e', padx=3, pady=3)
        self.name = Entry(name_frame, font=('Arial', 14))
        self.name.focus()
        self.name.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        # Price Input Frame
        price_frame = Frame(frame, bg='#e0f7fa', bd=0, relief=FLAT)
        price_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=150)
        price_frame.grid_columnconfigure(0, weight=1)
        price_frame.grid_columnconfigure(1, weight=2)
        Label(price_frame, text='Price: ', bg='#e0f7fa', font=('Arial', 14)).grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.price = Entry(price_frame, font=('Arial', 14))
        self.price.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        # Model Name Input Frame
        model_frame = Frame(frame, bg='#e0f7fa', bd=0, relief=FLAT)
        model_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=150)
        model_frame.grid_columnconfigure(0, weight=1)
        model_frame.grid_columnconfigure(1, weight=2)
        Label(model_frame, text='Model Name: ', bg='#e0f7fa', font=('Arial', 14)).grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.model_name = Entry(model_frame, font=('Arial', 14))
        self.model_name.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        # Year of Launch Input Frame
        year_frame = Frame(frame, bg='#e0f7fa', bd=0, relief=FLAT)
        year_frame.grid(row=3, column=0, columnspan=2, pady=10, padx=150)
        year_frame.grid_columnconfigure(0, weight=1)
        year_frame.grid_columnconfigure(1, weight=2)
        Label(year_frame, text='Year of Launch: ', bg='#e0f7fa', font=('Arial', 14)).grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.year_of_launch = Entry(year_frame, font=('Arial', 14))
        self.year_of_launch.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        # Button Add Product
        save_button = Button(frame, text='Save Product', command=self.add_product, bg='#00796b', fg='white', font=('Arial', 14), relief=RAISED, bd=2)
        save_button.grid(row=4, column=0, columnspan=2, pady=10, padx=150, ipadx=10)

        # Output Messages
        self.message = Label(self.wind, text='', fg='red', font=('Arial', 14))
        self.message.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=(600, 500), pady=20)

        # Table
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=("Arial", 14), rowheight=30)
        style.configure("mystyle.Treeview.Heading", font=("Arial", 16, 'bold'))
        table_frame = Frame(self.wind, bd=2, relief=RIDGE)
        table_frame.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=400, pady=20)
        table_frame.grid_columnconfigure(0, weight=1)
        self.tree = ttk.Treeview(table_frame, height=10, columns=(1, 2, 3, 4), style="mystyle.Treeview")
        self.tree.grid(row=0, column=0, sticky='nsew')

        self.tree.heading('#0', text='ID', anchor=CENTER)
        self.tree.heading('#1', text='Name', anchor=CENTER)
        self.tree.heading('#2', text='Price', anchor=CENTER)
        self.tree.heading('#3', text='Model Name', anchor=CENTER)
        self.tree.heading('#4', text='Year of Launch', anchor=CENTER)

        # Add these lines to center the text in the columns
        self.tree.column('#0', anchor=CENTER, width=50)
        self.tree.column('#1', anchor=CENTER, width=150)
        self.tree.column('#2', anchor=CENTER, width=100)
        self.tree.column('#3', anchor=CENTER, width=150)
        self.tree.column('#4', anchor=CENTER, width=150)

        # Buttons
        button_frame = Frame(self.wind, bd=0, relief=FLAT)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=150)
        Button(button_frame, text='DELETE', command=self.delete_product, bg='#d9534f', fg='white',font=('Arial', 14, 'bold'), padx=10, pady=5, borderwidth=2, relief=SOLID).grid(row=0, column=0, padx=5,pady=10)
        Button(button_frame, text='EDIT', command=self.edit_product, bg='#5bc0de', fg='white',font=('Arial', 14, 'bold'), padx=10, pady=5, borderwidth=2, relief=SOLID).grid(row=0, column=1, padx=5,pady=10)

        # Filling the Rows
        self.get_products()

    # Function to Execute Database Queries
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
    def get_products(self):
        # Cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Getting data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]), tags=('center',))

        # Apply tag configuration to center the text
        self.tree.tag_configure('center', anchor=CENTER)

    # User Input Validation
    def validation(self):
        try:
            int(self.year_of_launch.get())
            int(self.price.get())
            return len(self.name.get()) != 0 and len(self.model_name.get()) != 0
        except ValueError:
            self.message['text'] = 'Year of Launch and Price must be integers'
            return False

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?, ?, ?)'
            parameters = (self.name.get(), self.price.get(), self.model_name.get(), self.year_of_launch.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
            self.model_name.delete(0, END)
            self.year_of_launch.delete(0, END)
        else:
            self.message['text'] = 'All fields are Required'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        id = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE id = ?'
        self.run_query(query, (id,))
        self.message['text'] = 'Record {} deleted Successfully'.format(id)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            id = self.tree.item(self.tree.selection())['text']
        except IndexError:
            self.message['text'] = 'Please select a Record'
            return

        old_name = self.tree.item(self.tree.selection())['values'][0]
        old_price = self.tree.item(self.tree.selection())['values'][1]
        old_model_name = self.tree.item(self.tree.selection())['values'][2]
        old_year_of_launch = self.tree.item(self.tree.selection())['values'][3]

        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        self.edit_wind.configure(bg='#e0f7fa')

        Label(self.edit_wind, text='Old Name:', bg='#e0f7fa', font=('Arial', 14)).grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_name), state='readonly', font=('Arial', 14)).grid(row=0, column=2)

        Label(self.edit_wind, text='New Name:', bg='#e0f7fa', font=('Arial', 14)).grid(row=1, column=1)
        new_name = Entry(self.edit_wind, font=('Arial', 14))
        new_name.grid(row=1, column=2)

        Label(self.edit_wind, text='Old Price:', bg='#e0f7fa', font=('Arial', 14)).grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_price), state='readonly', font=('Arial', 14)).grid(row=2, column=2)

        Label(self.edit_wind, text='New Price:', bg='#e0f7fa', font=('Arial', 14)).grid(row=3, column=1)
        new_price = Entry(self.edit_wind, font=('Arial', 14))
        new_price.grid(row=3, column=2)

        Label(self.edit_wind, text='Old Model Name:', bg='#e0f7fa', font=('Arial', 14)).grid(row=4, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_model_name), state='readonly', font=('Arial', 14)).grid(row=4, column=2)

        Label(self.edit_wind, text='New Model Name:', bg='#e0f7fa', font=('Arial', 14)).grid(row=5, column=1)
        new_model_name = Entry(self.edit_wind, font=('Arial', 14))
        new_model_name.grid(row=5, column=2)

        Label(self.edit_wind, text='Old Year of Launch:', bg='#e0f7fa', font=('Arial', 14)).grid(row=6, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_year_of_launch), state='readonly', font=('Arial', 14)).grid(row=6, column=2)

        Label(self.edit_wind, text='New Year of Launch:', bg='#e0f7fa', font=('Arial', 14)).grid(row=7, column=1)
        new_year_of_launch = Entry(self.edit_wind, font=('Arial', 14))
        new_year_of_launch.grid(row=7, column=2)

        Button(self.edit_wind, text='Update', command=lambda: self.edit_records(
            new_name.get(), old_name, new_price.get(), old_price, new_model_name.get(), old_model_name,
            new_year_of_launch.get(), old_year_of_launch, id), bg='#00796b', fg='white', font=('Arial', 14)).grid(row=8, column=2, sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, old_name, new_price, old_price, new_model_name, old_model_name, new_year_of_launch,
                     old_year_of_launch, id):
        query = 'UPDATE product SET name = ?, price = ?, model_name = ?, year_of_launch = ? WHERE id = ?'
        parameters = (new_name, new_price, new_model_name, new_year_of_launch, id)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated Successfully'.format(id)
        self.get_products()

if __name__ == '__main__':
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                model_name TEXT NOT NULL,
                year_of_launch INTEGER NOT NULL
            )
        ''')
        conn.commit()

    window = Tk()
    application = Product(window)
    window.mainloop()
