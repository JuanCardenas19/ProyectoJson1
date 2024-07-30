import tkinter as ventana
class Vista:
    def __init__(self,objControlador):
        self.objControlador=objControlador

    def crearVentana(self):
        self.Ventana=ventana.Tk()
        self.Ventana.title("Menu")
        self.Ventana.minsize(width=300, height=300)
        self.Ventana.config(background="#40cfff")
        botonCrear=ventana.Button(text="Crear Texto",command=self.crearTexto)
        botonCrear.pack(padx=10,pady=10)
        botonModificar=ventana.Button(text="Modificar Texto", command=self.modificarTexto)
        botonModificar.pack(padx=10,pady=10)
        botonMostrar=ventana.Button(text="Mostrar Texto", command=self.mostrarTexto)
        botonMostrar.pack(padx=10,pady=10)
        botonEliminar=ventana.Button(text="Eliminar Texto", command=self.eliminarTexto)
        botonEliminar.pack(padx=10,pady=10)
        botonSalir=ventana.Button(text="Salir",command=lambda:self.salir(self.Ventana))
        botonSalir.pack(padx=10,pady=10)

        self.Ventana.mainloop()

    def crearTexto(self):
        self.ventanaCrear=ventana.Toplevel()
        self.ventanaCrear.title("Creacion Del Texto")
        self.ventanaCrear.minsize(width=300,height=300)
        self.ventanaCrear.config(background="cyan")
        self.contenedor=ventana.Frame(self.ventanaCrear,bg="cyan")
        self.contenedor.pack(padx=20,pady=20)
        self.documentoId=ventana.StringVar()
        self.numeroDocumento=ventana.StringVar()
        self.nombre=ventana.StringVar()
        self.apellido=ventana.StringVar()
        self.edad=ventana.IntVar()
        self.correo=ventana.StringVar()
        self.genero=ventana.StringVar()
        generos=[("masculino","masculino"),("femenino","femenino"),("otro","otro")]
        documentos=[("cedula de ciudadania","cedula de ciudadania"),("tarjeta de identidad","tarjeta de identidad")]
        self.labelDocumentoId=ventana.Label(self.contenedor,text="Escoge el Tipo De Identidad")
        self.labelDocumentoId.grid(column=1,row=1)
        for texto, valor in documentos:
            ventana.Radiobutton(self.contenedor, text=texto, variable=self.documentoId, value=valor).grid(column=2, row=documentos.index((texto, valor))+1)
        self.labelNumeroDocumento=ventana.Label(self.contenedor,text="Ingresa el numero del documento")
        self.labelNumeroDocumento.grid(column=1,row=3)
        self.entryNumeroDocumento=ventana.Entry(self.contenedor,textvariable=self.numeroDocumento)
        self.entryNumeroDocumento.grid(column=2,row=3)
        self.labelNombre=ventana.Label(self.contenedor,text="Digita tu nombre")
        self.labelNombre.grid(column=1,row=4)
        self.entryNombre=ventana.Entry(self.contenedor,textvariable=self.nombre)
        self.entryNombre.grid(column=2,row=4)
        self.labelApellido=ventana.Label(self.contenedor,text="Digita tu apellido")
        self.labelApellido.grid(column=1,row=5)
        self.entryApellido=ventana.Entry(self.contenedor,textvariable=self.apellido)
        self.entryApellido.grid(column=2,row=5)
        self.labelEdad=ventana.Label(self.contenedor,text="Digita tu edad")
        self.labelEdad.grid(column=1,row=6)
        self.entryEdad=ventana.Entry(self.contenedor,textvariable=self.edad)
        self.entryEdad.grid(column=2,row=6)
        self.labelCorreo=ventana.Label(self.contenedor,text="Digita tu correo")
        self.labelCorreo.grid(column=1,row=7)
        self.entryCorreo=ventana.Entry(self.contenedor,textvariable=self.correo)
        self.entryCorreo.grid(column=2,row=7)
        self.labelGenero=ventana.Label(self.contenedor,text="Elige tu genero")
        self.labelGenero.grid(column=1,row=8)
        for texto, valor in generos:
            ventana.Radiobutton(self.contenedor, text=texto, variable=self.genero, value=valor).grid(column=2, row=generos.index((texto, valor))+8)
        self.botonRegistrar=ventana.Button(self.contenedor,text="Registrar datos",command=lambda:self.enviarDatos(self.numeroDocumento,self.documentoId,self.nombre,self.apellido,self.edad,self.correo,self.genero))
        self.botonRegistrar.grid(column=2,row=15)

    def enviarDatos(self,datoNumeroDocumento,datoDocumentoId,datoNombre,datoApellido,datoEdad,datoCorreo,datoGenero):
        numeroDocumento=datoDocumentoId.get()
        documentoID=datoNumeroDocumento.get()
        nombre=datoNombre.get()
        apellido=datoApellido.get()
        edad=datoEdad.get()
        correo=datoCorreo.get()
        genero=datoGenero.get()
        datos={"tipo de documento":numeroDocumento,"documento de identidad":documentoID,"nombre":nombre,"apellido":apellido,"edad":edad,"correo":correo,"genero":genero}
        self.objControlador.pasarDatos(datos)


    def modificarTexto(self):
        print("modificado")

    def mostrarTexto(self):
        print("mostrado")

    def eliminarTexto(self):
        print("eliminado")

    def salir(self,Ventana):
        Ventana.destroy()
            
