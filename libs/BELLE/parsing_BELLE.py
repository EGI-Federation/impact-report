#!/usr/bin/env python3

import io, requests
from bs4 import BeautifulSoup
from pyparsing import unicode

def print_details(url):
    rn = requests.get(url)
    soup = BeautifulSoup(rn.text, "lxml")

    for index in range (2):
        results = soup.find("li", {"value": index})
        if results is not None:
           #print(results)
           title=results.find_all("Belle Collaboration")
           print(title)
           for item in results.find_all("a"):
               #print(item)
               href=item.get("href")
               if href is not None:
                  if "arXiv.org" in href:
                     print(href)
               #print(item.text)
               #print(item.get("href"))
        
           
    #       soup_2 = BeautifulSoup(results, "lxml")
    #       for items in soup_2.find_all("li"):
    #           print(items)

       
    #for items in soup.find_all("li"):
    #    print(items.title.strip())
    exit() 

    for items in soup.find_all("li"):
        for elem in items:
            title=elem.find("a")
            authors=soup.find_all("a", string="(Belle Collabortion)")
            if title is not None:
               try:
                   print(title.text.strip())
               except AttributeError: pass

    #for items in soup.findAll("a"):
    #    print(items.get("href"))



def main():
    print("- Parsing BELLE-II publications in progress...")
    url="https://belle.kek.jp/bdocs/b_journal.html"

    print_details(url)

if __name__ == "__main__":
        main()

