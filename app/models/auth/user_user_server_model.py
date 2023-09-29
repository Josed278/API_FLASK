from ...database import DatabaseConnection

class UserUserServerModel:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.usuarios_id_usuario = kwargs.get('usuarios_id_usuario')
        self.servidores_id_servidor = kwargs.get('servidores_id_servidor')


    def serialize(self):
        return {
            "id": self.id,
            "role_name": self.role_name,            
            "usuarios_id_us":UserServidoresModel.get(UserServidoresModel(id_servidor=self.id_servidor)).serializa(),
            "servidores_id_se":User.get(User(id_usuario=self.id_usuario)).serializa()     
                
            
               }
    
    @classmethod
    def get(cls, user_server):
        query = """SELECT id, usuarios_id_usuario FROM chatnet.user_server WHERE id = %(id)s"""
        params = user_server.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                id = result[0],
                usuarios_id_usuario = result[1],
                servidores_id_servidor = result[2]
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