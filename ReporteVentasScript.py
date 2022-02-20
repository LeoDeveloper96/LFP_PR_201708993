class ReporteVentas:

    def __init__(self):
        self.mes = None
        self.periodo = None
        self.productos = None
        self.instrucciones = None

    # Setters

    def setMes(self, mes):
        self.mes = mes

    def setPeriodo(self, periodo):
        self.periodo = periodo

    def setProductos(self, productos):
        self.productos = productos

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    # Getters

    def getMes(self):
        return self.mes

    def getPeriodo(self):
        return self.periodo

    def getProductos(self):
        return self.productos

    def setInstrucciones(self):
        return self.instrucciones
