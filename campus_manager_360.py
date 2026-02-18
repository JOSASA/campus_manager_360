# ==========================================
#           LISTAS GLOBALES
# ==========================================
lista_estudiante = []
lista_profesor = []  # Opcional si decides usarlos por separado
lista_investigador = []  # Opcional si decides usarlos por separado
lista_profesor_investigador = []
lista_libros = []  # Se usará dentro de la clase Biblioteca
lista_vehiculos = []


# ==========================================
#           MODULO 1: GESTION ACADEMICA
# ==========================================
class Persona:
    def __init__(self, nombre, apaterno, amaterno, edad):
        self.__nombre = nombre
        self.__apaterno = apaterno
        self.__amaterno = amaterno
        self.__edad = edad

    @property
    def nombre(self): return self.__nombre

    @property
    def apaterno(self): return self.__apaterno

    @property
    def amaterno(self): return self.__amaterno

    @property
    def edad(self): return self.__edad


class Estudiante(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, expediente, carrera, semestre, promedio):
        super().__init__(nombre, apaterno, amaterno, edad)  # Corregido
        self.__expediente = expediente
        self.__carrera = carrera
        self.__semestre = semestre
        self.__promedio = promedio

    @property
    def expediente(self): return self.__expediente

    @property
    def carrera(self): return self.__carrera

    @property
    def semestre(self): return self.__semestre

    @property
    def promedio(self): return self.__promedio


class Profesor(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, num_empleado, area_docente):
        Persona.__init__(self, nombre, apaterno, amaterno, edad)
        self.__num_empleado = num_empleado
        self.__area_docente = area_docente

    @property
    def num_empleado(self): return self.__num_empleado

    @property
    def area_docente(self): return self.__area_docente


class Investigador(Persona):
    def __init__(self, nombre, apaterno, amaterno, edad, linea_investigacion, publicaciones):
        Persona.__init__(self, nombre, apaterno, amaterno, edad)
        self.__linea_investigacion = linea_investigacion
        self.__publicaciones = publicaciones

    @property
    def linea_investigacion(self): return self.__linea_investigacion

    @property
    def publicaciones(self): return self.__publicaciones


class ProfesorInvestigador(Profesor, Investigador):
    def __init__(self, nombre, apaterno, amaterno, edad, num_empleado, area_docente,
                 linea_investigacion, publicaciones):
        # Llamada explícita a los constructores padres
        Profesor.__init__(self, nombre, apaterno, amaterno, edad, num_empleado, area_docente)
        Investigador.__init__(self, nombre, apaterno, amaterno, edad, linea_investigacion, publicaciones)


# ==========================================
#           MODULO 2: BIBLIOTECA
# ==========================================
class Libro:
    def __init__(self, titulo, autor, numPaginas, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__numPaginas = numPaginas
        self.__disponible = disponible

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


class Biblioteca():
    def __init__(self):
        self.libros = []  # Usamos lista interna de la instancia

    def registrar_libro(self, libro):
        if int(libro.numPaginas) > 0:
            self.libros.append(libro)
            print(f'>> El libro "{libro.titulo}" se agregó exitosamente.')
        else:
            print('\n>> Error: El número de páginas no es válido.')

    def listar_libros(self):
        if not self.libros:
            print(">> No hay libros registrados.")
            return

        print("\n--- Catálogo de Libros ---")
        for libro in self.libros:
            print(f'Título: {libro.titulo}')
            print(f'Autor:  {libro.autor}')
            print(f'Págs:   {libro.numPaginas}')
            estado = "Disponible" if libro.disponible else "Prestado/Reservado"
            print(f'Estado: {estado}')
            print("-" * 25)

    def cambiar_disponibilidad(self, titulo_buscar):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_buscar.lower():
                libro.disponible = not libro.disponible
                nuevo_estado = "Disponible" if libro.disponible else "Prestado/Reservado"
                print(f"\n>> Éxito: El estado de '{libro.titulo}' cambió a: {nuevo_estado}")
                return
        print(f"\n>> Error: El libro '{titulo_buscar}' no fue encontrado.")


# Instancia global de la biblioteca
mi_biblioteca = Biblioteca()


# ==========================================
#           MODULO 3: GESTION VEHICULAR
# ==========================================
class Vehiculo:
    def __init__(self, marca, consumo_combustibleKm):
        self.__marca = marca
        self.__consumo_combustibleKm = consumo_combustibleKm

    @property
    def consumo_combustibleKm(self):
        return self.__consumo_combustibleKm

    def mostrar_informacion(self):
        tipo = self.__class__.__name__  # Obtiene el nombre de la clase (Auto, Moto, etc)
        print(f"[{tipo}] Marca: {self.__marca}")

    def calcular_costo_viaje(self, distancia, precio_combustible):
        pass


class Automovil(Vehiculo):
    def calcular_costo_viaje(self, distancia, precio_combustible):
        litros = distancia * self.consumo_combustibleKm
        return litros * precio_combustible


class Motocicleta(Vehiculo):
    def calcular_costo_viaje(self, distancia, precio_combustible):
        litros = distancia * self.consumo_combustibleKm
        return litros * precio_combustible


class Camion(Vehiculo):
    def __init__(self, marca, consumo_combustibleKm, costoExtra):
        super().__init__(marca, consumo_combustibleKm)
        self.costoExtra = costoExtra

    def calcular_costo_viaje(self, distancia, precio_combustible):
        litros = distancia * self.consumo_combustibleKm
        return (litros * precio_combustible) + self.costoExtra


# ==========================================
#           MENUS Y SUBMENUS
# ==========================================

def menu_academico():
    while True:
        print("\n--- SUBMENÚ: GESTIÓN ACADÉMICA ---")
        print("1. Registrar Estudiante")
        print("2. Registrar Profesor Investigador")
        print("3. Mostrar Estudiantes")
        print("4. Mostrar Profesores Investigadores")
        print("5. Regresar al Menú Principal")

        op = input("Seleccione: ")

        if op == '1':
            print("\n-> Datos del Estudiante:")
            n = input("Nombre: ")
            ap = input("Apaterno: ")
            am = input("Amaterno: ")
            e = input("Edad: ")
            exp = input("Expediente: ")
            c = input("Carrera: ")
            s = input("Semestre: ")
            p = input("Promedio: ")
            est = Estudiante(n, ap, am, e, exp, c, s, p)
            lista_estudiante.append(est)
            print(">> Estudiante registrado.")

        elif op == '2':
            print("\n-> Datos del Prof. Investigador:")
            n = input("Nombre: ")
            ap = input("Apaterno: ")
            am = input("Amaterno: ")
            e = input("Edad: ")
            num = input("No. Empleado: ")
            area = input("Área Docente: ")
            lin = input("Línea Investigación: ")
            pub = input("Publicaciones: ")
            pi = ProfesorInvestigador(n, ap, am, e, num, area, lin, pub)
            lista_profesor_investigador.append(pi)
            print(">> Profesor Investigador registrado.")

        elif op == '3':
            print("\n--- LISTA ESTUDIANTES ---")
            if not lista_estudiante: print(" (Vacía) ")
            for item in lista_estudiante:
                print(f"{item.nombre} {item.apaterno} | Carrera: {item.carrera}")

        elif op == '4':
            print("\n--- LISTA PROF. INVESTIGADORES ---")
            if not lista_profesor_investigador: print(" (Vacía) ")
            for item in lista_profesor_investigador:
                print(f"{item.nombre} {item.apaterno} | Área: {item.area_docente} | Inv: {item.linea_investigacion}")

        elif op == '5':
            break
        else:
            print("Opción inválida.")


def menu_biblioteca():
    while True:
        print("\n--- SUBMENÚ: BIBLIOTECA ---")
        print("1. Registrar Libro")
        print("2. Listar Libros")
        print("3. Prestar/Devolver Libro")
        print("4. Regresar al Menú Principal")

        op = input("Seleccione: ")

        if op == '1':
            t = input("Título: ")
            a = input("Autor: ")
            try:
                p = int(input("Número de Páginas: "))
                l = Libro(t, a, p)
                mi_biblioteca.registrar_libro(l)
            except ValueError:
                print(">> Error: Las páginas deben ser un número entero.")

        elif op == '2':
            mi_biblioteca.listar_libros()

        elif op == '3':
            busq = input("Ingrese el título exacto del libro: ")
            mi_biblioteca.cambiar_disponibilidad(busq)

        elif op == '4':
            break


def menu_vehicular():
    while True:
        print("\n--- SUBMENÚ: GESTIÓN VEHICULAR ---")
        print("1. Agregar Automóvil")
        print("2. Agregar Motocicleta")
        print("3. Agregar Camión")
        print("4. Calcular Costos de Viaje (Flota completa)")
        print("5. Regresar al Menú Principal")

        op = input("Seleccione: ")

        if op == '1':
            m = input("Marca del Auto: ")
            try:
                c = float(input("Consumo (Litros/Km, ej. 0.12): "))
                v = Automovil(m, c)
                lista_vehiculos.append(v)
                print(">> Automóvil agregado.")
            except ValueError:
                print(">> Error: Ingrese un número válido.")

        elif op == '2':
            m = input("Marca de la Moto: ")
            try:
                c = float(input("Consumo (Litros/Km, ej. 0.05): "))
                v = Motocicleta(m, c)
                lista_vehiculos.append(v)
                print(">> Motocicleta agregada.")
            except ValueError:
                print(">> Error: Ingrese un número válido.")

        elif op == '3':
            m = input("Marca del Camión: ")
            try:
                c = float(input("Consumo (Litros/Km, ej. 0.35): "))
                extra = float(input("Costo Extra (Peajes/Mantenimiento): "))
                v = Camion(m, c, extra)
                lista_vehiculos.append(v)
                print(">> Camión agregado.")
            except ValueError:
                print(">> Error: Ingrese un número válido.")

        elif op == '4':
            if not lista_vehiculos:
                print(">> No hay vehículos registrados.")
            else:
                try:
                    dist = float(input("Distancia del viaje (Km): "))
                    precio = float(input("Precio combustible (por Litro): "))
                    print("-" * 30)
                    total = 0
                    for v in lista_vehiculos:
                        costo = v.calcular_costo_viaje(dist, precio)
                        v.mostrar_informacion()
                        print(f"Costo: ${costo:.2f}")
                        total += costo
                        print("-" * 15)
                    print(f"TOTAL FLOTA: ${total:.2f}")
                except ValueError:
                    print(">> Error: Ingrese números válidos.")

        elif op == '5':
            break


def menu_principal():
    while True:
        print("\n################################")
        print("      SISTEMA INTEGRAL")
        print("################################")
        print("1. Gestión Académica")
        print("2. Biblioteca")
        print("3. Gestión Vehicular")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_academico()
        elif opcion == '2':
            menu_biblioteca()
        elif opcion == '3':
            menu_vehicular()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


# ==========================================
#           EJECUCION
# ==========================================
menu_principal()