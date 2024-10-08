# Usado para pressionar as teclas
import keyboard
# Usado para abrir o navegador
import selenium.webdriver as webdriver
# Usado para realizar comunicação com o arduino
import serial

def open_site(browser:str | None = 'chrome', url:str | None = 'https://www.onlinepianist.com/virtual-piano'):
    '''
    Abre um navegador no site especificado por meio dos parâmetros\n
    Parâmetros\n
    browser (str) :  indica o navegador que deseja abrir, podendo ser "chrome", "firefox", "edge" ou "safari"\n
    url (str) :  indica o endereço do site a ser aberto. Preferencialmente, ponha o "https://" no início da url por segurança
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
    '''
    Verifica se a tecla "key" está sendo pressionada analisando o termo na posição "note" na string "serial_data".
    Se a tecla do piano está sendo apertada, ele apertará a do teclado até que a do piano seja solta\n
    Parâmetros\n
    key (str) : indica a tecla do teclado a ser apertada pela função\n
    note (int) : indica a posição no "serial_data" correspondente a nota que será tocada\n
    serial_data (str) : indica a mensagem do serial, que é salva em uma variavel que recebe o valor da função read_terminal()
    '''
    if serial_data[note] == "1":
        keyboard.press(key)
    else:
        keyboard.release(key)

def connect_terminal(port:str, baudrate:int | None = 9600):
    '''
    Realiza a conexão com o arduino recebendo a porta e baudrate retornando a classe um objeto da classe Serial utilizado para interagir com o serial do arduino\n
    Parâmetros\n
    port (str) : indica a porta USB em que o arduino está ligado. Ex: 'COM6'\n
    baudrate (int) : taxa de atualização da porta, por padrão fica em 9600

    '''
    global arduino
    arduino = serial.Serial(port, baudrate)
    return arduino

def read_terminal(terminal:serial.Serial):
    '''
    Realiza a leitura do terminal e retorna esse valor tratado, além de ser escrito no terminal \n
    Parâmetros\n
    terminal (Serial) : indica o terminal que será lido. Variável que recebe o valor da função connect_terminal()
    '''
    data = terminal.readline().decode().strip()
    print(data)
    return data

