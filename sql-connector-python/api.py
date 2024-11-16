import requests
def generar_datos_dni(dni):
    url = "https://api.consultasperu.com/api/v1/query"
    headers = { "Content-Type": "application/json" }
    data = {
        "token": "19d47b46d71090ad7239d6ac7ac133cfb3ff3ccc15bdfd5938395f0e68096cb3", # si no sirve actualizar token
        "type_document": "dni",
        "document_number": dni
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("success"):
            data = response_data.get("data", {})
            nombre_completo = data.get("full_name", "").split()
            nombre = nombre_completo[0].capitalize() if nombre_completo else ""
            apellidos = data.get("surname", "").split()
            apellido_paterno = apellidos[0].capitalize() if len(apellidos) > 0 else ""
            apellido_materno = apellidos[1].capitalize() if len(apellidos) > 1 else ""
            fecha_nacimiento = data.get("date_of_birth", "")
            return {
                "nombre": nombre,
                "apellido_paterno": apellido_paterno,
                "apellido_materno": apellido_materno,
                "fecha_nacimiento": fecha_nacimiento
            }
        else:
            print("Error en la respuesta:", response_data.get("message"))
            return None
    else:
        print("Error:", response.status_code, response.json())
        return None

def generar_dato_direccion(dni):
    url = "https://api.consultasperu.com/api/v1/query"
    headers = { "Content-Type": "application/json"}
    data = {
        "token": "d52a25f105f21909c4dbb19cbf01514282782ad9dcbfa154e087ef6189a0ba33",
        "type_document": "dni",
        "document_number": dni
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("success"):
            data = response_data.get("data", {})
            direccion = data.get("address", "").capitalize()
            return {"direccion": direccion}
        else:
            print("Error en la respuesta:", response_data.get("message"))
            return None
    else:
        print("Error:", response.status_code, response.json())
        return None