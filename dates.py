def b_students():
    students = [
    {'nombre':'Carlos', 'edad':15, 'documento':'1234567896'},
    {'nombre':'Julian', 'edad':17, 'documento':'1234567898'},
    {'nombre':'Maria', 'edad':15, 'documento':'1234567'},
    {'nombre':'Henry', 'edad':15, 'documento':'1234563'},
    {'nombre':'Liliana', 'edad':15, 'documento':'1234569'}
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

#case 1
def b_assignment_1():
    assignments = []
    return assignments
# case 2
def b_assignment_2():
    assignments = [
    {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materia':['Fisica', 'Etica'], 'codigo':['111','112']},
    {'nombre':'Julian', 'edad':17, 'documento':'1234567898', 'materia':['Español', 'Etica'], 'codigo':['113','112']}
    ]
    return assignments
# case 3
def b_assignment():
    assignments = [
    {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materia':['Fisica', 'Etica'], '%_acumulado':[100, 80], 'nota':[[4.0], [3.6]]},
    {'nombre':'Julian', 'edad':17, 'documento':'1234569', 'materia':['Español', 'Etica'], '%_acumulado':[25,30], 'nota':[[3.0], [3.9]]},
    {'nombre':'Pedro', 'edad':18, 'documento':'1234567', 'materia':['Sociales', 'Etica'], '%_acumulado':[50,60], 'nota':[[3.0, 4.6], [3.9, 3.1]]},
    {'nombre':'Ana', 'edad':19, 'documento':'1234563', 'materia':['Ingles', 'sociales'], '%_acumulado':[70,80], 'nota':[[3.0, 2.0], [3.9]]},
    {'nombre':'Elia', 'edad':16, 'documento':'1234568', 'materia':['Español', 'Fisica'], '%_acumulado':[60,90], 'nota':[[3.0, 4.6], [3.9]]}
    ]
    return assignments