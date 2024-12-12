import yaml

def cargar_configuracion(ruta_config):
    with open(ruta_config, 'r') as archivo:
        config = yaml.safe_load(archivo)
    return config

# Cargar la configuración
config = cargar_configuracion('config.yml')

# Acceder a los valores de configuración
print(f"Nombre de la aplicación: {config['app']['name']}")
print(f"Base de datos: {config['database']['name']}")
print(f"API URL: {config['api']['url']}")
