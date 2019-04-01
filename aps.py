import requests
import pandas as pd
import json
import xlwt

xl = pd.ExcelFile("Cidades-IBGE_CR.xlsx")
list = xl.sheet_names



df = xl.parse("Plan1")




mesAnoList = ['201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611','201612',
          '201701','201702','201703','201704','201705','201706','201707','201708','201709','201710','201711','201712',
          '201801','201802','201803','201804','201805','201806','201807','201808','201809','201810','201811','201812']

wb = xlwt.Workbook()
ws = wb.add_sheet('pca',
                                    cell_overwrite_ok=True)
p = 0
j = 0
for i in range(1,5565):
    for mesAno in mesAnoList:
            URL = "http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio/?mesAno="+mesAno+"&codigoIbge="+\
            str(df.values[i][1])+"&pagina=1"
            r = requests.get(url=URL)
            data = r.json()
            print(data)
            comments = json.loads(r.content)
            # print(df.values[i][3])
            # print(comments[j]['municipio']['codigoIBGE'])
            # print(df.values[j][3])
            # print(comments[j]['id'])
            # print(comments[j]['dataReferencia'])
            # print(comments[j]['municipio']['codigoIBGE'])
            # print(comments[j]['municipio']['nomeIBGE'])
            # print(comments[j]['municipio']['uf']['nome'])
            # print(comments[j]['valor'])
            # print(comments[0]['quantidadeBeneficiados'])
            # h = 0
            #
            # # print(j)
            # ws.write(j, h, df.values[i][3])
            # ws.write(j, (h+1), comments[0]['id'])
            # ws.write(j, (h+2), comments[0]['dataReferencia'])
            # ws.write(j, (h+3), comments[0]['municipio']['codigoIBGE'])
            # ws.write(j, (h+4), comments[0]['municipio']['nomeIBGE'])
            # ws.write(j, (h+5), comments[0]['municipio']['uf']['nome'])
            # ws.write(j, (h+6), comments[0]['valor'])
            # ws.write(j, (h+7), comments[0]['quantidadeBeneficiados'])
            # j = j + 1
            # p = p + 1
            # wb.save('ex5.xls')
            # if p == 10:
            #     print('=========')
            #     p = 0
            #print(data)




# Queries - Bolsa Família
#
# # Tabela DM_REGIAO
#
# - Criar o ID_REGIAO manualmente, sendo incremental;
#
# engine.execute('INSERT INTO DM_REGIAO (ID_REGIAO, REGIAO, UF, CIDADE, COD_IBGE) VALUES (:id,:regiao,:uf,:cidade,:cod_ibge)’,{‘id': str(array_dm[0]),’regiao’: str(df.values[i][3]),’uf’: str(comments[0]['uf'][sigla]), ‘cidade’: str(comments[0]['municipio']['nomeIBGE']), ‘cod_ibge’: str(comments[0]['municipio']['nomeIBGE'])})
#
# # Tabela DM_TEMPO
#
# - Criar o ID_TEMPO manualmente, sendo incremental;
#
# engine.execute('INSERT INTO DM_TEMPO (ID_TEMPO, SEMESTRE, TRIMESTRE, BIMESTRE, ANOMES) VALUES (:id,:semestre,:trimestre,:bimestre,:anomes)’,{‘id': str(array_dm[0]),’semestre’: str(0),’trimestre’: str(0), ‘bimestre’: str(0), ‘ANOMES’: str(anoMes)})
#
# ——————————————DEPOIS—————————————
#
# # Tabela FT_BOLSA_FAMILIA
#
# engine.execute('INSERT INTO DM_REGIAO (ID_REGIAO, REGIAO, UF, CIDADE, COD_IBGE) VALUES (:id,:regiao,:uf,:cidade,:cod_ibge)’,{‘id': str(array_dm[0]),’regiao’: str(array_dm[1]),’uf’: str(array_dm[2]), ‘cidade’: str(array_dm[3]), ‘cod_ibge’: str(array_dm[4])})
# # extracting data in json format
