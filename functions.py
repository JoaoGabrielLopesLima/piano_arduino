import keyboard
import selenium.webdriver as webdriver
import serial

def open_site(browser:str | None = 'chrome', url:str | None = 'https://www.onlinepianist.com/virtual-piano'):
    '''
    Abre um navegador no site especificado por meio dos parâmetros
    ______________________
    Parâmetros:\n
    browser (str):  indica o navegador que deseja abrir, podendo ser "chrome", "firefox", "edge" ou "safari"\n
    url (str):  indica o endereço do site a ser aberto. Preferencialmente, ponha o "https://" no início da url por segurança
    '''
    global driver
    driver = browser.lower().strip()
    if driver == 'chrome':
        driver = webdriver.Chrome(keep_alive=True)
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
        raise ValueError("Navegador não suportado! escolha entre Chrome, Edge, Safari ou FireFox")


def click_release_key(key:str, note:int, serial_data:str):
    if serial_data[note] == "1":
        keyboard.press(key)
    else:
        keyboard.release(key)

def connect_terminal(port:str, baudrate:int):
    global arduino
    arduino = serial.Serial(port, baudrate)
    return arduino

def read_terminal(terminal):
    data = terminal.readline().decode().strip()
    return data

