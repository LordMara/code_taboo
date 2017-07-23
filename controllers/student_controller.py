from datetime import date

from models.checkpoint import Checkpoint
from models.events import Event
from models.private_mentoring import PrivateMentoring

from views import view


def start_controller(user):
    """
    Contain main logic of controller,
    call functions to perform task choosen by user

    Raises:
        FileNotFoundError: if file to open is not present
    """

    try:
        Checkpoint.read_events()
    except FileNotFoundError as err:
        view.print_msg(err)
        pass

    try:
        PrivateMentoring.read_events()
    except FileNotFoundError as err:
        view.print_msg(err)
        pass

    choice = None

    head = "Chose option:"
    options_list = ["Book private mentoring",
                    "Show all my events",
                    "Cancel event",
                    "Reschedule event"
                    ]
    exit_msg = "Exit program"

    while choice != "0":
        view.print_menu(head, options_list, exit_msg)
        choice = view.get_choice()
        if choice == "1":
            book_private_mentoring(user.user_id)
        elif choice == "2":
            display_user_evets(user.user_id)
        elif choice == "3":
            cancel_event(user.user_id)
        elif choice == "4":
            reschedule_event(user.user_id)
        elif choice == "0":
            say_goodbye()
        else:
            view.print_msg("Wrong option!")

    Checkpoint.save_events()
    PrivateMentoring.save_events()


def display_user_evets(user_id):
    """
    Call function to print all user private mentoring
    and checkpoints Events objects to user

    Examples:
        "mt" are two first signs of mentor id
    """

    user_events = []

    events = Event.get_events()
    for event in events:
        if event.user_id == user_id or event.user_id[0:2] == "mt" and event.__class__.__name__ == "Checkpoint":
            user_events.append(event)

    view.print_all_events(user_events)


def book_private_mentoring(user_id):
    """
    Call functions that allow user create PrivateMentoring object
    """

    date = view.get_event_date()

    date = validate_date(date)
    preffered_mentor = choice_preffered_mentor()
    goal = view.get_goal()

    if date is not None and preffered_mentor is not None and goal:

        PrivateMentoring(date, goal, preffered_mentor, user_id)

    else:
        view.print_msg("Mentoring not scheduled!")


def say_goodbye():
    """
    Call function that print goodbye massage to user
    """

    view.print_goodbye()


def convert_date(date_str):
    """
    Convert data from string to date object

    Args:
        date_str: date of event choose by user

    Returns:
        :obj: `date`: date of event choose by user
    """

    date_list = date_str.split('-')
    return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))


def cancel_event(user_id):
    """
    Call functions to cancel event
    """

    date = view.get_event_date()

    date = validate_date(date, False)

    if date is not None:
        for event in Event.events:
            if event.date == date and event.__class__.__name__ == "PrivateMentoring" and event.user_id == user_id:
                PrivateMentoring.del_event(event)


def reschedule_event(user_id):
    """
    Call functions to change event date
    """

    view.print_msg("Enter old event date")
    date = view.get_event_date()

    view.print_msg("Enter new event date")
    new_date = view.get_event_date()

    date = validate_date(date, False)
    new_date = validate_date(new_date)

    if date is not None and new_date is not None:
        for event in Event.events:
            if event.date == date and event.__class__.__name__ == "PrivateMentoring" and event.user_id == user_id:
                PrivateMentoring.change_date(event, new_date)


def validate_date(date_str, future_date=True):
    """
    Validate if given date is correct
    and if parametr future_date set tu True check if date is in future

    Args:
        date_str: date of event choose by user

    Returns:
        :obj: `date`: date of event choose by user

    Raises:
        ValueError: if string given to convert have letters or
        scope of numbers are to low or high
        IndexError: if given string have to little delimiters as sing "-"
    """

    try:
        date = convert_date(date_str)
    except (ValueError, IndexError):
        view.print_msg("Wrong data format!")
    else:
        if future_date:
            if date <= date.today():
                view.print_msg("Date have to be in future!")
            else:
                return date
        else:
            return date


def choice_preffered_mentor():
    """
    Call functions to diplay manu and choose preferred mentor
    """

    AVAIALBLE_OPTIONS_LIST = ["0", "1", "2", "3", "4", "5"]

    choice = None
    preffered_mentor = None

    head = "Chose option:"
    options_list = ["Mateusz Ostafi",
                    "Agnieszka Koszany",
                    "Dominik Starzyk",
                    "Mateusz Steliga",
                    "Marcin Izworski"
                    ]
    exit_msg = "Exit booking provate mentoring"

    while choice not in AVAIALBLE_OPTIONS_LIST:
        view.print_menu(head, options_list, exit_msg)
        choice = view.get_choice()
        if choice == "1":
            preffered_mentor = "Mateusz Ostafi"
        elif choice == "2":
            preffered_mentor = "Agnieszka Koszany"
        elif choice == "3":
            preffered_mentor = "Dominik Starzyk"
        elif choice == "4":
            preffered_mentor = "Mateusz Steliga"
        elif choice == "5":
            preffered_mentor = "Marcin Izworski"
        elif choice == "0":
            view.print_msg("End of booking")
        else:
            view.print_msg("Wrong option!")

    return preffered_mentor
