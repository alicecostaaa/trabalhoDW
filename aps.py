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
mesAnoLista = {'201601': ['20160102', '20160103', '20160106'], '201602': ['20160102', '20160103', '20160106'],
               '201603': ['20160202', '20160103', '20160106'], '201604': ['20160202', '20160203', '20160106'],
               '201605': ['20160302', '20160203', '20160106'], '201606': ['20160302', '20160203', '20160106'],
               '201607': ['20160402', '20160303', '20160206'], '201608': ['20160402', '20160303', '20160206'],
               '201609': ['20160502', '20160303', '20160206'], '201610': ['20160502', '20160403', '20160206'],
               '201611': ['20160602', '20160403', '20160206'], '201612': ['20160602', '20160403', '20160206'],
               '201701': ['20170102', '20170103', '20170106'], '201702': ['20170102', '20170103', '20170106'],
               '201703': ['20170202', '20170103', '20170106'], '201704': ['20170202', '20170203', '20170106'],
               '201705': ['20170302', '20170203', '20170106'], '201706': ['20170302', '20170203', '20170106'],
               '201707': ['20170402', '20170303', '20170206'], '201708': ['20170402', '20170303', '20170206'],
               '201709': ['20170502', '20170303', '20170206'], '201710': ['20170502', '20170403', '20170206'],
               '201711': ['20170602', '20170403', '20170206'], '201712': ['20170602', '20170403', '20170206'],
               '201801': ['20180102', '20180103', '20180106'], '201802': ['20180102, 20170103', '20180106'],
               '201803': ['20180202', '20180103', '20180106'], '201804': ['20180202', '20180203', '20180106'],
               '201805': ['20180302', '20180203', '20180106'], '201806': ['20180302', '20180203', '20180106'],
               '201807': ['20180402', '20180303', '20180206'], '201808': ['20180402', '20180303', '20180206'],
               '201809': ['20180502', '20180303', '20180206'], '201810': ['20180502', '20180403', '20180206'],
               '201811': ['20180602', '20180403', '20180206'], '201812': ['20180602', '20180403', '20180206']}





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
            print(mesAno)
            print(mesAnoLista[mesAno][1])
            print(mesAnoLista[mesAno][0])
            print(mesAnoLista[mesAno][2])
            print(df.values[i][3])
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
# engine.execute('INSERT INTO DM_TEMPO (ID_TEMPO, SEMESTRE, TRIMESTRE, BIMESTRE, ANOMES) VALUES (:id,:semestre,:trimestre,:bimestre,:anomes)’,{‘id': str(mesAno+'00'),’semestre’: mesAnoLista[mesAno][2],’trimestre’: mesAnoLista[mesAno][1], ‘bimestre’: mesAnoLista[mesAno][0], ‘ANOMES’: str(anoMes)})
#
# ——————————————DEPOIS—————————————
#
# # Tabela FT_BOLSA_FAMILIA
#
# engine.execute('INSERT INTO DM_REGIAO (ID_REGIAO, REGIAO, UF, CIDADE, COD_IBGE) VALUES (:id,:regiao,:uf,:cidade,:cod_ibge)’,{‘id': str(comments[j]['id']),’regiao’: str(df.values[i][3]),’uf’:str(comments[0]['uf'][sigla]), ‘cidade’: str(comments[0]['municipio']['nomeIBGE']), ‘cod_ibge’: str(comments[0]['municipio']['codigoIBGE'])})
# # extracting data in json format
