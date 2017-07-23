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
    options_list = ["Book checkpoint",
                    "Show all my events",
                    "Cancel event",
                    "Reschedule event"
                    ]
    exit_msg = "Exit program"

    while choice != "0":
        view.print_menu(head, options_list, exit_msg)
        choice = view.get_choice()
        if choice == "1":
            book_checkpoint(user.user_id)
        elif choice == "2":
            display_all_students_evets(user.user_id)
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


def display_all_students_evets(user_id):
    """
    Call function to print all students and user Events object
    and all Checkpoint objects

    Examples:
        "st" are two first signs of student id
    """

    user_events = []

    events = Event.get_events()
    for event in events:
        if event.user_id == user_id or event.user_id[0:2] == "st" or event.__class__.__name__ == "Checkpoint":
            user_events.append(event)

    view.print_all_events(user_events)


def book_checkpoint(user_id):
    """
    Call functions that allow user create Checkpoint object
    """

    date = view.get_event_date()

    date = validate_date(date)

    if date is not None:
        Checkpoint(date, user_id)
    else:
        view.print_msg("Checkpoint not scheduled!")


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

    Examples:
        "st" are two first signs of student id
    """

    date = view.get_event_date()

    date = validate_date(date, False)

    if date is not None:
        for event in Event.events:
            if event.date == date and event.user_id == user_id or event.user_id[0:2] == "st":
                event_name = view.get_event_name().lower()

                if event_name == "checkpoint":
                    Checkpoint.del_event(event)

                elif event_name == "private mentoring":
                    PrivateMentoring.del_event(event)

                else:
                    view.print_msg("No such event!")


def reschedule_event(user_id):
    """
    Call functions to change event date

    Examples:
        "st" are two first signs of student id
    """

    view.print_msg("Enter old event date")
    date = view.get_event_date()

    view.print_msg("Enter new event date")
    new_date = view.get_event_date()

    date = validate_date(date, False)
    new_date = validate_date(new_date)

    if date is not None and new_date is not None:
        for event in Event.events:
            if event.date == date and event.user_id == user_id or event.user_id[0:2] == "st":
                event_name = view.get_event_name().lower()
                if event_name == "checkpoint":
                    Checkpoint.change_date(event, new_date)

                elif event_name == "private mentoring":
                    PrivateMentoring.change_date(event, new_date)

                else:
                    view.print_msg("No such event!")


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
