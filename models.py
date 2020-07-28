#File need to be runned once!
import sqlite3

class Product:
    def __init__(self):
        """Подключение к БД и создание полей"""

        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()

        fields = self.get_product('Товар')
        self.name = fields[0][1]
        self.desc = fields[0][2]
        self.img = fields[0][3]
        self.category = fields[0][4]
        self.cost = fields[0][5]
        self.page = fields[0][6]
    
    def get_product(self,product):
        """Получить товар из базы данных"""
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM products WHERE name = '{product}';").fetchall()


a = Product()
print(a.category)