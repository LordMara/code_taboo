class Event():

    events = []

    def __init__(self, date):
        '''date: Date object
        '''

        self.date = date

    def get_date(self):
        return self.date

    @classmethod
    def sort_events(cls):
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
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        return cls.events


class Checkpoint(Event):
    events = []

    def __init__(self, date):
        super().__init__(date)

        Event.add_event(self)
        Checkpoint.add_event(self)

    def get_chechpoint_details(self):
        return self.get_event_date()

    def __str__(self):
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
