def print_all_events(events):
    for event in events:
        print(event)

def print_main_menu():
    menu = """
    Chose option:
    1. Book private mentoring
    2. Book checkpoint
    3. Show all my events
    """
    print(menu)

def print_goodbye():
    print("Bye bye")

def get_choice():
    return input("Chose option: ")

def get_chechpoint_details():
    return self.get_event_date()

def get_event_date():
    return input("Enter date in format dd-mm-yyyy: ")

def preferred_mentor(self):
    return input("Enter preferred mentor: ")

def get_goal(self):
    return input("Enter your goal: ")