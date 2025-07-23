from selenium import webdriver
from time import sleep
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException, NoSuchDriverException
from selenium.webdriver.chrome.options import Options
import traceback

class WebDriverManager:

    def __init__(self, headless = False):
        self._headless = headless
        self._driver = None
    
    def _configure_options(self):
        
        options = Options()

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
        options.add_argument('window-size=1000,800')

        if self._headless:
            options.add_argument('--headless')
            return options
        else:
            return options


    def start_driver(self) -> webdriver.Chrome:
        if self._driver is None:
            try:
                options = self._configure_options()
                self._driver = webdriver.Chrome(options=options)
                
    
            except (SessionNotCreatedException, NoSuchDriverException) as e:
                print(f"ERRO CRÍTICO: Problema de compatibilidade ou driver não encontrado/configurado. Detalhes: {e}")
                print("Por favor, verifique:")
                print("  1. Se a versão do chromedriver é compatível com a versão do seu Google Chrome.")
                print("  2. Se o chromedriver está no PATH do sistema OU o caminho está correto no driver_path.")
                self._driver = None 
                raise 

            except WebDriverException as e:
                print(f"ERRO: Um erro do WebDriver ocorreu durante a inicialização. Detalhes: {e}")
                self._driver = None
                raise

            except FileNotFoundError as e:
                print(f"ERRO: O arquivo do WebDriver não foi encontrado. Detalhes: {e}")
                self._driver = None
                raise

            except Exception as e:
                print(f"ERRO: Um erro inesperado ocorreu durante a inicialização do WebDriver: {e}")
                self._driver = None
                raise
        
        return self._driver

    def get_driver(self) -> webdriver.Chrome:
        if self._driver:
            return self._driver
        else:
            return self.start_driver()


    def close_driver(self):
        if(self._driver):
            self._driver.quit()
            self._driver = None
