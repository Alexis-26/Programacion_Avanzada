from tkinter import *
from Registro_Productos import producto
from tkinter import messagebox

class Ventana_admin():
    #diccionario de productos
    base_de_datos_Productos = []
    def __init__(self):
        #Crear ventana
        self.ventana_dos = Tk()
        self.config_ventana_registro()
        self.encabezado_ventana_dos()
        self.Texto_registro()
        self.Entry_registro()
        self.Registrar_datos()
        self.btn_registro()
        self.btn_imprimir()
        self.btn_atras()
        self.ventana_dos.mainloop()

    def config_ventana_registro(self):
        #Configuración de la segunda ventana
        self.ventana_dos.geometry("900x600+190+20")
        self.ventana_dos.resizable(width=False, height=False)

    def encabezado_ventana_dos(self):
        #Configuración de los elementos de la segunda ventana
        self.ventana_dos.title("Registro")
        self.ventana_dos.config(background="#dff3ff")
        Encabezado = Label(self.ventana_dos, background="#6499e9", width=190, height=3)
        Encabezado.pack()
        

        #Agregar paneles de texto a la segunda ventana
    def Texto_registro(self):
        Registro_txt = Label(self.ventana_dos, text= "Registrar",
                            font= ("Calibri", 35),
                            bg= "#dff3ff",
                            fg= "grey37")
        Registro_txt.place(x = 370, y = 100)
        
        Seccion_txt = Label(self.ventana_dos, text= "SECCION",
                           font= ("Calibri", 15),
                           bg= "#dff3ff",
                           fg= "grey37")
        Seccion_txt.place(x = 210, y = 190)
        
        Modelo_txt = Label(self.ventana_dos, text= "MODELO",
                           font= ("Calibri", 15),
                           bg= "#dff3ff",
                           fg= "grey37")
        Modelo_txt.place(x = 500, y = 190)
        
        Nombre_txt = Label(self.ventana_dos, text= "NOMBRE",
                           font= ("Calibri", 15),
                           bg= "#dff3ff",
                           fg= "grey37")
        Nombre_txt.place(x = 210, y = 300)
        
        Descripcion_txt = Label(self.ventana_dos, text= "DESCRIPCION",
                           font= ("Calibri", 15),
                           bg= "#dff3ff",
                           fg= "grey37")
        Descripcion_txt.place(x = 500, y = 300)
        
        Codigo_txt = Label(self.ventana_dos, text= "CODIGO",
                           font= ("Calibri", 15),
                           bg= "#dff3ff",
                           fg= "grey37")
        Codigo_txt.place(x = 210, y = 410)
        
        Precio_txt = Label(self.ventana_dos, text= "PRECIO",
                           font= ("Calibri", 15),
                           bg= "#dff3ff",
                           fg= "grey37")
        Precio_txt.place(x = 500, y = 410)
        
    def Entry_registro(self):
        
        self.Seccion = Entry(self.ventana_dos, highlightthickness = 2, highlightcolor = "blue", selectbackground = "pink", selectforeground = "green")
        self.Seccion.config(width= 15, font= "Arial 18")
        self.Seccion.place(x = 210, y = 220)
        
        self.Nombre = Entry(self.ventana_dos, highlightthickness = 2, highlightcolor = "blue", selectbackground = "pink", selectforeground = "green")
        self.Nombre.config(width= 15, font= "Arial 18")
        self.Nombre.place(x = 210, y = 330)
        
        self.Codigo = Entry(self.ventana_dos, highlightthickness = 2, highlightcolor = "blue", selectbackground = "pink", selectforeground = "green")
        self.Codigo.config(width= 15, font= "Arial 18")
        self.Codigo.place(x = 210, y = 440)
        
        self.Modelo = Entry(self.ventana_dos, highlightthickness = 2, highlightcolor = "blue", selectbackground = "pink", selectforeground = "green")
        self.Modelo.config(width= 15, font= "Arial 18")
        self.Modelo.place(x = 500, y = 220)
        
        self.Descripcion = Entry(self.ventana_dos, highlightthickness = 2, highlightcolor = "blue", selectbackground = "pink", selectforeground = "green")
        self.Descripcion.config(width= 15, font= "Arial 18")
        self.Descripcion.place(x = 500, y = 330)
        
        self.Precio = Entry(self.ventana_dos, highlightthickness = 2, highlightcolor = "blue", selectbackground = "pink", selectforeground = "green")
        self.Precio.config(width= 15, font= "Arial 18")
        self.Precio.place(x = 500, y = 440)
        
    def btn_registro(self):
        #Se realiza el boton para ingresar una vez que los datos se escribieron correcatamente
        boton_registrar = Button(self.ventana_dos,
                                 text= "Registrar",
                                 font=("Arial", 12 ,"bold"),
                                 foreground="white",
                                 width= 20, height= 1,
                                 anchor=N,
                                 command=self.Registrar_datos)
        
        boton_registrar.config(bg="#6499e9", relief=FLAT, activebackground="white")
        
        boton_registrar.place(relx=0.25, rely=0.85)
        
    def Registrar_datos(self):
        #Obtener los valores ingresados
        Seccion_capturada = self.Seccion.get()
        
        Nombre_capturada = self.Nombre.get()
        
        Codigo_capturada = self.Codigo.get()
        
        Modelo_capturada = self.Modelo.get()
        
        Descripcion_capturada = self.Descripcion.get()
        
        Precio_capturada = self.Precio.get()

        # Verificar si todos los campos están llenos
        if Seccion_capturada and Nombre_capturada and Codigo_capturada and Modelo_capturada and Descripcion_capturada and Precio_capturada:
            # Crear una instancia de la clase producto
            producto_capturado = producto(Seccion_capturada, Modelo_capturada, Nombre_capturada, Codigo_capturada,
                                        Descripcion_capturada, Precio_capturada)
        
            datos_capturados = producto_capturado.Codigo, producto_capturado.Nombre, producto_capturado.Seccion, producto_capturado.Modelo, producto_capturado.Descripcion, producto_capturado.Precio
            self.base_de_datos_Productos.append(datos_capturados)
            self.Codigo.delete(0, END)
            self.Nombre.delete(0, END)
            self.Seccion.delete(0, END)
            self.Modelo.delete(0, END)
            self.Descripcion.delete(0, END)
            self.Precio.delete(0, END)
            messagebox.showinfo(title="Registro", message="Producto registrado correctamente")
        else:
            messagebox.showinfo(title="Registro", message="Ingrese los datos")

    def datos_validos(self):
        if self.base_de_datos_Productos:
            mensaje = " "
            for i in self.base_de_datos_Productos:
                mensaje = mensaje + f"{i}\n"
            messagebox.showinfo(title="Registro", message=mensaje)
        else:
            messagebox.showwarning(title="Registro", message="No existe registros")
            
    def btn_imprimir(self):
        boton_imprimir = Button(self.ventana_dos,
                                 text= "Imprimir Producto",
                                 font=("Arial", 12 ,"bold"),
                                 foreground="white",
                                 width= 20, height= 1,
                                 anchor=N,
                                 command=self.datos_validos)
        
        boton_imprimir.config(bg="#6499e9", relief=FLAT, activebackground="white")
        
        boton_imprimir.place(relx=0.5, rely=0.85)
        
    def btn_atras(self):
        boton_registrar = Button(self.ventana_dos,
                                 text= "Cerrar Sesion",
                                 font=("Arial", 12 ,"bold"),
                                 foreground="white",
                                 width= 20, height= 1,
                                 anchor=N,
                                 command=self.cerrar_sesion)
        
        boton_registrar.config(bg="#6499e9", relief=FLAT, activebackground="white")
        
        boton_registrar.place(relx=0.76, rely=0.02)

    def cerrar_sesion(self):
        from Interfaz_General import Ventana_Principal
        messagebox.showinfo(title="Sesion", message="¡Hasta pronto!")
        self.ventana_dos.withdraw()
        ventana_principal = Ventana_Principal()
        ventana_principal.ventana.deiconify()
