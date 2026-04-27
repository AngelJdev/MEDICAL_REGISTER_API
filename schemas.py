from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, date
from decimal import Decimal

# --- AUTH SCHEMAS ---
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: Optional[str] = "admin"

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

# --- MEDICAL SCHEMAS ---

class PacienteBase(BaseModel):
    nombre: str
    curp: Optional[str]

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int
    fecha_registro: datetime
    class Config:
        from_attributes = True

class NotaMedicaBase(BaseModel):
    paciente_id: int
    medico_id: int
    contenido: str
    tipo_nota: Optional[str] = "Consulta"

class NotaMedicaCreate(NotaMedicaBase):
    pass

class NotaMedica(NotaMedicaBase):
    id: int
    fecha: datetime
    class Config:
        from_attributes = True

class SignosVitalesBase(BaseModel):
    paciente_id: int
    tension_arterial: str
    frecuencia_cardiaca: int
    frecuencia_respiratoria: Optional[int]
    temperatura: Decimal
    saturacion_oxigeno: Optional[int]
    peso: Optional[Decimal]
    talla: Optional[Decimal]

class SignosVitalesCreate(SignosVitalesBase):
    pass

class SignosVitales(SignosVitalesBase):
    id: int
    fecha: datetime
    class Config:
        from_attributes = True

class DiagnosticoBase(BaseModel):
    nota_id: int
    descripcion: str
    codigo_cie: Optional[str]

class DiagnosticoCreate(DiagnosticoBase):
    pass

class Diagnostico(DiagnosticoBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class TratamientoBase(BaseModel):
    diagnostico_id: int
    medicamento: str
    dosis: str
    frecuencia: Optional[str]
    duracion: Optional[str]

class TratamientoCreate(TratamientoBase):
    pass

class Tratamiento(TratamientoBase):
    id: int
    class Config:
        from_attributes = True

class NacimientoBase(BaseModel):
    paciente_id: int
    fecha_nacimiento: date
    lugar: Optional[str]
    nombre_madre: Optional[str]
    nombre_padre: Optional[str]

class NacimientoCreate(NacimientoBase):
    pass

class Nacimiento(NacimientoBase):
    id: int
    class Config:
        from_attributes = True

class DefuncionBase(BaseModel):
    paciente_id: int
    fecha_defuncion: datetime
    causa: str
    lugar: Optional[str]

class DefuncionCreate(DefuncionBase):
    pass

class Defuncion(DefuncionBase):
    id: int
    class Config:
        from_attributes = True

class DocumentoBase(BaseModel):
    paciente_id: int
    tipo_documento: str
    numero_documento: str
    fecha_emision: Optional[date]

class DocumentoCreate(DocumentoBase):
    pass

class Documento(DocumentoBase):
    id: int
    class Config:
        from_attributes = True

class DomicilioBase(BaseModel):
    calle: str
    numero_ext: Optional[str]
    numero_int: Optional[str]
    colonia: Optional[str]
    municipio: Optional[str]
    estado: Optional[str]
    cp: Optional[str]

class DomicilioCreate(DomicilioBase):
    pass

class Domicilio(DomicilioBase):
    id: int
    class Config:
        from_attributes = True

class ValoracionBase(BaseModel):
    paciente_id: int
    escala: str
    resultado: str
    observaciones: Optional[str]

class ValoracionCreate(ValoracionBase):
    pass

class Valoracion(ValoracionBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
