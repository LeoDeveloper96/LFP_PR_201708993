import re
import webbrowser
import tkinter as tk
from tkinter import filedialog
from pip._vendor.distlib.compat import raw_input
from ProductoScript import Producto
from InstruccionScript import Instruccion
from ReporteVentasScript import ReporteVentas


class Script:
    data = ""
    instrucciones = ""
    listaProds = []
    listaInstrucciones = []

    def menu(self):
        print("\n")
        print("1 Cargar Data")
        print("2 Cargar Instrucciones")
        print("3 Analizar")
        print("4 Reportes")
        print("5 salir" + "\n")
        entrada = input("Ingrese un numero 1-5" + "\n")
        patron = "[1-5]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.cargarData()
                self.menu()
            elif entrada == "2":
                self.cargarInstrucciones()
                self.menu()
            elif entrada == "3":
                self.analizar()
                self.menu()
            elif entrada == "4":
                self.generarReporte()
                self.menu()
            elif entrada == "5":
                raw_input("Presione una tecla" + "\n")
        else:
            self.menu()

    def cargarData(self):
        root = tk.Tk()
        root.withdraw()
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.data"), ("todos", "*.*")))
        try:
            with open(nombre_archivo, "r", encoding="utf8") as archivo:
                self.data += archivo.read()
        except FileNotFoundError:
            print("archivo no encontrado")

    def cargarInstrucciones(self):
        root = tk.Tk()
        root.withdraw()
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.data"), ("todos", "*.*")))
        try:
            archivo = open(nombre_archivo, "r")
            self.instrucciones += archivo.read()
        except FileNotFoundError:
            print("archivo no encontrado")

    def analizar(self):
        reporteVentas = ReporteVentas()
        producto = Producto()
        cadProd = ""
        indice1 = 0
        indice2 = 0
        for linea in self.data.split('\n'):
            for caracter in linea:
                if caracter == ':':
                    reporteVentas.setMes(self.data[0:self.data.index(':')-1])
                    indice2 = self.data.index(':')
                elif caracter == '=':
                    reporteVentas.setPeriodo((self.data[self.data.index(':')+1:self.data.index('=') - 1]).strip())
                    indice2 = self.data.index('=')
                elif caracter == '[':
                    indice1 = self.data.find('[', indice1)+1
                    cadProd = self.data[indice1:(self.data.find(']', indice1+2))].strip()
                    detalles = cadProd.split(',')
                    producto.setNombre(detalles[0].replace("\"", ""))
                    producto.setPrecio(detalles[1])
                    producto.setVentas(detalles[2])
                    self.listaProds.append(producto)
                    producto = Producto()
                indice2 += 1
                indice1 += 1
        reporteVentas.setProductos(self.listaProds)
        a = 1




    def generarReporte(self):
        pass
