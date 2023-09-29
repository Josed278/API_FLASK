from flask import Flask
from flask_cors import CORS
from config import Config



from .routes.auth_bp import auth_bp

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(auth_bp, url_prefix = '/auth')

    return app

# - La función `init_app` crea y configura la aplicación Flask.
# - La aplicación Flask se crea en la línea `app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)`,
#  donde se especifica el nombre del módulo actual (__name__), la carpeta donde se encuentran los archivos estáticos y la carpeta donde se encuentran 
#  los archivos de plantillas.
# - Se habilita el CORS (Cross-Origin Resource Sharing) para permitir el intercambio de recursos entre dominios diferentes en la línea `CORS(app, supports_credentials=True)`.
# - La configuración de la aplicación se toma de la clase `Config` definida en el archivo `config.py` en la línea `app.config.from_object(Config)`.
# - Se configura la conexión a la base de datos en la línea `DatabaseConnection.set_config(app.config)`.
# - Se registra el Blueprint `auth_bp` en la aplicación Flask en la línea `app.register_blueprint(auth_bp, url_prefix='/auth')`, 
# con la URL base prefixada '/auth'. Esto significa que todas las rutas definidas en el Blueprint `auth_bp` tendrán la forma '/auth/<ruta>'.