from ...database import DatabaseConnection

class UserCanalModel:

    def __init__(self, **kwargs):
        self.id_canal = kwargs.get('id_canal')
        self.nombre_canal = kwargs.get('nombre_canal')
        self.id_servidor = kwargs.get('id_servidor')

    def serialize(self):
        return {
            "id_canal": self.id_canal,
            "nombre_canal": self.nombre_canal,
            "servidor":UserServidoresModel.get(UserServidoresModel(id_servidor=self.id_servidor)).serializa()
        }
    
    @classmethod
    def get(cls, canal):
        query = """SELECT id_canal, nombre_canal FROM chatnet.canales WHERE id_canal = %(id_canal)s"""
        params = canal.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                id_canal = result[0],
                nombre_canal = result[1],
                id_servidor = result [2]
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