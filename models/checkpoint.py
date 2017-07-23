import csv

from datetime import datetime

from models.events import Event


class Checkpoint(Event):
    """
    Class representing checkpoint events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    def __init__(self, date, user_id):
        """
        Construct Checkpoint object

        Args:
            date (:obj: `date`): date of checkpoint
        """

        super().__init__(date)
        self.user_id = user_id

        Event.add_event(self)

    def __str__(self):
        """
        Return information about checkpoint date as formatted string
        """

        return '{} Checkpoint'.format(self.date)

    @classmethod
    def save_events(cls, file_name="csv/checkpoint.csv"):
        """
        Save Checkpoint objects from events list to file of given name

        Args:
            file_name (string): name of csv file
        """

        list_to_save = []

        with open(file_name, "w", newline="") as csvfile:
            file_writier = csv.writer(csvfile, delimiter="|")

            for event in cls.events:
                if event.__class__.__name__ == cls.__name__:
                    list_to_save.append(event.__class__.__name__)
                    list_to_save.append(str(event.date))
                    list_to_save.append(event.user_id)

                    file_writier.writerow(list_to_save)

    @classmethod
    def read_events(cls, file_name="csv/checkpoint.csv"):
        """
        Read Checkpoint objects from csv of given name and add them to list of events

        Args:
            file_name (string): name of csv file
        """

        with open(file_name, "r", newline="") as csvfile:
            file_reader = csv.reader(csvfile, delimiter="|")

            for row in file_reader:
                if row[0] == cls.__name__:
                    date = datetime.strptime(row[1], "%Y-%m-%d").date()
                    user_id = row[2]

                    cls(date, user_id)
