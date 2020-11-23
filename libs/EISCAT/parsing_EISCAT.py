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

        for div in soup.findAll("div", {"class": "publication-content"}):
            for publication in div.findChildren("p", {"class": "all-publication-name"}):
                if publication.text:
                    item_title = publication.text

            for item in div.findChildren("p", {"class": "publication-information"}):
                item_authors = item.find("em").text
                # Stripping '\n' and '\t' from string
                item_authors = item_authors.replace("\n", "")
                item_authors = item_authors.replace("\t", "")
                # Getting the year
                item_year = item.text.strip()[-4:]

                if (item.find("a")) is not None:
                    # Getting the DOI
                    item_doi = item.find("a").get("href")
                    # Getting the Journal
                    item_journal = item.find("a").text

                if int(item_year) in years:
                    print("\n")
                    print(item_title)
                    print(item_authors)
                    print(item_year)
                    print(item_journal)
                    print(item_doi)

                    writer.writerow(
                        {
                            "Author(s)": item_authors,
                            "Year": item_year,
                            "Title": item_title,
                            "Journal": item_journal,
                            "DOI": item_doi,
                        }
                    )

        index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "https://www.eiscat.se/scientist/publications/"
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
