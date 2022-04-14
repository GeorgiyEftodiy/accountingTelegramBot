# Работа с базами данных

# Импортирования нужных модулей
import sqlite3

# Класс в котором реализуется вся работа с базами данных
class botDB:
    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def account_exist(self,user_id, login, password):
        """Проверяем есть ли аккаунт в базе данных"""


    def all_users(self):
        """Вывод всех сотрудников завода"""
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        text = '\n\n'.join([', '.join(map(str, x)) for x in users])
        return str(text)


    def select_production(self):
        """Выборка производства"""



    def close(self):
        """Закрытия соединения с БД"""
        self.conn.close()