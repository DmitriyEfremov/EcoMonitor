from datetime import datetime

from sqlalchemy import (
    UUID,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class FileEcoProblem(Base):
    __tablename__ = "files_for_eco"

    id = Column(Integer, primary_key=True, index=True)
    eco_problem_id = Column(Integer, ForeignKey("eco_problems.id"))
    user_id = Column(UUID, nullable=False)
    storage_id = Column(UUID, nullable=True)
    created_at = Column(DateTime, server_default=text("TIMEZONE('utc', now())"),
                        onupdate=datetime.utcnow)

    eco_problems = relationship("EcoProblem", back_populates="files")


class FileReport(Base):
    __tablename__ = "files_for_reports"

    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(Integer, ForeignKey("reports.id"))
    user_id = Column(UUID, nullable=False)
    storage_id = Column(UUID, nullable=True)
    created_at = Column(DateTime, server_default=text("TIMEZONE('utc', now())"),
                        onupdate=datetime.utcnow)

    reports = relationship("Report", back_populates="files")


class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    is_final = Column(Boolean, nullable=False)

    eco_problems = relationship("EcoProblem", back_populates="status")


class TypeIncident(Base):
    __tablename__ = "types_incident"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    eco_problems = relationship("EcoProblem", back_populates="type_incident")


class EcoProblem(Base):
    __tablename__ = "eco_problems"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(UUID, nullable=False)
    manager_id = Column(UUID, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status_id = Column(
        Integer,
        ForeignKey("statuses.id"),
        nullable=False
    )
    type_incident_id = Column(
        Integer,
        ForeignKey("types_incident.id"),
        nullable=False
    )
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    is_closed = Column(
        Boolean,
        default=False,
        server_default=text("FALSE"),
        nullable=False
    )

    status = relationship("Status", back_populates="eco_problems")
    type_incident = relationship("TypeIncident", back_populates="eco_problems")
    files = relationship("FileEcoProblem", back_populates="eco_problems")

class ReportStatus(Base):
    __tablename__ = "report_statuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    is_final = Column(Boolean, nullable=False)

    report = relationship("Report", back_populates="report_status")


class Report(Base):
    __tablename__ = "reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True)
    manager_id = Column(UUID, nullable=True)
    user_id = Column(UUID, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(
        Integer,
        ForeignKey("report_statuses.id"),
        nullable=False
    )
    duplicate_task_id = Column(Integer, nullable=True)
    created_at = Column(
        DateTime,
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow
    )

    report_status = relationship("ReportStatus", back_populates="report")
    files = relationship("FileReport", back_populates="reports")
