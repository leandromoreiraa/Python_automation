
import pyautogui as auto #faz a automacao do mouse e teclado
import time #controla o tempo do nosso programa
import pyperclip as clip #permite copiar e colar com python

link = 'https://drive.google.com/drive/folders/1wRTFw0sUVBjRr4hW5U9LF7DjLixRyxym'# arquivos da aula
#passo 1 -entrar no sistema (link do drive, ou caminho)
auto.PAUSE = 2 #sempre que executar esperar 1 sgudo
auto.press('win') #abrir win
auto.write('chrome') #escrever chrome
auto.press('enter') #enter
#passo 2 - entrar na pasta aula 1
auto.click(x=343, y=50) # clicar no campo de escrever
auto.write(link) # escreve o link armazenado na avariavel
auto.press('enter') #enter
time.sleep(3) # segundos para carregar o conteudo da pagina
#passo 3 - fazer download da base de vendas
auto.click(x=1123, y=402) # clica no arquivo
auto.click(x=1396, y=189) # clica em opcoes
auto.click(x=1199, y=561) # clica em download
time.sleep(5)
auto.click(x=1583, y=14)
auto.alert('Tarefa Finalizada')
