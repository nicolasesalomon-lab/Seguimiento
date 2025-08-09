from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="read")
    created_at = Column(DateTime, default=datetime.utcnow)

    comments = relationship("Comment", back_populates="user")


class Stage(Base):
    __tablename__ = "stages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    order = Column(Integer, nullable=False)

    projects = relationship("Project", back_populates="stage")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    grupo = Column(String, index=True)
    modelo = Column(String, unique=True, index=True, nullable=False)
    marca = Column(String, index=True)
    proveedor = Column(String)
    producto = Column(String)
    detalles = Column(Text)
    estado_muestra = Column(String)
    ingenieria_owner = Column(String)
    certificacion_se = Column(Boolean, default=False)
    certificacion_ee = Column(Boolean, default=False)
    ensayo_ruido = Column(Boolean, default=False)
    comentario_certificacion = Column(Text)
    comentario_artes = Column(Text)
    etd_comercial = Column(DateTime)
    stage_id = Column(Integer, ForeignKey("stages.id"))

    stage = relationship("Stage", back_populates="projects")
    attachments = relationship("Attachment", back_populates="project")
    comments = relationship("Comment", back_populates="project")


class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    filename = Column(String, nullable=False)
    url = Column(String, nullable=False)

    project = relationship("Project", back_populates="attachments")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="comments")
    user = relationship("User", back_populates="comments")


class AuditLog(Base):
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True)
    action = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
