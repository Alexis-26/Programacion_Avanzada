class Usuarios():
    def __init__(self, Nombre, Usuario, Contrasena):
        self.Nombre = Nombre
        self.Usuario = Usuario
        self.Contrasena = Contrasena
    
Usuario1 = Usuarios("Alexis Cruz", "Alexis", "2609A")
Usuario2 = Usuarios("Hortencia Bravo", "Hortencia", "3110")

Base_de_datos = {Usuario1.Usuario:Usuario1.Contrasena,
                 Usuario2.Usuario:Usuario2.Contrasena}