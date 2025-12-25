import pyautogui
import pyperclip
import time
import datetime
import pytz
import random
import sys

from pathlib import Path

# ---
# by geanclm on 25/12/2025 at 7h30
# Objetivo: Automatizar pesquisas no Bing via Microsoft Edge
# Procedimento para arquivo executável com PyInstaller:
# 1 - !pip install pyinstaller
# 2 - from pathlib import Path
# 3 - COMANDO PRINCIPAL: pyinstaller --onedir --noconsole --add-data "frases.txt;." --name "BingPyAutoGUI" bing_pyautogui.py
# 4 - Para --onefile, envie apenas o .exe gerado na pasta dist
# 5 - Salvar atalho no iniciar do windows para rápido acesso
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
    pyautogui.press("win")
    pyautogui.write("Microsoft Edge")
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

def pesquisar(repeticoes=3, delay=3, arquivo="frases.txt"):
    """
    Executa pesquisas no Edge usando CTRL+L para focar a barra de endereços.
    A cada repetição escolhe uma frase diferente do arquivo.
    """
    for i in range(repeticoes + 1):
        frase_base = ler_frase_aleatoria(arquivo)  # nova frase a cada loop
        texto_base = f"{frase_base} {data_hoje()} {agora()}"

        pyautogui.hotkey("ctrl", "l")  # foca a barra de endereços
        digitar_com_acentos(texto_base)
        pyautogui.press("enter")
        time.sleep(delay + i)

if __name__ == "__main__":
    abrir_edge()
    pesquisar(repeticoes=60, delay=3)