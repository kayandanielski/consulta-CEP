import requests
import json

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"CEP: {dados['cep']}")
            print(f"Rua: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")

            with open("consulta_cep.json", "w") as arquivo_json:
                json.dump(dados, arquivo_json, indent=4)
    else:
        print("Erro ao acessar a API.")

cep_digitado = input("Digite o CEP (somente números): ")
consultar_cep(cep_digitado)
