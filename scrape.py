from urllib import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import sys

year = raw_input("Enter desired year to scrape data:\n ")

try:
    year = int(year)
except ValueError:
    year = 2019
    print("Input error: Defaulting to 2019...")

url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
html = urlopen(url)
soup = BeautifulSoup(html, features='lxml')

headers = [th.getText() for th in soup.findAll('tr', limit=2)]
headers = headers[0].split("\n")
headers = headers[2:-1]

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                        for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)
print(stats)

# TODO:
# WRITE UP A PANDAS INDEXING TUTORIAL FOR GRABBING NBA DATA
# Helps you (re)learn pandas and will be nice to learn markdown and tutorial making
print("\n\nData is now imported as a pandas DataFrame object named \'stats\', happy hunting!")
print("\nIndexing: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html")
print("API reference: https://pandas.pydata.org/pandas-docs/stable/reference/index.html")
print("To see column names, run: \'stats.columns\'")
print(stats.columns)
print("E.g. If you wanted the first 10 players block numbers, run \'stats[['Player', 'BLK']][1:10]\'")
print(stats[['Player', 'BLK']][1:10])
