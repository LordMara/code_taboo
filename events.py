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


class Checkpoint(Event):
    """
    Class representing checkpoint events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    def __init__(self, date):
        """
        Construct Checkpoint object

        Args:
            date (:obj: `date`): date of checkpoint
        """

        super().__init__(date)

        Event.add_event(self)

    def __str__(self):
        """
        Return information about checkpoint date as formatted string
        """

        return '{} Checkpoint'.format(self.date)


class PrivateMentoring(Event):
    """
    Class representing private mentoring events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    def __init__(self, date, goal, preffered_mentor):
        """
        Construct PrivateMentoring object

        Args:
            date (:obj: `date`): date of checkpoint
            goal (string): gaol of private mentoring
            preffered_mentor (string): preffered mentor to private mentoring sesion
        """

        super().__init__(date)
        self.preffered_mentor = None
        self.goal = None

        self.set_goal(goal)
        self.set_preffered_mentor(preffered_mentor)

        Event.add_event(self)

    def set_goal(self, goal):
        """
        Set goal of private moentoring

        Args:
            goal (string): gaol of private mentoring
        """

        self.goal = goal

    def set_preffered_mentor(self, preffered_mentor):
        """
        Set goal of preffered mentor

        Args:
            preffered_mentor (string): preffered mentor to private mentoring sesion
        """

        self.preffered_mentor = preffered_mentor

    def __str__(self):
        """
        Return information about private mentoring as formatted string
        """

        return '{} Private mentoring with {} about {}'.format(self.date,
                                                              self.preffered_mentor,
                                                              self.goal
                                                              )
