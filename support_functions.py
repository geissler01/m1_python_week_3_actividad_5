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
        return -1
#-----------------------------------------------------------------------------------------
# ****************************************************************************************
        # MENÚ 1
# ****************************************************************************************
def add_student(b_dates, name, age, id):  # añadir estudiante
    dict_new_student = {
        'nombre': name,
        'edad': age,
        'documento': id
    }
    b_dates.append(dict_new_student)
    return b_dates
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
#       MENÚ 2
#****************************************************************************************************************
def check_code_subject(b_dates):  # Busca el codigo
    code_subject = input('CÓDIGO MATERIA: ').strip()
    b_found = False
    for line in b_dates:
        if line['codigo'] == code_subject:
            print('\nCódigo encontrado en los registros de materias')
            b_found = True
            return code_subject
    if not b_found:
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
#       MENÚ 3
# *********************************************************************************************************************
def check_fast_id_student_2(b_students, b_assignments): 
    id_student = input('DOCUMENTO ESTUDIANTE: ').strip()    # buscar id rapidamente en la base de datos
    b_found = False
    for d in b_students:
        if d['documento'] == id_student:
            for line in b_assignments:
                if id_student in line['documento']:
                    print(f'\nEstudiante encontrado')
                    b_found = True
                    return id_student
            else:
                print('Error: Estudiante no registrado')
                return -1
    if not b_found:
        print('Estudiante no existe en las bases de datos')
        return -1
# -----------------------------------------------------------------------------------------------------------------
def check_code_subject_2(b_assignments, b_subjects):  # Busca el codigo
    code_subject = input('CÓDIGO MATERIA: ').strip()
    
    for line in b_subjects:
        if line['codigo'] == code_subject:
            name_subject = line['nombre']
            for line_2 in b_assignments:
                if code_subject in line_2['codigo']:
                    return code_subject, name_subject
            else:
                print('\nError: Matería no asiganada ningún estudiante')
                return -1, -1
    else:
        print('\nEl código ingresado no corresponde a una materia registrada')
        return -1, -1
# -----------------------------------------------------------------------------------------------------------------
def name_subeject_code(b_dates, code):  # SOLO SIRVE PARA AÑADIR MATERIAS A ESTUDIANTES
    a = ''
    for line in b_dates:
        if line['codigo'] == code:
            a = line['nombre']
            return a
    else:
        return -1
#------------------------------------------------------------------------------------------------------------------
def assign_col(b_students, b_assignments, id_validated):
    if id_validated not in (assign['documento'] for assign in b_assignments):  # esta condicion debe funcionar
        for line in b_students:
            if id_validated == line['documento']:
                name = line.get('nombre')
                age = line.get('edad')
                document = line.get('documento')
                break
        dic_new_student = {
            'nombre': name,
            'edad': age,
            'documento': document,
            'codigo': [],
            'materia': [],
            '%_acumulado': [[]],
            'nota': [[]]
        }
        b_assignments.append(dic_new_student)
        return b_assignments
    else:
        return b_assignments
#------------------------------------------------------------------------------------------------------------------
def add_subject_student (b_students, b_subjects, b_assignments, id_validated, code_validated):   # Asignar materia a un estudiante
    name_subject = name_subeject_code(b_subjects, code_validated)
    b_assignments = assign_col(b_students, b_assignments, id_validated)
    for assig in b_assignments[:]:
        if id_validated == assig['documento']:
            if name_subject not in assig['materia']:
                assig['codigo'].append(code_validated)
                assig['materia'].append(name_subject)
                print(f'\nMaterias asignadas a {assig['nombre']} => {assig['materia']}')
                if len(assig['materia']) > len(assig['nota']):  # añado listas para las notas posteriores
                    assig['nota'].append([])
                    assig['%_acumulado'].append([])
                return b_assignments
            else:
                print(f'\n{assig['nombre']} ya tiene asignad@ {name_subject}')
                print(f'Materias asignadas a {assig['nombre']} => {assig['materia']}')
                return b_assignments
# ---------------------------------------------------------------------------------------------------------------
def check_subject_student(b_assignments, id_validated):       # Ver materias que tiene un estudiante
    for assig in b_assignments:
        if assig['documento'] == id_validated:
            print(f'\nEstudiante: {assig['nombre']} => Materias: {assig['materia']}')
# ---------------------------------------------------------------------------------------------------------------
def student_in_subject(b_assignments, code_validated, name_subject):    # Consultar que estudiantes perteneces a una materia
    list_student = []
    for assig in b_assignments:
        if code_validated in assig['codigo']:
            list_student.append(assig['nombre'])
    print(f'Estudiantes en "{name_subject}" => {' | '.join(list_student)}')
# ---------------------------------------------------------------------------------------------------------------
def del_subject_student(b_assignments, id_validated, code_validated, name_subject):    # Eliminar materia a un estudiante
    for assig in b_assignments[:]:
        if id_validated == assig['documento']:
            if name_subject in assig['materia']:
                ind_percent = assig['materia'].index(name_subject)
                if ind_percent <= len(assig['%_acumulado']):
                    p_delate = assig['%_acumulado'].pop(ind_percent)
                    n_delate = assig['nota'].pop(ind_percent)
                assig['materia'].remove(name_subject)
                assig['codigo'].remove(code_validated)
                print(f'\n{name_subject} eliminada de {assig['nombre']} | Notas eliminadas {n_delate} | Porcentajes eliminados{p_delate}')
                return b_assignments
            else:
                print(f'\nError. El estudiante {assig['nombre']} no tiene asignado la materia {name_subject}')
                return b_assignments
# ***************************************************************************************************************
#       MENÚ 4
# ***************************************************************************************************************
def add_note_student(b_students, b_assignments, id_validated, note, percent):   # Registrar nota a un estudiante (porcentaje, calificación)
    assign_col(b_students, b_assignments, id_validated)
    for line in b_assignments:
        if id_validated == line['documento']:
            if len(line['codigo']) == 0:
                print('\nError. Primero debe asignar una materia al estudiante')
                return b_assignments
            else:
                print(f'\nMaterias de {line['nombre']}  => {line['materia']}')
                m_chosed = input('Nombre de la materia a la que va a asignar nota y su porcentaje: ').strip()
                if m_chosed in line['materia']:
                    ind_mod = line['materia'].index(m_chosed)  # con el indice voy a modificar de forma precisa
                else:
                    print(f'\nError: {m_chosed} no es una materia asignada a {line['nombre']}')
                    return b_assignments
    for assig in b_assignments[:]:
        if assig['documento'] == id_validated:
            if (sum(sum_p for sum_p in assig['%_acumulado'][ind_mod]) + percent) >= 100:
                print('\nError. Porcentaje sobrepasa el 100%')
                return b_assignments
            assig['%_acumulado'][ind_mod].append(percent)
            assig['nota'][ind_mod].append(note)
            print('\nRegistro de nota y porcentaje exitoso')
            return b_assignments
# --------------------------------------------------------------------------------------------------------------
def notes_related_subject(b_dates, code_validated, name_subject):    # Ver todas las notas asociadas a una materia
    print()
    for assig in b_dates:
        if code_validated in assig['codigo']:
            ind = assig['codigo'].index(code_validated)
            print(f'Notas asociadas a {name_subject} => {''.join(str(assig['nota'][ind]))} => {assig['nombre']}') # se puede mejorar
# --------------------------------------------------------------------------------------------------------------
def see_note_final_student(b_assignments, id_validated):    # consultar nota final estudiante
    print()
    for student in b_assignments:
        if student['documento'] == id_validated:
            for i in range(len(student['materia'])):
                note_f = 0
                for j in range(len(student['nota'][i])):
                    note = student['nota'][i][j]
                    percent = (student['%_acumulado'][i][j])/100
                    note_f += round(note * percent, 2)
                print(f'{student['nombre']} | {student['materia'][i]} | Nota final: {note_f} | Porcentaje evaluado: {sum(student['%_acumulado'][i])}')
            break
# --------------------------------------------------------------------------------------------------------------
def del_note_assignment(b_assignments, b_students, id_validated, code_validated, name_subject):    # Eliminar notas asignadas
    assign_col(b_students, b_assignments, id_validated)
    for assign in b_assignments[:]:
        if assign['documento'] == id_validated:
            if len(assign['codigo']) == 0:
                print(f'\nError: El estudiante "{assign['nombre']}" no tiene materias asignadas')
                return b_assignments
            if code_validated not in assign['codigo']:
                print(f'"{assign['nombre']}" no tiene asignado la materia {name_subject}')
                return b_assignments
            if len(assign['nota']) == 0:
                print(f'\nError: El estudiante "{assign['nombre']}" no tiene notas asignadas')
                return b_assignments
            dic_materias_notas = {name_subject: assign['nota']}
            print(dic_materias_notas)
            print('¿Qué nota desea eliminar?, elija su posicion empezando desde cero: ')
            note_del = filter_option_int()
            if note_del == -1:
                print('\nError. Posición invalida')
                return b_assignments
            else:
                note_delated = assign['nota'].pop(note_del)
                print(f'Nota {note_delated} eliminada de {assign['nombre']}')
                return b_assignments
            # assign['codigo'].remove(code)
            # assign['materia'].remove(name_subject)
# *************************************************************************************************************
#           MENÚ 5
# *************************************************************************************************************
def detailed_average_student(b_assignment):
    l_name = max(len(line['name']) for line in b_assignment)
    print('-'*(l_name + 15))
    print(f'{'NOMBRE':<{l_name}} | PROMEDIO FINAL')
    print('-'*(l_name + 15))
    for assign in b_assignment:
        average = sum(nota for nota in assign['nota'] )
        print()
# --------------------------------------------------------------------------------------------------------------
