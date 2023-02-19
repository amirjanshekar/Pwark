class ProductsController:

    @staticmethod
    def fetch_all_products(connection):
        connection.cur.execute("SELECT products.name FROM products")
        rows = connection.cur.fetchall()
        return rows

    @staticmethod
    def add_product(connection, name):
        connection.cur.execute("INSERT INTO products VALUES (NULL, ?)", [name])
        connection.conn.commit()

    @staticmethod
    def fetch_product_by_id(connection, product_id):
        connection.cur.execute("SELECT name FROM products WHERE id=?", (product_id,))

    @staticmethod
    def fetch_product_by_name(connection, product_name):
        connection.cur.execute("SELECT id FROM products WHERE name=?", (product_name,))
        rows = connection.cur.fetchone()
        return rows

    @staticmethod
    def remove_product(connection, product_id):
        connection.cur.execute("DELETE FROM products WHERE id=?", (product_id,))
        connection.conn.commit()

    @staticmethod
    def update_product(connection, product_id, name):
        connection.cur.execute("UPDATE products SET name = ? WHERE id = ?", (name, product_id))
        connection.conn.commit()
