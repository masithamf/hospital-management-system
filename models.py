from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
from database import Base
import enum

class UserRole(enum.Enum):
    doctor = "doctor"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(UserRole))

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    tanggal_lahir = Column(Date)
    tanggal_kunjungan = Column(DateTime(timezone=True), server_default=func.now())
    diagnosis = Column(String)
    tindakan = Column(String)
    dokter = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
