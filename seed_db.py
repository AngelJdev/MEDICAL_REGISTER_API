import auth, models
from database import SessionLocal, engine
from auth import get_password_hash

# Create tables
models.Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    
    # Check if admin user exists
    admin = db.query(models.User).filter(models.User.username == "admin").first()
    if not admin:
        print("Creando usuario administrador por defecto...")
        hashed_pw = get_password_hash("admin123")
        admin = models.User(
            username="admin",
            email="admin@medical.com",
            password_hash=hashed_pw,
            role="admin"
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
        print(f"Usuario 'admin' creado con ID: {admin.id}")
    else:
        print("El usuario 'admin' ya existe.")

    # Check if a default patient exists
    paciente = db.query(models.Paciente).first()
    if not paciente:
        print("Creando paciente de prueba...")
        paciente = models.Paciente(
            nombre="Juan Perez",
            curp="PERJ800101HDFRRN01"
        )
        db.add(paciente)
        db.commit()
        db.refresh(paciente)
        print(f"Paciente 'Juan Perez' creado con ID: {paciente.id}")
    else:
        print(f"Ya existe al menos un paciente (ID: {paciente.id}).")

    db.close()
    print("Seeding completado.")

if __name__ == "__main__":
    seed()
