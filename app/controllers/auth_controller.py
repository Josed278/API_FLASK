from ..models.auth.user_model import User

from flask import request, session

class UserController:
# 
# ROUTES---RUTAS
# auth_bp = Blueprint('auth_bp', __name__)

# auth_bp.route('/login', methods=['POST'])(UserController.login)
# auth_bp.route('/profile', methods=['GET'])(UserController.show_profile)
# auth_bp.route('/logout', methods=['GET'])(UserController.logout)
#auth_bp.route('/create', methods=['POST'])(UserController.crear_usuario)

    # @classmethod
    # def crear_usuario(cls):
    #     data = request.json
    #     usuarios = User(
    #         nombre_usuario = data.get('nombre_usuario',''),
    #         contraseña = data.get('contraseña',''),\
    #         email = data.get('email','')
    #     )
        
    #     if usuarios.is_registered(usuarios):
    #         return {"message": "Usuario ya registrado"}, 409
    #     else:
    #         if usuarios.create(usuarios):
    #             return {"message": "Usuario creado exitosamente"}, 201
    #         else:
    #             return {"message": "Error al crear el usuario"}, 500



    
    @classmethod
    def crear_usuario(self):        
        usuarios = User(
        nombre_usuario = request.args.get('nombre_usuario', ''),
        contraseña = request.args.get('contraseña', ''),\
        email = request.args.get('email', '')
        )

        User.crear_usuario(usuarios)
        return {'message':' Usuario creado con exito'}, 200





   
    @classmethod
    def login(cls):
        data = request.json
        user = User(
            nombre_usuario = data.get('nombre_usuario'),
            contraseña = data.get('contraseña')
        )
        
        if User.is_registered(user):
            session['nombre_usuario'] = data.get('nombre_usuario')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    """ @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get(User(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_of_birth": user.date_of_birth,
                "phone_number": user.phone_number,
                "creation_date": user.creation_date,
                "last_login": user.last_login,
                "status_id": user.status_id,
                "role_id": user.role_id
            }, 200 """

    @classmethod
    def show_profile(cls):
        nombre_usuario = session.get('nombre_usuario')
        user = User.get(User(nombre_usuario = nombre_usuario))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
    
    @classmethod
    def logout(cls):
        session.pop('nombre_usuario', None)
        return {"message": "Sesion cerrada"}, 200

# La clase `UserController` es un controlador que maneja todas las operaciones relacionadas con los usuarios.

# El método `login` maneja la lógica de inicio de sesión de un usuario. Se obtienen los datos de inicio de sesión
#  del usuario desde la solicitud, se crea una instancia del modelo `User` con esos datos y se verifica si el usuario 
#  está registrado. Si el usuario está registrado, se guarda el nombre de usuario en la sesión y se devuelve un mensaje 
#  de éxito. De lo contrario, se devuelve un mensaje de error.

# El método `show_profile` maneja la lógica para mostrar el perfil de un usuario. Se obtiene el nombre de usuario de la 
# sesión y se obtiene la instancia del modelo `User` correspondiente. Si el usuario existe, se devuelve la información del 
# perfil en formato JSON junto con el código de estado 200 (éxito). De lo contrario, se devuelve un mensaje de error junto
#  con el código de estado 404 (no encontrado).

# El método `logout` maneja la lógica para cerrar la sesión de un usuario. Simplemente elimina el nombre de usuario de la 
# sesión y devuelve un mensaje de éxito.
# En resumen, este controlador maneja las operaciones de inicio

# INSERT INTO usuarios (nombre_usuario, contraseña, email, imagen_perfil) VALUES ('Matilde Cazares', 'LWmq4QtE3w_TpAQ', 'matilde_cazares@gmail.com', NULL);

