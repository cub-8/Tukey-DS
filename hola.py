!pip install python-dotenv

import os
from dotenv import load_dotenv #!pip install dotenv


print("Hola mundo")

def saludar():
    print("Hola watoncito :3")

clave_super_secreta = os.getenv("llave_api_super_secreta")

def saludar_preguntar():
    print("Hola watoncito :3, ¿Cómo estás?")

