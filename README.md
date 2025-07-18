#  Spreadsheet Cell Dependency Backend API

A minimal **FastAPI** backend to manage **spreadsheet cells** and their **formula dependencies**, supporting:
-  Get direct **dependents** of a cell
-  Get direct **precedents** of a cell
-  Get **recalculation order** using **topological sort** with **cycle detection**

---

##  Tech Stack
- **Python 3.9+**
- **FastAPI** – lightweight, high-performance API framework
- **SQLAlchemy** – ORM for relational data handling
- **SQLite** (easy swap to PostgreSQL)

---

##  Features Covered

| Milestone | Description |
|------------|-------------|
| **1. Dependents** | API to get all cells that directly **depend** on a given cell |
| **2. Precedents** | API to get all cells a given cell **depends on** |
| **3. Recalculation Order** | API to return **topological order** of recalculation starting from any changed cell, with **cycle detection** |

---

##  Project Structure
