# testes de velociade de internet com ping detalhado e informações de rede
# by geanclm on 17/4/2026 at 11h35

# | Provedor   | DNS Primário 		            | Foco principal           |
# | ---------- | ------------		            | ----------------         |
# | Google     | 8.8.8.8	8.8.4.4      	    | Performance              |
# | Cloudflare | 1.1.1.1	1.0.0.1		        | Privacidade + velocidade |
# | Quad9      | 9.9.9.9	149.112.112.112	    | Segurança                |

import speedtest
import datetime
import subprocess
import requests
import re

# ==============================
# 🌐 IP Público
# ==============================
def obter_ip_publico():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except Exception as e:
        return f"Erro: {e}"


# ==============================
# 📡 Gateway (roteador local)
# ==============================
def obter_gateway():
    try:
        resultado = subprocess.check_output(
            "ipconfig",
            shell=True
        ).decode("utf-8", errors="ignore")

        linhas = resultado.splitlines()

        for i, linha in enumerate(linhas):
            if "Gateway Padrão" in linha:
                # tenta pegar IPv4 na mesma linha
                match = re.search(r'(\d+\.\d+\.\d+\.\d+)', linha)
                if match:
                    return match.group(1)

                # tenta na linha seguinte (caso esteja abaixo)
                if i + 1 < len(linhas):
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', linhas[i + 1])
                    if match:
                        return match.group(1)

        return "Não encontrado"

    except Exception as e:
        return f"Erro: {e}"


# ==============================
# 📊 Ping detalhado
# ==============================
def testar_ping(host="8.8.8.8"):
    try:
        resultado = subprocess.check_output(
            ["ping", "-n", "5", host],
            stderr=subprocess.STDOUT
        ).decode("cp1252", errors="ignore")

        return resultado

    except subprocess.CalledProcessError as e:
        return e.output.decode("cp1252", errors="ignore")

    except Exception as e:
        return f"Erro: {e}"


# ==============================
# 📈 Extrair métricas do ping
# ==============================
def extrair_metricas_ping(output):
    perda = re.search(r'(\d+)% de perda', output)
    tempo = re.search(r'Média = (\d+)', output)

    return {
        "perda": perda.group(1) + "%" if perda else "N/A",
        "latencia_media": tempo.group(1) + " ms" if tempo else "N/A"
    }


# ==============================
# 🚀 Teste principal
# ==============================
def testar_internet():
    try:
        s = speedtest.Speedtest()
        s.get_best_server()

        download = s.download() / 1_000_000
        upload = s.upload() / 1_000_000
        ping = s.results.ping
        servidor = s.get_best_server()        

        agora = datetime.datetime.now()
        ip_publico = obter_ip_publico()
        gateway = obter_gateway()
        ping_detalhado = testar_ping()
        metricas_ping = extrair_metricas_ping(ping_detalhado)

        print("=" * 60)
        print(f"📅 Data: {agora}")
        print(f"🌐 IP Público: {ip_publico}")
        print(f"📡 Gateway (Roteador): {gateway}")
        print(f"🛰️ Servidor: {servidor['host']} ({servidor['country']})")
        print("-" * 60)
        print(f"📶 Ping médio (Speedtest): {ping:.2f} ms")
        print(f"📊 Ping médio (Sistema): {metricas_ping['latencia_media']}")
        print(f"📉 Perda de pacotes: {metricas_ping['perda']}")
        print(f"⬇️ Download: {download:.2f} Mbps")
        print(f"⬆️ Upload: {upload:.2f} Mbps")
        print("-" * 60)
        print("📋 Ping detalhado:")
        print(ping_detalhado)
        print("=" * 60)

    except Exception as e:
        print(f"❌ Erro geral no teste: {e}")

# ==============================
# ▶️ Execução
# ==============================
if __name__ == "__main__":
    testar_internet()