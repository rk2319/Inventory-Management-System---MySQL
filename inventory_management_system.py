import tkinter as tk
from tkinter import ttk
import sqlite3

class FrontendApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Management System")
        
        self.tab_control = ttk.Notebook(self.master)
        
        # Customer Tab
        self.customer_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.customer_tab, text='Customers')
        
        # Order Tab
        self.order_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.order_tab, text='Orders')
        
        # Supplier Tab
        self.supplier_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.supplier_tab, text='Suppliers')
        
        # Product Tab
        self.product_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.product_tab, text='Products')
        
        # Inventory Tab
        self.inventory_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.inventory_tab, text='Inventory')
        
        # Adding tabs to the main window
        self.tab_control.pack(expand=1, fill="both")
        
        # Create SQLite Database and Tables
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        
        # Customer Table
        self.customer_tree = ttk.Treeview(self.customer_tab, columns=("ID", "Name", "Email", "Phone"))
        self.customer_tree.heading("#0", text="ID")
        self.customer_tree.heading("ID", text="ID")
        self.customer_tree.heading("Name", text="Name")
        self.customer_tree.heading("Email", text="Email")
        self.customer_tree.heading("Phone", text="Phone")
        self.customer_tree.pack(fill="both", expand=True)
        
        # Customer Entry Fields with Labels
        tk.Label(self.customer_tab, text="Name:").pack()
        self.customer_name_entry = tk.Entry(self.customer_tab)
        self.customer_name_entry.pack()
        tk.Label(self.customer_tab, text="Email:").pack()
        self.customer_email_entry = tk.Entry(self.customer_tab)
        self.customer_email_entry.pack()
        tk.Label(self.customer_tab, text="Phone:").pack()
        self.customer_phone_entry = tk.Entry(self.customer_tab)
        self.customer_phone_entry.pack()
        
        # Add Customer Button
        self.add_customer_button = tk.Button(self.customer_tab, text="Add Customer", command=self.add_customer)
        self.add_customer_button.pack()

        # Delete Customer Button
        self.delete_customer_button = tk.Button(self.customer_tab, text="Delete Selected", command=self.delete_customer)
        self.delete_customer_button.pack()

        # Order Table
        self.order_tree = ttk.Treeview(self.order_tab, columns=("ID", "Customer", "Product", "Quantity", "Total"))
        self.order_tree.heading("#0", text="ID")
        self.order_tree.heading("ID", text="ID")
        self.order_tree.heading("Customer", text="Customer")
        self.order_tree.heading("Product", text="Product")
        self.order_tree.heading("Quantity", text="Quantity")
        self.order_tree.heading("Total", text="Total")
        self.order_tree.pack(fill="both", expand=True)

        # Order Entry Fields with Labels
        tk.Label(self.order_tab, text="Customer ID:").pack()
        self.order_customer_id_entry = tk.Entry(self.order_tab)
        self.order_customer_id_entry.pack()
        tk.Label(self.order_tab, text="Product ID:").pack()
        self.order_product_id_entry = tk.Entry(self.order_tab)
        self.order_product_id_entry.pack()
        tk.Label(self.order_tab, text="Quantity:").pack()
        self.order_quantity_entry = tk.Entry(self.order_tab)
        self.order_quantity_entry.pack()

        # Add Order Button
        self.add_order_button = tk.Button(self.order_tab, text="Add Order", command=self.add_order)
        self.add_order_button.pack()

        # Delete Order Button
        self.delete_order_button = tk.Button(self.order_tab, text="Delete Selected", command=self.delete_order)
        self.delete_order_button.pack()

        # Supplier Table
        self.supplier_tree = ttk.Treeview(self.supplier_tab, columns=("ID", "Name", "Email", "Phone"))
        self.supplier_tree.heading("#0", text="ID")
        self.supplier_tree.heading("ID", text="ID")
        self.supplier_tree.heading("Name", text="Name")
        self.supplier_tree.heading("Email", text="Email")
        self.supplier_tree.heading("Phone", text="Phone")
        self.supplier_tree.pack(fill="both", expand=True)

        # Supplier Entry Fields with Labels
        tk.Label(self.supplier_tab, text="Name:").pack()
        self.supplier_name_entry = tk.Entry(self.supplier_tab)
        self.supplier_name_entry.pack()
        tk.Label(self.supplier_tab, text="Email:").pack()
        self.supplier_email_entry = tk.Entry(self.supplier_tab)
        self.supplier_email_entry.pack()
        tk.Label(self.supplier_tab, text="Phone:").pack()
        self.supplier_phone_entry = tk.Entry(self.supplier_tab)
        self.supplier_phone_entry.pack()

        # Add Supplier Button
        self.add_supplier_button = tk.Button(self.supplier_tab, text="Add Supplier", command=self.add_supplier)
        self.add_supplier_button.pack()

        # Delete Supplier Button
        self.delete_supplier_button = tk.Button(self.supplier_tab, text="Delete Selected", command=self.delete_supplier)
        self.delete_supplier_button.pack()

        # Product Table
        self.product_tree = ttk.Treeview(self.product_tab, columns=("ID", "Name", "Price", "Category"))
        self.product_tree.heading("#0", text="ID")
        self.product_tree.heading("ID", text="ID")
        self.product_tree.heading("Name", text="Name")
        self.product_tree.heading("Price", text="Price")
        self.product_tree.heading("Category", text="Category")
        self.product_tree.pack(fill="both", expand=True)

        # Product Entry Fields with Labels
        tk.Label(self.product_tab, text="Name:").pack()
        self.product_name_entry = tk.Entry(self.product_tab)
        self.product_name_entry.pack()
        tk.Label(self.product_tab, text="Price:").pack()
        self.product_price_entry = tk.Entry(self.product_tab)
        self.product_price_entry.pack()
        tk.Label(self.product_tab, text="Category:").pack()
        self.product_category_entry = tk.Entry(self.product_tab)
        self.product_category_entry.pack()

        # Add Product Button
        self.add_product_button = tk.Button(self.product_tab, text="Add Product", command=self.add_product)
        self.add_product_button.pack()

        # Delete Product Button
        self.delete_product_button = tk.Button(self.product_tab, text="Delete Selected", command=self.delete_product)
        self.delete_product_button.pack()

        # Inventory Table
        self.inventory_tree = ttk.Treeview(self.inventory_tab, columns=("ID", "Product", "Quantity"))
        self.inventory_tree.heading("#0", text="ID")
        self.inventory_tree.heading("ID", text="ID")
        self.inventory_tree.heading("Product", text="Product")
        self.inventory_tree.heading("Quantity", text="Quantity")
        self.inventory_tree.pack(fill="both", expand=True)

        # Inventory Entry Fields with Labels
        tk.Label(self.inventory_tab, text="Product ID:").pack()
        self.inventory_product_id_entry = tk.Entry(self.inventory_tab)
        self.inventory_product_id_entry.pack()
        tk.Label(self.inventory_tab, text="Quantity:").pack()
        self.inventory_quantity_entry = tk.Entry(self.inventory_tab)
        self.inventory_quantity_entry.pack()

        # Add Inventory Button
        self.add_inventory_button = tk.Button(self.inventory_tab, text="Add Inventory", command=self.add_inventory)
        self.add_inventory_button.pack()

        # Delete Inventory Button
        self.delete_inventory_button = tk.Button(self.inventory_tab, text="Delete Selected", command=self.delete_inventory)
        self.delete_inventory_button.pack()

    def create_tables(self):
        # Create Customer Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customers
                            (id INTEGER PRIMARY KEY,
                             name TEXT,
                             email TEXT,
                             phone TEXT)''')

        # Create Order Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                            (id INTEGER PRIMARY KEY,
                             customer_id INTEGER,
                             product_id INTEGER,
                             quantity INTEGER,
                             total REAL,
                             FOREIGN KEY (customer_id) REFERENCES customers(id),
                             FOREIGN KEY (product_id) REFERENCES products(id))''')

        # Create Supplier Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers
                            (id INTEGER PRIMARY KEY,
                             name TEXT,
                             email TEXT,
                             phone TEXT)''')

        # Create Product Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products
                            (id INTEGER PRIMARY KEY,
                             name TEXT,
                             price REAL,
                             category TEXT,
                             supplier_id INTEGER,
                             FOREIGN KEY (supplier_id) REFERENCES suppliers(id))''')

        # Create Inventory Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                            (id INTEGER PRIMARY KEY,
                             product_id INTEGER,
                             quantity INTEGER,
                             FOREIGN KEY (product_id) REFERENCES products(id))''')

        self.conn.commit()

    def add_customer(self):
        name = self.customer_name_entry.get()
        email = self.customer_email_entry.get()
        phone = self.customer_phone_entry.get()
        
        if name and email and phone:
            self.cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            self.conn.commit()
            self.customer_name_entry.delete(0, tk.END)
            self.customer_email_entry.delete(0, tk.END)
            self.customer_phone_entry.delete(0, tk.END)
            self.load_customers()  

    def load_customers(self):
        # Clear existing data in the treeview
        for row in self.customer_tree.get_children():
            self.customer_tree.delete(row)
        
        # Fetch and display updated customer data from the database
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()
        for customer in customers:
            self.customer_tree.insert("", tk.END, values=customer)

    def delete_customer(self):
        selected_item = self.customer_tree.selection()
        if selected_item:
            item_id = self.customer_tree.item(selected_item)['values'][0]
            self.cursor.execute("DELETE FROM customers WHERE id=?", (item_id,))
            self.conn.commit()
            self.load_customers()

    def add_order(self):
        customer_id = self.order_customer_id_entry.get()
        product_id = self.order_product_id_entry.get()
        quantity = self.order_quantity_entry.get()
        
        if customer_id and product_id and quantity:
            self.cursor.execute("INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)", (customer_id, product_id, quantity))
            self.conn.commit()
            self.order_customer_id_entry.delete(0, tk.END)
            self.order_product_id_entry.delete(0, tk.END)
            self.order_quantity_entry.delete(0, tk.END)
            self.load_orders()  

    def load_orders(self):
        # Clear existing data in the treeview
        for row in self.order_tree.get_children():
            self.order_tree.delete(row)
        
        # Fetch and display updated order data from the database
        self.cursor.execute("SELECT * FROM orders")
        orders = self.cursor.fetchall()
        for order in orders:
            self.order_tree.insert("", tk.END, values=order)

    def delete_order(self):
        selected_item = self.order_tree.selection()
        if selected_item:
            item_id = self.order_tree.item(selected_item)['values'][0]
            self.cursor.execute("DELETE FROM orders WHERE id=?", (item_id,))
            self.conn.commit()
            self.load_orders()

    def add_supplier(self):
        name = self.supplier_name_entry.get()
        email = self.supplier_email_entry.get()
        phone = self.supplier_phone_entry.get()
        
        if name and email and phone:
            self.cursor.execute("INSERT INTO suppliers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            self.conn.commit()
            self.supplier_name_entry.delete(0, tk.END)
            self.supplier_email_entry.delete(0, tk.END)
            self.supplier_phone_entry.delete(0, tk.END)
            self.load_suppliers()

    def load_suppliers(self):
        # Clear existing data in the treeview
        for row in self.supplier_tree.get_children():
            self.supplier_tree.delete(row)
        
        # Fetch and display updated supplier data from the database
        self.cursor.execute("SELECT * FROM suppliers")
        suppliers = self.cursor.fetchall()
        for supplier in suppliers:
            self.supplier_tree.insert("", tk.END, values=supplier)

    def delete_supplier(self):
        selected_item = self.supplier_tree.selection()
        if selected_item:
            item_id = self.supplier_tree.item(selected_item)['values'][0]
            self.cursor.execute("DELETE FROM suppliers WHERE id=?", (item_id,))
            self.conn.commit()
            self.load_suppliers()

    def add_product(self):
        name = self.product_name_entry.get()
        price = self.product_price_entry.get()
        category = self.product_category_entry.get()
        
        if name and price and category:
            self.cursor.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)", (name, price, category))
            self.conn.commit()
            self.product_name_entry.delete(0, tk.END)
            self.product_price_entry.delete(0, tk.END)
            self.product_category_entry.delete(0, tk.END)
            self.load_products()

    def load_products(self):
        # Clear existing data in the treeview
        for row in self.product_tree.get_children():
            self.product_tree.delete(row)
        
        # Fetch and display updated product data from the database
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        for product in products:
            self.product_tree.insert("", tk.END, values=product)

    def delete_product(self):
        selected_item = self.product_tree.selection()
        if selected_item:
            item_id = self.product_tree.item(selected_item)['values'][0]
            self.cursor.execute("DELETE FROM products WHERE id=?", (item_id,))
            self.conn.commit()
            self.load_products()

    def add_inventory(self):
        product_id = self.inventory_product_id_entry.get()
        quantity = self.inventory_quantity_entry.get()
        
        if product_id and quantity:
            self.cursor.execute("INSERT INTO inventory (product_id, quantity) VALUES (?, ?)", (product_id, quantity))
            self.conn.commit()
            self.inventory_product_id_entry.delete(0, tk.END)
            self.inventory_quantity_entry.delete(0, tk.END)
            self.load_inventory()

    def load_inventory(self):
        # Clear existing data in the treeview
        for row in self.inventory_tree.get_children():
            self.inventory_tree.delete(row)
        
        # Fetch and display updated inventory data from the database
        self.cursor.execute("SELECT * FROM inventory")
        inventory = self.cursor.fetchall()
        for item in inventory:
            self.inventory_tree.insert("", tk.END, values=item)

    def delete_inventory(self):
        selected_item = self.inventory_tree.selection()
        if selected_item:
            item_id = self.inventory_tree.item(selected_item)['values'][0]
            self.cursor.execute("DELETE FROM inventory WHERE id=?", (item_id,))
            self.conn.commit()
            self.load_inventory()

def main():
    root = tk.Tk()
    app = FrontendApp(root)
    app.load_customers() 
    app.load_orders()
    app.load_suppliers()
    app.load_products()
    app.load_inventory()
    root.mainloop()

if __name__ == "__main__":
    main()
