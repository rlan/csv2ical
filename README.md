# csv2ical

[![Tests badge](https://github.com/rlan/csv2ical/actions/workflows/tests.yml/badge.svg)](https://github.com/rlan/csv2ical/actions/workflows/tests.yml)

Convert a CSV file with event information to an iCalendar ICS file, which can be imported into Google Calendar, Microsoft Outlook and etc.

Installation:

* Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12.

```sh
pip install -r requirements.txt
```

Example:

An all-day event starts at midnight and ends at the midnight of the next day. Although `sample.csv` contains only all-day events, e.g. birthdays, any shorter events, e.g. meetings, would also work. The header row in the CSV file is for human to read and skipped by the code.

```csv
"Subject","Start Date","End Date","Description","Location"
"Harry Potter birthday","1980-07-31 00:00","1980-08-01 00:00","The Chosen One","Godric's Hollow"
"Ron Weasley birthday","1980-03-01 00:00","1980-03-02 00:00","Won-Won","Ottery St Catchpole"
"Hermione Granger birthday","1979-09-19 00:00","1979-09-20 00:00","'Mione",""
```

Usage:

```sh
python csv2ical.py --help
```

```txt
usage: csv2ical.py [-h] input output

positional arguments:
  input       Input csv file containing calendar events
  output      Output ics file

optional arguments:
  -h, --help  show this help message and exit
```

```sh
python csv2ical.py sample.csv sample.ics
```

```sh
cat sample.ics
```

```txt
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//sample.csv//mxm.dk//
BEGIN:VEVENT
SUMMARY:Harry Potter birthday
DTSTART;VALUE=DATE-TIME:19800731T000000
DTEND;VALUE=DATE-TIME:19800801T000000
DESCRIPTION:The Chosen One
LOCATION:Godric's Hollow
END:VEVENT
BEGIN:VEVENT
SUMMARY:Ron Weasley birthday
DTSTART;VALUE=DATE-TIME:19800301T000000
DTEND;VALUE=DATE-TIME:19800302T000000
DESCRIPTION:Won-Won
LOCATION:Ottery St Catchpole
END:VEVENT
BEGIN:VEVENT
SUMMARY:Hermione Granger birthday
DTSTART;VALUE=DATE-TIME:19790919T000000
DTEND;VALUE=DATE-TIME:19790920T000000
DESCRIPTION:'Mione
LOCATION:
END:VEVENT
END:VCALENDAR
```
