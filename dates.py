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
    {'codigo':'114', 'nombre':'Etica'},
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
def b_assignment_3():
    assignments = [
    {'nombre':'Carlos', 'edad':15, 'documento':'1234567896', 'materia':['Fisica', 'Etica'], 'codigo':['111','112'], 'porcentaje':[25,30], 'nota':[4.0, 3.6]},
    {'nombre':'Julian', 'edad':17, 'documento':'1234567898', 'materia':['Español', 'Etica'], 'codigo':['113','112'], 'porcentaje':[25,30], 'nota':[3.0, 3.9]}
    ]
    return assignments