from datetime import datetime
from ics import Calendar

from src.timetable import UniversityClass
from src.type_hints import ArgsDict


def create_calendar(args: ArgsDict, events: list[UniversityClass]):
    c = Calendar()
    for ev in events:
        if ev.class_name != 'None':
            print(ev.class_name, type(ev.class_name))
            monday_datetime = datetime.strptime(args["start"], "%d/%m/%Y")
            until_datetime = datetime.strptime(args["until"], "%d/%m/%Y")
            e = ev.create_ics_event(monday=monday_datetime,
                                    until_date=until_datetime)
            c.events.add(e)

    with open("my.ics", "w") as f:
        f.write(c.serialize())
