class Producto:

    def __init__(self):
        self.nombre = None
        self.precio = None
        self.ventas = None

    #Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio

    def setVentas(self, ventas):
        self.ventas = ventas

    #Getters
    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getVentas(self):
        return self.ventas
