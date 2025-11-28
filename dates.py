def b_students():
    students = [
    {'nombre':'Carlos', 'edad':15, 'documento':'1234567896'},
    {'nombre':'Julian', 'edad':17, 'documento':'1234569'},
    {'nombre':'Maria', 'edad':18, 'documento':'1234567'},
    {'nombre':'Ana', 'edad':19, 'documento':'1234563'},
    {'nombre':'Elia', 'edad':16, 'documento':'1234561'}
    ]
    return students

def b_subjects():
    subjects = [
    {'codigo':'111', 'nombre':'Fisica'},
    {'codigo':'112', 'nombre':'Etica'},
    {'codigo':'113', 'nombre':'Español'},
    {'codigo':'114', 'nombre':'Ingles'},
    {'codigo':'115', 'nombre':'Sociales'},
    ]
    return subjects


# case 3
def b_assignment():
    assignments = [
    {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'codigo':['111', '112'], 'materia':['Fisica', 'Etica'], '%_acumulado':[[80], [70]], 'nota':[[4.0], [3.6]]},
    {'nombre':'Julian', 'edad':17, 'documento':'1234569', 'codigo':['113', '112'], 'materia':['Español', 'Etica'], '%_acumulado':[[60, 10], [20, 80]], 'nota':[[3.0, 4.6], [3.9, 5.0]]},
    {'nombre':'Maria', 'edad':18, 'documento':'1234567', 'codigo':['115', '112'], 'materia':['Sociales', 'Etica'], '%_acumulado':[[30, 65], [40, 35]], 'nota':[[3.0, 4.6], [3.9, 3.1]]},
    {'nombre':'Ana', 'edad':19, 'documento':'1234563', 'codigo':['114', '115'], 'materia':['Ingles', 'Sociales'], '%_acumulado':[[40], [60]], 'nota':[[3.0], [3.9]]},
    {'nombre':'Elia', 'edad':16, 'documento':'1234561', 'codigo':['113', '111'], 'materia':['Español', 'Fisica'], '%_acumulado':[[80], [40]], 'nota':[[3.5], [3.9]]}
    ]
    return assignments

# #case 1
# def b_assignment_1():
#     assignments = []
#     return assignments
# # case 2
# def b_assignment_2():
#     assignments = [
#     {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materia':['Fisica', 'Etica'], 'codigo':['111','112']},
#     {'nombre':'Julian', 'edad':17, 'documento':'1234567898', 'materia':['Español', 'Etica'], 'codigo':['113','112']}
#     ]
#     return assignments