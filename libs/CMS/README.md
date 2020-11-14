# Parsing the scientific publications of the CMS experiment

With this script we will: 

* Use the [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to parse the CMS [repository](http://cms-results.web.cern.ch/cms-results/public-results/publications/CMS/index.html) 
* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements
* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `json`, `xmltodict`, `urlparse`, `urlopen`, `re`, `httplib` `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Usage
* Go to the [CMS repository](http://cms-results.web.cern.ch/cms-results/public-results/publications/CMS/index.html)
* Configure the settings (e.g.: `url`, and `years` range)

<pre>
[..]
url="http://cms-results.web.cern.ch/cms-results/public-results/publications/CMS/index.html"
csv_filename="publications.csv"

years = [2016, 2017, 2018, 2019]
print_details(url, csv_filename, years)
[..]
</pre>

* Parse and export the CMS publications as follows:
<pre>
]$ python3 parsing_CMS.py 
- Parsing publications in progress...[OK]
</pre>

