import requests
import json

URL_API = "http://localhost:8080"

def criarPersonagem(personagemDtoJson, campanhaId):
    url = f"{URL_API}/personagens/criar"
    params = {"campanhaId": campanhaId}
    headers = {"Content-Type": "application/json"}      
    
    response = requests.post(url, json=personagemDtoJson, params=params, headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Erro ao criar personagem: {response.status_code} {response.text}")
    
def listarPersonagens(campanhaId = None, campanhaNome = None):
    url = f"{URL_API}/personagens/listar"
    if campanhaId:
        params = {"campanhaId": campanhaId}
    elif campanhaNome:
        params = {"campanhaNome": campanhaNome}
    else:
        params = {}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao listar personagens: {response.status_code} {response.text}")
    

def criarCampanha(campanhaDtoJson):
    url = f"{URL_API}/campanha/criar"
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=campanhaDtoJson, headers=headers)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Erro ao criar campanha: {response.status_code} {response.text}")
    

def buscarTodasCampanhas():
    url = f"{URL_API}/campanha/listar"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao buscar campanha: {response.status_code} {response.text}")


def buscarCampanhaPorNome(nome):
    url = f"{URL_API}/campanha/buscaPorNome"
    params = {"nome": nome}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao buscar campanha: {response.status_code} {response.text}")

def buscarCampanhaPorSistema(sistema):
    url = f"{URL_API}/campanha/buscaPorSistema"
    params = {"sistema": sistema}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao buscar campanha: {response.status_code} {response.text}")
    
def deletarCampanha(id):
    url = f"{URL_API}/campanha/deletar"
    params = {"id": id}

    response = requests.delete(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao deletar campanha: {response.status_code} {response.text}")
    
def buscarPersonagem(nomeCampanha, nomePersonagem):
    url = f"{URL_API}/personagens/busca"
    params = {"nomeCampanha": nomeCampanha, "nomePersonagem": nomePersonagem}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao buscar personagem: {response.status_code} {response.text}")
    

def atualizarPersonagem(nomeCampanha, personagem):
    url = f"{URL_API}/personagens/atualizar"
    params = {"nomeCampanha": nomeCampanha}
    headers = {"Content-Type": "application/json"}

    response = requests.put(url, json=personagem, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao atualizar personagem: {response.status_code} {response.text}")
    

def atualizarCampanha(resumoDto):
    url = f"{URL_API}/campanha/atualizar"
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=resumoDto, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao atualizar campanha: {response.status_code} {response.text}")



    

    