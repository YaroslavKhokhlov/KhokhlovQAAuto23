import sqlite3

class Database():

    def __init__(self):
        self.connection = sqlite3.connect("c:/Users/Ярослав/khokhlovqaauto23" + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is:{record}")
    
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id (self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt} )"
        self.cursor.execute(query)
        self.connection.commit()
    
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def customer_postalcode (self, postalCode):
        query = "SELECT name FROM customers WHERE postalCode > 3000"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    
    
    def new_user_info (self,cust_name, cust_address, cust_city, cust_postalCode ):
        query = f"UPDATE customers SET address = '{cust_address}', city = '{cust_city}', postalCode = {cust_postalCode} \
            WHERE name = '{cust_name}'"
        self.cursor.execute(query)
        self.connection.commit()

    def select_inf_user_by_name (self, cust_name):
        query = f"SELECT address, city, postalCode FROM customers WHERE name = '{cust_name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    def insert_no_words_in_id(self, name):
        query = f"INSERT INTO products (id) VALUES ('{name}')"
        self.cursor.execute(query)
        self.connection.commit()
    
    

    
        
        

    def select_product_qnt_by_name(self, prod_name):
        query = f"SELECT quantity FROM products WHERE name = '{prod_name}' "
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
       
  
    
        
        

