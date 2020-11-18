#!/usr/bin/env python3

import os
import csv
import json


def parsing_publications(filename, csv_filename, years):
    """
       Parsing the scientific publications from the web site and 
       export the list in a CSV file
    """

    with open(filename) as fp:
        data = json.load(fp)
    fp.close()

    with open(csv_filename, "w", newline="") as csvfile:
        # Header of the CSV file
        fieldnames = ["Author(s)", "Year", "Title", "Journal", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        index = 0
        while index < len(data):
            if int(data[index]["year"]) in years:
                writer.writerow(
                    {
                        "Author(s)": data[index]["full_list_of_authors"],
                        "Year": data[index]["year"],
                        "Title": data[index]["title"],
                        "Journal": data[index]["journal"],
                        "DOI": data[index]["doi"],
                    }
                )

            index = index + 1


def main():
    print("- Parsing the CTA publications in progress...", end="")
    filename = "publications.json"
    csv_filename = "publications.csv"
    years = [2016, 2017, 2018, 2019]
    parsing_publications(filename, csv_filename, years)
    if os.stat(csv_filename).st_size > 34:
        print("[OK]")
    else:
        print("[WARNING]")
        print("No publications found in the list!")


if __name__ == "__main__":
    main()
