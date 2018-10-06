from urllib2 import urlopen
from os import system
from bs4 import BeautifulSoup
import time
import re

SITE = 'https://psychedelicsalon.com/'
PODCASTS_PAGE = SITE + '/podcasts/'

page = urlopen(PODCASTS_PAGE)
pot = BeautifulSoup(page, 'html.parser') # page with links to all podcasts

topics = [  '/podcast-',
            '/salon2-',
            '/important-podcast',
            '/the-divine-feminine',
            '/mckenna-alchemy-the-world-today',
            '/lorenzo-on-the-joe-rogan-experience-podcast',
            '/confessions-of-an-ecstasy-advocate',
            '/developing-a-community-tea-house-model',
            '/leary-vs-liddy-1990-debate',
            '/ufos-angels-aliens-archetypes',
            '/221-mckenna-evolving-times',
            '/220-damer-evogrid-the-ultimate-nerd-project'  ]

for link in pot.find_all('a'):
    for t in topics:
        if t in link.get('href'):
            podcast_page = link.get('href')
            page = urlopen(podcast_page)
            cup = BeautifulSoup(page, 'html.parser') # page with podcast d/l link
            spoon = cup.find("div", {"class": "powerpress_player"})
            bite = spoon.find('a')
            file_url = bite.get('href')
            time.sleep(30) # be respectful and don't spam
            title = podcast_page.replace(SITE, "")[:-1]

            try:
                f = system("wget {}".format(file_url))

            except Exception as e:
                print e
