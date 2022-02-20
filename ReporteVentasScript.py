class ReporteVentas:

    def __init__(self):
        self.mes = None
        self.periodo = None
        self.productos = None

        # Setters
    def setMes(self, mes):
        self.mes = mes

    def setPeriodo(self, periodo):
        self.periodo = periodo

    def setProductos(self, productos):
        self.productos = productos

    # Getters
    def getMes(self):
        return self.mes

    def getPeriodo(self):
        return self.periodo

    def getProductos(self):
        return self.productos

