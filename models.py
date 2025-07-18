from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Spreadsheet(Base):
    __tablename__ = "spreadsheets"
    id = Column(Integer, primary_key=True)

class Cell(Base):
    __tablename__ = "cells"
    id = Column(Integer, primary_key=True)
    spreadsheet_id = Column(Integer, ForeignKey('spreadsheets.id'))
    cell_id = Column(String, nullable=False)
    value = Column(String)
    formula_string = Column(String)

class CellDependency(Base):
    __tablename__ = "cell_dependencies"
    id = Column(Integer, primary_key=True)
    spreadsheet_id = Column(Integer, ForeignKey('spreadsheets.id'))
    cell_id = Column(String, nullable=False)
    depends_on_cell_id = Column(String, nullable=False)
