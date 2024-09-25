#!/bin/python3

# Importando as funções que iremos utilizar:
# - Função get do packote requests que faz chamadas HTTP GET
from requests import get
# - Função loads do pacote json que converte string em estrutura de dados (list ou dict)
from json import loads

# Constantes com as rotas das api's
api_ip = "https://api.ipify.org?format=json"
api_localizacao = "https://ipinfo.io/{}/geo"
api_tempo = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=temperature_2m,wind_speed_10m&timezone=America%2FSao_Paulo"

# Função obter_ip: retorna o IP público
def obter_ip():
    resposta = get(api_ip)
    if resposta.ok:
        obj_ip = loads(resposta.text) #Resposta {"ip":"45.191.204.161"}
        ip = obj_ip["ip"]
        return  ip
    return ""

def obter_localizacao(ip):
    if ip == "":
        return
    resposta = get(api_localizacao.format(ip))
    #Caso não tenha sucesso retorna None (sem valor) e sairá da função.
    if not resposta.ok: 
        return None
    # convert resposta string em um dicionário
    obj_localizacao = loads(resposta.text) # Resposta {...,"loc": "-16.6786,-49.2539",...}
    # pega o valor da chave loc
    localizacao = obj_localizacao["loc"] 
    # pega o valor de latitude e longitude. 
    # O split transforma a string em list separando por , e
    # é feita um destruturação da lista carregando as variáveis.
    [latitude, longitude] = localizacao.split(",") 
    # criação de um dicionário para retorno
    coordenadas = {
        "cidade": obj_localizacao["city"],
        "estado": obj_localizacao["region"],
        "latitude": latitude,
        "longitude": longitude
    }
    return coordenadas

def obter_tempo(latitude, longitude):
    return None # TODO: Implemente a funcionalidade de obter tempo

def mostrar_tempo(localizacao, tempo):
    print("+-----------------------+")
    print("|     T  E  M  P  O     |")
    print("+-----------------------+")
    print("| Em {} - {}:".format(localizacao["cidade"],localizacao["estado"]))
    print("| Dia:         {}".format(tempo["data"]))
    print("| Horas:       {}".format(tempo["hora"]))
    print("| Temperatura: {}".format(tempo["temperatura"]))
    print("| Vento:       {}".format(tempo["vento"]))
    print("+-----------------------+")

# Aplicação
def iniciar_app():
    print("Carregando...")
    # Pegar o meu ip público
    ip = obter_ip()
    #TODO: Pegar a localização pelo ip

    #TODO: Pegar a informação do tempo pela localização
    
    
# Validação para executar a função iniciar_app somente
# se for executado via python meutempo.py, caso
# seja importado, import meutempo, não será
# executada. 
if __name__ == "__main__":
    iniciar_app()

