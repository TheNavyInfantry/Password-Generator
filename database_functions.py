import sqlite3

def create_table():
    connection = sqlite3.connect("password_generator.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (
                        password TEXT,
                        password_difficulty TEXT,
                        saving_date timestamp)""")

    connection.commit()

def insert_table(password, password_difficulty, saving_date):
    connection = sqlite3.connect("password_generator.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO passwords VALUES(?,?,?)", (password, password_difficulty, saving_date))

    connection.commit()


def show_table():
    connection = sqlite3.connect("password_generator.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, rowid FROM passwords")
    get_data = cursor.fetchall()

    for line in get_data:
        pw = line[0]
        feature = line[1]
        date = line[2]
        row_id = line[3]
        print("PASSWORD: {} | DIFFICULTY: {} | ADDED ON {} | ID: {}".format(pw, feature, date, row_id))

    connection.commit()
    connection.close()

def delete_data(row_id):
    connection = sqlite3.connect("password_generator.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM passwords WHERE oid = (?)", row_id)

    connection.commit()
    connection.close()
