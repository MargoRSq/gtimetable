import io
import requests
import openpyxl.reader.excel

from pathlib import Path
from typing import List

from src.timetable import UniversityClass


def cell_to_str(cell) -> str:
    value = cell.value
    return str(value)


def parse_rasp(file):
    ps = openpyxl.reader.excel.load_workbook(file)
    sheet = ps['Лист1']

    pr_numbers = [3 * i for i in range(1, 31)]
    event_list = []
    for number in pr_numbers:
        wday = ((number - 3)) // (15)
        time = cell_to_str(sheet[f'B{number}'])
        odd_description = cell_to_str(sheet[f'C{number + 1}']) + "\n" + cell_to_str(sheet[f'C{number + 2}'])
        even_description = cell_to_str(sheet[f'D{number + 1}']) + "\n" + cell_to_str(sheet[f'D{number + 2}'])
        odd_class = UniversityClass(class_name=cell_to_str(sheet[f'C{number}']),
                                    desc=odd_description,
                                    time_interval=time,
                                    wday=wday,
                                    wtype=True)
        even_class = UniversityClass(class_name=cell_to_str(sheet[f'D{number}']),
                                     desc=even_description,
                                     time_interval=time,
                                     wday=wday,
                                     wtype=False)
        event_list.extend([odd_class, even_class])

    return event_list


def get_new_timetable_from_file(path: str) -> List[UniversityClass]:
    xlsx_file = Path(path)
    return parse_rasp(xlsx_file)


def get_new_timetable_by_url(url):
    resp = requests.get(url)
    bytes = io.BytesIO(resp.read())
    return parse_rasp(bytes)
