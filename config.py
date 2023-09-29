from dotenv import dotenv_values

class Config:
    config = dotenv_values(".env")
    
    SECRET_KEY = config['SECRET_KEY']
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

    DATABASE_USERNAME = config['DATABASE_USERNAME']
    DATABASE_PASSWORD = config['DATABASE_PASSWORD']
    DATABASE_HOST = config['DATABASE_HOST']
    DATABASE_PORT = config['DATABASE_PORT']

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"


# Este código define una clase Config que contiene varias variables de configuración para la aplicación.

# - SECRET_KEY: una clave secreta utilizada para firmar cookies y otros objetos.
# - SERVER_NAME: el nombre del servidor en el que se ejecuta la aplicación.
# - DEBUG: un indicador para activar el modo de depuración de la aplicación.

# - DATABASE_USERNAME: el nombre de usuario utilizado para acceder a la base de datos.
# - DATABASE_PASSWORD: la contraseña del usuario de la base de datos.
# - DATABASE_HOST: la dirección del servidor de la base de datos.
# - DATABASE_PORT: el puerto utilizado para acceder a la base de datos.

# - TEMPLATE_FOLDER: la carpeta que contiene los archivos de plantilla HTML.
# - STATIC_FOLDER: la carpeta que contiene los archivos estáticos de la aplicación, como CSS y JS.

# Todas estas variables se obtienen del archivo ".env" a través de la biblioteca dotenv.