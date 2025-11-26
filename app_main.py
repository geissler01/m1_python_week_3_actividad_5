from msm import *
from support_functions import *

students = [
    {'nombre':'Carlos', 'edad':15, 'documento':'1234567896'},
    {'nombre':'Julian', 'edad':17, 'documento':'1234567898'},
    {'nombre':'Maria', 'edad':15, 'documento':'1234567'},
    {'nombre':'Henry', 'edad':15, 'documento':'1234563'},
    {'nombre':'Liliana', 'edad':15, 'documento':'1234569'}
]

subjects = [
    {'codigo':'111', 'nombre':'Fisica'},
    {'codigo':'112', 'nombre':'Etica'},
    {'codigo':'113', 'nombre':'Español'},
] 

while True:
    menu_main()
    option_input = input('Seleccione una opción del menú principal: ').strip()
    opction_validated = filter_option_int(option_input)
    # ============================================================================================================
    if opction_validated == 1:
        while True:
            menu_sec_1()
            option_input = input('Seleccione una opción del menú: ').strip()
            opction_validated = filter_option_int(option_input)
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:  # registrar estudiante
                name_student = input('NOMBRE: ').strip()
                age_input = input('EDAD: ').strip()
                age_filtrated = filter_int_age(age_input)
                if age_filtrated == -1:
                    print('Introduzca una edad válida')
                    continue
                id_student_input = input('# DOCUMENTO: ').strip()
                id_student_validated = check_id_student_repit(students, id)
                if id_student_validated == -1:
                    print('Los documentos deben ser únicos')
                    continue
                students = add_student(students, name_student, age_filtrated, id_student_input)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:   # listar
                show_students(students)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:   # Buscar estudiante
                id_student_input = input('# DOCUMENTO: ').strip()
                id_student_validated = check_fast_id_student(students, id_student_input)
                if id_student_validated == -1:
                    continue
                check_student_id(students, id_student_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:        # del student
                id_student_input = input('# DOCUMENTO: ').strip()
                id_student_validated = check_fast_id_student(students, id_student_input)
                if id_student_validated == -1:
                    continue
                del_student(students, id_student_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:
                print('\nVolviendo al menú principal')
                break
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ==============================================================================================================
    elif opction_validated == 2:
        while True:
            menu_sec_2()
            option_input = input('Seleccione una opción del menú: ').strip()
            opction_validated = filter_option_int(option_input)
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:    # Añadir materia
                code_input = input('CÓDIGO MATERIA: ').strip()
                code_validated = check_code_subject_repit(subjects, code_input)
                if code_validated == -1:
                    print('\nError. El código ya existe')
                    continue
                name_subject = input('NOMBRE MATERIA: ').strip()
                subjects = add_subject(subjects, code_validated, name_subject)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:
                pass
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ===============================================================================================================
    elif opction_validated == 3:
        while True:
            menu_sec_1()
            option_input = input('Seleccione una opción del menú: ').strip()
            opction_validated = filter_option_int(option_input)
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:
                pass
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ===============================================================================================================
    elif opction_validated == 4:
        while True:
            menu_sec_1()
            option_input = input('Seleccione una opción del menú: ').strip()
            opction_validated = filter_option_int(option_input)
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:
                pass
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ===============================================================================================================
    elif opction_validated == 5:
        while True:
            menu_sec_1()
            option_input = input('Seleccione una opción del menú: ').strip()
            opction_validated = filter_option_int(option_input)
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:
                pass
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 6:
                pass
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ===============================================================================================================
    elif opction_validated == 6:
        print('\n*** HASTA PRONTO ***\n')
    else:
        print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    
