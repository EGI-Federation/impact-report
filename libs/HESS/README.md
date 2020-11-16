# Parsing the H.E.S.S. scientific publications

With this script we will: 

* Use the [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to parse the H.E.S.S. [repository](https://www.mpi-hd.mpg.de/hfm/HESS/pages/publications/pubs_jour.shtml) 
* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements
* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `io`, `os`, `csv`, `parse`, `ParserError`, `re`, `requests` and `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Usage
* Go to the [H.E.S.S. repository](https://www.mpi-hd.mpg.de/hfm/HESS/pages/publications/pubs_jour.shtml)
* Configure the settings (e.g.: `url`, and `years` range)

<pre>
[..]
url="https://www.mpi-hd.mpg.de/hfm/HESS/pages/publications/pubs_jour.shtml"
csv_filename="publications.csv"

years = [2016, 2017, 2018, 2019]
print_details(url, csv_filename, years)
[..]
</pre>

* Parse and export the H.E.S.S. publications as follows:
<pre>
]$ python3 parsing_HESS.py 
- Parsing publications in progress...[OK]
</pre>

* Publications are saved in the `publications.csv` file.
