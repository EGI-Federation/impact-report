# Parsing scientific publications of the ALICE experiment

With this script we will: 

* Use the [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to parse the ALICE [repository](https://alice-publications.web.cern.ch/publications) 
* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements
* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `json`, `xmltodict`, `urlparse`, `urlopen`, `re`, `httplib` `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Usage
* Navigate the [Physics Publications of the ALICE Collaboration in Refereed Journals](https://alice-publications.web.cern.ch/publications)
* Select `Items per page` = 100 and the page of interest
* Configure the settings (e.g.: `url`, and `years` range)

<pre>
[..]
url="https://alice-publications.web.cern.ch/publications?....&items_per_page=100"
csv_filename="publications.csv"
years = [2016, 2017, 2018, 2019]
print_details(url, csv_filename, years)
</pre>

* Parse and export the ALICE publications as follows:
<pre>
]$ python3 parsing_ALICE.py 
- Parsing publications in progress...[OK]
</pre>

### Note:
* Publications are saved in the `publications.csv` file.
* If necessary repeat the procedure moving between pages and concat the different CSV files.


