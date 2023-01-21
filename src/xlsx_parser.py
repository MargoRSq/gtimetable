import io
import requests
import openpyxl.reader.excel

from pathlib import Path
from typing import List

from src.timetable import UniversityClass


def parse_rasp(file):
    ps = openpyxl.reader.excel.load_workbook(file)
    sheet = ps['Лист1']

    pr_numbers = [3 * i for i in range(1, 31)]
    event_list = []
    for number in pr_numbers:
        wday = ((number - 3)) // (15)
        time = sheet[f'B{number}'].value
        odd_class = UniversityClass(sheet[f'C{number}'].value, time, wday, 1)
        even_class = UniversityClass(sheet[f'D{number}'].value, time, wday, 0)
        event_list.extend([odd_class, even_class])

    return event_list


def get_new_timetable_from_file(path: str) -> List[UniversityClass]:
    xlsx_file = Path(path)
    return(parse_rasp(xlsx_file))

def get_new_timetable_by_url(url):
    resp = requests.get(url)
    bytes = io.BytesIO(resp.read())
    return parse_rasp(bytes)
