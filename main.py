from datetime import timedelta
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import uvicorn
import models
import schemas
import auth
from database import engine, get_db
from config import Config

app = FastAPI(title="Medical Register API", description="API para la gestión del área de Registros Médicos")

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Root"])
def root():
    return {"message": "API de Registro Medico activa", "docs": "/docs"}

# --- AUTH ENDPOINTS ---

@app.post("/api/auth/register", response_model=schemas.User, tags=["Auth"])
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")

    hashed_pwd = auth.get_password_hash(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_pwd,
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

# --- MEDICAL ENDPOINTS ---

# 1. Pacientes
@app.post("/api/medical/pacientes", response_model=schemas.Paciente, tags=["Pacientes"])
def create_paciente(item: schemas.PacienteCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.Paciente(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/api/medical/pacientes", response_model=List[schemas.Paciente], tags=["Pacientes"])
def read_pacientes(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    return db.query(models.Paciente).all()

# 2. Notas Médicas
@app.post("/api/medical/notas-medicas", response_model=schemas.NotaMedica, tags=["Notas Médicas"])
def create_nota(item: schemas.NotaMedicaCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.NotaMedica(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/api/medical/notas-medicas", response_model=List[schemas.NotaMedica], tags=["Notas Médicas"])
def read_notas(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    return db.query(models.NotaMedica).all()

# 3. Signos Vitales
@app.post("/api/medical/signos-vitales", response_model=schemas.SignosVitales, tags=["Signos Vitales"])
def create_signos(item: schemas.SignosVitalesCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.SignosVitales(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# 4. Diagnósticos
@app.post("/api/medical/diagnosticos", response_model=schemas.Diagnostico, tags=["Diagnósticos"])
def create_diagnostico(item: schemas.DiagnosticoCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.Diagnostico(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# 5. Tratamientos
@app.post("/api/medical/tratamientos", response_model=schemas.Tratamiento, tags=["Tratamientos"])
def create_tratamiento(item: schemas.TratamientoCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.Tratamiento(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# 6. Nacimientos
@app.post("/api/medical/nacimientos", response_model=schemas.Nacimiento, tags=["Nacimientos"])
def create_nacimiento(item: schemas.NacimientoCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.Nacimiento(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# 7. Defunciones
@app.post("/api/medical/defunciones", response_model=schemas.Defuncion, tags=["Defunciones"])
def create_defuncion(item: schemas.DefuncionCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.Defuncion(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# 8. Documentos Oficiales
@app.post("/api/medical/documentos-oficiales", response_model=schemas.Documento, tags=["Documentos Oficiales"])
def create_documento(item: schemas.DocumentoCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.DocumentoOficial(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# 9. Domicilios
@app.post("/api/medical/domicilios", response_model=schemas.Domicilio, tags=["Domicilios"])
def create_domicilio(item: schemas.DomicilioCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.Domicilio(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# 10. Valoraciones
@app.post("/api/medical/valoraciones", response_model=schemas.Valoracion, tags=["Valoraciones"])
def create_valoracion(item: schemas.ValoracionCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    new_item = models.Valoracion(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
