import os

os.chdir('Aula7 - Módulos e Bibliotecas')

lista_arquivos = os.listdir()

contador = 1

for arquivo in lista_arquivos:
    tipo_arquivo = arquivo.split('.')
    
    if tipo_arquivo[1] == 'txt':
        novo_nome = f"arquivo_{contador}.txt"
        os.rename(arquivo, novo_nome)
        contador += 1
    else:
        print(f"Arquivo {arquivo} não é do tipo .txt, portanto não foi renomeado.")    
