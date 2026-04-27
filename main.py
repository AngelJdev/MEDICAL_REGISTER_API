from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List

import models, schemas, auth
from database import engine, get_db
from config import Config

# Create tables in MySQL if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Medical Register API - FastAPI", 
    description="API para la gestión del área de Registros Médicos",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "API de Registro Médico activa (FastAPI + MySQL)"}

# --- AUTH ENDPOINTS ---

@app.post("/api/auth/register", response_model=schemas.User, tags=["Auth"])
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/auth/login", response_model=schemas.Token, tags=["Auth"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --- PROTECTED MEDICAL ENDPOINTS ---

# Helper function to create generic CRUD endpoints
def add_crud_endpoints(router_app, model, schema, schema_create, path, tag):
    @router_app.get(f"/api/medical/{path}", response_model=List[schema], tags=[tag])
    def read_items(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
        return db.query(model).all()

    @router_app.post(f"/api/medical/{path}", response_model=schema, tags=[tag])
    def create_item(item: schema_create, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
        new_item = model(**item.dict())
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item

# Registering all medical entities
add_crud_endpoints(app, models.Paciente, schemas.Paciente, schemas.PacienteCreate, "pacientes", "Pacientes")
add_crud_endpoints(app, models.NotaMedica, schemas.NotaMedica, schemas.NotaMedicaCreate, "notas-medicas", "Notas Médicas")
add_crud_endpoints(app, models.SignosVitales, schemas.SignosVitales, schemas.SignosVitalesCreate, "signos-vitales", "Signos Vitales")
add_crud_endpoints(app, models.Diagnostico, schemas.Diagnostico, schemas.DiagnosticoCreate, "diagnosticos", "Diagnósticos")
add_crud_endpoints(app, models.Tratamiento, schemas.Tratamiento, schemas.TratamientoCreate, "tratamientos", "Tratamientos")
add_crud_endpoints(app, models.Nacimiento, schemas.Nacimiento, schemas.NacimientoCreate, "nacimientos", "Nacimientos")
add_crud_endpoints(app, models.Defuncion, schemas.Defuncion, schemas.DefuncionCreate, "defunciones", "Defunciones")
add_crud_endpoints(app, models.DocumentoOficial, schemas.Documento, schemas.DocumentoCreate, "documentos-oficiales", "Documentos")
add_crud_endpoints(app, models.Domicilio, schemas.Domicilio, schemas.DomicilioCreate, "domicilios", "Domicilios")
add_crud_endpoints(app, models.Valoracion, schemas.Valoracion, schemas.ValoracionCreate, "valoraciones", "Valoraciones")

# --- STARTUP MESSAGE ---
if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*50)
    print("API de Registro Medico iniciada correctamente")
    print("URL del API: http://localhost:8000")
    print("Documentacion Swagger: http://localhost:8000/docs")
    print("="*50 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)

