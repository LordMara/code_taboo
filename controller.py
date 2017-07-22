from datetime import date
import view
import events


def start():
    """
    Contain main logic of controller, 
    call functions to perform task choosen by user
    """

    choice = None

    while choice != "0":
        view.print_main_menu()
        choice = view.get_choice()
        if choice == "1":
            book_private_mentoring()
        elif choice == "2":
            book_checkpoint()
        elif choice == "3":
            display_all_evets()
        elif choice == "0":
            say_goodbye()
        else:
            view.print_msg("Wrong option!")


def display_all_evets():
    """
    Call function to print all Events objects to user
    """

    view.print_all_events(events.Event.get_events())


def book_checkpoint():
    """
    Call functions that allow user create Checkpoint object
    """

    date = view.get_event_date()

    try:
        date = convert_date(date)
    except (ValueError, IndexError):
        view.print_msg("Wrong data format!")
    else:
        events.Checkpoint(date)


def book_private_mentoring():
    """
    Call functions that allow user create PrivateMentoring object
    """

    date = view.get_event_date()

    try:
        date = convert_date(date)
    except (ValueError, IndexError):
        view.print_msg("Wrong data format!")
    else:

        goal = view.get_goal()
        preffered_mentor = view.preferred_mentor()

        events.PrivateMentoring(date, goal, preffered_mentor)


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
