cvs2ical
========

Convert a cvs file with event information to ical, which can be imported into Google Calendar, Microsoft Outlook and etc.


# Installation

```pip install -r requirements.txt```

# Example


`sample.csv` has all-day events. The header row is for human to read and skipped by the code.
```
"Subject","Start Date","End Date","Description","Location"
"Harry Potter birthday","1980-07-31 00:00","1980-08-01 00:00","The Chosen One","Godric's Hollow"
"Ron Weasley birthday","1980-03-01 00:00","1980-03-02 00:00","Won-Won","Ottery St Catchpole"
"Hermione Granger birthday","1979-09-19 00:00","1979-09-20 00:00","'Mione",""
```

## Usage

```
$ python csv2ical.py --help
usage: csv2ical.py [-h] input output

positional arguments:
  input       Input csv file containing calendar events
  output      Output ics file

optional arguments:
  -h, --help  show this help message and exit
```


```
python cvs2ical.py sample.csv sample.ics
```


```
$ cat sample.ics
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
