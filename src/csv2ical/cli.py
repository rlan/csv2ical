#!/usr/bin/env python3
"""CLI for csv2ical.

This module creates a CLI app and validates arguments.
"""

import csv
import datetime

import click
from icalendar import Calendar, Event


@click.command()
@click.argument("csv_name", type=click.Path(exists=True))
@click.argument("ics_name", type=click.Path())
@click.version_option()
def main(csv_name: str, ics_name: str):
    """Convert a CSV file to an ICS file.

    Convert a CSV file with event details to an iCalendar ICS file,
    which can be imported into apps like Google Calendar, Microsoft
    Outlook, Apple macOS Calendar and etc.

    CSV_NAME is the file name of a CSV file with event details.

    ICS_NAME is the resulting iCalendar ICS file.
    """
    with open(csv_name) as csv_file:
        reader = csv.reader(csv_file)

        # required to be compliant:
        cal = Calendar()
        cal.add("prodid", "-//" + csv_name + "//mxm.dk//")
        cal.add("version", "2.0")

        for n, row in enumerate(reader):
            # Skip header row
            if n == 0:
                continue
            summary = row[0]
            start = " ".join([row[1].strip(), row[2].strip()])
            dtstart = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M")
            end = " ".join([row[3].strip(), row[4].strip()])
            dtend = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M")
            description = row[5].strip()
            location = row[6].strip()

            event = Event()
            event.add("summary", summary)
            event.add("dtstart", dtstart)
            event.add("dtend", dtend)
            event.add("description", description)
            event.add("location", location)
            cal.add_component(event)

        with open(ics_name, "wb") as ics_file:
            ics_file.write(cal.to_ical())
            ics_file.close()
            return 0
