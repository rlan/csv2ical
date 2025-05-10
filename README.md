# csv2ical

[![Testing badge](https://github.com/rlan/csv2ical/actions/workflows/tests.yml/badge.svg)](https://github.com/rlan/csv2ical/actions/workflows/tests.yml)
![Python versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![MIT license](https://img.shields.io/github/license/rlan/csv2ical)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15024834.svg)](https://doi.org/10.5281/zenodo.15024834)

A CLI tool that converts a CSV file with event details into an iCalendar [ICS](https://docs.fileformat.com/email/ics/) file. The ICS file can then be imported into apps like Google Calendar, Microsoft Outlook, Apple macOS Calendar and etc.

## Installation

First, install [uv](https://github.com/astral-sh/uv).

Then:

```sh
uv tool install git+https://github.com/rlan/csv2ical
```

Verify installation:

```sh
uv tool list
```

```txt
csv2ical v1.0.1
- csv2ical
```

## Usage

```sh
csv2ical --help
```

```txt
Usage: csv2ical [OPTIONS] CSV_NAME ICS_NAME

  Converts a CSV file with event information to an iCalendar ICS file, which
  can be imported into Google Calendar, Microsoft Outlook, macOS calendar and
  etc.

  CSV_NAME is the file name of a CSV file with event information.

  ICS_NAME is the resulting iCalendar ICS file.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.
```


Example:

[`sample.csv`](sample.csv):

```csv
"Subject","Start Date","Start Time","End Date","End Time","Description","Location"
"Harry Potter birthday","1980-07-31","00:00","1980-08-01","00:00","The Chosen One","Godric's Hollow"
"Ron Weasley birthday","1980-03-01","00:00","1980-03-02","00:00","Won-Won","Ottery St Catchpole"
"Hermione Granger birthday","1979-09-19","00:00","1979-09-20","00:00","'Mione",""
```

An all-day event starts at midnight and ends at the midnight of the next day. Although `sample.csv` contains only all-day events, e.g. birthdays, any shorter events, e.g. meetings, would also work.

The names in the CSV header row is documentation. It tells the author of the CSV file which column to write the event details. Editing that row has no effect on the output ICS file, but **do not** omit it.


Reproduce [`sample.ics`](sample.ics):

```sh
csv2ical sample.csv sample.ics
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

## Update to a new version

```sh
uv tool upgrade csv2ical
```

## Uninstallation

```sh
uv tool uninstall csv2ical
```

## Development

See [development.md](development.md)

## Citation

If this project helps your research, don't hesitate to spread the word! Click on the badge below and find citation formats (e.g., BibTeX and etc) at the bottom of that page.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15024834.svg)](https://doi.org/10.5281/zenodo.15024834)

## License

[MIT](LICENSE)
