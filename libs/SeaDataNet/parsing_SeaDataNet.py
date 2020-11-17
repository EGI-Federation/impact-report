#!/usr/bin/env python3

import re
import requests
import csv
import os
from bs4 import BeautifulSoup


def print_details(url, csv_filename, years):
    """
       Parsing the scientific publications from the web site and 
       export the list in a CSV file
    """

    item_authors = item_year = item_href = item_journal = item_doi = item_title = ""

    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["Author(s)", "Year", "Title", "Journal", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        index = 0
        rn = requests.get(url)
        soup = BeautifulSoup(rn.text, "lxml")

        divs = soup.findAll("div", {"class": "col-sm-12"})[4]
        links = divs.findAll("li")

        for item in links:
            tmp = item.get_text()

            # Find whether DOI/doi is specified
            if "DOI" in tmp:
                item_doi = tmp[tmp.find("DOI") + 4 :].strip()
            elif "doi" in tmp:
                item_doi = tmp[tmp.find("doi") + 4 :].strip()

            # Find the index of the first digit in a string
            m = re.search(r"\d", tmp)
            if m is not None:
                item_authors = tmp[0 : m.start() - 2]

            if item.find("strong") is not None:
                try:
                    item_year = str(item.find("strong").text)
                except AttributeError:
                    pass

            if item.find("a") is not None:
                item_title = item.find("a").text
                item_href = item.find("a").attrs["href"]

            if item.find("em") is not None:
                item_journal = item.find("em").text

            if item_year in years:
                # print("- Year = %s " %item_year)
                # print("- Author(s) = %s " %item_authors)
                # print("- Title = %s " %item_title)
                # print("- Journal = %s " %item_journal)
                # if (item_doi):
                #   print("- DOI = %s\n " %item_doi)
                # else:
                #   print("- DOI = %s\n " %item_href)

                if item_doi:
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
                else:
                    writer.writerow(
                        {
                            "Author(s)": item_authors,
                            "Year": item_year,
                            "Title": item_title,
                            "Journal": item_journal,
                            "DOI": item_href,
                        }
                    )

                index = index + 1


def main():
    print("- Parsing publications in progress...", end="")
    url = "https://www.seadatanet.org/Publications/Scientific-publications"
    csv_filename = "publications.csv"
    years = ["2016", "2017", "2018", "2019", "2020"]
    print_details(url, csv_filename, years)
    if os.stat(csv_filename).st_size > 34:
        print("[OK]")
    else:
        print("[WARNING]")
        print("No publications found in the list!")


if __name__ == "__main__":
    main()
