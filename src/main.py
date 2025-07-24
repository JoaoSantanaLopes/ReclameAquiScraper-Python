from scraper_package.reclame_aqui_scraper import ReclameAquiScraper
from scraper_package.data_processor import DataProcessor
import traceback

Scraper = ReclameAquiScraper()
try:
    if Scraper.get_best_and_worst_links("Casa de Aposta"):

        melhores = Scraper.get_best_companies_info()
        piores = Scraper.get_worst_companies_info()
        melhores_e_piores = melhores + piores
        data_processor = DataProcessor()

        if data_processor.export_to_excel(melhores_e_piores, 'melhores_e_piores.xlsx', "planilhas"):
            print("informações extraídas com sucesso!")

except Exception as e:
            print(f"Um erro inesperado ocorreu. {e}")
            traceback.print_exc()
            
            