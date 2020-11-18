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

    item_year = item_doi = item_title = ""

    with open(csv_filename, "w", newline="") as csvfile:
        # Header of the CSV file
        fieldnames = ["Author(s)", "Year", "Title", "Journal", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        index = 0
        rn = requests.get(url)
        soup = BeautifulSoup(rn.text, "lxml")

        trs = soup.findAll("tr")
        items_list = []

        for tr in trs:
            for td in tr.findAll("td"):
                items_list.append(td.text.strip())

                if td.findAll("a") is not None:
                    for href in td.findAll("a"):
                        items_list.append(href.get("href"))

            if len(items_list) > 0:
                item_author = items_list[1]
                item_title = items_list[2]
                item_year = items_list[4][0:4]
                item_doi = items_list[3]
                items_list = []

                if int(item_year) in years:
                    # print("Authors: %s" % item_author)
                    # print("Title: %s" % item_title)
                    # print("Year: %s" % item_year)
                    # print("DOI: %s" % item_doi)

                    writer.writerow(
                        {
                            "Author(s)": item_author,
                            "Year": item_year,
                            "Title": item_title,
                            "Journal": "",
                            "DOI": item_doi,
                        }
                    )

        index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "https://lofar-surveys.org/publications.html"
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
