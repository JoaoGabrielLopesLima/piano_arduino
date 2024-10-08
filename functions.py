import libs.keyboard as keyboard
from selenium import webdriver

def open_site(browser:str = 'chrome', url:str='https://www.google.com'):
    driver = browser.lower().strip()
    if driver == 'chrome':
        driver = webdriver.Chrome()
        driver.get(url)
    elif driver == 'firefox':
        driver = webdriver.Firefox()
        driver.get(url)
    elif driver == 'edge':
        driver = webdriver.Edge()
        driver.get(url)
    elif driver == 'safari':
        driver = webdriver.Safari()
        driver.get(url)
    else:
        raise ValueError("Navegador não suportado! escolha entre Chrome, Microsoft Edge, Safari ou FireFox")


