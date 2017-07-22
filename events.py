from abc import ABCMeta


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
        Add event to events list and call function to rot that list

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


class Checkpoint(Event):
    """
    Class representing checkpoint events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    events = []

    def __init__(self, date):
        """
        Construct Checkpoint event

        Args:
            date (:obj: `date`): date of checkpoint
        """

        super().__init__(date)

        Event.add_event(self)
        Checkpoint.add_event(self)

    def __str__(self):
        """
        Return information about checkpoint date as formatted string
        """

        return '{} Checkpoint'.format(self.date)


class PrivateMentoring(Event):

    events = []

    def __init__(self, date, goal, preffered_mentor):
        super().__init__(date)
        self.preffered_mentor = None
        self.goal = None

        self.set_goal(goal)
        self.set_preffered_mentor(preffered_mentor)

        Event.add_event(self)
        self.__class__.add_event(self)

    def set_goal(self, goal):
        self.goal = goal

    def set_preffered_mentor(self, preffered_mentor):
        self.preffered_mentor = preffered_mentor

    def __str__(self):
        return '{} Private mentoring with {} about {}'.format(self.date,
                                                              self.preffered_mentor,
                                                              self.goal
                                                              )
