

# .xlsx Timetable to Google calendar
  

## Installation

 Required:
 - python3.6 or higher
 - poetry or virtualenv

### poetry installation

    $ poetry install
### virtualenv installation

    $ python3 -m venv env/
    $ source env/bin/activate  ## for mac os users 
    OR
    $ .\env\bin\activate ## for windows users
    $ pip3 install -r requirements.txt

## Usage
Change timetable.xlsx file for yourself and run command with start and end dates.

    python3 main.py 26/09/2022 30/12/2022 timetable.xlsx
    
## todo

 - [ ] custom class length (1.35hrs now)
