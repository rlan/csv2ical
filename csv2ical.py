#!/usr/bin/env python

import csv
from icalendar import Calendar, Event
from datetime import datetime
import argparse


parser = argparse.ArgumentParser(
    description=(
        "Convert a CSV file with event information to an iCalendar ICS file, which"
        " can be imported into Google Calendar, Microsoft Outlook and etc."
    )
)
parser.add_argument("input", type=str, help="Input CSV file containing calendar events")
parser.add_argument("output", type=str, help="Output iCalendar ICS file")
args = parser.parse_args()


def csv2ical(input_file: str, output_file: str):
    """
    Convert a CSV file with event information to an iCalendar ICS file, which
    can be imported into Google Calendar, Microsoft Outlook and etc.

    Parameters
    ----------
    input_file : str
    output_file : str

    Returns
    -------
    Empty
    """

    with open(input_file) as csv_file:
        reader = csv.reader(csv_file)

        # required to be compliant:
        cal = Calendar()
        cal.add("prodid", "-//" + input_file + "//mxm.dk//")
        cal.add("version", "2.0")

        for n, row in enumerate(reader):
            # Skip header row
            if n == 0:
                continue
            summary = row[0]
            dtstart = datetime.strptime(row[1], "%Y-%m-%d %H:%M")
            dtend = datetime.strptime(row[2], "%Y-%m-%d %H:%M")
            description = row[3].strip()
            location = row[4].strip()

            event = Event()
            event.add("summary", summary)
            event.add("dtstart", dtstart)
            event.add("dtend", dtend)
            event.add("description", description)
            event.add("location", location)
            cal.add_component(event)

        with open(output_file, "wb") as out_f:
            out_f.write(cal.to_ical())
            out_f.close()


def main(args):
    csv2ical(args.input, args.output)


if __name__ == "__main__":
    main(parser.parse_args())
