from database import engine, SessionLocal, Base
from models import User, UserRole
import auth

# Create tables
Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    try:
        # Check if we already have users
        existing_users = db.query(User).first()
        if existing_users is None:
            # Create admin user
            admin = User(
                username="admin",
                password=auth.get_password_hash("admin123"),
                role=UserRole.admin
            )
            
            # Create doctor user
            doctor = User(
                username="doctor",
                password=auth.get_password_hash("doctor123"),
                role=UserRole.doctor
            )
            
            db.add(admin)
            db.add(doctor)
            db.commit()
            print("Created admin and doctor users")
        else:
            print("Users already exist")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Done.")
