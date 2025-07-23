from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import traceback
from selenium.webdriver.remote.webelement import WebElement

class Page:
    """
    Classe base para representar e interagir com uma página web usando Selenium.
    Encapsula operações comuns de navegação e obtenção de conteúdo da página.
    """
    def __init__(self, driver: webdriver.Chrome):
        """
        Inicializa a Page com uma instância do Selenium WebDriver.
        """
        self._driver = driver
        print("INFO: Classe Page inicializada com o WebDriver.")

    def navigate_to_url(self, url: str, timeout: int = 15) -> bool:
        """
        Navega para uma URL especificada pelo usuário.
        """
        print(f"INFO: Navegando para: {url}")
        try:
            self._driver.get(url)
            
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print(f"INFO: Navegação para {url} concluída e página carregada (espera de {timeout}s).")
            return True
        except TimeoutException: 
            print(f"ERRO: Tempo esgotado ({timeout}s) ao carregar a página: {url}")
            traceback.print_exc()
            return False
        except WebDriverException as e:
            print(f"ERRO: Erro do WebDriver ao navegar para {url}. Detalhes: {e}")
            traceback.print_exc()
            return False
        except Exception as e:
            print(f"ERRO: Um erro inesperado ocorreu ao navegar para {url}. Detalhes: {e}")
            traceback.print_exc()
            return False

    def get_current_page_source(self) -> str:
        """
        Retorna o código fonte HTML da página atualmente carregada no navegador.
        """
        print("INFO: Obtendo o código fonte HTML da página atual.")
        try:
            html_content = self._driver.page_source
            return html_content
        except WebDriverException as e:
            print(f"ERRO: Erro do WebDriver ao obter o código fonte da página. Detalhes: {e}")
            traceback.print_exc()
            return ""
        except Exception as e:
            print(f"ERRO: Um erro inesperado ocorreu ao obter o código fonte da página. Detalhes: {e}")
            traceback.print_exc()
            return ""

    def find_elements(self, by: By, value: str, timeout: int = 10) -> list[WebElement]:
        """
        Localiza e retorna uma lista de elementos web na página que possuem o valor especificado.
        """
        print(f"INFO: Procurando MÚLTIPLOS elementos por '{value}' (timeout: {timeout}s)...")
        try:
            # Espera até que pelo menos um elemento esteja presente no DOM
            # Note que presence_of_all_elements_located retornará uma lista vazia se nenhum for encontrado no timeout
            elements = WebDriverWait(self._driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            print(f"INFO: Encontrados {len(elements)} elementos por  '{value}'.")
            return elements
        except TimeoutException: # Captura a exceção de timeout de WebDriverWait
            print(f"AVISO: Nenhum elemento encontrado após {timeout}s por  '{value}'.")
            traceback.print_exc()
            return []
        except WebDriverException as e:
            print(f"ERRO: Erro do WebDriver ao procurar múltiplos elementos por  '{value}'. Detalhes: {e}")
            traceback.print_exc()
            return []
        except Exception as e:
            print(f"ERRO: Um erro inesperado ocorreu ao procurar múltiplos elementos por '{value}'. Detalhes: {e}")
            traceback.print_exc()
            return []

    def find_element(self, by: By, value: str, timeout: int = 10): # 
        """
        Localiza e retorna um elemento web na página, procurando ele pelo valor espeficado.
        """
        print(f"INFO: Procurando elemento por: '{value}' (timeout: {timeout}s)...") 
        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            print(f"INFO: Elemento encontrado por: '{value}'.") 
            return element
        except TimeoutException: 
            print(f"AVISO: Elemento não encontrado ou não visível após {timeout}s por: '{value}'.")
            traceback.print_exc()
            return None
        except WebDriverException as e:
            print(f"ERRO: Erro do WebDriver ao procurar elemento por: '{value}'. Detalhes: {e}") 
            traceback.print_exc() 
            return None
        except Exception as e:
            print(f"ERRO: Um erro inesperado ocorreu ao procurar elemento por: '{value}'. Detalhes: {e}") 
            traceback.print_exc() 
            return None

    def click_element(self, by: By, value: str, timeout: int = 10) -> bool: 
        """
        Clica em um elemento na página, esperando até que ele esteja clicável.
        """
        print(f"INFO: Tentando clicar no elemento por: '{value}' (timeout: {timeout}s)...") 

        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            print(f"SUCESSO: Clicado no elemento por: '{value}'.") 
            return True
        except TimeoutException: 
            print(f"AVISO: Não foi possível clicar. Elemento não clicável ou não encontrado após {timeout}s por: '{value}'.") # CORRIGIDO: by.value
            traceback.print_exc()
            return False
        except WebDriverException as e:
            print(f"ERRO: Erro do WebDriver ao tentar clicar no elemento por: '{value}'. Detalhes: {e}") # CORRIGIDO: by.value
            traceback.print_exc() 
            return False
        except Exception as e:
            print(f"ERRO: Um erro inesperado ocorreu ao tentar clicar no elemento por: '{value}'. Detalhes: {e}") 
            traceback.print_exc() 
            return False
        
        