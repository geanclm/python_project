# Loteca Webscraping
# by geanclm on 28/01/2024

# Objetivo do script: capturar todos os números do concurso da loteca respectivas datas de sorteio

# importar bibliotecas necessárias
import pyautogui
import time
import pyperclip
import pandas as pd
import re

# Etapas da automação:
# 1 - entrar no site
link = 'https://loterias.caixa.gov.br/Paginas/Loteca.aspx'
pyautogui.PAUSE = 0.3
pyautogui.press('win')
pyautogui.write('Microsoft Edge')
time.sleep(1)
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=2861, y=605)
# pyautogui.click(x=3506, y=858)
# pyautogui.click(x=3506, y=858)

pyautogui.scroll(-250)

# 2 - digitar o número do concurso no campo de busca
# 3 - copiar o número do concurso e data respectiva
# 4 - salvar dados em dicionário
# 5 - salvar dicionário em arquivo

resultados = []

for i in range(10):    
    pyautogui.doubleClick(x=3130, y=785)
    time.sleep(1)
    pyautogui.write(str(i+1))
    pyautogui.press('enter')
    # time.sleep(3)    
    time.sleep(1)    
    pyautogui.tripleClick(x=2588, y=746)
    pyautogui.hotkey('ctrl', 'c')    
    resultados.append(pyperclip.paste())    

# salvar dados em dataframe
# Função para extrair o número do concurso e a data usando expressões regulares
def extrair_info(resultado):
    match = re.search(r'Concurso (\d+).*\((\d{2}/\d{2}/\d{4})\)', resultado)
    if match:
        return match.group(1), match.group(2)
    return None, None

dados = [extrair_info(resultado) for resultado in resultados]
df = pd.DataFrame(dados, columns=['concurso', 'data'])

df.to_csv('resultados.csv', index=False)