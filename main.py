import datetime
import time
import database_functions
import password_functions

class password_generator:

    def __init__(self, choice):
        self.choice = choice

    def generate_password(self, length):

        database_functions.create_table()

        if self.choice == 'EASY':
            generated = password_functions.easy_password(length)
            database_functions.insert_table(generated, self.choice, datetime.datetime.now())

            print("Generated Easy Password: {}".format(generated), "\nSaving to Database...")
            time.sleep(2)
            print("Saved to Database!")

        elif self.choice == 'MEDIUM':
            generated = password_functions.medium_password(length)
            database_functions.insert_table(generated, self.choice, datetime.datetime.now())

            print("Generated Medium Password: {}".format(generated), "\nSaving to Database...")
            time.sleep(1.5)
            print("Saved to Database!")

        elif self.choice == 'HARD':
            generated = password_functions.hard_password(length)
            database_functions.insert_table(generated, self.choice, datetime.datetime.now())

            print("Generated Hard Password: {}".format(generated), "\nSaving to Database...")
            time.sleep(2)
            print("Saved to Database!")

        else:
            print("Wrong Input Type! TRY AGAIN!")

    def get_all_data(self):

        if self.choice == "SHOW":
            return database_functions.show_table()

        else:
            print("Wrong Input Type! TRY AGAIN!")

    def delete_one(self, row_id):

        if self.choice == "DELETE":
            database_functions.delete_data(row_id)

        else:
            print("Wrong Input Type! TRY AGAIN!")

passw = password_generator("hard".upper())
passw.generate_password(15)

show_data = password_generator("show".upper())
show_data.get_all_data()

delete = password_generator("delete".upper())
delete.delete_one('1')
