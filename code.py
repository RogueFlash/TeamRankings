#Hacktoberfest2021
#start here!

#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
import requests
from bs4 import BeautifulSoup


# In[2]:

cricket = []

with open('CricketTeams.txt', 'r') as file:
  print(cricket)
  
  for line in file:
      x = line.strip()
      url = 'http://www.espncricinfo.com/' + x.split(',')[0] + '/content/player/country.html?country=' + x.split(',')[1]
      print(url)
      
      html = requests.get(url)
      soup = BeautifulSoup(html.content, 'html.parser')
      
      rawPlayers = soup.find_all('td', class_="divider")
      playerSet = set([])
      
      for child in rawPlayers:
            playerSet.add(child.text)
          

with open('CricketTeams.json', 'w', encoding='utf-8') as file:
    json.dump(cricket, file, ensure_ascii=False, indent=2)
