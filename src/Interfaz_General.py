from tkinter import *
import Usuarios_Login
from Ventana_Registro import Ventana_admin
from tkinter import messagebox

class Ventana_Principal():
    def __init__(self):
        #Crear ventana
        self.ventana = Tk()
        self.configuracion_ventana()
        self.encabezado_diseño()
        self.btn_login()
        self.entry_login()
        self.Texto_login()
        self.login_acceso = False
        self.ventana.mainloop()

    def configuracion_ventana(self):
        #Configuración de la ventana
        self.ventana.geometry("900x600+190+20")
        self.ventana.resizable(width=False, height=False)

    def encabezado_diseño(self):
        #Configuración de los elementos
        self.ventana.title("Sistema")
        self.ventana.config(background="#dff3ff")
        Encabezado = Label(self.ventana, background="#6499e9", width=190, height=3)
        Encabezado.pack()

        #Agregar paneles de texto a la ventana 
    def Texto_login(self):
        Ingresa_txt = Label(self.ventana, text= "Ingresá",
                            font= ("Calibri", 35),
                            bg= "#dff3ff",
                            fg= "grey37")
        Ingresa_txt.place(x = 390, y = 130)
        Inicio_txt = Label(self.ventana, text= "Iniciá sesión para continuar",
                           font= ("Calibri", 15),
                           bg= "#dff3ff",
                           fg= "grey37")
        Inicio_txt.place(x = 349, y = 200)
        Correo_txt = Label(self.ventana, text= "USUARIO",
                           font= ("Calibri", 13),
                           bg= "#dff3ff",
                           fg= "grey37")
        Correo_txt.place(x = 300, y = 270)
        Contraseña_txt = Label(self.ventana, text= "CONTRASEÑA",
                           font= ("Calibri", 13),
                           bg= "#dff3ff",
                           fg= "grey37")
        Contraseña_txt.place(x = 300, y = 370)

        #Datos capturados
    def entry_login(self):
        self.Nom_usuario = Entry(self.ventana, highlightthickness = 2, highlightcolor = "blue", selectbackground = "pink", selectforeground = "green")
        self.Nom_usuario.config(width= 25, font= "Arial 18")
        self.Nom_usuario.place(x = 300, y = 300)
        #Un segundo entry con un Show = que establece un * para sustituir los caracteres
        self.Contrasena = Entry(self.ventana, highlightthickness=2, highlightcolor="blue", selectbackground="pink", selectforeground="green", show="*")
        self.Contrasena.config(width= 25, font= "Arial 18")
        self.Contrasena.place(x=300, y=400)

    #Boton para ingresar a la siguiente ventana
    def btn_login(self):
        #Se realiza el boton para ingresar una vez que los datos se escribieron correcatamente
        boton_ingresar = Button(self.ventana,
                                text= "Ingresar",
                                font=("Arial", 12 ,"bold"),
                                foreground="white",
                                width= 20, height= 1,
                                anchor=N,
                                command=self.login)
        
        boton_ingresar.config(bg="#6499e9", relief=FLAT, activebackground="white")
        
        boton_ingresar.place(relx=0.4, rely=0.8)
    
    #Proceso de login
    def login(self):
        usuario_capturado = self.Nom_usuario.get()
        contrasena_capturado = self.Contrasena.get()
        print(f'Usuario ingresado: "{usuario_capturado}"')
        print(f'Contraseña ingresada: "{contrasena_capturado}"')

        if usuario_capturado in Usuarios_Login.Base_de_datos and contrasena_capturado == Usuarios_Login.Base_de_datos[usuario_capturado]:
            self.login_acceso = True
            messagebox.showinfo(title="Login", message="¡Bienvenido!")
            self.ventana.withdraw()
            Ventana_admin()

        else:
            self.login_acceso = False
            messagebox.showerror(title="Login", message="Datos incorrectos")
            self.Nom_usuario.delete(0, END)
            self.Contrasena.delete(0, END)
        return self.login_acceso
    
#Iniciador de pantalla principal 
if __name__ == "__main__":
    programa = Ventana_Principal()
    