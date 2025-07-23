from selenium import webdriver
from time import sleep
import traceback

navegador = webdriver.Chrome()

navegador.get("https://reclameaqui.com")

a = input("aa")

navegador.quit()