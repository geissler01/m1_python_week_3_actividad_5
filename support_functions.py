# *****************************************************************
def filter_option_int():  # filtro para numeros enteros en menu
    num = input('Seleccione una opción del menú: ').strip()
    try:
        num = int(num)
        if num < 0:
            print('\nError. Ingrese una opción listada en el menú')
            return -1
        else:
            return num
    except ValueError:
        print('\nError. Ingrese un valor válido')
        return -1
# --------------------------------------------------------------------
def filter_int_percent():  # filtro para numeros enteros
    percent = input('PORCENTAJE DE NOTA: ').strip()
    try:
        percent = int(percent)
        if percent >= 0 and percent <= 100:
            return percent 
        else:
            return -1
    except ValueError:
        return -1
# --------------------------------------------------------------------
def filter_int_age():  # filtro de edad
    num = input('EDAD: ').strip()
    try:
        num = int(num)
        if num >= 0 and num <= 130:
            return num
        else:
            return -1
    except ValueError:
        return -1
#----------------------------------------------------------------------
def filter_float_note():  # filtro para numeros flotantes
    note = input('NOTA ESTUDIANTE: ').strip()
    try:
        note = float(note)
        if note >= 0 and note <= 5:
            return note
        else:
            return -1
    except ValueError:
        return -1
#-------------------------------------------------------------------------
def check_id_student_repit(b_dates):    # filtro para id unicos y dimension de 7 u 10 digitos
    id_student_input = input('# DOCUMENTO: ').strip()
    for line in b_dates:
        if line['documento'] == id_student_input:
            print(f'\nEl # documento ya existe')
            return -1
        if len(line['documento']) == 10 or len(line['documento']) == 7:
            return id_student_input
        else:
            print('\nDocuemnto inváido (debe tener 7 o 10 dígitos)')
            return -1
#------------------------------------------------------------------------
def check_fast_id_student(b_dates): 
    id_student = input('DOCUMENTO ESTUDIANTE: ').strip()    # buscar id rapidamente en la base de datos
    b_found = False
    for d in b_dates:
        if d['documento'] == id_student:
            print(f'\nEstudiante encontrado')
            b_found = True
            return id_student
    if not b_found:
        print('\nEl documento ingresado no corresponde a ningún estudiante registrado')
        return -1
#-----------------------------------------------------------------------------------------
# ****************************************************************************************
def add_student(b_dates, name, age, id):  # añadir estudiante
    dict_new_student = {
        'nombre': name,
        'nombre': age,
        'nombre': id
    }
    return b_dates.append(dict_new_student)
# --------------------------------------------------------------------------
def show_students(b_dates):     # listar estudiantes
    l_name = max(len(line['nombre']) for line in b_dates)
    l_age = max(len(str(line['edad'])) for line in b_dates)
    l_doc = max(len(line['documento']) for line in b_dates)
    long_sum = l_name + l_age + l_doc + 10
    print('-'*long_sum)
    print(' Registro de estudiantes')
    print('-'*long_sum)
    print(f'{'NOMBRE':<{l_name}} | {'EDAD':<{l_age}} | {'DOCUMENTO':<{l_doc}}')
    print('-'*long_sum)
    for line in b_dates:
        print(f'{line['nombre']:<{l_name}} | {str(line['edad']):<{l_age + 2}} | {line['documento']:<{l_doc}}')
    print('-'*long_sum)
# --------------------------------------------------------------------------
def check_student_id(b_dates, id):      # Buscar estudiante
    l_name = max(len(line['nombre']) for line in b_dates)
    l_age = max(len(str(line['edad'])) for line in b_dates)
    l_doc = max(len(line['documento']) for line in b_dates)
    long_sum = l_name + l_age + l_doc + 10
    print('-'*long_sum)
    print(f'{'NOMBRE':<{l_name}} | {'EDAD':<{l_age}} | {'DOCUMENTO':<{l_doc}}')
    print('-'*long_sum)
    for line in b_dates:
        if line['documento'] == id:
            print(f'{line['nombre']:<{l_name}} | {str(line['edad']):<{l_age + 2}} | {line['documento']:<{l_doc}}')
            break
    print('-'*long_sum)
# --------------------------------------------------------------------------
def del_student(b_dates, id):       # Eliminar estudiante
    for line in b_dates[:]:
        if line['documento'] == id:
            print(f'El estudiante "{line['nombre']}" con ID:{line['documento']} ha sido elimininado')
            b_dates.remove(line)
            break
    return b_dates
#****************************************************************************************************************
#****************************************************************************************************************
def check_code_subject (b_dates):  # Busca el codigo
    code_subject = input('CÓDIGO MATERIA: ').strip()
    b_found = False
    for line in b_dates:
        if line['codigo'] == code_subject:
            print('\nCódigo encontrado')
            b_found = True
            return code_subject
    if not b_found:
        print('\nEl código ingresado no corresponde a una materia')
        return -1
#---------------------------------------------------------------------------------------------------------------
def check_code_subject_repit (b_dates, code): # me dice si el codigo está repetido
    b_found = False
    for line in b_dates:
        if line['codigo'] == code:
            b_found = True
            return -1
    if not b_found:
        print('\nError. El código ingresado ya existe')
        return code
#-----------------------------------------------------------------------------------------------------------------
# *******************************************************************************************************************
def add_subject(b_dates, code, name):
    dict_new_subject = {
        'codigo': code,
        'nombre': name,
    }
    print('\nMateria registrada exitosamente')
    return b_dates.append(dict_new_subject)
# -----------------------------------------------------------------------------------------------------------------
def show_subjects(b_dates):
    l_code = max(len(line['codigo']) for line in b_dates)
    l_subject = max(len(line['nombre']) for line in b_dates)
    long_sum = l_code + l_subject + 7
    print('-'*(long_sum + 5))
    print(' MATERIAS REGISTRADAS')
    print('-'*(long_sum + 5))
    print(f'{'CÓDIGO':<{l_code}} | {'NOMBRE':<{l_subject}}')
    print('-'*long_sum)
    for line in b_dates:
        print(f'{line['codigo']:<{l_code + 3}} | {str(line['nombre']):<{l_subject}}')
    print('-'*long_sum)
# -----------------------------------------------------------------------------------------------------------------
def check_subject_code(b_dates, code):
    l_code = max(len(line['codigo']) for line in b_dates)
    l_subject = max(len(line['nombre']) for line in b_dates)
    long_sum = l_code + l_subject + 7
    print('-'*long_sum)
    print(f'{'CÓDIGO':<{l_code}} | {'NOMBRE':<{l_subject}}')
    print('-'*long_sum)
    for line in b_dates:
        if line['codigo'] == code:
            print(f'{line['codigo']:<{l_code + 3}} | {str(line['nombre']):<{l_subject}}')
    print('-'*long_sum)

# -----------------------------------------------------------------------------------------------------------------
def del_subject(b_dates, code):
    for line in b_dates[:]:
        if line['codigo'] == code:
            print(f'Codigo: {code} => Materia: {line['nombre']} => Eliminado exitosamente')
            b_dates.remove(line)
# *********************************************************************************************************************
# *********************************************************************************************************************
def check_fast_id_student_vf(b_dates, id):     # buscar id rapidamente en la base de datos
    b_found = False
    for d in b_dates:
        if d['documento'] == id:
            b_found = True
            return id
    if not b_found:
        return -1
#------------------------------------------------------------------------------------------------------------------
def check_code_subject_vf(b_dates, code):  # Busca el codigo
    b_found = False
    for line in b_dates:
        if line['codigo'] == code:
            b_found = True
            return code
    if not b_found:
        return -1
# -----------------------------------------------------------------------------------------------------------------
def name_subeject_code(b_dates, code):
    a = ''
    for line in b_dates:
        if line['codigo'] == code:
            a = line['nombre']
            return a
    else:
        return -1
#------------------------------------------------------------------------------------------------------------------
def add_subject_student (b_students, b_subjects, b_assignment, id_validated, code_validated):
    name_subject = name_subeject_code(b_subjects, code_validated)
    if 'materia' not in b_assignment[0]:
        for student in b_students:
            if student['documento'] == id_validated:
                for subject in b_subjects:
                    if subject['codigo'] == code_validated:
                        asig = student
                        asig['codigo'] = []
                        asig['codigo'].append(code_validated)
                        asig['materia'] = []
                        asig['materia'].append(name_subject)
                        b_assignment.append(asig)
                        return b_assignment
    else:
        for assig in b_assignment:
            if id_validated == assig['documento']:
                assig['codigo'].append(code_validated)
                assig['materia'].append(name_subject)
                return b_assignment
# ---------------------------------------------------------------------------------------------------------------
def check_subject_student(b_dates, id_validated):
    for assig in b_dates:
        if assig['documento'] == id_validated:
            print(f'\nEstudiante: {assig['nombre']} => Materias: {assig['materia']}')
# ---------------------------------------------------------------------------------------------------------------
def student_in_subject(b_dates, code_validated):
    list_student = []
    subject = name_subeject_code(b_dates, code_validated)
    for assig in b_dates:
        if code_validated in assig['codigo']:
            list_student.append(assig['nombre'])
    print(f'Estudiantes en "{subject}" son: {' | '.join(list_student)}')
# ---------------------------------------------------------------------------------------------------------------
def del_subject_student(b_dates, code_validated):
    subject = name_subeject_code(b_dates, code_validated)
    for assig in b_dates[:]:
        if subject in assig['materia']:
            assig['materia'].remove(subject)
    return b_dates
# ***************************************************************************************************************
# ***************************************************************************************************************
def add_note_student(b_assignment, id_validated, note, percent):   # Registrar nota a un estudiante (porcentaje, calificación)
    if 'porcentaje' not in b_assignment[0]:
        for assig in b_assignment[:]:
            if assig['documento'] == id_validated:
                assig['porcentaje'] = []
                assig['porcentaje'].append(percent)
                assig['nota'] = []
                assig['nota'].append(note)
                return b_assignment
    else:
        for assig in b_assignment:
            if id_validated == assig['documento']:
                assig['porcentaje'].append(percent)
                assig['nota'].append(note)
                return b_assignment
# --------------------------------------------------------------------------------------------------------------
def notes_related_subject(b_dates, subjects, code):    # Ver todas las notas asociadas a una materia
    name_subject = name_subeject_code(subjects, code)
    print()
    for assig in b_dates:
        if code in assig['codigo']:
            print(f'Notas asociadas a {name_subject} => {''.join(str(assig['nota']))}') # se puede mejorar
# --------------------------------------------------------------------------------------------------------------
def see_note_final_student(b_dates, id_student):    # consultar nota final estudiante
    print()
    for student in b_dates:
        if student['documento'] == id_student:
            note_prom = 0
            comulative_percent = 0
            for i,j in zip(student['nota'], student['porcentaje']):
                note_prom += i*j
                comulative_percent += j
            print(f'Nota acumulada de "{student['nombre']}" es => {note_prom} con el {comulative_percent}%')
            break
# --------------------------------------------------------------------------------------------------------------
def del_note_assignment(b_dates, subjects, id_student, code):     # Eliminar notas asignadas
    name_subject = name_subeject_code(subjects, code)
    for assign in b_dates[:]:
        if assign['documento'] == id_student:
            if len(assign['codigo']) == 0:
                print(f'\nError: El estudiante "{assign['nombre']}" no tiene materias asignadas')
                return b_dates
            if code not in assign['codigo']:
                print(f'"{assign['nombre']}" no tiene asignado la materia {name_subject}')
                return b_dates
            if len(assign['nota']) == 0:
                print(f'\nError: El estudiante "{assign['nombre']}" no tiene notas asignadas')
                return b_dates
            dic_materias_notas = {name_subject: assign['nota']}
            print(dic_materias_notas)
            note_del = int(input('¿Qué nota desea eliminar?, elija su posicion empezando desde cero: '))
            note_delated = assign['nota'].pop(note_del)
            print(f'Nota {note_delated} eliminada de {assign['nombre']}')
            return b_dates
            # assign['codigo'].remove(code)
            # assign['materia'].remove(name_subject)

# --------------------------------------------------------------------------------------------------------------
