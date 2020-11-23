# Parsing the EISCAT scientific publications

With this script we will:

* Use the [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to parse the EISCAT [repository](https://www.eiscat.se/scientist/publications/)
* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements

* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `requests`, `csv`, `os` and `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Usage

* Go to the [EISCAT repository](https://www.eiscat.se/scientist/publications/)
* Configure the settings (e.g.: `url`, and `years` range)

```sh
[..]
url="https://www.eiscat.se/scientist/publications/"
csv_filename="publications.csv"

years = [2016, 2017, 2018, 2019]
print_details(url, csv_filename, years)
[..]
```

* Parse and export the EISCAT publications as follows:
  ```sh
  ]$ python3 parsing_EISCAT.py
     - Parsing publications in progress...[OK]
  ```

* Publications are stored in the `publications.csv` file.
