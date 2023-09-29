from flask import Blueprint

from ..controllers.auth_controller import UserController

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(UserController.login)
auth_bp.route('/profile', methods=['GET'])(UserController.show_profile)
auth_bp.route('/logout', methods=['GET'])(UserController.logout)
auth_bp.route('/create', methods=['POST'])(UserController.crear_usuario)

# auth_bp.route('/', methods=['GET'])(UserController.lista_usuario)
# auth_bp.route('/', methods=['GET'])(UserController.buscar_usuario)

# auth_bp.route('/<init:id_usuario>', methods=['PUT'])(UserController.actualizar_usuario)
# auth_bp.route('/<init:id_usuario>', methods=['DELETE'])(UserController.delete_usuario)
# auth_bp.route('/verificar', methods=['GET'])(UserController.verificar_usuario)






















# En este código, se define un Blueprint llamado "auth_bp" que agrupa varias rutas relacionadas con la autenticación de usuarios.

# El Blueprint se importa desde Flask y se crea utilizando el constructor "Blueprint()". Se le pasa el nombre del Blueprint y el nombre
#  del módulo o paquete para que Flask pueda encontrar los recursos estáticos asociados a él.

# Luego, se definen varias rutas utilizando el decorador "route()" del Blueprint. Cada ruta tiene un endpoint y un método asociado a él.

# - "/login": Esta ruta está asociada al método "login()" del controlador "UserController". Se espera una petición POST para procesar el 
# inicio de sesión de un usuario.

# - "/profile": Esta ruta está asociada al método "show_profile()" del controlador "UserController". Se espera una petición GET para mostrar 
# el perfil de un usuario.

# - "/logout": Esta ruta está asociada al método "logout()" del controlador "UserController". Se espera una petición GET para cerrar la sesión de un usuario.





# GET, POST, PUT y DELETE son los métodos HTTP más comunes utilizados para interactuar con recursos en una API RESTful.

# - GET (Obtener): Se utiliza para obtener información de un recurso específico o de una colección de recursos. En una 
# solicitud GET, los parámetros se incluyen en la URL y la información se devuelve en el cuerpo de la respuesta.

# - POST (Crear): Se utiliza para enviar datos y crear un nuevo recurso en el servidor. Los datos se incluyen en el cuerpo
#  de la solicitud y la respuesta devuelve información sobre el nuevo recurso creado.

# - PUT (Actualizar): Se utiliza para enviar datos y actualizar un recurso existente en el servidor. Los datos se incluyen 
# en el cuerpo de la solicitud y la respuesta devuelve información sobre el recurso actualizado.

# - DELETE (Eliminar): Se utiliza para enviar una solicitud para eliminar un recurso existente en el servidor. No se incluyen
#  datos en el cuerpo de la solicitud y la respuesta devuelve información sobre el recurso eliminado. 