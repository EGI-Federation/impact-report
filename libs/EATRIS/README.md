# Parsing the EATRIS scientific publications

With this script we will: 

* Use the [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to parse the EATRIS [repository](https://eatris.eu/publications-citing-eatris/) 
* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements
* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `io`, `os`, `csv`, `requests`, `re`, and `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Usage
* Go to the [EATRIS repository](https://eatris.eu/publications-citing-eatris/)
* Configure the settings (e.g.: `url`, and `years` range)

<pre>
[..]
url="https://eatris.eu/publications-citing-eatris/"
csv_filename="publications.csv"

years = [2016, 2017, 2018, 2019]
print_details(url, csv_filename, years)
[..]
</pre>

* Parse and export the EATRIS publications as follows:
<pre>
]$ python3 parsing_EATRIS.py 
- Parsing publications in progress...[OK]
</pre>

* Publications are saved in the `publications.csv` file.
