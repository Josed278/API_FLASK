import mysql.connector

class DatabaseConnection:
    _connection = None
    _config = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host = cls._config['DATABASE_HOST'],
                user = cls._config['DATABASE_USERNAME'],
                port = cls._config['DATABASE_PORT'],
                password = cls._config['DATABASE_PASSWORD']
            )
        
        return cls._connection

    @classmethod
    def set_config(cls, config):
        cls._config = config
    
    @classmethod
    def execute_query(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        
        return cursor
    
    @classmethod
    def fetch_all(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    @classmethod
    def fetch_one(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        
        return cursor.fetchone()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None

            

# Este código implementa una clase llamada `DatabaseConnection` que proporciona métodos
#  para conectarse a una base de datos MySQL y ejecutar consultas SQL.

# El método `get_connection()` devuelve una instancia de conexión a la base de datos. 
# Si no existe una conexión establecida previamente, se crea una nueva instancia utilizando la configuración especificada en `_config`.

# El método `set_config()` permite configurar la conexión a la base de datos proporcionando un diccionario de configuración que incluye
#  el nombre de host, nombre de usuario, puerto y contraseña.

# El método `execute_query()` ejecuta una consulta SQL y realiza commit de los cambios en la base de datos. Puede recibir opcionalmente
#  el nombre de la base de datos y los parámetros de la consulta.

# El método `fetch_all()` ejecuta una consulta que espera obtener múltiples filas de resultados y devuelve todas las filas en forma de lista de tuplas.

# El método `fetch_one()` ejecuta una consulta que espera obtener una sola fila de resultado y devuelve esa fila como una tupla.

# El método `close_connection()` cierra la conexión a la base de datos.

# En resumen, esta clase proporciona una interfaz para conectarse a una base de datos MySQL, ejecutar consultas SQL y obtener los resultados.