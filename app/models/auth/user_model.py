from ...database import DatabaseConnection
from .user_canal_model import UserCanalModel
from .user_mensajes_model import UserMensajesModel
from .user_servidores_model import UserServidoresModel
from .user_user_server_model import UserUserServerModel

class User:

    

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.nombre_usuario = kwargs.get('nombre_usuario')
        self.contraseña = kwargs.get('contraseña')
        self.email = kwargs.get('email')
        self.imagen_perfil = kwargs.get('imagen_perfil')
       
    
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contraseña": self.contraseña,
            "email": self.email


        }



        @classmethod
        def create(cls, usuarios):
            query = "INSERT INTO chatnet.usuarios (nombre_usuario, contraseña, email) VALUES (%s,%s,%s);"
            params = (usuarios.nombre_usuario, usuarios.contraseña, usuarios.email)
            DatabaseConnection.execute_query(query, params)


    # @classmethod
    # def create(cls, usuarios):
    #     query = "INSERT INTO chatnet.usuarios (nombre_usuario, contraseña, email) VALUES (%s,%s,%s);"
    #     params = (usuarios.nombre_usuario, usuarios.contraseña, usuarios.email)
    #     DatabaseConnection.execute_query(query, params)
    #     params = usuarios.serialize()
    #     result = DatabaseConnection.execute(query, params=params)


    #     if result is not None:
    #         return True
    #     return False
    






    @classmethod
    def is_registered(cls, user):
        query = """SELECT id_usuario FROM chatnet.usuarios 
        WHERE nombre_usuario = %(nombre_usuario)s and contraseña = %(contraseña)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        query = """SELECT * FROM chatnet.usuarios 
        WHERE nombre_usuario = %(nombre_usuario)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_usuario = result[0],
                nombre_usuario = result[1],
                contraseña = result[2],
                email = result[3],
                imagen_perfil = result[4]              
                
            )
        return None




# 1. `__init__(self, **kwargs)`: Este es el constructor de la clase User. Toma los parámetros nombrados (kwargs) 
#         y los asigna a las variables de instancia de la clase.

# 2. `serialize(self)`: Este método serializa los datos de la instancia de User en un diccionario.

# 3. `is_registered(cls, user)`: Este método de clase verifica si un usuario está registrado en la base de datos. 
# Toma un objeto User como parámetro y devuelve True si el usuario está registrado y False si no lo está.

# 4. `get(cls, user)`: Este método de clase recupera un usuario de la base de datos. Toma un objeto User como parámetro 
# y devuelve una instancia de User con los datos del usuario recuperado de la base de datos. 
# Si el usuario no existe en la base de datos, devuelve None.