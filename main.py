from argparse import ArgumentParser
from datetime import datetime

from src.xlsx_parser import get_new_timetable_from_file, UniversityClass
from src.primarycalendar import PrimaryCalendar
from src.type_hints import ArgsDict
from src.icscal import create_calendar


def parse_argv() -> ArgsDict:
    parser = ArgumentParser(
        prog="gtimetable",
        description="usage: python3 main.py -u 5/1/2023 -s 5/2/2023 -f timetable.xlsx",
        epilog="")
    parser.add_argument('-f', "--filename")
    parser.add_argument('-s', "--start")
    parser.add_argument('-u', "--until")
    parser.add_argument('--evenness')

    parser.add_argument('--clear', required=False,
                        help="Will delete all your events in chosen calendar")
    parser.add_argument('--credentials', required=False)
    parser.add_argument('--output', required=False)
    return vars(parser.parse_args())


def fill_google_calendar(args: ArgsDict, events: list[UniversityClass]):
    if args['credentials']:
        credentials_dir = args['credentials']
    else:
        credentials_dir = "credentials"
    calendar = PrimaryCalendar(cred_path=credentials_dir)

    if args['clear']:
        calendar.delete_events()
    calendar.post_to_gcalendar(
            events=events,
            start_time=datetime.strptime(args['start'], "%d/%m/%Y"),
            until_time=datetime.strptime(args['until'], "%d/%m/%Y")
    )


def create_ics_calendar(args: dict, events: list[UniversityClass]):
    cal = create_calendar(args, events)
    # if args['output']:
    #     filename = args['output'] + ".ics"
    # else:
    #     filename = "timetable.ics"

    # write_cal_to_file(cal, filename)


def main():
    args = parse_argv()
    print(args)
    events = get_new_timetable_from_file("timetable.xlsx")
    create_ics_calendar(args, events)


if __name__ == '__main__':
    main()
