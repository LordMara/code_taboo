import csv

from models.user import User


class Student(User):
    def __init__(self, name, surname, user_id, password):
        super().__init__(name, surname, user_id, password)

        User.add_user(self)

    @classmethod
    def read_users(cls, file_name="csv/users.csv"):
        """
        Read Student objects from csv of given name and add them to list of users

        Args:
            file_name (string): name of csv file
        """

        with open(file_name, "r", newline="") as csvfile:
            file_reader = csv.reader(csvfile, delimiter="|")

            for row in file_reader:
                name = row[1]
                surname = row[2]
                user_id = row[3]
                password = row[4]

                if row[0] == cls.__name__:
                    cls(name, surname, user_id, password)
