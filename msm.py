# ==============================================
def menu_main():
    print("""
            *** MENÚ PRINCIPAL ***
        
        1.  Gestión del estudiante
        2.  Gestión de materias
        3.  Asignaciones (Estudiantes <> Materias)
        4.  Notas y calificaciones
        5.  Reportes y estadísticas
        6.  Salir
        """)

# ==============================================
def menu_sec_1():
    print("""
            --- Gestión del estudiante ---
        
        1.  Registrar nuevo estudiante
        2.  Listar todos los estudiantes registrados
        3.  Consultar estudiante por ID
        4.  Eliminar estudiante por ID
        5.  Salir
        """)
# ==============================================
def menu_sec_2():
    print("""
            --- Gestión de materias ---
        
        1.  Registrar nueva materia (codigo, nombre)
        2.  Listar todas las meterias registradas
        3.  Consultar materia por código
        4.  Eliminar materia por código
        5.  Salir
        """)
# ==============================================
def menu_sec_3():
    print("""
            --- Asignaciones (Estudiantes <> Materias) ---
        
        1.  Asignar materia a un estudiante
        2.  Ver materias que tiene un estudiante
        3.  Consultar que estudiantes perteneces a una materia
        4.  Retirar materias asignadas a un estudiante
        5.  Salir
        """)
# ==============================================
def menu_sec_4():
    print("""
            --- Notas y calificaciones ---
        
        1.  Registrar nota a un estudiante (porcentaje, calificación)
        2.  Ver todas las notas asociadas a una materia
        3.  Consultar promedio final de un estudiante
        4.  Eliminar notas asignadas
        5.  Salir
        """)
# ==============================================
def menu_sec_5():
    print("""
            --- Reportes y estadísticas ---
        
        1.  Promedio detallado por estudiante
        2.  Estudiante con mayor promedio
        3.  Porcentaje de aprovación del grupo
        4.  Promedio general del curso
        5.  Ranking por desempeño
        6.  Salir
        """)

