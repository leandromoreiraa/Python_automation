import pyautogui as auto #faz a automacao do mouse e teclado
import time #controla o tempo do nosso programa
import pyperclip as clip #permite copiar e colar com python
from arquivo import faturamento, qtd_produtos

link = 'https://mail.google.com'
email = 'leandromercesmoreiraa@gmail.com'
texto = f"""

Faturamento: {faturamento}
Quantidade de Produtos: {qtd_produtos}

"""
assunto = """
Relatório de Faturamento
"""


#passo 5 - entrar no meu email
auto.PAUSE = 2
auto.press('win')
auto.write('chrome')
auto.press('enter')
auto.click(x=325, y=58)
auto.write(link)
auto.press('enter')
time.sleep(4)

#passo 6 - criar o email
auto.click(x=73, y=206)
auto.write(email)
auto.press('tab')
auto.press('tab')
clip.copy(assunto)
auto.hotkey('ctrl', 'v')
auto.press('tab')
clip.copy(texto)
auto.hotkey('ctrl', 'v')

#passo 7 - enviar o email
auto.click(x=996, y=830)
time.sleep(2)
auto.alert('Tarefa Finalizada.')

