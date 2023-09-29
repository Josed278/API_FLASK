from app import init_app

if __name__ == "__main__":
    app = init_app()
    app.run()



# Este código es un punto de entrada para iniciar la aplicación Flask. 

# La función `init_app()` se importa de un módulo llamado `app` y se 
# llama para inicializar la aplicación Flask. Dentro de esta función se 
# configuran las rutas y las configuraciones necesarias para la aplicación. 

# Luego, se llama a la función `run()` de la aplicación Flask para ejecutar 
# el servidor web integrado en Flask y que la aplicación comience a escuchar
#  las solicitudes entrantes. 

# En resumen, este código inicia y ejecuta la aplicación Flask, permitiendo 
# que la aplicación pueda responder a las solicitudes entrantes y generar respuestas.