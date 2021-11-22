from gcsa.google_calendar import GoogleCalendar
from datetime import datetime

from xlsx_parser import get_new_timetable_from_file
from gcalendar import post_to_gcalendar, delete_events
from config import CREDENTIALS_PATH, TIMETABLE_PATH


def main():
    gc = GoogleCalendar(credentials_path=CREDENTIALS_PATH)
    event_list = get_new_timetable_from_file(TIMETABLE_PATH)
    # uncomment this line if you want to rewrite your classes
    # !!! BUT IT WILL DELETE ALL OF YOUR EVENTS THAT YOU CREATED BY YOURSELF !!!
    # delete_events(gc)
    post_to_gcalendar(gc, event_list, until_time=datetime(2021, 12, 31))



if __name__ == '__main__':
    main()
