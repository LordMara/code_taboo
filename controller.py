from datetime import date
import view
import events


def start():
    while True:
        view.print_main_menu()
        choice = view.get_choice()
        if choice == "1":
            book_private_mentoring()
        elif choice == "2":
            book_checkpoint()
        elif choice == "3":
            print_all_evets()
        else:
            say_goodbye()


def print_all_evets():
    view.print_all_events(events.Event.get_events())


def book_events():
    pass


def book_checkpoint():
    date = view.get_event_date()
    date = convert_date(date)
    events.Checkpoint(date)


def book_private_mentoring():
    date = view.get_event_date()
    date = convert_date(date)
    events.PrivateMentoring(date)


def say_goodbye():
    view.print_goodbye()


def convert_date(date_str):
    date_list = date_str.split('-')
    return(date(int(date_list[2]), int(date_list[1]), int(date_list[0])))
