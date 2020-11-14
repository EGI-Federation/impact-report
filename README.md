# impact-report

This repository is dedicated to the tracking of user communities supported by the EGI Federation, their scientific impact, and user community engagement. Overall, this activity aims at identifying the value proposition of the EGI Federation and maximizing its impact through the identification of new user communities.

To facilitate the assessment of the scientific impact of the user communities, a set of Python scripts for pulling data out of HTML and XML files and produce, in a CSV format, a list of scientific publications from the main project's experiments have been developed.

## Requirements

* Basic knowledge of Linux user environment and Python as programming language
* Basic knowledge of the `json`, `xmltodict`, `urlparse`, `urlopen`, `re`, `httplib`, `Beautiful Soap` python libraries are requested
* Python v3.5.2+
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (v4.9.2)

## Scientific paper repositories

The list of scientific publications is collected from the following repositories:

| Collaboration | Repository                                                 |
| ------------- | ---------------------------------------------------------- |
| ALICE         | [link](http://alice-publications.web.cern.ch/publications) |
| ATLAS         | [link](https://twiki.cern.ch/twiki/bin/view/AtlasPublic/Publications)  |


## Available libs

- [ALICE publications](libs/ALICE)
