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
        Insertion sort alghoritm of sorting all events by date on events list
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
    def del_event(cls, date):
        """
        Remove Event object form events list
        """

        for event in cls.events:
            if event.date == date and event.__class__.__name__ == cls.__name__:
                Event.events.remove(event)

    @classmethod
    def change_date(cls, date, new_date):
        """
        Change event date
        """

        for event in cls.events:
            if event.date == date and event.__class__.__name__ == cls.__name__:
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
