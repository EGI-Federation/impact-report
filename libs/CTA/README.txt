]$ wget https://www.cta-observatory.org/science/library/
]$ cat index.html | grep -i window._libraryData | awk -F 'window._libraryData = ' '{print $2}' | awk -F '</script>' '{print $1}'> publications.json 
]$ python3 parsing_CTA.py 
