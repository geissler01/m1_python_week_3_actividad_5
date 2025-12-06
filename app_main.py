from msm import *
from support_functions import *
from dates import *

students = b_students()
subjects = b_subjects()
assignments = b_assignment()

while True:
    menu_main()
    opction_validated = filter_option_int()
    # ============================================================================================================
    if opction_validated == 1:
        while True:
            menu_sec_1()
            opction_validated = filter_option_int()
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:  # registrar estudiante
                name_student = input('NOMBRE: ').strip()
                age_filtrated = filter_int_age()
                if age_filtrated == -1:
                    print('\nError. Edad no válida')
                    continue
                id_student_validated = check_id_student_repit(students)
                if id_student_validated == -1:
                    print('Los documentos deben ser únicos')
                    continue
                students = add_student(students, name_student, age_filtrated, id_student_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:   # listar
                show_students(students)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:   # Buscar estudiante
                id_student_validated = check_fast_id_student(students)
                if id_student_validated == -1:
                    continue
                check_student_id(students, id_student_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:        # del student
                id_student_validated = check_fast_id_student(students)
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
            opction_validated = filter_option_int()
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:    # Añadir materia

                code_validated = check_code_subject_repit(subjects)
                if code_validated == -1:
                    continue
                name_subject = input('NOMBRE MATERIA: ').strip()
                subjects = add_subject(subjects, code_validated, name_subject)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:  # Listar materias
                show_subjects(subjects)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:  # Consultar materia
                code_validated = check_code_subject(subjects)
                if code_validated == -1:
                    continue
                check_subject_code(subjects, code_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:    # Eliminar materia
                code_validated = check_code_subject(subjects)
                if code_validated == -1:
                    continue
                del_subject(subjects, code_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:    # Salir
                print('\nVolviendo al menú principal')
                break
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ===============================================================================================================
    elif opction_validated == 3:
        while True:
            menu_sec_3()
            opction_validated = filter_option_int()
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:  # Asignar materia a un estudiante     
                id_validated = check_fast_id_student(students)
                if id_validated == -1:
                    continue
                code_validated = check_code_subject(subjects)
                if code_validated == -1:
                    print('\nError: Código materia no existe')
                    continue
                assignments = add_subject_student(students, subjects, assignments, id_validated, code_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:  #Ver materias que tiene un estudiante
                id_validated = check_fast_id_student_2(students, assignments)
                if id_validated == -1:
                    print('\nError: El estudiante no existe')
                    continue
                check_subject_student(assignments, id_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:    # Consultar que estudiantes perteneces a una materia
                code_validated, name_subject = check_code_subject_2(assignments, subjects)
                if code_validated == -1:
                    print('\nError: La materia no tiene estudiantes matriculados')
                    continue
                student_in_subject(assignments, code_validated, name_subject)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:    # Retirar materias asignadas a un estudiante
                id_validated = check_fast_id_student_2(students, assignments)
                if id_validated == -1:
                    continue
                code_validated, name_subject = check_code_subject_2(assignments, subjects)
                if code_validated == -1:
                    continue
                assignments = del_subject_student(assignments, id_validated, code_validated, name_subject)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:
                print('\nVolviendo al menú principal')
                break
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ===============================================================================================================
    elif opction_validated == 4:
        while True:
            menu_sec_4()
            opction_validated = filter_option_int()
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:   #registrar nota
                id_validated = check_fast_id_student_2(students, assignments)
                if id_validated == -1:
                    continue
                note_validated = filter_float_note()
                if note_validated == -1:
                    print('\nError: Nota no válida (0.0 a 5.0)')
                    continue
                percent_validated = filter_int_percent()
                if percent_validated == -1:
                    print('\nError. Porcentaje no válido (0 a 100%)')
                    continue
                assignments = add_note_student(students, assignments, id_validated, note_validated, percent_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 2:   # ver notas asociadas a una materia
                code_validated, name_subject = check_code_subject_2(assignments, subjects)
                if code_validated == -1:
                    continue
                assignments = notes_related_subject(assignments, code_validated, name_subject)

            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 3:    #Consultar promedio final de un estudiante
                id_validated = check_fast_id_student_2(students, assignments)
                if id_validated == -1:
                    continue
                see_note_final_student(assignments, id_validated)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 4:    # Eliminar notas a un estudiante
                id_validated = check_fast_id_student_2(students, assignments)
                if id_validated == -1:
                    continue
                code_validated, name_subject = check_code_subject_2(assignments, subjects)
                if code_validated == -1:
                    continue
                del_note_assignment(assignments, students, id_validated, code_validated, name_subject)
            # ----------------------------------------------------------------------------------------------------
            elif opction_validated == 5:
                print('\nVolviendo al menú principal')
                break
            # ----------------------------------------------------------------------------------------------------
            else:
                print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    # ===============================================================================================================
    elif opction_validated == 5:
        while True:
            menu_sec_5()
            opction_validated = filter_option_int()
            # ----------------------------------------------------------------------------------------------------
            if opction_validated == 1:
                detailed_average_student(assignments)
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
        break
    else:
        print('\nError. Su elección no está en el menú, vuelva a intentarlo')
    
