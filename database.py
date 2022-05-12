# Работа с базами данных

# Импортирования нужных модулей
import sqlite3

# Класс в котором реализуется вся работа с базами данных
class botDB:
    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()


    def add_user(self,user_id):
        """Добавление нового пользователя в БД"""
        with self.conn:
            return self.cursor.execute("INSERT INTO 'users' (user_id) VALUES(?)", (user_id,))

    def user_exist(self,user_id):
        """Проверка есть ли пользователя в БД"""
        with self.conn:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,))
            return bool(len(result.fetchall()))

    def add_info(self, last_name, first_name, user_id):
        """Добавления информации о сотруднике"""
        with self.conn:
            self.cursor.execute("UPDATE 'users' SET 'last_name' = ?, 'first_name' = ? WHERE 'user_id' = ?", (last_name, first_name, user_id,))
            self.conn.commit()


    def all_users(self):
        """Вывод всех сотрудников завода"""
        self.cursor.execute("SELECT user_id, last_name, first_name, doljnost  FROM users")
        users = self.cursor.fetchall()
        text = '\n\n'.join([' - '.join(map(str, x)) for x in users])
        return str(text)

    def close(self):
        """Закрытия соединения с БД"""
        self.conn.close()