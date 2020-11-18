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

    item_year = item_journal = item_doi = item_title = ""

    with open(csv_filename, "w", newline="") as csvfile:
        # Header of the CSV file
        fieldnames = ["Author(s)", "Year", "Title", "Journal", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        index = 0
        rn = requests.get(url)
        soup = BeautifulSoup(rn.text, "lxml")
        divs = soup.findAll("div", {"class": "pubs-item-cnt"})
        for div in divs:
            title_divs = div.findAll("div", {"class": "title"})
            for title in title_divs:
                item_title = title.find("em").text
                item_author = title.find("span", {"class": "authors"}).text
                item_journal = div.find("span", {"class": "type"}).next_sibling.strip()

                str_start = "("
                str_end = ")"
                if item_journal.find(str_start) != -1:
                    item_year = item_journal[
                        item_journal.find(str_start) + 1 : item_journal.rfind(str_end)
                    ]
                else:
                    item_year = item_journal.split()[-1]

            item_doi = div.find("a").get("href")

            if int(item_year) in years:
                # print(item_title)
                # print(item_year)
                # print(item_journal)
                # print(item_doi)

                writer.writerow(
                    {
                        "Author(s)": item_author,
                        "Year": item_year,
                        "Title": item_title,
                        "Journal": item_journal,
                        "DOI": item_doi,
                    }
                )

        index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "https://icecube.wisc.edu/pubs"
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
