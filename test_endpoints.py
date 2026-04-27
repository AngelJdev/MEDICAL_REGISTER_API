import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_all():
    # 1. Login to get token
    login_data = {"username": "admin", "password": "admin123"}
    r = requests.post(f"{BASE_URL}/api/auth/login", data=login_data)
    if r.status_code != 200:
        print(f"Login failed: {r.text}")
        return
    token = r.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    print("Logged in successfully.")

    results = []

    # 1. Paciente
    paciente_data = {"nombre": "Test Patient", "curp": f"TEST{int(datetime.now().timestamp())}"}
    
    r = requests.post(f"{BASE_URL}/api/medical/pacientes", headers=headers, json={"nombre": "Test Patient", "curp": f"CURP{int(datetime.now().timestamp())}"})
    results.append(("Paciente", r.status_code, r.text))
    if r.status_code == 200:
        paciente_id = r.json()["id"]
    else:
        print(f"Paciente failed: {r.text}")
        return

    # 2. Nota Medica
    nota_data = {"paciente_id": paciente_id, "medico_id": 1, "contenido": "Test note", "tipo_nota": "Consulta"}
    r = requests.post(f"{BASE_URL}/api/medical/notas-medicas", headers=headers, json=nota_data)
    results.append(("Nota Medica", r.status_code, r.text))
    if r.status_code == 200:
        nota_id = r.json()["id"]
    else:
        nota_id = 1

    # 3. Diagnostico
    diag_data = {"nota_id": nota_id, "descripcion": "Test diag", "codigo_cie": "Z00"}
    r = requests.post(f"{BASE_URL}/api/medical/diagnosticos", headers=headers, json=diag_data)
    results.append(("Diagnostico", r.status_code, r.text))
    if r.status_code == 200:
        diag_id = r.json()["id"]
    else:
        diag_id = 1

    # 4. Tratamiento
    trat_data = {"diagnostico_id": diag_id, "medicamento": "Test med", "dosis": "1", "frecuencia": "1", "duracion": "1"}
    r = requests.post(f"{BASE_URL}/api/medical/tratamientos", headers=headers, json=trat_data)
    results.append(("Tratamiento", r.status_code, r.text))

    # 5. Signos Vitales
    sv_data = {"paciente_id": paciente_id, "tension_arterial": "120/80", "frecuencia_cardiaca": 70, "temperatura": 36.5, "peso": 70, "talla": 1.7}
    r = requests.post(f"{BASE_URL}/api/medical/signos-vitales", headers=headers, json=sv_data)
    results.append(("Signos Vitales", r.status_code, r.text))

    # 6. Valoraciones
    val_data = {"paciente_id": paciente_id, "escala": "Test", "resultado": "Good", "observaciones": "None"}
    r = requests.post(f"{BASE_URL}/api/medical/valoraciones", headers=headers, json=val_data)
    results.append(("Valoraciones", r.status_code, r.text))

    # 7. Nacimientos
    nac_data = {"paciente_id": paciente_id, "fecha_nacimiento": "2000-01-01", "lugar": "Test", "nombre_madre": "Test", "nombre_padre": "Test"}
    r = requests.post(f"{BASE_URL}/api/medical/nacimientos", headers=headers, json=nac_data)
    results.append(("Nacimientos", r.status_code, r.text))

    # 8. Defunciones
    def_data = {"paciente_id": paciente_id, "fecha_defuncion": "2026-04-27T12:00:00", "causa": "Test", "lugar": "Test"}
    r = requests.post(f"{BASE_URL}/api/medical/defunciones", headers=headers, json=def_data)
    results.append(("Defunciones", r.status_code, r.text))

    # 9. Documentos
    doc_data = {"paciente_id": paciente_id, "tipo_documento": "Test", "numero_documento": "123", "fecha_emision": "2024-01-01"}
    r = requests.post(f"{BASE_URL}/api/medical/documentos-oficiales", headers=headers, json=doc_data)
    results.append(("Documentos", r.status_code, r.text))

    # 10. Domicilios
    dom_data = {"calle": "Test", "numero_ext": "1", "colonia": "Test", "municipio": "Test", "estado": "Test", "cp": "123"}
    r = requests.post(f"{BASE_URL}/api/medical/domicilios", headers=headers, json=dom_data)
    results.append(("Domicilios", r.status_code, r.text))

    for name, code, resp in results:
        print(f"{name}: {code}")
        if code != 200:
            print(f"  Error: {resp}")

if __name__ == "__main__":
    test_all()
