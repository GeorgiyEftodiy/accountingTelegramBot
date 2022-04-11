# Работа с базами данных

# Импортирования нужных модулей
import sqlite3

# Класс в котором реализуется работа с базами данных
class botDB:
    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def account_exist(self,user_id, login, password):
        """Проверяем есть ли аккаунт в базе данных"""


    def all_users(self, last_name, first_name, otchestvo, doljnost):
        """Вывод всех сотрудников завода"""
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM users WHERE row = ?, ?, ?, ? ", (last_name, first_name, otchestvo, doljnost))
        data = self.cursor.fetchone()



    def close(self):
        """Закрытия соединения с БД"""
        self.conn.close()