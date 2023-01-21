<!-- # .xlsx Timetable to Google calendar -->
  
# GTIMETABLE
An easy to use parser that represents .xlsx timetable to your Google Calendar

Google Calendar |  Timetable.xslx
:-------------------------:|:-------------------------:
![image](https://i.ibb.co/hMFRZ6n/Screenshot-2023-01-21-at-9-18-02-PM.png) |  ![image](https://i.ibb.co/kDt5v3G/Screenshot-2023-01-21-at-9-16-38-PM.png)


## 📦 Installation

### Required:
 - Python3.10 or higher
 - Google Cloud Credentials (**credentials.json**) for Google Calendar ([guide](https://developers.google.com/workspace/guides/create-credentials))
 <!-- - [Poetry](https://python-poetry.org/) or [virtualenv](https://virtualenv.pypa.io/en/latest/)  -->


### Packages and environment installation
    poetry install
You can also install packages from `requirements.txt` file copd

## ⚡Usage

Change `timetable.xlsx` file for yourself and run `main.py` with 2 args

- date until you timetable will be filled in calendar in format `day/month/year`
- `timetable.xslx` or new filename for `.xslx` file that you want to parse

### Example:
`python3 main.py 30/12/2022 timetable.xlsx`

    
## todo

 - [ ] custom class length (1.35hrs now)

