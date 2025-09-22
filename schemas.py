from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from models import UserRole

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: UserRole

class User(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class PatientBase(BaseModel):
    nama: str
    tanggal_lahir: date
    diagnosis: str
    tindakan: str
    dokter: str

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    tanggal_kunjungan: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class DashboardStats(BaseModel):
    total_patients: int
    recent_patients: list[Patient]
