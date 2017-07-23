import csv

from datetime import datetime

from models.events import Event


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

    @classmethod
    def save_events(cls, file_name="csv/private_mentoring.csv"):
        """
        Save PrivateMentoring objects from events list to file of given name

        Args:
            file_name (string): name of csv file
        """

        with open(file_name, "w", newline="") as csvfile:
            file_writier = csv.writer(csvfile, delimiter="|")

            for event in cls.events:
                list_to_save = []

                if event.__class__.__name__ == cls.__name__:
                    list_to_save.append(event.__class__.__name__)
                    list_to_save.append(str(event.date))
                    list_to_save.append(event.goal)
                    list_to_save.append(event.preffered_mentor)

                    file_writier.writerow(list_to_save)

    @classmethod
    def read_events(cls, file_name="csv/private_mentoring.csv"):
        """
        Read PrivateMentoring objects from csv of given name and add them to list of events

        Args:
            file_name (string): name of csv file
        """

        with open(file_name, "r", newline="") as csvfile:
            file_reader = csv.reader(csvfile, delimiter="|")

            for row in file_reader:
                if row[0] == cls.__name__:
                    date = datetime.strptime(row[1], "%Y-%m-%d").date()
                    goal = row[2]
                    preffered_mentor = row[3]

                    cls(date, goal, preffered_mentor)
