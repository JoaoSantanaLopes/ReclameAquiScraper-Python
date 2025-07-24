
# Reclame Aqui Web Scraper

Este projeto é um web scraper em Python para coletar informações das 3 empresas com as melhores e as 3 com as piores avaliações de reputação no Reclame Aqui, de alguma categoria específica escolhida, para posteriormente, exportar essas informações para uma planilha do Excel, utilizando as bibliotecas selenium, pandas e beautifulSoup.

## Requisitos

* **Python 3.9+**
* **Google Chrome Browser**
* **Chrome WebDriver** 

## Instalação e Uso

1.  **Clone o repositório para sua máquina:**
    ```bash
    git clone https://github.com/JoaoSantanaLopes/ReclameAquiScraper-Python.git
    ```

2.  **abra um terminal na raiz do projeto e instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o scraper:**
    Abra um terminal na pasta "src" e rode o comando.
    ```bash
    python main.py
    ```

##  Saída

O scraper gerará um arquivo Excel (`.xlsx`) na pasta "planilhas" com as informações extraídas das empresas.
