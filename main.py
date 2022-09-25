import os

from sys import argv

from google.auth.exceptions import RefreshError
from gcsa.google_calendar import GoogleCalendar
from datetime import datetime

from xlsx_parser import get_new_timetable_from_file
from gcalendar import post_to_gcalendar, delete_events
from config import CREDENTIALS_PATH, TIMETABLE_PATH, TOKEN_FILE


def main():
    try:
        gc = GoogleCalendar(credentials_path=CREDENTIALS_PATH)
    except RefreshError:
        os.remove(TOKEN_FILE)
    event_list = get_new_timetable_from_file(argv[3])
    # uncomment this line if you want to rewrite your classes
    # !!! BUT IT WILL DELETE ALL OF YOUR EVENTS THAT YOU CREATED BY YOURSELF !!!
    # delete_events(gc)
    post_to_gcalendar(gc, event_list, until_time=datetime.strptime(argv[2], "%d/%m/%Y"))


if __name__ == '__main__':
    main()
