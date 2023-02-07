import pytz

from ics import Event
from ics.grammar.parse import ContentLine
from datetime import datetime, timedelta


class UniversityClass:

    def __init__(self, class_name: str, desc: str, time_interval: str = None,
                 wday: int = None, wtype: int = 0):
        self.class_name = class_name
        self.desc = desc
        time_tuple = tuple(time_interval.split('-'))
        self.dt_data = {
            "weekday": wday,
            "start_time": datetime.strptime(time_tuple[0], "%H:%M").replace(tzinfo=pytz.timezone('Europe/Moscow')),
            "end_time": datetime.strptime(time_tuple[1], "%H:%M").replace(tzinfo=pytz.timezone('Europe/Moscow')),
            "time_interval": time_interval,
            "evenness": wtype,
        }

    def create_ics_event(self, monday: datetime, until_date: datetime) -> Event:
        target_day = monday + timedelta(days=self.dt_data["weekday"])
        if not self.dt_data["evenness"]:
            target_day = target_day + timedelta(days=7)
        e = Event(
            name=self.class_name,
            description=self.desc,
            begin=datetime(target_day.year, target_day.month, target_day.day,
                           self.dt_data["start_time"].hour,
                           self.dt_data["start_time"].minute,
                           tzinfo=pytz.timezone('Europe/Moscow')),
            end=datetime(target_day.year, target_day.month, target_day.day,
                         self.dt_data["end_time"].hour,
                         self.dt_data["end_time"].minute,
                         tzinfo=pytz.timezone('Europe/Moscow'))
        )
        until_date_str = until_date.strftime("%Y%M%D") + "T000001Z"
        e.extra.append(ContentLine(name="RRULE", value=until_date_str))
        return e

    def __repr__(self) -> str:
        return f'{self.class_name} - {self.wday} - {self.wtype}'
