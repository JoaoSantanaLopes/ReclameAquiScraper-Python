from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import traceback
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
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

    def navigate_to_url(self, url: str, timeout: int = 15) -> bool:
        """
        Navega para uma URL especificada pelo usuário.
        """
        try:
            self._driver.get(url)
            
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            return True
        except TimeoutException: 
            print(f"Tempo esgotado  ao carregar a página: {url}")
            traceback.print_exc()
            return False
        except WebDriverException as e:
            print(f"Erro do WebDriver ao navegar para {url}. {e}")
            traceback.print_exc()
            return False
        except Exception as e:
            print(f"Um erro inesperado ocorreu ao navegar para {url}. {e}")
            traceback.print_exc()
            return False

    def get_current_page_source(self) -> str:
        """
        Retorna o código fonte HTML da página atualmente carregada no navegador.
        """
        try:
            html_content = self._driver.page_source
            return html_content
        except WebDriverException as e:
            print(f"Erro do WebDriver ao obter o código fonte da página. {e}")
            traceback.print_exc()
            return ""
        except Exception as e:
            print(f"Um erro inesperado ocorreu ao obter o código fonte da página. {e}")
            traceback.print_exc()
            return ""

    def find_elements(self, by: By, value: str, timeout: int = 10) -> list[WebElement]:
        """
        Localiza e retorna uma lista de elementos web na página que possuem o valor especificado.
        """
        try:
            elements = WebDriverWait(self._driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        
        except TimeoutException: 
            print(f"AVISO: Nenhum elemento encontrado após {timeout}s por  '{value}'.")
            traceback.print_exc()
            return []
        except WebDriverException as e:
            print(f"Erro do WebDriver ao procurar múltiplos elementos. {e}")
            traceback.print_exc()
            return []
        except Exception as e:
            print(f"Um erro inesperado ocorreu ao procurar múltiplos elementos. {e}")
            traceback.print_exc()
            return []

    def find_element(self, by: By, value: str, timeout: int = 10): 
        """
        Localiza e retorna um elemento web na página, procurando ele pelo valor espeficado.
        """
        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except TimeoutException: 
            print(f"Elemento não encontrado ou não visível após {timeout}s")
            traceback.print_exc()
            return None
        except WebDriverException as e:
            print(f"Erro do WebDriver ao procurar elemento. {e}") 
            traceback.print_exc() 
            return None
        except Exception as e:
            print(f"ERRO: Um erro inesperado ocorreu ao procurar elemento. {e}") 
            traceback.print_exc() 
            return None

    def click_element(self, by: By, value: str, timeout: int = 10, jsClick=False) -> bool: 
        """
        Clica em um elemento na página, esperando até que ele esteja clicável.
        """
        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            
            if jsClick:
                self._driver.execute_script("arguments[0].click();", element)
            else:
                self._driver.execute_script(f"window.scrollBy({800}, {800});")
                element.click()
            
            return True
        except TimeoutException: 
            print(f"Não foi possível clicar. Elemento não clicável ou não encontrado após {timeout}s") 
            traceback.print_exc()
            return False
        except WebDriverException as e:
            print(f"Erro do WebDriver ao tentar clicar no elemento por: '{value}'. Detalhes: {e}") 
            traceback.print_exc() 
            return False
        except Exception as e:
            print(f"Um erro inesperado ocorreu ao tentar clicar no elemento. {e}") 
            traceback.print_exc() 
            return False
        
        