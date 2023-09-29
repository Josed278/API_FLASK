from ...database import DatabaseConnection

class UserServidoresModel:

    def __init__(self, **kwargs):
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')

    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "descripcion" : self.descripcion
        }
    
    @classmethod
    def get(cls, servidor):
        query = """SELECT id_servidor, nombre_servidor FROM chatnet.servidores WHERE id_servidor = %(id_servidor)s"""
        params = servidor.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                id_servidor = result[0],
                role_name = result[1],
                descripcion = result[2]
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