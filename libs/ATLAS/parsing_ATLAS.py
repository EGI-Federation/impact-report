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

         rn = requests.get(url)
         soup = BeautifulSoup(rn.text, "lxml")
  
         gdp_table = soup.find("table") 
         if gdp_table.findAll('tr') is not None:
            item_list = []
            for tds in gdp_table.findAll('td'):
                item_list.append(tds.text)
                for href in tds.findAll('a'):
                    if "Internal" in href.text:
                        item_list.append(href.get('href'))
            
            index=0
            while index < len(item_list):
                # Remove "Keywords" from the title
                item_title=item_list[index][0:item_list[index].find("Keywords")+1]
                # Remove "Full Title" from the title
                item_title=item_title[item_list[index].find("Full Title:")+11:-1]

                item_journal = item_list[index+2] 
                item_year = (item_list[index+3][7:9]).strip()
                
                item_doi = item_list[index+7]
                
                if int(item_year) in years:
                    #print(item_title)
                    #print(item_year)
                    #print(item_journal)
                    #print(item_doi)
                    writer.writerow({
                     'Author(s)': "ATLAS Collaboration",
                     'Year': "20"+item_year,
                     'Title': item_title,
                     'Journal': item_journal,
                     'DOI': item_doi
                    })

                index=index+8
   

def main():
    print("- Parsing publications in progress...", end="")
    url="https://twiki.cern.ch/twiki/bin/view/AtlasPublic/Publications"
    csv_filename="publications.csv"
    years = [16, 17, 18, 19]
    print_details(url, csv_filename, years)
    if (os.stat(csv_filename).st_size > 34):
       print("[OK]")
    else:
       print("[WARNING]")
       print("No publications found in the list!")

if __name__ == "__main__":
        main()

