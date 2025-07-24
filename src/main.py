from scraper_package.reclame_aqui_scraper import ReclameAquiScraper
from bs4 import BeautifulSoup
from scraper_package.data_processor import DataProcessor

Scraper = ReclameAquiScraper()

if Scraper.get_best_and_worst_links("Casa de Aposta"):
    melhores = Scraper.get_best_companies_info()
    piores = Scraper.get_worst_companies_info()
    melhores_e_piores = melhores + piores
    data_processor = DataProcessor()
    data_processor.export_to_excel(melhores_e_piores, 'melhores_e_piores.xlsx')
    print("____")


