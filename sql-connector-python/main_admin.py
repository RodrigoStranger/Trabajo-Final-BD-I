from functions_users import *
from gestion_personal import * 

if __name__ == "__main__":
    dni_cliente = "73714089"
    if persona_existe(dni_cliente):
        print(f"La Persona con dni {dni_cliente} existe en la base de datos.")
    else:
        print(f"La Persona con dni {dni_cliente} NO existe en la base de datos.")

