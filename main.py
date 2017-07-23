from controllers import central_controller

from models.user import User


def main():
    """
    Contain main logic of program
    """

    central_controller.start_controller()

    User.save_users(file_name="csv/users.csv")

if __name__ == "__main__":
    main()
