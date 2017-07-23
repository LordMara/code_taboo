import csv

from abc import ABCMeta


class User(metaclass=ABCMeta):
    """
    Abstract class representing users

    Attributes:
        users_list (list of :obj: `User`): list of all User objects
    """

    users_list = []

    def __init__(self, name, surname, user_id, password):

        '''
        Construct User object

        Args:
            name (string): user name
            surname (string): user surname
            user_id (string): user id
            password (string): user password
        '''
        self.name = name
        self.surname = surname
        self.user_id = user_id
        self.password = password

    @classmethod
    def add_user(cls, user):
        """
        Add user to users list

        Args:
            user (:obj: `User`): some event
        """

        cls.users_list.append(user)

    @staticmethod
    def save_users(file_name="csv/users.csv"):
        """
        Save User objects from user list to file of given name

        Args:
            file_name (string): name of csv file
        """

        with open(file_name, "w", newline="") as csvfile:
            file_writier = csv.writer(csvfile, delimiter="|")

            for user in User.users_list:
                list_to_save = []

                list_to_save.append(user.__class__.__name__)
                list_to_save.append(user.name)
                list_to_save.append(user.surname)
                list_to_save.append(user.user_id)
                list_to_save.append(user.password)

                file_writier.writerow(list_to_save)

    @staticmethod
    def read_users(file_name="csv/users.csv"):
        """
        Read User objects from csv of given name and add them to list of users

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

                if row[0] == "Student":
                    Student(name, surname, user_id, password)

                if row[0] == "Mentor":
                    Mentor(name, surname, user_id, password)
