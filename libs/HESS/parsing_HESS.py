#!/usr/bin/env python3

import re
import requests
import csv
import os
from dateutil.parser import parse, ParserError
from bs4 import BeautifulSoup


def print_details(url, csv_filename, years):
    """
       Parsing the scientific publications from the web site and 
       export the list in a CSV file
    """

    item_year = item_journal = item_doi = item_title = ""
    doi_list = journal_list = []

    with open(csv_filename, "w", newline="") as csvfile:
        # Header of the CSV file
        fieldnames = ["Author(s)", "Year", "Title", "Journal", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        index = 0
        rn = requests.get(url)
        soup = BeautifulSoup(rn.text, "lxml")

        divs = soup.find("div", {"id": "content"}).find_all("p")

        for div in divs:
            for col in div.findAll("b"):
                item_title = col.text.strip()

            for col in div.findAll("a"):
                if "information" not in col.text:
                    journal_list.append(col.text)

                if "auxiliary" not in col.get("href"):
                    doi_list.append(col.get("href"))

            if len(doi_list) > 0:
                item_doi = doi_list[len(doi_list) - 2]

            if len(journal_list) > 0:
                item_journal = journal_list[len(journal_list) - 1].strip()
                # Extracting item_year from item_journal
                match = re.match(r".*(([1-2][0-9]{3}))", item_journal)
                if match is not None:
                    item_year = match.group(1)
                    item_year = parse(item_year).year

            doi_list = []
            journal_list = []

            if item_title and item_journal:
                if item_year in years:
                    # print("\nTitle = %s "%item_title)
                    # print("Year = %s "%item_year)
                    # print("DOI = %s "%item_doi)
                    # print("Journal = %s" %item_journal)

                    writer.writerow(
                        {
                            "Author(s)": "The H.E.S.S. Collaboration",
                            "Year": item_year,
                            "Title": item_title,
                            "Journal": item_journal,
                            "DOI": item_doi,
                        }
                    )

        index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "https://www.mpi-hd.mpg.de/hfm/HESS/pages/publications/pubs_jour.shtml"
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
