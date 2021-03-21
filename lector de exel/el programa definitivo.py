"aqui deberia estar el programa xd"
import csv
archivo = '1-12-2020.csv'

def lector(archivo):
    excel = open(archivo,'r')
    dic = {"AV. BERNARDO O'HIGGINS 555":[],"AV. LOS PAJARITOS  4500":[],"sucursal":[]}
    for linea in excel:
        separado = linea.split(';')
        llave = separado[7].rstrip()
        dic[llave].append(separado[3])
    excel.close()
    return (dic["AV. BERNARDO O'HIGGINS 555"],dic["AV. LOS PAJARITOS  4500"])
#print(lector(archivo))
print('en las siguientes preguntas solo se pone el numero del dia')
inicio = int(input('fecha inicial:'))
final = int(input('facha final:'))
mes = input('mes:')
anno = input('año:')
dic = {'dia':[],'boleta_m':[],'dinero_m':[],'boleta_b':[],'dinero_b':[]}
while inicio <= final:
    buin, maipu = lector(str(inicio)+'-'+mes+'-'+anno+'.csv')
    dic['dia'].append(str(inicio))
    dic['boleta_m'].append(len(maipu))
    w = 0
    for x in maipu:
        w += int(x)
    dic['dinero_m'].append(w)
    dic['boleta_b'].append(len(buin))
    q = 0
    for x in buin:
        q += int(x)
    dic['dinero_b'].append(q)
    inicio+=1
lista=['dia','boletas_m','dinero_m','boletas_b','dinero_b']
n=0
data = [lista]
while n <= len(dic['dinero_b'])-1:
    data.append([dic['dia'][n],dic['boleta_m'][n],dic['dinero_m'][n],dic['boleta_b'][n],dic['dinero_b'][n]])
    n +=1
print(data)
with open('archivo_final.csv', 'w', newline='') as fila:
    writer = csv.writer(fila, delimiter=';')
    writer.writerows(data)
print(dic)
