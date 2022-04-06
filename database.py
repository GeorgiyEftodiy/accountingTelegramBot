# Работа с базами данных

# Импортирования нужных модулей
import sqlite3

# Класс в котором реализуется работа с базами данных
class botDB:
    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_users(self,user_id):
        """Добовляем нового пользователя"""
        self.cursor.execute("INSERT INTO 'users' ('код_с','фамилия') VALUES(?,?)",(user_id))
        return self.conn.commit()

    def close(self):
        """Закрытия соединения с БД"""
        self.conn.close()