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

| Collaboration | Repository |
| :---          | :---       |
| ALICE         | [link](http://alice-publications.web.cern.ch/publications) |
| ATLAS         | [link](https://twiki.cern.ch/twiki/bin/view/AtlasPublic/Publications)  |
| BELLE II (ç)  | [link](https://inspirehep.net/) |
| BIOMED        | Direct reporting via interview |
| CLARIN        | [link](https://beta.clarin.openaire.eu/) |
| CTA           | [link](https://www.cta-observatory.org/science/library/) |
| CMS           | [link](http://cms-results.web.cern.ch/cms-results/public-results/publications/CMS/index.html) |
| DARIAH        | [link](https://halshs.archives-ouvertes.fr/DARIAH), [link](https://beta.dariah.openaire.eu/) |
| DUNE (ç)      | [link](https://inspirehep.net/) |
| EATRIS        | [link](https://eatris.eu/publications-citing-eatris/) |
| EISCAT        | [link](https://www.eiscat.se/scientist/publications/) |
| ELI-NP        | [link](https://www.eli-np.ro/scientific_papers.php) |
| H.E.S.S.      | [link](https://www.mpi-hd.mpg.de/hfm/HESS/pages/publications/pubs_jour.shtml) |
| IceCube       | [link](https://icecube.wisc.edu/pubs) |
| JUNO (ç)      | [link](https://inspirehep.net/) |
| KM3NET (ç)    | [link](https://inspirehep.net/) |
| LifeWatch     | Direct reporting via interview and OpenAIRE |
| LOFAR         | [link](https://old.astron.nl/radio-observatory/lofar-science/lofar-papers/lofar-papers) |
| LHCb          | [link](http://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/Summary_all.html) |
| LSST          | [link](https://ui.adsabs.harvard.edu/) |
| NBIS          | Direct reporting via interview and OpenAIRE |
| NextGEOSS     | Direct reporting via interview and OpenAIRE |
| SeaDataNet    | [link](https://www.seadatanet.org/Publications/Scientific-publications) |
| SKA           | [link](https://explore.openaire.eu/) |
| VIRGO         | [link](https://pnp.ligo.org/ppcomm/Papers.html) |
| WeNMR         | Direct reporting via interview and OpenAIRE |
| XENON (ç)     | [link](https://inspirehep.net/) |


## Available libs
- [ALICE publications](libs/ALICE)
- [CMS publications](libs/CMS)
- [CTA publications](libs/CTA)
- [EATRIS publications](libs/EATRIS)
- [ELI-NP publications](libs/ELI-NP)
- [H.E.S.S. publications](lib/HESS)

<<<<<<< HEAD
## Note (�)
To parse the publications from the [Inspire HEP portal](https://inspirehep-net) we will use:
* Export from the portal the list of publications in bibtex format  
=======
## Note (ç)
To parse the publications from the [Inspire HEP portal](https://inspirehep-net) we will:
* Export from the portal the list of publications in `bibtex` format  
>>>>>>> 0089da5af7c24eb76685a059fb0af864326d3d9a
* Generate the CVS file using the repo...

