<!-- # .xlsx Timetable to Google calendar -->
  
# GTIMETABLE
An easy to use parser that represents .xlsx timetable to your Google Calendar

Timetable.xslx |  Google Calendar
:-------------------------:|:-------------------------:
![image](https://i.postimg.cc/K4XC0Cdj/Screenshot-2023-01-21-at-9-37-20-PM.png) |  ![image](https://i.postimg.cc/0kVPvQY5/Screenshot-2023-01-21-at-9-36-52-PM.png)


## 📦 Installation

### Required:
 - Python3.10 or higher
 - Google Cloud Credentials (**credentials.json**) for Google Calendar ([guide](https://developers.google.com/workspace/guides/create-credentials))
 <!-- - [Poetry](https://python-poetry.org/) or [virtualenv](https://virtualenv.pypa.io/en/latest/)  -->


### Packages and environment installation
    poetry install
You can also install packages from `requirements.txt` file

## ⚡Usage

Change `timetable.xlsx` file for yourself and run `main.py` with 2 args

- date until you timetable will be filled in calendar in format `day/month/year`
- `timetable.xslx` or new filename for `.xslx` file that you want to parse

### Example:
`python3 main.py 30/12/2022 timetable.xlsx`

    
## 👨‍💻 TODO 

 - [ ] custom class length (1.35hrs now)

