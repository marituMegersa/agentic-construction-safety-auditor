from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.construction_safety_auditor.schemas import AgenticConstructionSafetyAuditorSessionCreate, AgenticConstructionSafetyAuditorSessionResponse
from app.domain.construction_safety_auditor.service import AgenticConstructionSafetyAuditorService

router = APIRouter(prefix="/api/v1/construction_safety_auditor", tags=["Agentic Construction Safety Auditor Domain"])

@router.post("/sessions", response_model=AgenticConstructionSafetyAuditorSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticConstructionSafetyAuditorSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Construction Safety Auditor.
    """
    return AgenticConstructionSafetyAuditorService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticConstructionSafetyAuditorSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticConstructionSafetyAuditorService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
