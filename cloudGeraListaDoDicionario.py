import pandas as pd
import os
import sys

dicionarioDados="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\SICP_BARE\\Dicionário de Dados DGDS - SICPv2.xlsx"
saidaTemp="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\SICP_BARE\\saida.txt"
saida="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\SICP_BARE\\listaColSensiveis.txt"
pdDf = pd.read_excel(dicionarioDados, sheet_name="Dicionário de Dados",skiprows=3,usecols='A:B')
pdDf.rename(columns={"Nome Tabela": "NomeTabela", "Nome do Campo": "Campo"},inplace=True)
pdDf['NomeTabela'] = pdDf.apply(lambda row: ('sicp_'+row.NomeTabela).lower(), axis = 1)
agregado=pdDf.groupby("NomeTabela")['Campo'].apply(list)
agregado.to_csv(saidaTemp, index=True,header=None,sep=";")
quantLinhas=agregado.count()

# Using readlines()
count=0
s = open(saida,'w')

with open(saidaTemp, 'r+') as f:
    registers = f.readlines()
    s.write("listaColSensiveis=[\n")
    for register in registers:
        count += 1
        register=register.replace('"','')
        register=register.strip()
        if count == quantLinhas:
            strTemp = '"' + register + '"\n';
        else:
            strTemp = '"' + register + '",\n';
        s.write(strTemp)
    s.write("]")
    s.close()
os.remove(saidaTemp)