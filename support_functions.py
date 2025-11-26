# *****************************************************************
def filter_option_int(num):  # filtro para numeros enteros en menu
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
def filter_int(num):  # filtro para numeros enteros
    try:
        num = int(num)
        if num < 0:
            print('\nError. Ingrese un valor válido')
            return -1
        else:
            return num
    except ValueError:
        print('\nError. Ingrese un valor válido')
        return -1
# --------------------------------------------------------------------
def filter_int_age(num):  # filtro de edad
    try:
        num = int(num)
        if num >= 0 and num <= 130:
            return num
            
        else:
            print('\nError. Ingrese un valor válido')
            return -1
    except ValueError:
        print('\nError. Ingrese un valor válido')
        return -1
#----------------------------------------------------------------------
def filter_float(num):  # filtro para numeros flotantes
    try:
        num = float(num)
        if num < 0:
            print('\nError. Ingrese un valor válido')
            return -1
        else:
            return num
    except ValueError:
        print('\nError. Ingrese un valor válido')
        return -1
#-------------------------------------------------------------------------
def check_id_student_repit(b_dates, id):    # filtro para id unicos y dimension de 7 u 10 digitos
    for line in b_dates:
        if line['documento'] == id:
            print(f'\nEl # documento ya existe')
            return -1
        if len(line['documento']) == 10 or len(line['documento']) == 7:
            return id
        else:
            print('\nDocuemnto inváido (debe tener 7 o 10 dígitos)')
            return -1
#------------------------------------------------------------------------
def check_fast_id_student(b_dates, id):     # buscar id rapidamente en la base de datos
    b_found = False
    for d in b_dates:
        if d['documento'] == id:
            print(f'\nEstudiante encontrado')
            b_found = True
            return id
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
def check_code_subject (b_dates, code):  # Busca el codigo
    b_found = False
    for line in b_dates:
        if line['codigo'] == code:
            print('\nCódigo encontrado')
            b_found = True
            return code
    if not b_found:
        print('\nEl código ingresado no corresponde a una materia')
#---------------------------------------------------------------------------------------------------------------
def check_code_subject_repit (b_dates, code): # me dice si el codigo está repetido
    b_found = False
    for line in b_dates:
        if line['codigo'] == code:
            b_found = True
            return -1
    if not b_found:
        print('\nError. El código ingresado ya existe')
#-----------------------------------------------------------------------------------------------------------------
# *******************************************************************************************************************
def add_subject(b_dates, code, name):
    dict_new_subject = {
        'codigo': code,
        'nombre': name,
    }
    print('\nMateria registrada exitosamente')
    return b_dates.append(dict_new_subject)

