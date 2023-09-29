# Obtener todos los servidores:
   SELECT * FROM servidores;
	SELECT * FROM usuarios;
      SELECT contraseña FROM usuarios;


# Obtener todos los canales de un servidor específico:

   SELECT * FROM canales WHERE id_servidor = 1;
   

# Obtener todos los mensajes de un canal específico:

   SELECT * FROM mensajes WHERE id_canal = 1;   

# Obtener todos los usuarios que pertenecen a un servidor específico:

   SELECT u.* FROM usuarios u
   INNER JOIN user_server us ON u.id_usuario = us.usuarios_id_usuario
   WHERE us.servidores_id_servidor = 1;   

# Obtener todos los mensajes enviados por un usuario específico:
   
   SELECT * FROM mensajes WHERE id_usuario_emisor = 1;

#Obtener el perfil de un usuario específico:
  SELECT * FROM usuarios WHERE id_usuario = 1;
