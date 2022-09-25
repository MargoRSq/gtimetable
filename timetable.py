from sys import argv
from datetime import datetime, timedelta, date

class UniversityClass:

    def __init__(self, class_name: str, time: str, wday: int, wtype: int):
        self.class_name = class_name
        self.time = time
        self.wday = wday
        self.wtype = wtype
        self.set_start_end_dt(time)

    def set_start_end_dt(self, time_str: str):
        first_day = datetime.strptime(argv[1], "%d/%m/%Y")
        today = datetime.today()
        week_num = int(datetime.today().strftime("%W")) - int(first_day.strftime("%W"))
        week_mn = 1 if week_num % 2 == self.wtype else 0
        closest_entry = today + timedelta(
                                days=((self.wday + 7 * week_mn) - today.weekday()))
        time_tuple = tuple(time_str.split('-'))
        start_time = datetime.strptime(time_tuple[0], "%H:%M")
        end_time = datetime.strptime(time_tuple[1], "%H:%M")
        self.start = datetime(closest_entry.year, closest_entry.month, closest_entry.day,
                                    start_time.hour, start_time.minute)
        self.end = datetime(closest_entry.year, closest_entry.month, closest_entry.day,
                                    end_time.hour, end_time.minute)

    def __repr__(self) -> str:
        return f'{self.class_name} - {self.wday} - {self.wtype}'
