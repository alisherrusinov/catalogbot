#File need to be runned once!
import sqlite3

class DBManager:
    def __init__(self):
        """Подключение к БД и создание полей"""
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
    
    def get_product(self, product):
        """Получить товар из базы данных"""
        with self.connection:
            query = self.cursor.execute(f"SELECT * FROM products WHERE name = '{product}';").fetchall()
            return list(query[0])
    def get_from_category(self, category):
        """Получить все товары из категории"""
        with self.connection:
            query = self.cursor.execute(f"SELECT name FROM products WHERE category = '{category}';").fetchall()
            products = []
            for i in query:
                products.append(i[0])
            return products
    def get_categories(self):
        """Получить все категории товаров"""
        with self.connection:
            query = self.cursor.execute("SELECT category FROM products;").fetchall()
            categories = []
            for i in query:
                categories.append(i[0])
            return categories
    def get_products(self):
        """Получить имена всех товаров"""
        with self.connection:
            query = self.cursor.execute("SELECT name FROM products;").fetchall()
            products = []
            for i in query:
                products.append(i[0])
            return products
