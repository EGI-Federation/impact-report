# Parsing scientific publications of the CTA experiment

With this script we will: 

* Use the [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to parse the CTA [repository](https://www.cta-observatory.org/science/library/) 
* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements
* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `json`, `xmltodict`, `urlparse`, `urlopen`, `re`, `httplib` `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Usage
* Navigate the [CTA library](https://www.cta-observatory.org/science/library/)
* Download the HTML web site
<pre>
]$ wget https://www.cta-observatory.org/science/library/
</pre>

* Parse the HTML page and extract the list of publication in JSON format
<pre>
]$ cat index.html \
       | grep -i window._libraryData \
       | awk -F 'window._libraryData = ' '{print $2}' \
       | awk -F '</script>' '{print $1}'> publications.json 
</pre>

* Configure the settings (e.g.: `filename`, and `years` range)

<pre>
[..]
filename="publications.json"
csv_filename="publications.csv"

years = [2016, 2017, 2018, 2019]
parsing_publications(filename, csv_filename, years)
[..]
</pre>

* Parse and export the CTA publications as follows:
<pre>
]$ python3 parsing_CTA.py 
- Parsing publications in progress...[OK]
</pre>

### Note:
* Publications are saved in the `publications.csv` file.
* If necessary repeat the procedure moving between pages and concat the different CSV files.


