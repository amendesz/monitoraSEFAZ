import logging
import time
import requests
from bs4 import BeautifulSoup

# Configuração de log
logging.basicConfig(filename='status_bolinhas.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# URL do site que contém as bolinhas
url = "http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=2.00"

# URL para enviar o GET/heartbeat
get_url = "https://uptime.betterstack.com/api/v1/heartbeat/XXXXXXXX"

# Função para verificar o status das bolinhas e enviar o GET/heartbeat
def verificar_status_e_enviar_get():
    try:
        # Faz a requisição GET à URL
        response = requests.get(url)
        response.raise_for_status()

        # Analisa o conteúdo da página com BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra todas as tags de imagem que representam as bolinhas
        bolinhas = soup.find_all("img", src=True)

        # Verifica o status de cada bolinha
        status = {}
        for bolinha in bolinhas:
            src = bolinha["src"]
            cor = src.split("/")[-1]  # Obtém o nome da bolinha
            status[src] = cor

        # Verifica se há bolinhas amarelas ou vermelhas
        if any("bola_amarela_P.png" in cor for cor in status.values()) or any("bola_vermelho_P.png" in cor for cor in status.values()):
            print("Pelo menos uma bolinha está amarela ou vermelha. O serviço está com problemas.")
        else:
            print("Todas as bolinhas estão verdes. O serviço está OK.")
            # Enviar o GET/heartbeat quando todas as bolinhas estiverem verdes
            try:
                response = requests.get(get_url)
                if response.status_code == 200:
                    print("GET/heartbeat enviado com sucesso.")
                else:
                    print(f"Erro ao enviar GET/heartbeat: Código de status {response.status_code}")
            except Exception as e:
                print(f"Erro ao enviar GET/heartbeat: {str(e)}")
    except Exception as e:
        print(f"Erro ao verificar o status das bolinhas: {str(e)}")

# Loop principal
while True:
    verificar_status_e_enviar_get()

    # Aguarda 10 segundos antes de verificar novamente
    time.sleep(10)
