from bs4 import BeautifulSoup, SoupStrainer
import re
import pandas
import csv

f = open('emailsamples.txt', 'r',encoding='utf8')

with f:    
    reader = f.readlines()
    for line in reader:
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        print(match)
        df = pandas.DataFrame([match])
        df.to_csv('emailsamples.csv', index=False, header=None, mode='a')
