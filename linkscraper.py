from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import re
import pandas
import csv

http = httplib2.Http()
status, response = http.request('http://www.nytimes.com')


for link in BeautifulSoup(response, features='html.parser', parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        linktitle = link['href']
        df = pandas.DataFrame([linktitle])
        df.to_csv('linktitles.csv', index=False, header=None, mode='a')
