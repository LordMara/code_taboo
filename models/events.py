from abc import ABCMeta, abstractclassmethod


class Event(metaclass=ABCMeta):
    """
    Abstract class representing events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    events = []

    def __init__(self, date):
        '''
        Construct Event object

        Args:
            date (:obj: `date`): date of event
        '''

        self.date = date

    def get_date(self):
        """
        Return date of event
        """

        return self.date

    @classmethod
    def sort_events(cls):
        """
        Bubble sort alghoritm of sorting all events by date on events list
        """

        is_sorted = False

        while not is_sorted and len(cls.events) > 1:
            is_sorted = True

            for i in range(len(cls.events) - 1):
                if cls.events[i].date > cls.events[i+1].date:
                    temp = cls.events[i]
                    cls.events[i] = cls.events[i+1]
                    cls.events[i+1] = temp

                    is_sorted = False

    @classmethod
    def add_event(cls, event):
        """
        Add event to events list and call function to sort that list

        Args:
            event (:obj: `Event`): some event
        """

        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        """
        Return list of events
        """

        return cls.events

    @classmethod
    def del_event(cls, event):
        """
        Remove Event object form events list
        """

        cls.events.remove(event)

    @staticmethod
    def change_date(event, new_date):
        """
        Change event date
        """

        event.date = new_date

    @abstractclassmethod
    def save_events(cls, file_name):
        """
        Save Events objects from events list to file of given name

        Args:
            file_name (string): name of csv file
        """

        pass

    @abstractclassmethod
    def read_events(cls, file_name):
        """
        Read Events objects from csv of given name and add them to list of events

        Args:
            file_name (string): name of csv file
        """

        pass
