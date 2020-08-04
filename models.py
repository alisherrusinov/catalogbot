#File need to be runned once!
import sqlite3

class DBManager:
    def __init__(self):
        """Подключение к БД и создание полей"""

        self.connection = sqlite3.connect('db.db')
    
    def get_product(self, product):
        """Получить товар из базы данных"""
        with self.connection:
            cur = self.connection.cursor()
            return cur.execute(f"SELECT * FROM products WHERE name = '{product}';").fetchall()
    def get_from_category(self, category):
        """Получить все товары из категории"""
        with self.connection:
            rcur = self.connection.cursor()
            return cur.execute(f"SELECT name FROM products WHERE category = '{category}';").fetchall()
    def get_categories(self):
        """Получить все категории товаров"""
        with self.connection:
            cur = self.connection.cursor()
            return cur.execute("SELECT category FROM products;").fetchall()
