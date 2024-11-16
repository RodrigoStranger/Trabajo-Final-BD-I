import requests
def generar_datos_completos(dni):
    url = "https://api.consultasperu.com/api/v1/query"
    headers = {"Content-Type": "application/json"}
    data = {
        "token": "19d47b46d71090ad7239d6ac7ac133cfb3ff3ccc15bdfd5938395f0e68096cb3",  # Actualizar si es necesario
        "type_document": "dni",
        "document_number": dni
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("success"):
            data = response_data.get("data", {})
            # Procesar datos personales
            nombre_completo = data.get("full_name", "").split()
            nombre = nombre_completo[0].capitalize() if nombre_completo else ""
            apellidos = data.get("surname", "").split()
            apellido_paterno = apellidos[0].capitalize() if len(apellidos) > 0 else ""
            apellido_materno = apellidos[1].capitalize() if len(apellidos) > 1 else ""
            fecha_nacimiento = data.get("date_of_birth", "")
            # Procesar dirección
            direccion = data.get("address", "").capitalize()
            return {
                "nombre": nombre,
                "apellido_paterno": apellido_paterno,
                "apellido_materno": apellido_materno,
                "fecha_nacimiento": fecha_nacimiento,
                "direccion": direccion
            }
        else:
            print("Error en la respuesta de la API:", response_data.get("message"))
            return None
    else:
        print("Error en la solicitud a la API:", response.status_code, response.json())
        return None