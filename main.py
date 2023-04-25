import csv  # Importar la biblioteca csv para trabajar con archivos CSV

from alumnos import alumnos # Importa el modulo alumnos


class Main(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menu(self): # Metodo que muestra el menu del sistema
        alumnos = alumnos() # Crea un objeto de la clase Prodcutos

# Definir el nombre del archivo CSV y los nombres de las columnas
filename = "alumnos.csv"
fields = ["matricula", "nombre", "unidad1", "unidad2", "unidad3", "promedio"]

def mostrar_menu():# Función para mostrar el menú y obtener la opción seleccionada por el usuario
    print("=== MENÚ ===")
    print("1. Listar alumnos")
    print("2. Insertar alumno")
    print("3. Buscar alumno")
    print("4. Actualizar alumno")
    print("5. Borrar alumno")
    print("6. Promedio del grupo")
    print("7. Promedio más alto")
    print("8. Promedio más bajo")
    print("s. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion
  
  def insertar_alumno():# Función para insertar un nuevo alumno en el archivo CSV
    
    matricula = input("Matrícula: ")# Obtener los datos del nuevo alumno desde el usuario
    nombre = input("Nombre: ")
    unidad1 = float(input("Unidad 1: "))
    unidad2 = float(input("Unidad 2: "))
    unidad3 = float(input("Unidad 3: "))
    promedio = (unidad1 + unidad2 + unidad3) / 3  # Calcular el promedio

    
    alumno = {"matricula": matricula, "nombre": nombre, "unidad1": unidad1, "unidad2": unidad2, "unidad3": unidad3, "promedio": promedio}# Crear un nuevo diccionario con los datos del alumno

    
   with open(filename, "a", newline="") as csvfile:# Abrir el archivo CSV en modo de escritura y agregar el nuevo alumno
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writerow(alumno)
        print("Alumno insertado correctamente.")

def actualizar_alumno():
    matricula = input('Ingrese la matricula del alumno a actualizar: ')
    with open('alumnos.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for i in range(len(rows)):
            if rows[i][0] == matricula:
                nombre = input('Ingrese el nombre del alumno: ')
                unidad1 = float(input('Ingrese la calificación de la unidad 1: '))
                unidad2 = float(input('Ingrese la calificación de la unidad 2: '))
                unidad3 = float(input('Ingrese la calificación de la unidad 3: '))
                promedio = (unidad1 + unidad2 + unidad3) / 3
                rows[i] = [matricula, nombre, unidad1, unidad2, unidad3, promedio]
                with open('alumnos.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                print('Alumno actualizado correctamente.')
                return
        print('No se encontró ningún alumno con esa matrícula.')

def borrar_alumno():
    matricula = input('Ingrese la matricula del alumno a borrar: ')
    with open('alumnos.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for i in range(len(rows)):
            if rows[i][0] == matricula:
                del rows[i]
                with open('alumnos.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                print('Alumno borrado correctamente.')
                return
        print('No se encontró ningún alumno con esa matrícula.')
        
def promedio_grupo():
    with open("alumnos.csv", "r") as f:
        alumnos = csv.reader(f)
        next(alumnos)  # Salta la primera fila
        total = 0
        contador = 0
        for alumno in alumnos:
            total += float(alumno[5])
            contador += 1
        promedio = total / contador
        print("El promedio del grupo es:", promedio)
        
def promedio_mas_alto():
    with open("alumnos.csv", "r") as f:
        alumnos = csv.reader(f)
        next(alumnos)  # Salta la primera fila
        maximo = 0
        for alumno in alumnos:
            if float(alumno[5]) > maximo:
                maximo = float(alumno[5])
        print("El promedio más alto es:", maximo)
        
def promedio_mas_bajo():
    with open("alumnos.csv", "r") as f:
        alumnos = csv.reader(f)
        next(alumnos)  # Salta la primera fila
        minimo = float("inf")
        for alumno in alumnos:
            if float(alumno[5]) < minimo:
                minimo = float(alumno[5])
        print("El promedio más bajo es:", minimo)
        
           
