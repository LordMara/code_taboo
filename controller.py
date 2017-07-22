from datetime import date
import view
import events


def start():
    choice = None

    while choice != "0":
        view.print_main_menu()
        choice = view.get_choice()
        if choice == "1":
            book_private_mentoring()
        elif choice == "2":
            book_checkpoint()
        elif choice == "3":
            print_all_evets()
        elif choice == "0":
            say_goodbye()
        else:
            view.print_msg("Wrong option!")


def print_all_evets():
    view.print_all_events(events.Event.get_events())


def book_events():
    pass


def book_checkpoint():
    date = view.get_event_date()

    try:
        date = convert_date(date)
    except (ValueError, IndexError):
        view.print_msg("Wrong data format!")
    else:
        events.Checkpoint(date)


def book_private_mentoring():
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
    view.print_goodbye()


def convert_date(date_str):
    date_list = date_str.split('-')
    return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
