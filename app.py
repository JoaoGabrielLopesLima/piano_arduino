# Importa o módulo das funções
import functions


# Realiza a conexão com o arduino
connection = functions.connect_terminal('COM6', 9600)


# Abre o site que será utilizado
functions.open_site()

# Cria o loop de verificações que pode ser encerrado clicando no terminal e usando "Ctrl + C"
while True:
    try:
        # Realiza a leitura do terminal do arduino programado
        data = functions.read_terminal(connection)
        # Mostrar a mensagem do terminal do arduino no terminal da IDE para verificação
        print(data)

        # Verificar e clicar ou soltar cada tecla
        functions.click_release_key('q', 0, data)
        functions.click_release_key('w', 1, data)
        functions.click_release_key('e', 2, data)
        functions.click_release_key('r', 3, data)
        functions.click_release_key('t', 4, data)
        functions.click_release_key('y', 5, data)
        functions.click_release_key('u', 6, data)
        functions.click_release_key('i', 7, data)
        
    except Exception:
        pass
