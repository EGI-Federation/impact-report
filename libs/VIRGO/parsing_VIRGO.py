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

        gdp_table = soup.findAll("table")
        for tr in gdp_table[1].findAll("tr"):
            doi_list = year_list = []
            for td in tr.findAll("td"):
                year_list.append(td.text)

                if "summary" not in td:
                    for b in td.findAll("b"):
                        if len(b.text) > 10:
                            # Getting the title of the publication
                            item_title = b.text
                            # print(item_title)

                for href in tr.findAll("a"):
                    if "summary" not in href.text:
                        doi_list.append(href.get("href"))

                # Getting the doi of the publication
                item_doi = doi_list[len(doi_list) - 2]
                doi_list = []

                for i in tr.findAll("i"):
                    if "-" not in i.text:
                        # Getting the name of the journal
                        item_journal = i.text.strip()

            if len(year_list) > 0:
                # Parsing the year
                item_year = year_list[0].split()[-1]
                item_year = parse(item_year[0:4]).year
                year_list = []

            if item_year in years:
                # print(item_title)
                # print(item_year)
                # print(item_journal)
                # print(item_doi)

                writer.writerow(
                    {
                        "Author(s)": "VIRGO Collaboration",
                        "Year": item_year,
                        "Title": item_title,
                        "Journal": item_journal,
                        "DOI": item_doi,
                    }
                )

        index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "https://pnp.ligo.org/ppcomm/Papers.html"
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
