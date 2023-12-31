import sqlite3

class Staff:
    def __init__(self):
        self.connection = sqlite3.connect(database='database.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS staff (
                            id INTEGER PRIMARY KEY,
                            full_name TEXT,
                            email TEXT,
                            phone_number TEXT,
                            salary INTEGER
        )""")

    def insert(self, full_name, email, phone_number, salary):
        insert_query = "INSERT INTO staff (full_name, email, phone_number, salary) VALUES (?, ?, ?, ?)"
        self.cursor.execute(insert_query, (full_name, email, phone_number, salary))

        self.connection.commit()

    def delete(self, id):
        delete_query = "DELETE FROM staff WHERE id = (?)"
        self.cursor.execute(delete_query, (id,))

        self.connection.commit()

    def update(self, id, full_name='', email='', phone_number='', salary=''):
        update_query = "UPDATE staff SET "
        update_query += "full_name = ?, " if full_name != '' else ''
        update_query += "email = ?, " if email != '' else ''
        update_query += "phone_number = ?, " if phone_number != '' else ''
        update_query += "salary = ?, " if salary != '' else ''
        update_query += "WHERE id = ?"
        update_query = update_query.replace(', WHERE', ' WHERE')

        update_data = [full_name, email, phone_number, salary]
        if full_name == '':
            update_data.remove(full_name)
        if email == '':
            update_data.remove(email)
        if phone_number == '':
            update_data.remove(phone_number)
        if salary == '':
            update_data.remove(salary)

        update_data.append(int(id))

        self.cursor.execute(update_query, tuple(update_data))
        self.connection.commit()

    def search(self, full_name='', id=None):
        search_query = "SELECT * FROM staff WHERE"
        search_data = []

        if full_name != '':
            search_query += ' full_name=?'
            search_data.append(full_name)

        if id != '' and full_name != '':
            search_query += ', AND id=?'
            search_data.append(id)
        elif id!='':
            search_query += ' id=?'
            search_data.append(id)

        self.cursor.execute(search_query, tuple(search_data))
        self.connection.commit()

        staff_data = self.cursor.fetchall()

        return staff_data[0]
    
    def order(self):
        order_query = "SELECT * FROM staff ORDER BY id"
        self.cursor.execute(order_query)
        self.connection.commit()

        return self.cursor.fetchall()
