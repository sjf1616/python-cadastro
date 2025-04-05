def loadsql():
    import csv
    import os
    if os.path.exists('src/data/data.csv'):
        with open('src/data/data.csv', 'r',newline='', encoding='utf-8') as file:
            dict_file = csv.DictReader(file)
            for e, r in enumerate(dict_file):
                print(f'{e+1}- {r['nome'].capitalize():<20}{r['idade']} anos')
            print()
    else:
        with open('src/data/data.csv', 'w',newline='', encoding='utf-8') as file:
            dict_file = csv.writer(file)
            dict_file.writerow(['Nome','Idade'])
        print(f'Não existe pessoas para verificar - Adicione no módulo 2')

def insert_sql(name, age):
    import csv
    with open('src/data/data.csv', 'a', newline='', encoding='utf-8') as file:
        write_file = csv.writer(file)
        try:
            write_file.writerow([str(name).capitalize(), int(age)])
        except TypeError:
            print(f'ERROR: Verifique o tipo corretamente.')
        else:
            print(f'{name} adicionada com sucesso!')
