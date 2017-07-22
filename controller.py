from datetime import date
import view
import events

class Controller:

    def start(self):
        while True:
            view.print_main_menu()
            choice = view.get_choice()
            if choice == "1":
                self.book_private_mentoring()
            elif choice == "2":
                self.book_checkpoint()
            elif choice == "3":
                self.print_all_evets()
            else:
                self.say_goodbye()

    def print_all_evets(self):
        view.print_all_events(events.Event.get_events())


    def book_events(self):
        pass

    def book_checkpoint(self):
        date = view.get_event_date()
        date = self.__class__.convert_date(date)
        events.Checkpoint(date)
    
    def book_private_mentoring(self):
        date = view.get_event_date()
        date = self.__class__.convert_date(date)
        evetns.PrivateMentoring(date)

    def say_goodbye(self):
        view.print_goodbye()

    @staticmethod
    def convert_date(date_str):
        date_list = date_str.split('-')
        return(date(int(date_list[2]), int(date_list[1], int(date_list[0]))))
        
