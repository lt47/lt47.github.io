from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import re
import pandas
import csv

f = open('linktitles.csv', 'r')

with f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            readlinks = e
            html = urlopen(readlinks)
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find_all('img', {'src':re.compile('.jpg')})
            for image in images:
                imgtitle = image['src']+'\n'
                df = pandas.DataFrame([imgtitle])
                df.to_csv('imgwebscraper.csv', index=False, header=None, mode='a')
