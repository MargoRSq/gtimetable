from datetime import datetime
from typing import List
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
from gcsa.recurrence import Recurrence
from gcsa.recurrence import WEEKLY

from timetable import UniversityClass

def post_to_gcalendar(gc, events: List[UniversityClass], until_time: datetime):
    for et in events:
        if et.class_name:
            event = Event(
                et.class_name,
                start=et.start,
                end=et.end,
                recurrence=[
                Recurrence.rule(freq=WEEKLY, interval=2, until=until_time)],
                minutes_before_popup_reminder=15,
            )
            gc.add_event(event)

def delete_events(gc: GoogleCalendar):
    for event in gc:
        gc.delete_event(event)
