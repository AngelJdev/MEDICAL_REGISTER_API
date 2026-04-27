from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum, Numeric, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "md_usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="admin")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    notas_creadas = relationship("NotaMedica", back_populates="medico")

class Paciente(Base):
    __tablename__ = "md_pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    curp = Column(String(20), unique=True)
    fecha_registro = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    notas = relationship("NotaMedica", back_populates="paciente")
    signos = relationship("SignosVitales", back_populates="paciente")
    nacimiento = relationship("Nacimiento", back_populates="paciente", uselist=False)
    defuncion = relationship("Defuncion", back_populates="paciente", uselist=False)
    documentos = relationship("DocumentoOficial", back_populates="paciente")
    valoraciones = relationship("Valoracion", back_populates="paciente")

class NotaMedica(Base):
    __tablename__ = "md_notas_medicas"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("md_pacientes.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("md_usuarios.id"), nullable=False)
    contenido = Column(Text, nullable=False)
    tipo_nota = Column(Enum('Consulta', 'Evolución', 'Interconsulta'), default='Consulta')
    fecha = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    paciente = relationship("Paciente", back_populates="notas")
    medico = relationship("User", back_populates="notas_creadas")
    diagnosticos = relationship("Diagnostico", back_populates="nota")

class SignosVitales(Base):
    __tablename__ = "md_signos_vitales"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("md_pacientes.id"), nullable=False)
    tension_arterial = Column(String(20), nullable=False)
    frecuencia_cardiaca = Column(Integer, nullable=False)
    frecuencia_respiratoria = Column(Integer)
    temperatura = Column(Numeric(4,2), nullable=False)
    saturacion_oxigeno = Column(Integer)
    peso = Column(Numeric(5,2))
    talla = Column(Numeric(5,2))
    fecha = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    paciente = relationship("Paciente", back_populates="signos")

class Diagnostico(Base):
    __tablename__ = "md_diagnostico"
    id = Column(Integer, primary_key=True, index=True)
    nota_id = Column(Integer, ForeignKey("md_notas_medicas.id"))
    descripcion = Column(Text, nullable=False)
    codigo_cie = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())

    nota = relationship("NotaMedica", back_populates="diagnosticos")
    tratamientos = relationship("Tratamiento", back_populates="diagnostico")

class Tratamiento(Base):
    __tablename__ = "md_tratamientos"
    id = Column(Integer, primary_key=True, index=True)
    diagnostico_id = Column(Integer, ForeignKey("md_diagnostico.id"))
    medicamento = Column(String(100), nullable=False)
    dosis = Column(String(50), nullable=False)
    frecuencia = Column(String(50))
    duracion = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())

    diagnostico = relationship("Diagnostico", back_populates="tratamientos")

class Nacimiento(Base):
    __tablename__ = "md_nacimientos"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("md_pacientes.id"), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    lugar = Column(String(255))
    nombre_madre = Column(String(100))
    nombre_padre = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())

    paciente = relationship("Paciente", back_populates="nacimiento")

class Defuncion(Base):
    __tablename__ = "md_defunciones"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("md_pacientes.id"), nullable=False)
    fecha_defuncion = Column(DateTime, nullable=False)
    causa = Column(Text, nullable=False)
    lugar = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())

    paciente = relationship("Paciente", back_populates="defuncion")

class DocumentoOficial(Base):
    __tablename__ = "md_documentos_oficiales"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("md_pacientes.id"), nullable=False)
    tipo_documento = Column(String(50), nullable=False)
    numero_documento = Column(String(50), nullable=False)
    fecha_emision = Column(Date)
    created_at = Column(DateTime, server_default=func.now())

    paciente = relationship("Paciente", back_populates="documentos")

class Domicilio(Base):
    __tablename__ = "md_domicilios"
    id = Column(Integer, primary_key=True, index=True)
    calle = Column(String(100), nullable=False)
    numero_ext = Column(String(20))
    numero_int = Column(String(20))
    colonia = Column(String(100))
    municipio = Column(String(100))
    estado = Column(String(100))
    cp = Column(String(10))
    created_at = Column(DateTime, server_default=func.now())

class PersonaTieneDomicilio(Base):
    __tablename__ = "md_personas_tiene_domicilio"
    id = Column(Integer, primary_key=True, index=True)
    persona_id = Column(String(50), nullable=False)
    domicilio_id = Column(Integer, ForeignKey("md_domicilios.id"))
    tipo_relacion = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())

class Valoracion(Base):
    __tablename__ = "md_valoraciones"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("md_pacientes.id"), nullable=False)
    escala = Column(String(50), nullable=False)
    resultado = Column(Text, nullable=False)
    observaciones = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    paciente = relationship("Paciente", back_populates="valoraciones")
