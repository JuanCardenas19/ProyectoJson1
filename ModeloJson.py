class modeloFormula:
    def __init__(self):
        pass
    
    def crearArchivo(datoTexto):
        nombreArchivo=str(input("Elige El Nombre De Tu Archivo: "))
        nombreArchivo=nombreArchivo+".Txt"
        with open(nombreArchivo,"w") as archivoTexto:
            archivoTexto.write(datoTexto)
            mensaje="Archivo Creado.."
        archivoTexto.close()
        return mensaje

    def leerArchivo():
        with open("Datos.txt","r") as archivo:
            datoContenido=archivo.read()
            print(datoContenido)
            archivo.close()
            
    def leerLinea():
        with open("Datos.txt","r") as archivo:
            datoContenido=archivo.readline()
            print(datoContenido)
            archivo.close()
            
    def leerLineas():
        with open("Datos.txt","r") as archivo:
            datoContenido=archivo.readlines()
            print(datoContenido)
            print("Cantidad de lineas: ",len(datoContenido))
            archivo.close()
            
    def escribeCadenas():
        listaDatos=["Primera Linea.\n","Segunda Linea\n","Tercera Linea\n"]
        with open("Datos.txt","w") as archivo:
            archivo.writelines(listaDatos)
            print("Cantidad de lineas: ",len(listaDatos))
            archivo.close()
    
    
    crearArchivo()
    leerArchivo()
    leerLinea()
    leerLineas()
    escribeCadenas()