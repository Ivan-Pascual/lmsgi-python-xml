from utils import read
from clases.Movil import Movil
from clases.Fabricante import Fabricante

arrayMoviles = []

f = open('datos/moviles.xml')
moviles = read(f)
for movil in moviles:
    id = movil.attrib["id"]
    modelo = movil.attrib["modelo"]
    precio = movil.attrib["precio"]
    so = movil.attrib["SO"]

    fabricante = movil.find("fabricante")
    nombre = fabricante.attrib["nombre"]
    pais = fabricante.attrib["pais"]

    arrayMoviles.append(Movil(id,modelo,precio,so,Fabricante(nombre,pais)))


for a in arrayMoviles:
    print("Id: "+ a.id+"\nModelo: "+ a.modelo+"\nPrecio: "+ a.precio+"\nSO: "+ a.so+"\nNombre del fabricante: " + a.fabricante.nombre+"\nPais del fabricante: " + a.fabricante.pais+"\n")
