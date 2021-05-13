import time
from datetime import date
import os

def exibir_menu():
    print("Escolha uma opção:"
          "\n\n1. Cadastrar anúncio"
          "\n2. Relatorio de anúncios cadastrados"
          "\n3. Buscar anúncio"
          "\n4. sair")

def cadastrar(anuncios):
    nome = input("Digite o nome do anúncio: ")
    cliente = input("Digite o nome do cliente: ")
    print("Quando começará a investir ?\n")
    ano = int(input("ANO: "))
    mes = int(input("MES: "))
    dia = int(input("DIA: "))
    print("\n\nQuando encerrará o investimento ?\n")
    ano_final = int(input("ANO: "))
    mes_final = int(input("MES: "))
    dia_final = int(input("DIA: "))
    valor_investido = float(input("\nQuanto deseja investir por dia "))
    dias_contados = (date(year=ano_final, month=mes_final, day=dia_final) - date(year=ano, month=mes, day=dia))
    total_investido = float(dias_contados.days * valor_investido)
    numero_views = float((total_investido * 21.6) * 4 + (total_investido * 30))
    total_cliques = float(dias_contados.days * 3.6 * valor_investido)
    total_compartilhado = float(dias_contados.days * 0.54 * valor_investido)
    anuncios.append((nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado))
    print('\n' * 130)


def listar(anuncios):

        for anuncio in anuncios:
            nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
            print(f'Nome: {nome}\nCliente: {cliente}\nTotal investido: R$ {"%.2f"%total_investido}'
                  f'\nTotal de cliques: {"%.2f"%total_cliques}\nTotal de compartilhamento: {"%.2f"%total_compartilhado}\n'
                  f'Visualizações: {"%.2f"%numero_views}\n')


            print("\n" * 2)

def buscar(anuncios):
    print("1. Procurar por cliente"
           "\n2. Procurar por período")

    opcao = int(input("Opção: \n"))

    if opcao == 1:
        cliente_desejado = input("Nome do cliente: ")
        for anuncio in anuncios:
            nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
            if cliente == cliente_desejado:
                print(
                f'Nome:  {nome}\nCliente: {cliente}\nTotal investido: R$ {"%.2f"%total_investido}\n'
                f'Visualizações: {"%.2f"%numero_views}\nTotal de cliques: {"%.2f"%total_cliques}\nTotal de compartilhamento: {"%.2f"%total_compartilhado}')
                print("\n" * 2)
            else:
                print("Cliente não encontrado")
                break

    elif opcao == 2:
        ano_periodo = int(input("ANO: "))
        mes_periodo = int(input("MES: "))
        dia_periodo = int(input("DIA: "))
        for anuncio in anuncios:
            nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
        if date(year=ano_periodo, month=mes_periodo, day=dia_periodo) >= date(year=ano, month=mes, day=dia) and date(
                year=ano_periodo, month=mes_periodo, day=dia_periodo) <= date(year=ano_final, month=mes_final, day=dia_final):
            for anuncio in anuncios:
                nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio

                print(

                f'Nome:  {nome}\nCliente: {cliente}\nValor investido: R$ {"%.2f"%valor_investido}\nTotal investido: R$ {"%.2f"%total_investido}\n'
                f'Visualizações: {"%.2f"%numero_views}\nTotal de cliques: {"%.2f"%total_cliques}\nTotal de compartilhamento: {"%.2f"%total_compartilhado}')

                print("\n" * 2)
        else:
            print("cliente não encontrado: ")
    else:
        print("Opção Inválida")



def main():
    anuncios = []
    while True:
        exibir_menu()
        opcao = int(input("Opção ?\n"))
        if opcao == 1:
            cadastrar(anuncios)
        elif opcao == 2:
            listar(anuncios)
        elif opcao == 3:
            buscar(anuncios)
        elif opcao == 4:
            break
        else:
            print("Opção inválida")

main()