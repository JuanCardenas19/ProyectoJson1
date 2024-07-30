import json

from VistaJson import Vista
class Controlador:
    def __init__(self):
        pass

    def pasarDatos(self,datos):
        datosPersona=json.dumps(datos)
        with open("baseDatos.txt", "w") as archivo:
            json.dump(datosPersona,archivo)



objControlador=Controlador()
objVIsta=Vista(objControlador)
objVIsta.crearVentana()