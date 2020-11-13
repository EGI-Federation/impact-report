#!/usr/bin/env python3

import io, requests, csv, os
from dateutil.parser import parse
from bs4 import BeautifulSoup

def print_details(url, csv_filename, years):
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
  
         gdp_table = soup.find("table", {"class": "views-table"}) 
         if gdp_table.findAll('tr') is not None:
            for row in gdp_table.findAll('tr'):
                for col in row.findAll('td'):
                    
                    # Getting the title of the publication
                    item_title=(col.text[0:col.text.find('Article reference')]).strip()

                    for li in row.findAll('li'):
                        if li.b is not None:
                           # Getting the Journal of the publication
                           if "Article reference:" in li.text:
                              item=li.text.split()
                              item_journal=item[2]+" "+item[3]+" "+item[4]

                           # Getting the year of the publication
                           if "Publication date:" in li.text:
                              item_year=li.text.split()[-1]
                              item_year=parse(item_year).year

                        if li.a is not None:
                           # Get the reference
                           item_href=li.a.get('href')

                    if item_year in years:
                       #print(item_title)
                       #print(item_year)
                       #print(item_journal)
                       #print(item_doi)

                       writer.writerow({
                        'Author(s)': "ALICE Collaboration",
                        'Year': item_year,
                        'Title': item_title,
                        'Journal': item_journal,
                        'DOI': item_doi
                       })

            index=index+1
   

def main():
    print("- Parsing publications in progress...", end="")
    url="https://alice-publications.web.cern.ch/publications?title=&field_draft_pub_date_value%5Bmin%5D=&field_draft_pub_date_value%5Bmax%5D=&items_per_page=100"
    csv_filename="publications.csv"
    years = [2016, 2017, 2018, 2019]
    print_details(url, csv_filename, years)
    if (os.stat(csv_filename).st_size > 34):
       print("[OK]")
    else:
       print("[WARNING]")
       print("No publications found in the list!")

if __name__ == "__main__":
        main()

