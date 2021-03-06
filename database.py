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


    def get_cost_detail(self, id):
        """Берем стоимость детали из таблицы details"""
        with self.conn:
            cost = self.cursor.execute("SELECT cost from details WHERE id = ?",(id,)).fetchall()
            for row in cost:
                cost = str(row[0])
            return cost

    def new_cost(self, cost, id):
        """Редактирования стоимости детали"""
        with self.conn:
            return self.cursor.execute("UPDATE details SET cost = ? WHERE id =?",(cost, id,))


    def delete_user(self, id):
        """Удаления пользователя из таблицы users"""
        with self.conn:
            return self.cursor.execute("DELETE FROM users WHERE id =?",(id,))

    def all_users(self):
        """Вывод всех сотрудников завода"""
        with self.conn:
            self.cursor.execute("SELECT id, name  FROM users")
            users = self.cursor.fetchall()
            line = '\n\n'.join([' ➖ '.join(map(str, x)) for x in users])
            return str(line)

    def all_prod(self):
        """Вывод всех работ на заводе"""
        with self.conn:
            self.cursor.execute("SELECT date, user_name, amount, type_detail, summ  FROM productions")
            users = self.cursor.fetchall()
            text = '\n\n'.join([' ┃ '.join(map(str, x)) for x in users])
            return str(text)

    def personal_prod(self, user_id):
        """Вывод личной истории работ сотрудника"""
        with self.conn:
            self.cursor.execute("SELECT id_p, date, user_name, amount, type_detail, summ  FROM productions WHERE user_id = ?", (user_id,))
            users = self.cursor.fetchall()
            text = '\n\n'.join([' ┃ '.join(map(str, x)) for x in users])
            return str(text)


    def add_work(self, user_id, user_name, type_detail, amount, summ,):
        """Запись в таблицу производства"""
        with self.conn:
            self.cursor.execute("INSERT INTO productions(user_id, user_name, type_detail, amount, summ) VALUES(?,?,?,?,?)", (user_id, user_name, type_detail, amount, summ,))

    def delete_work(self, id_p):
        """Удаления записи из таблицы 'productions'"""
        with self.conn:
            return self.cursor.execute("DELETE FROM productions WHERE id_p =?", (id_p,))


    def get_amount_work(self, user_id):
        """Функция для определения общего количества сделанных мешков сотрудником"""
        with self.conn:
            workamount = self.cursor.execute("SELECT SUM(amount) FROM productions WHERE user_id = ?", (user_id,))
            for row in workamount:
                workamount = str(row[0])
            return workamount

    def get_money_work(self, user_id):
        """Функция для подсчета денег от работ сотрудника"""
        with self.conn:
            money = self.cursor.execute("SELECT SUM(summ) FROM productions WHERE user_id = ?", (user_id,))
            for row in money:
                money = str(row[0])
            return money

    def clear_history(self, user_id):
        """Удалиение всей истории работ сотрудника"""
        with self.conn:
            return self.cursor.execute("DELETE FROM productions WHERE user_id = ?", (user_id,))


    def close(self):
        """Закрытия соединения с БД"""
        self.conn.close()