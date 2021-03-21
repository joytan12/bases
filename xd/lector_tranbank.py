import os
import csv

def lector(archivo):
    excel = open(archivo, 'r')
    contador = 1
    dic = {'TOUCH BERNARDO O HIGGINSS 555LOCAL 5':[], 'TOUCH DENTRO DE SUPERM HIPERLIDER AV PAJARITOS 45007':[]}
    dinero_m = []
    dinero_b = []
    b, m = dic.keys()
    for linea in excel:
        if contador > 17:
            separado = linea.split(';')
            plata = separado[7]
            if len(dinero_b) == 0:
                dinero_b.append(separado[0][:10])
            if len(dinero_m) == 0:
                dinero_m.append(separado[0][:10])
            if separado[2] == b:
                dinero_b.append(plata)
            if separado[2] == m:
                dinero_m.append(plata)
            if separado[0][:10] != dinero_m or separado[0][:10] != dinero_b:
                dic[separado[2]].append(dinero_m) 
                dinero_m = []
                dic[b].append(dinero_b)
                dinero_b = []
            """
            if separado [0][:10] != dinero_m[0] and separado[2] == m:
                dic[separado[2]].append(dinero_m) 
                dinero_m = []
            elif separado [0][:10] != dinero_b[0] and separado[2] == b:
                dic[separado[2]].append(dinero_b) 
                dinero_b = []"""
        contador += 1
    dic[m].append(dinero_m) 
    dic[b].append(dinero_b)
    return dic
archivos = os.listdir()
for i in archivos:
    data = [['fecha', 'boletab', 'plata_b', 'boleta_m', 'plata_m']]
    if i[-3:] != '.py':
        dic = lector(i)
        b, m = dic.keys()
        if len(dic[b]) != len(dic[m]):
            cont = 0
            while len(dic[m])+2 != len(dic[b]):
                #
                # print(dic[b][cont][0], dic[m][cont][0])
                if dic[b][cont][0] != dic[m][cont][0]:
                    dic[m].insert(cont, [dic[b][cont][0]])
                else:
                    cont += 1
            dic[m].append([dic[b][cont+1][0]])
            dic[m].append([dic[b][cont+2][0]])
        n = 0 
        while n <= len(dic[b])-1:
            suma_b = 0
            for x in dic[b][n][1:]:
                num = x.split('.')
                if len(num) > 1:
                    num = num[0] + num [1]
                else:
                    num = num[0]
                suma_b += int(num)
            suma_m = 0
            #print(dic[m][n])
            #print(len(dic[m][n]))
            if len(dic[m][n]) == 1: 
                suma_m =0
            else:
                for x in dic[m][n][1:]:
                    num = x.split('.')
                    if len(num) > 1:
                        num = num[0] + num [1]
                    else:
                        num = num[0]
                    suma_m += int(num)
            data.append([dic[b][n][0], len(dic[b][n])-1, suma_b, len(dic[m][n])-1, suma_m])
            n += 1
        define = i[:-4] + '.csv'
        with open( define , 'w', newline='') as fila:
            writer = csv.writer(fila, delimiter=';')
            writer.writerows(data)