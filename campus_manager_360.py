
#GESTION ACADEMICA

#Clase Padre (Superclase): Define los atributos comunes para cualquier persona.
class Persona:
    #Constructor
    def __init__(self, nombre, apaterno, amaterno, edad):
        self.__nombre = nombre
        self.__apaterno = apaterno
        self.__amaterno = amaterno
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apaterno(self):
        return self.__apaterno

    @property
    def amaterno(self):
        return self.__amaterno

    @property
    def edad(self):
        return self.__edad

class Estudiante(Persona):
    # Constructor: Recibe datos de persona + datos escolares.
    def __init__(self, nombre, apaterno, amaterno, edad, expediente, carrera, semestre, promedio):
        #Usamos super() para enviar los datos comunes al constructor de Persona.
        super().__init__(nombre, apaterno, amaterno, edad)
        self.__expediente = expediente
        self.__carrera = carrera
        self.__semestre = semestre
        self.__promedio = float(promedio)

    @property
    def expediente(self):
        return self.__expediente

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera

    @property
    def semestre(self):
        return self.__semestre

    @semestre.setter
    def semestre(self, nuevo_semestre):
        self.__semestre = nuevo_semestre

    @property
    def promedio(self):
        return self.__promedio

    @promedio.setter
    def promedio(self, nuevo_promedio):
        self.__promedio = float(nuevo_promedio)

    def mostrar_datos(self):
        print("--- DATOS DEL ESTUDIANTE ---")
        print(f"Expediente: {self.expediente}")
        print(f"Nombre: {self.nombre} {self.apaterno}")
        print(f"Carrera: {self.carrera} | Semestre: {self.semestre}")
        print(f"Promedio: {self.promedio}")

class Profesor(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, num_empleado, area_docente):
        Persona.__init__(self, nombre, apaterno, amaterno, edad)
        self.__num_empleado = num_empleado
        self.__area_docente = area_docente

    @property
    def num_empleado(self):
        return self.__num_empleado

    @property
    def area_docente(self):
        return self.__area_docente

    @area_docente.setter
    def area_docente(self, nueva_area):
        self.__area_docente = nueva_area

class Investigador(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, linea_investigacion, publicaciones):
        # Inicializa la parte de Persona.
        Persona.__init__(self, nombre, apaterno, amaterno, edad)
        self.__linea_investigacion = linea_investigacion
        self.__publicaciones = int(publicaciones)

    # --- Propiedades (Getters y Setters) ---
    @property
    def linea_investigacion(self):
        return self.__linea_investigacion

    @linea_investigacion.setter
    def linea_investigacion(self, nueva_linea):
        self.__linea_investigacion = nueva_linea

    @property
    def publicaciones(self):
        return self.__publicaciones

    @publicaciones.setter
    def publicaciones(self, nuevas_pubs):
        self.__publicaciones = int(nuevas_pubs)


# Clase de Herencia Múltiple: Combina Profesor e Investigador.
class ProfesorInvestigador(Profesor, Investigador):
    def __init__(self, nombre, apaterno, amaterno, edad, num_empleado, area_docente, linea_inv, publicaciones):
        Profesor.__init__(self, nombre, apaterno, amaterno, edad, num_empleado, area_docente)
        Investigador.__init__(self, nombre, apaterno, amaterno, edad, linea_inv, publicaciones)

    def mostrar_datos(self):
        print("--- DATOS PROFESOR INVESTIGADOR ---")
        print(f"Empleado: {self.num_empleado}")
        print(f"Nombre: {self.nombre}")
        print(f"Area: {self.area_docente}")
        print(f"Linea Investigación: {self.linea_investigacion}")
        print(f"Publicaciones: {self.publicaciones}")

class ControlAcademico:
    def __init__(self):
        # Listas para guardar los objetos.
        self.lista_estudiantes = []
        self.lista_profesores = []

    def registrar_estudiante(self):
        print("\n--- REGISTRAR ESTUDIANTE ---")
        exp = input("Ingresa el expediente: ")

        existe = False
        for est in self.lista_estudiantes:
            if est.expediente == exp:
                existe = True
                break

        if existe:
            print("Error: Ya existe un estudiante con ese expediente.")
        else:
            nom = input("Nombre: ")
            apa = input("Apellido Paterno: ")
            ama = input("Apellido Materno: ")
            edad = input("Edad: ")
            carrera = input("Carrera: ")
            sem = input("Semestre: ")
            prom = float(input("Promedio (0-10): "))

            if prom >= 0 and prom <= 10:
                est = Estudiante(nom, apa, ama, edad, exp, carrera, sem, prom)
                self.lista_estudiantes.append(est)
                print("Estudiante registrado correctamente.")
            else:
                print("Error: El promedio debe estar entre 0 y 10.")

    #Imprime la lista completa de estudiantes registrados
    def mostrar_estudiantes(self):
        print("\n--- LISTADO DE ESTUDIANTES ---")
        if not self.lista_estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for est in self.lista_estudiantes:
                est.mostrar_datos()

    #Busca por expediente y permite editar carrera, semestre y promedio
    def actualizar_estudiante(self):
        exp = input("\nIngresa el expediente del estudiante a modificar: ")

        encontrado = False
        for est in self.lista_estudiantes:
            if est.expediente == exp:
                print(f"Estudiante encontrado: {est.nombre}")
                nueva_carrera = input("Nueva carrera: ")
                nuevo_semestre = input("Nuevo semestre: ")
                nuevo_promedio = float(input("Nuevo promedio: "))

                if nuevo_promedio >= 0 and nuevo_promedio <= 10:
                    #actualizar los valores encapsulados.
                    est.carrera = nueva_carrera
                    est.promedio = nuevo_promedio
                    est.semestre = nuevo_semestre
                    print("Datos actualizados correctamente.")
                else:
                    print("Error: Promedio invalido.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontro un estudiante con ese expediente.")

    def registrar_profesor_investigador(self):
        print("\n--- REGISTRAR PROFESOR INVESTIGADOR ---")
        num = input("Ingresa numero de empleado: ")

        existe = False
        for p in self.lista_profesores:
            if p.num_empleado == num:
                existe = True
                break

        if existe:
            print("Error: Ya existe ese numero de empleado.")
        else:
            nom = input("Nombre: ")
            apa = input("Apellido Paterno: ")
            ama = input("Apellido Materno: ")
            edad = input("Edad: ")
            area = input("Area Docente: ")
            linea = input("Linea de Investigacion: ")
            pubs = int(input("Cantidad de Publicaciones: "))

            if pubs >= 0:
                pi = ProfesorInvestigador(nom, apa, ama, edad, num, area, linea, pubs)
                self.lista_profesores.append(pi)
                print("Profesor Investigador registrado correctamente.")
            else:
                print("Error: Las publicaciones no pueden ser negativas.")

    def mostrar_profesores(self):
        print("\n--- LISTADO PROFESORES INVESTIGADORES ---")
        if not self.lista_profesores:
            print("No hay registros.")
        else:
            for p in self.lista_profesores:
                p.mostrar_datos()

    # Busca por numero de empleado y actualiza sus datos
    def actualizar_profesor(self):
        num = input("\nIngresa el numero de empleado a modificar: ")
        encontrado = False

        for p in self.lista_profesores:
            if p.num_empleado == num:
                print(f"Profesor encontrado: {p.nombre}")
                nueva_area = input("Nueva Area Docente: ")
                nueva_linea = input("Nueva Linea Investigacion: ")
                nuevas_pubs = int(input("Nuevas Publicaciones: "))

                if nuevas_pubs >= 0:
                    p.area_docente = nueva_area
                    p.linea_investigacion = nueva_linea
                    p.publicaciones = nuevas_pubs
                    print("Datos actualizados correctamente.")
                else:
                    print("Error: Publicaciones invalidas.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontro el profesor.")


#BIBLIOTECA

class Libro:
    def __init__(self, titulo, autor, numPaginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__numPaginas = int(numPaginas)
        self.__disponible = True  # Por defecto al crear un libro esta disponible.

    # Propiedades (Getters y Setters)
    @property
    def titulo(self): return self.__titulo

    @property
    def autor(self): return self.__autor

    @property
    def numPaginas(self): return self.__numPaginas

    @property
    def disponible(self): return self.__disponible

    @disponible.setter
    def disponible(self, valor): self.__disponible = valor


class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def registrar_libro(self):
        t = input("Ingresa el titulo: ")
        a = input("Ingresa el autor: ")
        p = int(input("Ingresa numero de paginas: "))

        if p > 0:
            nuevo_libro = Libro(t, a, p)
            self.lista_libros.append(nuevo_libro)
            print("Libro registrado exitosamente.")
        else:
            print("Error: El libro debe tener mas de 0 paginas.")

    def listar_libros(self):
        print("\n--- CATALOGO BIBLIOTECA ---")
        if not self.lista_libros:
            print("No hay libros registrados.")
        else:
            for l in self.lista_libros:
                #True/False a texto
                if l.disponible:
                    estado = "Disponible"
                else:
                    estado = "Prestado"
                print(f"Titulo: {l.titulo}, Paginas: {l.numPaginas}, Estado: {estado}")

    #Busca por titulo y cambia su estado.
    def cambiar_disponibilidad(self):
        busq = input("Ingresa el titulo del libro a buscar: ")
        encontrado = False
        for l in self.lista_libros:
            if l.titulo.lower() == busq.lower():  # Compara minusculas para evitar errores.
                if l.disponible:
                    l.disponible = False
                    print("El libro ahora esta Prestado.")
                else:
                    l.disponible = True
                    print("El libro ahora esta Disponible.")
                encontrado = True
                break

        if not encontrado:
            print("Libro no encontrado.")

#TRANSPORTE

class Vehiculo:
    def __init__(self, marca, consumo):
        self.__marca = marca
        self.__consumo = float(consumo)

    @property
    def marca(self): return self.__marca

    @property
    def consumo(self): return self.__consumo

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Consumo: {self.consumo} L/km")

    def calcular_costo_viaje(self, distancia, precio):
        pass


class Automovil(Vehiculo):
    def mostrar_informacion(self):
        print("----- AUTOMOVIL -----")
        super().mostrar_informacion()

    def calcular_costo_viaje(self, distancia, precio):
        return (distancia * self.consumo) * precio

class Motocicleta(Vehiculo):
    def mostrar_informacion(self):
        print("----- MOTOCICLETA -----")
        super().mostrar_informacion()

    def calcular_costo_viaje(self, distancia, precio):
        return (distancia * self.consumo) * precio

class Camion(Vehiculo):
    def __init__(self, marca, consumo, costo_extra):
        # Llama al constructor del padre.
        super().__init__(marca, consumo)
        self.__costo_extra = float(costo_extra)

    def mostrar_informacion(self):
        print("----- CAMION -----")
        super().mostrar_informacion()
        print(f"Costo extra: ${self.__costo_extra}")

    def calcular_costo_viaje(self, distancia, precio):
        costo_base = (distancia * self.consumo) * precio
        return costo_base + self.__costo_extra


#Polimorfismo
def calcular_costos(vehiculos, distancia, precio):
    print("\n--- REPORTE DE COSTOS DE VIAJE ---")
    if not vehiculos:
        print("No hay vehiculos registrados.")
    else:
        for v in vehiculos:
            #POLIMORFISMO
            v.mostrar_informacion()
            costo = v.calcular_costo_viaje(distancia, precio)
            print(f"Costo del viaje: ${costo}")
            print("-------------------------")

#MENUS

control_acad = ControlAcademico()
mi_biblioteca = Biblioteca()
lista_vehiculos_global = []

def menu_academico():
    while True:
        print("\n--- GESTION ACADEMICA ---")
        print("1. Registrar Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Actualizar Estudiante")
        print("4. Registrar Profesor Investigador")
        print("5. Mostrar Profesores Investigadores")
        print("6. Actualizar Profesor Investigador")
        print("7. Volver")

        op = int(input("Ingresa la opcion: "))

        if op == 1:
            control_acad.registrar_estudiante()
        elif op == 2:
            control_acad.mostrar_estudiantes()
        elif op == 3:
            control_acad.actualizar_estudiante()
        elif op == 4:
            control_acad.registrar_profesor_investigador()
        elif op == 5:
            control_acad.mostrar_profesores()
        elif op == 6:
            control_acad.actualizar_profesor()
        elif op == 7:
            break
        else:
            print("Opcion invalida.")

def menu_biblioteca():
    while True:
        print("\n--- BIBLIOTECA ---")
        print("1. Registrar Libro")
        print("2. Listar Libros")
        print("3. Cambiar Disponibilidad")
        print("4. Volver")

        op = int(input("Ingresa la opcion: "))

        if op == 1:
            mi_biblioteca.registrar_libro()
        elif op == 2:
            mi_biblioteca.listar_libros()
        elif op == 3:
            mi_biblioteca.cambiar_disponibilidad()
        elif op == 4:
            break
        else:
            print("Opcion invalida.")


def menu_transporte():
    while True:
        print("\n--- GESTION VEHICULAR ---")
        print("1. Agregar Automovil")
        print("2. Agregar Motocicleta")
        print("3. Agregar Camion")
        print("4. Calcular Costos (Polimorfismo)")
        print("5. Volver")

        op = int(input("Ingresa la opcion: "))

        if op == 1:
            marca = input("Marca: ")
            consumo = float(input("Consumo (L/Km): "))
            if consumo > 0:
                v = Automovil(marca, consumo)
                lista_vehiculos_global.append(v)
                print("Automovil agregado.")
            else:
                print("Consumo debe ser mayor a 0.")

        elif op == 2:
            marca = input("Marca: ")
            consumo = float(input("Consumo (L/Km): "))
            if consumo > 0:
                v = Motocicleta(marca, consumo)
                lista_vehiculos_global.append(v)
                print("Motocicleta agregada.")
            else:
                print("Consumo debe ser mayor a 0.")

        elif op == 3:
            marca = input("Marca: ")
            consumo = float(input("Consumo (L/Km): "))
            if consumo > 0:
                extra = float(input("Costo Extra por Carga: "))
                v = Camion(marca, consumo, extra)
                lista_vehiculos_global.append(v)
                print("Camion agregado.")
            else:
                print("Consumo debe ser mayor a 0.")

        elif op == 4:
            if lista_vehiculos_global:
                dist = float(input("Ingresa distancia del viaje (km): "))
                precio = float(input("Ingresa precio combustible: "))
                calcular_costos(lista_vehiculos_global, dist, precio)
            else:
                print("No hay vehiculos para calcular.")

        elif op == 5:
            break
        else:
            print("Opcion invalida.")


def menu_principal():
    while True:
        print("\n===== CAMPUS MANAGER 360 =====")
        print("1. Gestion Academica")
        print("2. Biblioteca")
        print("3. Transporte")
        print("4. Salir")

        opcion = int(input("Ingresa opcion: "))

        if opcion == 1:
            menu_academico()
        elif opcion == 2:
            menu_biblioteca()
        elif opcion == 3:
            menu_transporte()
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no reconocida.")

menu_principal()