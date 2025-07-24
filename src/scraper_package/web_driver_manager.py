from selenium import webdriver
from time import sleep
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException, NoSuchDriverException
from selenium.webdriver.chrome.options import Options
import traceback

class WebDriverManager:
    """
    Esta classe serve para gerenciar o ciclo de vida do Selenium WebDriver para o Chrome,
    responsável por inicializar, configurar e encerrar a instância do navegador.
    """
    def __init__(self, headless = False):
        """
        Inicializa o WebDriverManager.
        """
        self._headless = headless
        self._driver = None
    
    def _configure_options(self):
        """
        Configura e retorna o objeto ChromeOptions para a instância do WebDriver,
        define argumentos como headless, user-agent, tamanho da janela e outras otimizações
        para evitar detecção de bot.
        """
        options = Options()

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
        options.add_argument('window-size=1000,1000')

        if self._headless:
            options.add_argument('--headless')
            return options
        else:
            return options


    def start_driver(self) -> webdriver.Chrome:
        """
        Inicializa uma nova instância do navegador,
        se o driver já estiver ativo, retorna a instância existente.
        """
        if self._driver is None:
            try:
                options = self._configure_options()
                self._driver = webdriver.Chrome(options=options)
                
    
            except (SessionNotCreatedException, NoSuchDriverException) as e:
                print(f"ERRO CRÍTICO: Problema de compatibilidade ou driver não encontrado. {e}")
                self._driver = None 
                raise 

            except WebDriverException as e:
                print(f"Um erro do WebDriver ocorreu durante a inicialização. {e}")
                self._driver = None
                raise

            except FileNotFoundError as e:
                print(f"O arquivo do WebDriver não foi encontrado. {e}")
                self._driver = None
                raise

            except Exception as e:
                print(f"Um erro inesperado ocorreu durante a inicialização do WebDriver. {e}")
                self._driver = None
                raise
        
        return self._driver

    def get_driver(self) -> webdriver.Chrome:
        """
        Retorna a instância do navegador,
        Se o driver ainda não foi iniciado, ele é inicializado automaticamente.
        """
        if self._driver:
            return self._driver
        else:
            return self.start_driver()


    def close_driver(self):
        """
        Encerra a instância atual do navegador.
        """
        if(self._driver):
            self._driver.quit()
            self._driver = None
