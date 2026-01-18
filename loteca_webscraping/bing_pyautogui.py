import pyautogui
import pyperclip
import time
import datetime
import pytz
import random
import sys

from pathlib import Path

# Opção 1 de janela windows após a conclusão do script:
# import tkinter as tk
# from tkinter import messagebox

# Opção 2 de janela windows após a conclusão do script:
import ctypes

# ---
# by geanclm on 25/12/2025 at 7h30
# Objetivo: Automatizar pesquisas no Bing via Microsoft Edge
# Procedimento para arquivo executável com PyInstaller:
# 1 - !pip install pyinstaller
# 2 - from pathlib import Path
# 3 - COMANDO PRINCIPAL: pyinstaller --onedir --noconsole --add-data "frases.txt;." --name "BingPyAutoGUI" bing_pyautogui.py
# 4 - Para --onefile, envie apenas o .exe gerado na pasta dist
# 5 - Arquivo gerado em C:\Users\geanc\OneDrive\Documentos\GitHub\python_project\loteca_webscraping\dist\BingPyAutoGUI\BingPyAutoGUI.exe
# 6 - Salvar atalho no iniciar do windows para rápido acesso
# ---

# Configurações globais
pyautogui.PAUSE = 0.3
fuso_brasilia = pytz.timezone("America/Sao_Paulo")

def agora():
    """Retorna hora atual formatada."""
    return datetime.datetime.now(fuso_brasilia).strftime("%H:%M:%S.%f")[:-4]

def data_hoje():
    """Retorna data de hoje formatada."""
    return datetime.datetime.now(fuso_brasilia).strftime("%Y-%m-%d")

def abrir_edge():
    """Abre o Microsoft Edge pelo menu iniciar."""
    
    # pyautogui.press("win")
    # pyautogui.write("Microsoft Edge")
    # pyautogui.press("enter")
    
    pyautogui.hotkey("shift", "win", "f")
    pyperclip.copy("btc hoje")
    pyautogui.hotkey("ctrl", "v")        
    pyautogui.press("enter")
        
    time.sleep(2)

def digitar_com_acentos(texto):
    """Copia o texto para a área de transferência e cola no campo ativo."""
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")

# --- Adaptação para funcionar em executável ---
# def ler_frase_aleatoria(arquivo="frases.txt"):
#     """Lê uma frase aleatória de um arquivo .txt"""
#     with open(arquivo, "r", encoding="utf-8") as f:
#         frases = [linha.strip() for linha in f if linha.strip()]
#     return random.choice(frases)
def resource_path(relative_path: str) -> Path:
    """Retorna o caminho correto do recurso, mesmo dentro do executável."""
    base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return base_path / relative_path

def ler_frase_aleatoria(arquivo="frases.txt"):
    """Lê uma frase aleatória de um arquivo .txt"""
    frases_path = resource_path(arquivo)
    with open(frases_path, "r", encoding="utf-8") as f:
        frases = [linha.strip() for linha in f if linha.strip()]
    return random.choice(frases)
# --- Adaptação para funcionar em executável ---

def pesquisar(pesquisas=3, delay=3, arquivo="frases.txt"):
    """
    Executa pesquisas no Edge usando CTRL+L para focar a barra de endereços.
    A cada repetição escolhe uma frase diferente do arquivo.
    """
    for i in range(pesquisas + 1):
        frase_base = ler_frase_aleatoria(arquivo)  # nova frase a cada loop
        texto_base = f"{frase_base} {data_hoje()} {agora()}"
        pyautogui.hotkey("ctrl", "l")  # foca a barra de endereços
        digitar_com_acentos(texto_base)
        pyautogui.press("enter")
        time.sleep(delay + i)

if __name__ == "__main__":
    abrir_edge()
    
    pesquisas = 30  # Defina o número de pesquisas desejadas
    delay = 1     # Defina o delay entre pesquisas
    pesquisar(pesquisas=pesquisas, delay=delay)    

# Opção 1 de janela windows após a conclusão do script:
# root = tk.Tk()
# root.withdraw()
# messagebox.showinfo("Tarefa concluída", "A automação foi finalizada com sucesso!")

# Opção 2 de janela windows após a conclusão do script:
ctypes.windll.user32.MessageBoxW(0, f"---\nTotal de pesquisas: {pesquisas+1}\n---", f"Tarefa concluída",1)