# assignment = [
#     {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materias':{'codigo:materia'}},
#     {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materias':[nombre], 'codigo':[numeros]}
#     {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materias':{'codigo:materia'}},
#     {'nombre':'Julian', 'edad':17, 'documento':'1234567898', '1213':[{'codigo':'id', 'nombre':'materia'}]}
# ]

# a = students[0]['materias']
# print(a)

# a = {'nombre': 'Geisler'}
# b = {'edad': 27}
c = []
print(len(c))
# c[0] = a
# c[1] = b
# print(c)
# a = {'nombre': 'Geisler'}
# a['edad'] = 23
# print(a)

# a = {'materias':['fisica', 'mate'], 'codigo':['111','222']}
# b = a['codigo'].remove('111')
# print(a)
# if 'mate' in a['materias']:
#     print('encontrado')

# a = {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materias':['nombre','cvbcb'], 'codigo':['numeros'], 'nota':4.5, 'porcentaje': 40}

a = {'%_acumulado':[[50, 30], [40,50]], 'nota':[[3.0, 4.6], [3.9, 3.1]]}

for i in range(len(a)):
    nota_final = 0
    for j in range(len(a['nota'][0])):
        nota_final += ((a['%_acumulado'][i][j])/100)*(a['nota'][i][j])
    print(nota_final)
b = list(a.keys())   # a los diccionarios primero hay que pasar sus claves a una lista
print(b.index('nota'))
#print(f'Posicion de nota : {a.index('nota')}')

# a = {'%_acumulado':[[50, 30], [40, 50]], 'nota':[[3.0, 4.6], [3.9, 3.1]]}

# nota_final = 0

# for i in range(len(a['%_acumulado'])):          # número de filas
#     for j in range(len(a['%_acumulado'][0])):   # número de columnas
#         nota_final += (a['%_acumulado'][i][j] / 100) * a['nota'][i][j]

# print(nota_final)


# print(a['%_acumulado'][0])
# print(sum(a['nota'][0][:]))
# a = [3.9, 3.1]
# for b in a:
#     print(b)
