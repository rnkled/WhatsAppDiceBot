from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from roll import roll


def envia_msg(msg):
    """ Envia uma mensagem para a conversa aberta """
    try:

        # Finds the Text Box
        # Seleciona a caixa de mensagem

        inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'

        caixa_de_mensagem = driver.find_element_by_xpath(inp_xpath)

        # Writes the Message
        # Digita a mensagem
        caixa_de_mensagem.send_keys(msg)

        # Finds the Send Button
        # Seleciona botão enviar
        botao_enviar = driver.find_element_by_class_name("_1U1xa")

        # Sends the Message
        # Envia msg
        botao_enviar.click()
    except Exception as e:
        print("Erro ao enviar msg", e)


def ultima_msg():
    """ Captura a ultima mensagem da conversa """
    try:
        post = driver.find_elements_by_class_name("_274yw")
        ultimo = len(post) - 1

        # Get the Text of the Last Message
        # O texto da ultima mensagem
        texto = post[ultimo].find_element_by_css_selector(
            "span.selectable-text").text
        return texto
    except Exception as e:
        print(e)
        print("Erro ao ler msg, tentando novamente!")


# Set Here your Chromedriver path.
# Ajuste aqui a localização do seu Chromedriver.
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.get("https://web.whatsapp.com/")

assert "WhatsApp" in driver.title

#print("Connect to You WhatsApp Account")
print("Faça Login Por Favor")
while True:
    try:
        element = driver.find_element_by_class_name("landing-headerTitle")
    except:
        break
sleep(5)

#print("Now, open the Group to be monitored.")
print("Agora, Abra o Grupo que deseja Monitorar")
#input("Are you Ready?")
input("Você já Está Pronto?")

while True:
    msg = ultima_msg()
    if msg[0] == "/":
        envia_msg(roll(msg))
