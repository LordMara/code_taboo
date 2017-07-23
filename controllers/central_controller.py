from controllers import mentor_controller
from controllers import student_controller

from models.mentor import Mentor
from models.user import User
from models.student import Student

from views import view


def start_controller():
    """
    Contain main logic of controller,
    call functions to perform task choosen by user

    Raises:
        FileNotFoundError: if file to open is not present
    """

    try:
        Student.read_users()
    except FileNotFoundError as err:
        view.print_msg(err)
        pass

    try:
        Mentor.read_users()
    except FileNotFoundError as err:
        view.print_msg(err)
    else:

        user_id = view.get_user_id()
        user_password = view.get_user_password()

        try:
            user = login_user(user_id, user_password)
        except ValueError as err:
            view.print_msg(err)
        else:
            if user.__class__.__name__ == "Student":
                student_controller.start_controller(user)

            elif user.__class__.__name__ == "Mentor":
                mentor_controller.start_controller(user)


def login_user(user_id, user_password):
    """
    Validate if user id and password are correct

    Args:
        user_id (string): user id
        password (string): user password

    Returns:
        :obj: `User`: object representation of user

    Raises:
        Value Error: if uer id or password are wrong
    """

    for user in User.users_list:
        if user_id == user.user_id and user_password == user.password:
            return user
        else:
            raise ValueError("Wrong user id or password!")
