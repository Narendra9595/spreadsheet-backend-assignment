from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Spreadsheet, Cell, CellDependency

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Milestone 1: Dependents
@app.get("/spreadsheets/{spreadsheet_id}/cells/{cell_id}/dependents")
def get_dependents(spreadsheet_id: int, cell_id: str, db: Session = Depends(get_db)):
    dependents = db.query(CellDependency.cell_id).filter(
        CellDependency.spreadsheet_id == spreadsheet_id,
        CellDependency.depends_on_cell_id == cell_id
    ).all()
    return [d.cell_id for d in dependents]

# Milestone 2: Precedents
@app.get("/spreadsheets/{spreadsheet_id}/cells/{cell_id}/precedents")
def get_precedents(spreadsheet_id: int, cell_id: str, db: Session = Depends(get_db)):
    precedents = db.query(CellDependency.depends_on_cell_id).filter(
        CellDependency.spreadsheet_id == spreadsheet_id,
        CellDependency.cell_id == cell_id
    ).all()
    return [p.depends_on_cell_id for p in precedents]

# Milestone 3: Recalculation Order
@app.get("/spreadsheets/{spreadsheet_id}/recalculate-order")
def get_recalc_order(spreadsheet_id: int, changed_cell_id: str, db: Session = Depends(get_db)):
    dependencies = db.query(CellDependency).filter(
        CellDependency.spreadsheet_id == spreadsheet_id
    ).all()
    
    graph = {}
    for dep in dependencies:
        graph.setdefault(dep.depends_on_cell_id, []).append(dep.cell_id)

    visited, stack, order = set(), set(), []

    def dfs(cell):
        if cell in stack:
            raise HTTPException(status_code=400, detail={"error": "cycle_detected", "cell": cell})
        if cell in visited:
            return
        stack.add(cell)
        for neighbor in graph.get(cell, []):
            dfs(neighbor)
        stack.remove(cell)
        visited.add(cell)
        order.append(cell)

    dfs(changed_cell_id)
    order.reverse()
    return {"order": order}
