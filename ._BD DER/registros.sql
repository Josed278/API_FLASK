

INSERT INTO servidores (nombre_servidor, descripcion) VALUES ('Literatura Fantastica', 'Entendida como la ficción de lo irreal');
INSERT INTO servidores (nombre_servidor, descripcion) VALUES ('Locura Cinematografica', 'Propone indagar acerca de la relación entre cine y sociedad');
INSERT INTO servidores (nombre_servidor, descripcion) VALUES ('Relatos de Viajes', 'Desplazarse en el espacio y luego, narrarlo en una historia');
INSERT INTO servidores (nombre_servidor, descripcion) VALUES ('Salud y Bienestar', 'Busca garantizar una vida sana');
INSERT INTO servidores (nombre_servidor, descripcion) VALUES ('Central de Juegos', 'Cómo empezar en el desarrollo de vídeo juegos');

INSERT INTO usuarios (nombre_usuario, contraseña, email, imagen_perfil) VALUES ('Matilde Cazares', 'LWmq4QtE3w_TpAQ', 'matilde_cazares@gmail.com', NULL);
INSERT INTO usuarios (nombre_usuario, contraseña, email, imagen_perfil) VALUES ('Andrea Anguiano', 'XJsHpHizBBH_JXV', 'andrea_anguiano@hotmail.com', NULL);
INSERT INTO usuarios (nombre_usuario, contraseña, email, imagen_perfil) VALUES ('Pío Santana', 'cMF1jn52edh8ips', 'pío_santana@outlook.com', NULL);
INSERT INTO usuarios (nombre_usuario, contraseña, email, imagen_perfil) VALUES ('Andrea Carrera', 'ftJHXh6s1g6HT8m', 'andrea_carrera@gmail.com', NULL);
INSERT INTO usuarios (nombre_usuario, contraseña, email, imagen_perfil) VALUES ('Jennifer Zayas', 'cHa8_fX4fJ2Oa0h', 'jennifer_zayas@aol.com', NULL);

INSERT INTO canales (nombre_canal, id_servidor) VALUES ('Tolkien', 1);
INSERT INTO canales (nombre_canal, id_servidor) VALUES ('Harry Potter', 1);
INSERT INTO canales (nombre_canal, id_servidor) VALUES ('El Señor de los Anillos', 1);
INSERT INTO canales (nombre_canal, id_servidor) VALUES ('Star Wars', 2);
INSERT INTO canales (nombre_canal, id_servidor) VALUES ('Marvel', 2);

INSERT INTO mensajes (contenido, fecha, id_usuario_emisor, id_canal) VALUES ('Hola a todos!', '2023-09-18 10:00:00', 1, 1);
INSERT INTO mensajes (contenido, fecha, id_usuario_emisor, id_canal) VALUES ('¿Alguien ha leído el último libro de Tolkien?', '2023-09-18 11:00:00', 1, 1);
INSERT INTO mensajes (contenido, fecha, id_usuario_emisor, id_canal) VALUES ('Yo lo he leído y es increíble', '2023-09-18 11:30:00', 2, 1);
INSERT INTO mensajes (contenido, fecha, id_usuario_emisor, id_canal) VALUES ('¿Alguien quiere hablar sobre Harry Potter?', '2023-09-18 12:00:00', 3, 2);
INSERT INTO mensajes (contenido, fecha, id_usuario_emisor, id_canal) VALUES ('¡Me encanta la saga de Star Wars!', '2023-09-18 13:00:00', 4, 4);
INSERT INTO mensajes (contenido, fecha, id_usuario_emisor, id_canal) VALUES ('¿Cuál es tu película favorita de Marvel?', '2023-09-18 14:00:00', 5, 5);

######################################################################################################## no fue cargada la tabla user_sever
INSERT INTO user_server (id, usuarios_id_usuario, servidores_id_servidor) VALUES (1, 1, 1);
INSERT INTO user_server (id, usuarios_id_usuario, servidores_id_servidor) VALUES (2, 2, 1);
INSERT INTO user_server (id, usuarios_id_usuario, servidores_id_servidor) VALUES (3, 3, 2);
INSERT INTO user_server (id, usuarios_id_usuario, servidores_id_servidor) VALUES (4, 4, 2);
INSERT INTO user_server (id, usuarios_id_usuario, servidores_id_servidor) VALUES (5, 5, 3);