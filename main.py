from utils import *


def main():
    nome = './testes/teste5.ptc'
    programa = ler_arquivo(nome)
    original = open(nome, 'r')
    print(original.read())
    print("\n----------------------------------------------------\n")

    iniciar_analisador(programa)


def executar_codigo_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        codigo = arquivo.read()
        exec(codigo)


if __name__ == "__main__":
    print("----------------- Análise Iniciada -----------------\n")
    #executar_codigo_arquivo('./testes/codigo.txt')
    main()
