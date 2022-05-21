# Работа с базами данных

# Импортирования нужных модулей
import sqlite3

# Класс в котором реализуется вся работа с базами данных
class botDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()


    def add_user(self, user_id):
        """Добавление нового пользователя в БД"""
        with self.conn:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES(?)", (user_id,))

    def user_exist(self, user_id):
        """Проверка есть ли пользователя в БД"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_userid(self, user_id):
        """Получаем id пользователя по его id-телеграма"""
        with self.conn:
            result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
            return result.fetchone()[0]



    def set_name(self, user_id, name):
        """Добавления имени пользователя"""
        with self.conn:
            return self.cursor.execute("UPDATE users SET name = ? WHERE user_id =?",(name, user_id,))

    def get_name(self, user_id):
        """Получение этапа регистрации пользователя"""
        with self.conn:
            result = self.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def get_signup(self, user_id):
        """Получение этапа регистрации пользователя"""
        with self.conn:
            result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self,user_id, signup):
        """Изменения этапа регистрации пользователя"""
        with self.conn:
            return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id =?",(signup, user_id,))

    def get_cost_detail(self, id):
        with self.conn:
            cost = self.cursor.execute("SELECT cost from details WHERE id = ?",(id,)).fetchall()
            for row in cost:
                cost = str(row[0])
            return cost



    def all_users(self):
        """Вывод всех сотрудников завода"""
        with self.conn:
            self.cursor.execute("SELECT name  FROM users")
            users = self.cursor.fetchall()
            text = '\n\n'.join([' - '.join(map(str, x)) for x in users])
            return str(text)

    def all_prod(self):
        """Вывод всех сотрудников завода"""
        with self.conn:
            self.cursor.execute("SELECT *  FROM productions")
            users = self.cursor.fetchall()
            text = '\n\n'.join([' - '.join(map(str, x)) for x in users])
            return str(text)

    def add_work(self, user_id, type_detail, amount, summ,):
        """Запись в таблицу производства"""
        with self.conn:
            self.cursor.execute("INSERT INTO productions(user_id, type_detail, amount, summ) VALUES(?,?,?,?)", (user_id, type_detail, amount, summ,))

    def close(self):
        """Закрытия соединения с БД"""
        self.conn.close()