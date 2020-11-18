# Parsing the scientific publications of the ATLAS experiment

With this script we will:

* Use the [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to parse the ATLAS [repository](https://twiki.cern.ch/twiki/bin/view/AtlasPublic/Publications)
* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements

* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `os`, `csv`, `requests`, `parse` and `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Usage

* Configure the settings (e.g.: `url`, and `years` range)

```sh
[..]
url="https://twiki.cern.ch/twiki/bin/view/AtlasPublic/Publications"
csv_filename="publications.csv"

years = [16, 17, 18, 19]
print_details(url, csv_filename, years)
[..]
```

* Parse and export the ATLAS publications as follows:
  ```sh
  ]$ python3 parsing_ATLAS.py
  - Parsing publications in progress...[OK]
  ```
  
Publications will be saved in the `publications.csv` file
