#---LISTAS---
lista_estudiante = []
lista_profesor = []
lista_investigador = []
lista_profesor_investigador = []
lista_libros = []
lista_vehiculos = []

#-------------GESTION ACADEMICA--------------
class Persona:
    def __init__(self, nombre, apaterno, amaterno, edad):
        self.__nombre = nombre
        self.__apaterno = apaterno
        self.__amaterno = amaterno
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apaterno(self):
        return self.__apaterno

    @apaterno.setter
    def apaterno(self, nuevo_apaterno):
        self.__apaterno = nuevo_apaterno

    @property
    def amaterno(self):
        return self.__amaterno

    @amaterno.setter
    def amaterno(self, nuevo_amaterno):
        self.__amaterno = nuevo_amaterno

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

class Estudiante(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, expediente, carrera, semestre, promedio):
        super.__init__(self, nombre, apaterno, amaterno, edad)
        self.__expediente = expediente
        self.__carrera = carrera
        self.__semestre = semestre
        self.__promedio = promedio

    @property
    def expediente(self):
        return self.__expediente

    @expediente.setter
    def expediente(self, nuevo_expediente):
        self.__expediente = nuevo_expediente

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera

    @property
    def semestre(self):
        return self.__semestreq

    @semestre.setter
    def semestre(self, nuevo_semestre):
        self.__semestre = nuevo_semestre

    @property
    def promedio(self):
        return self.__promedio

    @promedio.setter
    def promedio(self, nuevo_promedio):
        self.__promedio = nuevo_promedio

class Profesor(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, num_empleado, area_docente):
        Persona.__init__(self, nombre, apaterno, amaterno, edad)
        self.__num_empleado = num_empleado
        self.__area_docente = area_docente

    @property
    def num_empleado(self):
        return self.__num_empleado

    @num_empleado.setter
    def num_empleado(self, num_empleado):
        self.__num_empleado = num_empleado

    @property
    def area_docente(self):
        return self.__area_docente

    @area_docente.setter
    def area_docente(self, area_docente):
        self.__area_docente = area_docente

class Investigador(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, linea_investigacion, publicaciones):
        Persona.__init__(self, nombre, apaterno, amaterno, edad)
        self.__linea_investigacion = linea_investigacion
        self.__publicaciones = publicaciones

    @property
    def linea_investigacion(self):
        return self.__linea_investigacion

    @linea_investigacion.setter
    def linea_investigacion(self, linea_investigacion):
        self.__linea_investigacion = linea_investigacion

    @property
    def publicaciones(self):
        return self.__publicaciones

    @publicaciones.setter
    def publicaciones(self, publicaciones):
        self.__publicaciones = publicaciones

class ProfesorInvestigador(Profesor, Investigador):
    def __init__(self, nombre, apellido_paterno, apellido_materno, edad, num_empleado, area_docente,
                 linea_investigacion, publicaciones):
        Profesor.__init__(self, nombre, apellido_paterno, apellido_materno, edad, num_empleado, area_docente)
        Investigador.__init__(self, nombre, apellido_paterno, apellido_materno, edad, linea_investigacion,
                              publicaciones)

class ControlAcademico:
    def mostrar_estudiantes(self):
        if not lista_estudiante:
            print("La lista de profesores investigadores está vacía.")
        else:
            for es in lista_estudiante:
                print(f"Nombre: {es.nombre} {es.apellido_paterno} {es.apellido_materno}")
                print(f"Edad: {es.edad}")
                print(f"No. Empleado: {es.num_empleado}")
                print(f"Área Docente: {es.area_docente}")
                print(f"Línea de Investigación: {es.linea_investigacion}")
                print(f"Publicaciones: {es.publicaciones}")
                print("-" * 30)

#-------------BIBLIOTECA--------------
class Libro:
    def __init__(self, titulo, autor, numPaginas, disponible):
        self.__titulo = titulo
        self.__autor = autor
        self.__numPaginas = numPaginas
        self.__disponible = disponible

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    @property
    def numPaginas(self):
        return self.__numPaginas

    @numPaginas.setter
    def numPaginas(self, nuevo_numPaginas):
        self.__numPaginas = nuevo_numPaginas

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, nuevo_disponible):
        if isinstance(nuevo_disponible, bool):
            self.__disponible = nuevo_disponible
        else:
            print("Error: El estado debe ser True o False")


class Biblioteca():
    def __init__(self):
        self.libros = []

    def registrar_libro(self, libro):
        if libro.numPaginas > 0:
            self.libros.append(libro)
            print(f'El libro "{libro.titulo}" se agregó exitosamente!')
        else:
            print('\nEl número de páginas no es válido')

    def listar_libros(self):
        for libro in self.libros:
            print("-------------------------")
            print(f'Título: {libro.titulo}')
            print(f'Autor: {libro.autor}')
            print(f'Páginas: {libro.numPaginas}')

            estado_texto = "Disponible" if libro.disponible else "Reservado"
            print(f'Estado: {estado_texto}')

    def cambiar_disponibilidad(self, titulo_buscar):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_buscar.lower():
                libro.disponible = not libro.disponible

                nuevo_estado_texto = "Disponible" if libro.disponible else "Reservado"
                print(f"\nÉxito: El estado de '{libro.titulo}' cambió a: {nuevo_estado_texto}")
                return
        print(f"\nError: El libro '{titulo_buscar}' no fue encontrado.")


#-------------GESTION VEHICULAR--------------

class Vehiculo:
    def __init__(self, marca, consumo_combustibleKm):
        self.__marca = marca
        self.__consumo_combustibleKm = consumo_combustibleKm

    @property
    def consumo_combustibleKm(self):
        return self.__consumo_combustibleKm

    def calcular_costo_viaje(self, distancia, precio_combustible):
        pass

    def mostrar_informacion(self):
        print("Informacion del vehiculo")
        print("Marca:", self.__marca)


class Automovil(Vehiculo):
    def calcular_costo_viaje(self, distancia, precio_combustible):
        litros_utilizados = distancia * self.consumo_combustibleKm
        costo = litros_utilizados * precio_combustible
        return costo


class Motocicleta(Vehiculo):
    def calcular_costo_viaje(self, distancia, precio_combustible):
        litros_utilizados = distancia * self.consumo_combustibleKm
        costo = litros_utilizados * precio_combustible
        return costo


class Camion(Vehiculo):
    def __init__(self, marca, consumo_combustibleKm, costoExtra):
        super().__init__(marca, consumo_combustibleKm)
        self.costoExtra = costoExtra

    def calcular_costo_viaje(self, distancia, precio_combustible):
        litros_utilizados = distancia * self.consumo_combustibleKm
        costo = litros_utilizados * precio_combustible
        return costo + self.costoExtra


def calcular_costo(lista_vehiculos, distancia, precio):
    for vehiculo in lista_vehiculos:
        costo = vehiculo.calcular_costo_viaje(distancia, precio)
        vehiculo.mostrar_informacion()
        print("Costo del viaje:", costo)
        print("----------------------")


#-------------MENUS--------------
def menu_principal():
    while True:
        print("\nOPCIONES ")
        print("1. Registrar Profesor Investigador")
        print("2. Mostrar registro Profesor Investigador")
        print("3. Modificar los datos del profesor investigador")
        print("4. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':

            print("Opcion uno.")

        elif opcion == '2':

            print("Opcion dos.")
        elif opcion == '3':

            print("Opcion tres.")
        elif opcion == '4':
            print("Gracias...")
            break
        else:
            print("Opción no válida, intente de nuevo.")