from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.construction_safety_auditor.models import AgenticConstructionSafetyAuditorSession, AgenticConstructionSafetyAuditorItem
from app.domain.construction_safety_auditor.schemas import AgenticConstructionSafetyAuditorSessionCreate, AgenticConstructionSafetyAuditorItemCreate

class AgenticConstructionSafetyAuditorService:
    @staticmethod
    def create_session(db: Session, data: AgenticConstructionSafetyAuditorSessionCreate) -> AgenticConstructionSafetyAuditorSession:
        db_obj = AgenticConstructionSafetyAuditorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticConstructionSafetyAuditorSession:
        return db.query(AgenticConstructionSafetyAuditorSession).filter(AgenticConstructionSafetyAuditorSession.id == session_id).first()
