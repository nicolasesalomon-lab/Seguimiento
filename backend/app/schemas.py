from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr


class AttachmentBase(BaseModel):
    filename: str
    url: str


class AttachmentCreate(AttachmentBase):
    project_id: int


class Attachment(AttachmentBase):
    id: int

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    project_id: int
    user_id: int


class Comment(CommentBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class StageBase(BaseModel):
    name: str
    order: int


class StageCreate(StageBase):
    pass


class Stage(StageBase):
    id: int

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    grupo: Optional[str] = None
    modelo: str
    marca: Optional[str] = None
    proveedor: Optional[str] = None
    producto: Optional[str] = None
    detalles: Optional[str] = None
    estado_muestra: Optional[str] = None
    ingenieria_owner: Optional[str] = None
    certificacion_se: Optional[bool] = False
    certificacion_ee: Optional[bool] = False
    ensayo_ruido: Optional[bool] = False
    comentario_certificacion: Optional[str] = None
    comentario_artes: Optional[str] = None
    etd_comercial: Optional[datetime] = None
    stage_id: Optional[int] = None


class ProjectCreate(ProjectBase):
    modelo: str


class Project(ProjectBase):
    id: int
    stage: Optional[Stage]
    attachments: List[Attachment] = []
    comments: List[Comment] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    role: str = "read"


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
