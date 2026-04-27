# 🏥 Medical Register API (Módulo de Registros Médicos)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

API robusta y escalable diseñada para la gestión integral de registros médicos en un entorno hospitalario. Implementa autenticación segura, relaciones complejas de base de datos y documentación interactiva.

## 🚀 Tecnologías Utilizadas

- **Python 3.12+**: Lenguaje de programación base.
- **FastAPI**: Framework moderno y de alto rendimiento para construir APIs.
- **MySQL**: Sistema de gestión de base de datos relacional.
- **SQLAlchemy**: ORM para la gestión eficiente de modelos y relaciones.
- **JWT (JSON Web Tokens)**: Sistema de autenticación y autorización.
- **Bcrypt**: Encriptación de alta seguridad para contraseñas.
- **Uvicorn**: Servidor ASGI de alto rendimiento.

## 🛠️ Instalación y Configuración

Siga estos pasos para desplegar el servidor localmente en Windows:

1. **Clonar el repositorio**:
   ```powershell
   git clone https://github.com/AngelJdev/MEDICAL_REGISTER_API.git
   cd MEDICAL_REGISTER_API
   ```

2. **Crear y activar entorno virtual**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**:
   Asegúrese de tener un archivo `.env` configurado con sus credenciales de MySQL:
   ```env
   DB_USER=root
   DB_PASSWORD=tu_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=medical_register_db
   SECRET_KEY=tu_secreto_para_jwt
   ```

5. **Inicializar y Sembrar DB**:
   ```powershell
   python seed_db.py
   ```

6. **Iniciar servidor**:
   ```powershell
   python main.py
   ```

## 📊 Diagrama Entidad-Relación (ERD)

Estructura relacional completa diseñada para mantener la integridad referencial:

```mermaid
erDiagram
    md_usuarios ||--o{ md_notas_medicas : "crea"
    md_pacientes ||--o{ md_notas_medicas : "tiene"
    md_pacientes ||--o{ md_signos_vitales : "registra"
    md_pacientes ||--o{ md_nacimientos : "pertenece"
    md_pacientes ||--o{ md_defunciones : "pertenece"
    md_pacientes ||--o{ md_documentos_oficiales : "identifica"
    md_pacientes ||--o{ md_valoraciones : "evalúa"
    md_notas_medicas ||--o{ md_diagnostico : "genera"
    md_diagnostico ||--o{ md_tratamientos : "prescribe"
    md_domicilios ||--o{ md_personas_tiene_domicilio : "pertenece"

    md_usuarios {
        int id PK
        string username
        string email
        string password_hash
        string role
        datetime created_at
    }

    md_pacientes {
        int id PK
        string nombre
        string curp
        datetime fecha_registro
        datetime created_at
    }

    md_notas_medicas {
        int id PK
        int paciente_id FK
        int medico_id FK
        text contenido
        enum tipo_nota
        datetime fecha
    }

    md_signos_vitales {
        int id PK
        int paciente_id FK
        string tension_arterial
        int frecuencia_cardiaca
        decimal temperatura
        datetime fecha
    }

    md_diagnostico {
        int id PK
        int nota_id FK
        text descripcion
        string codigo_cie
    }

    md_tratamientos {
        int id PK
        int diagnostico_id FK
        string medicamento
        string dosis
        string frecuencia
        string duracion
    }

    md_nacimientos {
        int id PK
        int paciente_id FK
        date fecha_nacimiento
        string lugar
        string nombre_madre
    }

    md_defunciones {
        int id PK
        int paciente_id FK
        datetime fecha_defuncion
        text causa
    }

    md_documentos_oficiales {
        int id PK
        int paciente_id FK
        string tipo_documento
        string numero_documento
    }

    md_domicilios {
        int id PK
        string calle
        string colonia
        string municipio
        string estado
        string cp
    }

    md_valoraciones {
        int id PK
        int paciente_id FK
        string escala
        text resultado
        text observaciones
    }
```


Desarrollado con ❤️ por el equipo de Registros Médicos.
