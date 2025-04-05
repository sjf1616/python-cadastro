from src.layout import *
from time import sleep
from src.data import *

def option_menu(r):
    if r == 1:
        title('Ver pessoas')
        loadsql()
    elif r == 2:
        title('Novo cadastro')
        name = input('Name: ').strip()
        age = input('Age: ')
        insert_sql(name, age)
    elif r == 3:
        title('Saindo do sistema... Até logo!')
        exit()
    else:
        print(f'{collors('red')}ERRO: Digite uma opção válida!{collors('clean')}')
        print()
    sleep(1.5)

def main_menu():
    while True:
        resposta = menu(['Ver Pessoas', 'Cadastrar Pessoas', 'Sair do sistema'])
        option_menu(resposta)

main_menu()