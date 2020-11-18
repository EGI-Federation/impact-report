#!/usr/bin/env python3

import csv
import os

import requests
from bs4 import BeautifulSoup


def print_details(url, csv_filename, years):
    """
    Parsing the scientific publications from the web site and
    export the list in a CSV file
    """

    item_authors = item_year = item_journal = item_doi = item_title = ""

    with open(csv_filename, "w", newline="") as csvfile:
        # Header of the CSV file
        fieldnames = ["Author(s)", "Year", "Title", "Journal", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        index = 0
        rn = requests.get(url)
        soup = BeautifulSoup(rn.text, "lxml")

        divs = soup.findAll("div", {"class": "col"})[2]
        links = divs.findAll("h5")

        for item in links:
            tmp = item.get_text().strip()

            if "Authors" in tmp:
                item_authors = tmp[9:].strip()

            if "Year" in tmp:
                item_year = tmp[6:].strip()

            if "Journal" in tmp:
                item_journal = tmp[8:].strip()

            if "DOI" in tmp:
                item_doi = tmp[4:].strip()

            if item_year in years:
                writer.writerow(
                    {
                        "Author(s)": item_authors,
                        "Year": item_year,
                        "Title": item_title,
                        "Author(s)": item_authors,
                        "Journal": item_journal,
                        "DOI": item_doi,
                    }
                )

            index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "https://eatris.eu/publications-citing-eatris/"
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
