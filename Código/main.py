from Src.reclame_aqui_scraper import ReclameAquiScraper
from bs4 import BeautifulSoup

Scraper = ReclameAquiScraper()
Scraper.get_best_and_worst_links("Casa de Aposta")
Scraper.get_best_companies_info()
Scraper.get_worst_companies_info()
#site = BeautifulSoup(, 'html.parser')
#noticias = site.find('button', attrs={'class': 'svelte-13kut5s'})
#print(noticias.prettify())