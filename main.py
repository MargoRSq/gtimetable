from sys import argv
from datetime import datetime

from src.xlsx_parser import get_new_timetable_from_file
from src.primarycalendar import PrimaryCalendar


def main():
    calendar = PrimaryCalendar(cred_path="credentials")

    # calendar.delete_events() # read docs!
    event_list = get_new_timetable_from_file(argv[2])
    calendar.post_to_gcalendar(
            events=event_list,
            until_time=datetime.strptime(argv[1], "%d/%m/%Y")
    )

if __name__ == '__main__':
    main()
