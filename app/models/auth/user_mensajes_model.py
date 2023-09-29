from ...database import DatabaseConnection

class UserMensajesModel:

    def __init__(self, **kwargs):
        self.id_mensaje = kwargs.get('id_mensaje')
        self.contenido = kwargs.get('contenido')
        self.fecha = kwargs.get('fecha')
        self.id_usuario_emisor = kwargs.get('id_usuario_emisor')
        self.id_canal = kwargs.get('id_canal')

    def serialize(self):
        return {
            "id_mensaje": self.role_id,
            "contenido": self.contenido,
            "fecha": self.fecha,
            #"id_usuario_emisor": self.id_usuario_emisor,
            "usuario_emisor":User.get(User(id_usuario=self.id_usuario)).serializa(),
            #"id_canal": self.id_canal
            "canal":UserCanalModel.get(UserCanalModel(id_canal=self.id_canal)).serializa()

            
        }
    
    @classmethod
    def get(cls, mensajes):
        query = """SELECT id_mensaje, contenido FROM chatnet.mensajes WHERE id_mensaje = %(id_mensaje)s"""
        params = mensajes.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserMensajesModel(
                id_mensaje = result[0],
                contenido = result[1],
                fecha = fecha[2],
                id_usuario_emisor = id_usuario_emisor[3],
                id_canal = id_canal[4]
             
            )
        return None
        
# ```sql
# SELECT role_id, role_name FROM authentication_db.user_roles WHERE role_id = 1;   #o role_id = 2.....
   # ```



# Este código define una clase llamada `UserRoleModel` que representa el modelo de datos de un rol de usuario en un sistema de autenticación.

# El constructor de la clase define los atributos `role_id` y `role_name` y los inicializa con los valores pasados como argumentos o con valores 
# predeterminados en caso de que no se proporcionen.

# El método `serialize` devuelve un diccionario que representa los datos del objeto en formato JSON.

# El método de clase `get` recibe un objeto `role` y ejecuta una consulta SQL para obtener los detalles 
# del rol correspondiente en la base de datos. Si se encuentra un resultado, crea y devuelve una instancia de `UserRoleModel` con 
# los datos obtenidos. Si no se encuentra ningún resultado, devuelve `None`.