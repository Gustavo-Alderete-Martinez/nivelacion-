from csv import csv # Importa el modulo csv


class Main(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menu(self): # Metodo que muestra el menu del sistema
        productos = Productos() # Crea un objeto de la clase csv
        
        while True:
            print("0.-menu alumnos")
            print("s.-Salir")
            option = input("selecciona una opcion: ")
            if option == "0":
                while True: # Bucle infinito para mostrar las opciones del sistema
                    print("0.- Listar alumnos") # Opcion para listar los alumnos
                    print("1.- Insertar alumnos") # Opcion para insertar un nuevo alumno
                    print("2.- Buscar producto por matricula") # Opcion para buscar alumnos por matricula
                    print("3.- Actualizar alumno") # Opcion para actualizar un alumno
                    print("4.- Borrar alumno") # Opcion para borrar un alumno
                    print("5.- Promedio grupo") # muestra el promedio  grupal
                    print("5.- Promedio mas alto")# muestra el promedio maas alto
                    print("7.- promedio mas bajo")# muestra el promedio mas bajo
                    print("s.- Salir") # Opcion para salir del sistema
                
                    opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
                    
                    if opcion == "0": # Valida si la opcion elegida es el 0
                        productos.listarAlumnos() # Llama al metodo listarProductos a traves del objeto productos
                    
                    elif opcion == "1": # Valida si la opcion elegida es el 1
                        productos.insertarAlumno() # llama al metodo inserttarAlumnos()
                        print("Llamar metodo listarAlumnos()")
                    elif opcion == "2": # Valida si la opcion elegida es el 2
                        productos.buscarAlumnos() #llamar al metodo buscarAlumnos()
                        print("Llamar metodo buscarAlumnos()")
                    elif opcion == "3": # Valida si la opcion elegida es el 3
                        productos.actualizarAlumnos() # llma al metodo actualizarAlumnos()
                        print("Llamar metodo actualizarAlumnos()")
                    elif opcion == "4": # Valida si la opcion elegida es el 4
                        productos.borrarAlumnos() # llama al metodo borrarAlumnos()
                        print("Llamar metodo borrarAlumnos()")
                    elif opcion == "5": # Valida si la opcion elegida es el 4
                        productos.borrarAlumnos() # llama al metodo borrarAlumnos()
                        print("Llamar metodo borrarAlumnos()")
                            
                    elif opcion == "s": # Valida si la opcion elegida es el 5
                        break
                    else:   
                        print("Opción no válida. Intente de nuevo.")
          
if __name__ == "__main__": # Define el modulo principal
    principal = Main() # Crea un objeto de la clase Main
    principal.menu() # Llama al metodo menu a traves del objeto principa
