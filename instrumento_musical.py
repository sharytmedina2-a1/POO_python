# Lista global para almacenar los instrumentos
lista_instrumentos = []

# CLASE PADRE
class Instrumento:

    def __init__(self, id_instrumento, nombre, marca, precio):
        self.id_instrumento = id_instrumento
        self.nombre = nombre
        self.marca = marca

        # ENCAPSULAMIENTO
        self.__precio = precio

    # GET
    def get_precio(self):
        return self.__precio

    # SET
    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
        print(f"Precio actualizado a ${nuevo_precio}")

    def mostrar_informacion(self):
        print(f"ID: {self.id_instrumento}")
        print(f"Nombre: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Precio: ${self.__precio}")

    # CRUD

    # CREATE
    def registrar_instrumento(self):
        lista_instrumentos.append(self)
        print(f"Instrumento {self.nombre} registrado correctamente.")

    # READ
    def consultar_instrumento(self):
        self.mostrar_informacion()

    # UPDATE
    def actualizar_instrumento(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print("Instrumento actualizado correctamente.")

    # DELETE
    def eliminar_instrumento(self):
        if self in lista_instrumentos:
            lista_instrumentos.remove(self)
            print("Instrumento eliminado correctamente.")

    # POLIMORFISMO
    def mantenimiento(self):
        pass


# HERENCIA
class Guitarra(Instrumento):

    def __init__(self, id_instrumento, nombre, marca, precio, numero_cuerdas):
        super().__init__(id_instrumento, nombre, marca, precio)
        self.numero_cuerdas = numero_cuerdas

    # POLIMORFISMO
    def mantenimiento(self):
        print(f"La guitarra {self.nombre} necesita cambio de cuerdas.")


# HERENCIA
class Piano(Instrumento):

    def __init__(self, id_instrumento, nombre, marca, precio, tipo):
        super().__init__(id_instrumento, nombre, marca, precio)
        self.tipo = tipo

    # POLIMORFISMO
    def mantenimiento(self):
        print(f"El piano {self.nombre} necesita afinación.")


# ABSTRACCIÓN (CREACIÓN DE OBJETOS)

guitarra_1 = Guitarra(
    1,
    "Guitarra Acústica",
    "Yamaha",
    800000,
    6
)

piano_1 = Piano(
    2,
    "Piano Digital",
    "Casio",
    2500000,
    "Digital"
)

# CREATE
guitarra_1.registrar_instrumento()
piano_1.registrar_instrumento()

# READ
guitarra_1.consultar_instrumento()
print("-------------------")
piano_1.consultar_instrumento()

# UPDATE
guitarra_1.actualizar_instrumento("Guitarra Clásica")

# ENCAPSULAMIENTO
print(f"Precio actual: ${guitarra_1.get_precio()}")

guitarra_1.set_precio(900000)

print(f"Nuevo precio: ${guitarra_1.get_precio()}")

# POLIMORFISMO
guitarra_1.mantenimiento()
piano_1.mantenimiento()

# DELETE
piano_1.eliminar_instrumento()

print(f"Cantidad de instrumentos registrados: {len(lista_instrumentos)}")