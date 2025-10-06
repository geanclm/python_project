import pyautogui
import pyperclip
import time
import datetime
import pytz

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

def pesquisar(frase_base, repeticoes=3, delay=3):
    """
    Executa pesquisas no Edge usando CTRL+L para focar a barra de endereços.
    Usa colagem via área de transferência para preservar acentos.
    
    frase_base: texto inicial da pesquisa
    repeticoes: número de pesquisas adicionais
    delay: tempo de espera entre pesquisas
    """
    texto_base = f"{frase_base} {data_hoje()}"

    # Pesquisa inicial
    pyautogui.hotkey("ctrl", "l")  # foca a barra de endereços
    digitar_com_acentos(f"{texto_base} {agora()}")
    pyautogui.press("enter")
    time.sleep(delay)
    
    for i in range(repeticoes):
        pyautogui.hotkey("ctrl", "l")  # volta para a barra de endereços
        digitar_com_acentos(f"{texto_base} {agora()}")
        pyautogui.press("enter")
        time.sleep(delay + i)

if __name__ == "__main__":
    abrir_edge()    
    pesquisar('A influência da Inteligência Artificial no trabalho e estudo em', repeticoes=1, delay=3) 