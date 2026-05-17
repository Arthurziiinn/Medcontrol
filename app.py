import json
import os
import requests

FILE = "medicamentos.json"


def carregar():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def salvar(dados):
    with open(FILE, "w") as f:
        json.dump(dados, f, indent=4)


def adicionar(nome, horario):
    dados = carregar()

    dados.append({
        "nome": nome,
        "horario": horario
    })

    salvar(dados)


def listar():
    return carregar()


def remover(nome):
    dados = carregar()

    novos = [m for m in dados if m["nome"] != nome]

    salvar(novos)


def mostrar_horario():
    url = "http://worldtimeapi.org/api/timezone/America/Sao_Paulo"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()

            horario = dados["datetime"]

            print("\nHorário atual:")
            print(horario)

        else:
            print("Erro ao acessar API")

    except requests.RequestException:
        print("Erro de conexão com API")


def menu():
    while True:
        print("\n1. Adicionar medicamento")
        print("2. Listar medicamentos")
        print("3. Remover medicamento")
        print("4. Mostrar horário atual")
        print("5. Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome do medicamento: ")
            horario = input("Horário: ")

            adicionar(nome, horario)

        elif op == "2":
            meds = listar()

            for m in meds:
                print(m["nome"], "-", m["horario"])

        elif op == "3":
            nome = input("Nome para remover: ")

            remover(nome)

        elif op == "4":
            mostrar_horario()

        elif op == "5":
            break


if __name__ == "__main__":
    menu()
