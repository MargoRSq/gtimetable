import os

from datetime import datetime
from typing import List

from google.auth.exceptions import RefreshError
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
from gcsa.recurrence import Recurrence
from gcsa.recurrence import WEEKLY

from src.timetable import UniversityClass


class PrimaryCalendar(GoogleCalendar):

    def __init__(self, cred_path: str = "credentials"):
        self.cred_path = cred_path + "/credentials.json"
        self.gc = self.auth()

    def auth(self) -> GoogleCalendar:
        gc = None
        while (gc == None):
            try:
                gc = GoogleCalendar(credentials_path=self.cred_path)
            except RefreshError:
                os.remove(self.cred_path + "/token.pickle")
        return gc


    def post_to_gcalendar(self, events: List[UniversityClass], until_time: datetime):
        for et in events:
            if et.class_name:
                event = Event(
                    et.class_name,
                    start=et.start,
                    end=et.end,
                    recurrence=[
                        Recurrence.rule(freq=WEEKLY, interval=2, until=until_time)
                    ],
                )
                self.gc.add_event(event)


    def delete_events(self):
        """Be careful, it will delete all of your events in this calendar"""
        for event in self.gc:
            self.gc.delete_event(event)
