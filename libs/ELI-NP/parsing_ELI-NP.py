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

        divs = soup.findAll("article")
        title_list = href_list = author_list = []

        for div in divs:
            for item in div.findAll("a"):
                # Get the title of the publication
                title_list.append(item.text.strip())
                # Get the DOI of the publication
                href_list.append(item.get("href"))

            for item in div.findAll("i"):
                # Get the list of author(s)
                author_list.append(item.next_sibling.strip())
                # Get the name of the journal
                item_journal = item.text.strip()
                # Extract the year of the publication
                item_year = item_journal[len(item_journal) - 5 : -1]

            item_title = title_list[0]
            item_author = author_list[0]
            item_doi = href_list[1]

            title_list = []
            href_list = []
            author_list = []

            if int(item_year) in years:
                # print("\nTitle = %s "%item_title)
                # print("Authors = %s "%item_author)
                # print("Year = %s "%item_year)
                # print("DOI = %s "%item_doi)
                # print("Journal = %s" %item_journal)

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
    url = "https://www.eli-np.ro/scientific_papers.php"
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
