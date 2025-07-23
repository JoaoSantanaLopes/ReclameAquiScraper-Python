
from bs4 import BeautifulSoup
from .web_driver_manager import WebDriverManager
from .page import Page 
from selenium.webdriver.common.by import By
import traceback
from time import sleep

class ReclameAquiScraper:
    """
    Orquestra o processo de scraping de reclamações de empresas no Reclame Aqui.
    """
    BASE_URL = "https://www.reclameaqui.com.br/" 

    def __init__(self, headless: bool = False):
        self._driver_manager = WebDriverManager(headless=headless)
        self._page_handler = Page(self._driver_manager.get_driver())
        self._best_companies_links = []
        self._worst_companies_links = []
    

    def get_best_and_worst_links(self, categoria : str):
        """
        Navega para a URL base e clica no link/botão 'Best Bets' (ou similar).
        """
        print("INFO: Tentando navegar e clicar no link 'Best Bets'...")
        
        # 1. Navegar para a URL base
        if not self._page_handler.navigate_to_url(self.BASE_URL):
            print("Falha ao navegar para a URL base para clicar no link.")
            return False
        try:
            if not self._page_handler.click_element(By.XPATH, "//input[contains(@placeholder, 'busque uma categoria')]"):
                print("Não foi possível clicar no input para escolher as empresas.")
                return False
            sleep(2)
            if not self._page_handler.click_element(By.XPATH, f"//*[contains(text(), '{categoria}')]"):
                print("Não foi possível clicar no botão Casa de Aposta.")
                return False
            
            melhores = self._page_handler.find_elements(By.ID, 'home_ranking_segmento_card_empresa')
            for melhor in melhores:
                self._best_companies_links.append(melhor.get_attribute('href'))
                print(self._best_companies_links)

            if not self._page_handler.click_element(By.CLASS_NAME, "svelte-1n79oku"):
                print("Não foi possível clicar no botão piores.")
                return False
            
            piores = self._page_handler.find_elements(By.ID, 'home_ranking_segmento_card_empresa')
            for pior in piores:
                self._worst_companies_links.append(pior.get_attribute('href'))
                print(self._worst_companies_links)

        except Exception as e:
            print(f"ERRO: Um erro inesperado ocorreu: {e}")
            traceback.print_exc()
            return False

    def get_best_companies_info(self) -> list[list[str]]: 
            
            infos = []

            for link in self._best_companies_links:
                self._driver_manager.close_driver()
                self._page_handler._driver = self._driver_manager.start_driver()
                self._page_handler.navigate_to_url(link)
                html = self._page_handler.get_current_page_source()
                infos.append(self._extract_info(BeautifulSoup(html, 'html.parser')))
 
            return infos
    
    def get_worst_companies_info(self) -> list[list[str]]: 
            
            infos = []

            for link in self._worst_companies_links:
                self._driver_manager.close_driver()
                self._page_handler._driver = self._driver_manager.start_driver()
                self._page_handler.navigate_to_url(link)
                html = self._page_handler.get_current_page_source()
                infos.append(self._extract_info(BeautifulSoup(html, 'html.parser')))
 
            return infos
    
    def _extract_info(self, html: BeautifulSoup) -> list[str]:
        infos = []
        nome = html.find('h2', attrs={'class': 'hero-font-semibold hero-text-[24px] max-md:hero-text-[18px] hero-text-[#191B1A] hero-text-ellipsis hero-overflow-hidden hero-m-0 hero-line-clamp-2'})
        nota = html.find('b', attrs={'class': 'go3621686408'})

        span = html.findAll('span', attrs={'class': "go2549335548"})
        respostas = span[1].find('strong')


        texto_nota = nota.text
        if texto_nota == '':
            texto_nota = '0/10.'
        
        print(nome.text)
        print(texto_nota)
        print(respostas.text)

