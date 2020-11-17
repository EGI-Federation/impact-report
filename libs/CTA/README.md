# Parsing the scientific publications of the CTA experiment

With this script we will:

* Produce a list of publications during the period of interest
* Export the list of publications in a CSV file

## Requirements

* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `json`, `csv` and `os` python libraries are requested
* Python v3.5.2+

## Usage

* Navigate the [CTA library](https://www.cta-observatory.org/science/library/)
* Download the HTML web site

```sh
]$ wget https://www.cta-observatory.org/science/library/
```

* Parse the HTML page and extract the CTA publications in JSON format

```sh
]$ cat index.html \
       | grep -i window._libraryData \
       | awk -F 'window._libraryData = ' '{print $2}' \
       | awk -F '</script>' '{print $1}'> publications.json
```

* Configure the settings (e.g.: `filename`, and `years` range)

```sh
[..]
filename="publications.json"
csv_filename="publications.csv"

years = [2016, 2017, 2018, 2019]
parsing_publications(filename, csv_filename, years)
[..]
```

* Parse the JSON file and export the CTA publications as follows:
```sh
]$ python3 parsing_CTA.py

- Parsing publications in progress...[OK]
```

* Publications are saved in the `publications.csv` file.
