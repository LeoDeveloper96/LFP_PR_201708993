class Instruccion:

    def __init__(self):
        self.nombre = None
        self.tipoGrafica = None
        self.titulo = None
        self.titulox = None
        self.tituloy = None

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setTipoGrafica(self, grafica):
        self.grafica = grafica

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setTitulox(self, titulox):
        self.titulox = titulox

    def setTituloy(self, tituloy):
        self.tituloy = tituloy

    # Getters
    def getNombre(self, nombre):
        self.nombre = nombre

    def getTipoGrafica(self, grafica):
        self.grafica = grafica

    def getTitulo(self, titulo):
        self.titulo = titulo

    def getTitulox(self, titulox):
        self.titulox = titulox

    def getTituloy(self, tituloy):
        self.tituloy = tituloy