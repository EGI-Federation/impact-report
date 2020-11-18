#!/usr/bin/env python3

import csv
import os
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse


def print_details(url, csv_filename, years):
    """
       Parsing the scientific publications from the web site and 
       export the list in a CSV file
    """

    item_year = item_journal = item_doi = item_title = ""

    with open(csv_filename, "w", newline="") as csvfile:
        # Header of the CSV file
        fieldnames = ["Author(s)", "Year", "Title", "Journal", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        index = 0

        rn = requests.get(url)
        soup = BeautifulSoup(rn.text, "lxml")

        gdp_table = soup.find("table")
        if gdp_table.findAll("tr") is not None:
            for row in gdp_table.findAll("tr"):
                col = row.findAll("td")
                # Get the title of the publication
                item_title = (col[0].text).strip()

                item_journal = (col[2].text).strip()

                if "Submitted on" not in col[3].text:
                    item_year = (col[3].text).strip()
                    # Strip the year from the string
                    item_year = parse(item_year).year

                for href in col[1].find_all("a"):
                    # Get the href from the first <a>
                    item_doi = ((col[1].find_all("a"))[0]).get("href")

                if item_year in years:

                    writer.writerow(
                        {
                            "Author(s)": "LHCb Collaborations",
                            "Year": item_year,
                            "Title": item_title,
                            "Journal": item_journal,
                            "DOI": item_doi,
                        }
                    )

                index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "http://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/Summary_all.html"
    csv_filename = "publications.csv"
    years = [2016, 2017, 2018, 2019]
    print_details(url, csv_filename, years)
    if os.stat(csv_filename).st_size > 34:
        print("[OK]")
    else:
        print("[WARNING]")
        print("No publications found in the list!")


if __name__ == "__main__":
    main()
