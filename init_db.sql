-- Script de inicialización para MySQL: Módulo de Registros Médicos

CREATE DATABASE IF NOT EXISTS medical_register_db;
USE medical_register_db;

-- Tabla de Usuarios
CREATE TABLE IF NOT EXISTS md_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'admin',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla de Notas Médicas
CREATE TABLE IF NOT EXISTS md_notas_medicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id VARCHAR(50) NOT NULL,
    medico_id VARCHAR(50) NOT NULL,
    contenido TEXT NOT NULL,
    tipo_nota ENUM('Consulta', 'Evolución', 'Interconsulta') DEFAULT 'Consulta',
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Signos Vitales
CREATE TABLE IF NOT EXISTS md_signos_vitales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id VARCHAR(50) NOT NULL,
    tension_arterial VARCHAR(20) NOT NULL,
    frecuencia_cardiaca INT NOT NULL,
    frecuencia_respiratoria INT,
    temperatura DECIMAL(4,2) NOT NULL,
    saturacion_oxigeno INT,
    peso DECIMAL(5,2),
    talla DECIMAL(5,2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Diagnósticos
CREATE TABLE IF NOT EXISTS md_diagnostico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nota_id INT NOT NULL,
    descripcion TEXT NOT NULL,
    codigo_cie VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (nota_id) REFERENCES md_notas_medicas(id) ON DELETE CASCADE
);

-- Tabla de Tratamientos
CREATE TABLE IF NOT EXISTS md_tratamientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    diagnostico_id INT NOT NULL,
    medicamento VARCHAR(100) NOT NULL,
    dosis VARCHAR(50) NOT NULL,
    frecuencia VARCHAR(50),
    duracion VARCHAR(50),
    FOREIGN KEY (diagnostico_id) REFERENCES md_diagnostico(id) ON DELETE CASCADE
);

-- Tabla de Nacimientos
CREATE TABLE IF NOT EXISTS md_nacimientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    lugar VARCHAR(255),
    nombre_madre VARCHAR(100),
    nombre_padre VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Defunciones
CREATE TABLE IF NOT EXISTS md_defunciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id VARCHAR(50) NOT NULL,
    fecha_defuncion TIMESTAMP NOT NULL,
    causa TEXT NOT NULL,
    lugar VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Documentos Oficiales
CREATE TABLE IF NOT EXISTS md_documentos_oficiales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id VARCHAR(50) NOT NULL,
    tipo_documento VARCHAR(50) NOT NULL,
    numero_documento VARCHAR(50) NOT NULL,
    fecha_emision DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Domicilios
CREATE TABLE IF NOT EXISTS md_domicilios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    calle VARCHAR(100) NOT NULL,
    numero_ext VARCHAR(20),
    numero_int VARCHAR(20),
    colonia VARCHAR(100),
    municipio VARCHAR(100),
    estado VARCHAR(100),
    cp VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Relación Personas-Domicilio
CREATE TABLE IF NOT EXISTS md_personas_tiene_domicilio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    persona_id VARCHAR(50) NOT NULL,
    domicilio_id INT NOT NULL,
    tipo_relacion VARCHAR(50),
    FOREIGN KEY (domicilio_id) REFERENCES md_domicilios(id) ON DELETE CASCADE
);

-- Tabla de Valoraciones
CREATE TABLE IF NOT EXISTS md_valoraciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id VARCHAR(50) NOT NULL,
    escala VARCHAR(50) NOT NULL,
    resultado TEXT NOT NULL,
    observaciones TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
