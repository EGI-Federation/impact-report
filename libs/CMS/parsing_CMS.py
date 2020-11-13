#!/usr/bin/env python3

import io, requests, csv, os
from dateutil.parser import parse
from bs4 import BeautifulSoup

def print_details(url, webroot, csv_filename, years):
    '''
       Parsing the scientific publications from the web site and 
       export the list in a CSV file
    '''

    item_authors=item_year=item_href=item_journal=item_doi=item_title=""

    with open(csv_filename, 'w', newline='') as csvfile:
         # Header of the CSV file
         fieldnames = ['Author(s)', 'Year', 'Title', 'Journal', 'DOI']
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         writer.writeheader()

         index=0
         rn = requests.get(url)
         soup = BeautifulSoup(rn.text, "lxml")

         gdp_table = soup.find("table")
         if gdp_table.findAll("tr") is not None:
            for row in gdp_table.findAll("tr"):
                for col in row.findAll("td", {"class": "cadi"}):
                    item_doi=webroot+col.a.get('href')
                for col in row.findAll("td", {"class": "title"}):
                    item_title=col.text.strip()
                for col in row.findAll("td", {"class": "status"}):
                    item_journal=col.text.strip()
                for col in row.findAll("td", {"class": "date"}):
                    item_year=(col.text.strip()).split()[-1]
                    item_year=parse(item_year).year
                    
                #print(item_title)
                #print(item_journal)
                #print(item_year)
                #print(item_doi)

                if item_year in years:
                       writer.writerow({
                        'Author(s)': "CMS Collaboration",
                        'Year': item_year,
                        'Title': item_title,
                        'Journal': item_journal,
                        'DOI': item_doi
                })

            index=index+1
   

def main():
    print("- Parsing publications in progress...", end="")
    url="http://cms-results.web.cern.ch/cms-results/public-results/publications/CMS/index.html"
    webroot="http://cms-results.web.cern.ch/cms-results/public-results/publications/"
    csv_filename="publications.csv"
    years = [2016, 2017, 2018, 2019]
    print_details(url, webroot, csv_filename, years)
    if (os.stat(csv_filename).st_size > 34):
       print("[OK]")
    else:
       print("[WARNING]")
       print("No publications found in the list!")

if __name__ == "__main__":
        main()

