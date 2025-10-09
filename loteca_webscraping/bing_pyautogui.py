import pyautogui
import pyperclip
import time
import datetime
import pytz
import random

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

def ler_frase_aleatoria(arquivo="frases.txt"):
    """Lê uma frase aleatória de um arquivo .txt"""
    with open(arquivo, "r", encoding="utf-8") as f:
        frases = [linha.strip() for linha in f if linha.strip()]
    return random.choice(frases)

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
    pesquisar(repeticoes=30, delay=3)