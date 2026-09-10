from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class AgenticConstructionSafetyAuditorItemBase(BaseModel):
    item_type: str = Field(..., example="Observation")
    name: str = Field(..., example="Domain Parameter")
    payload: Dict[str, Any] = Field(default_factory=dict)

class AgenticConstructionSafetyAuditorItemCreate(AgenticConstructionSafetyAuditorItemBase):
    pass

class AgenticConstructionSafetyAuditorItemResponse(AgenticConstructionSafetyAuditorItemBase):
    id: str
    session_id: str
    created_at: datetime

    class Config:
        from_attributes = True

class AgenticConstructionSafetyAuditorSessionBase(BaseModel):
    task_prompt: str = Field(..., description="Agent task prompt or query")
    metadata_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class AgenticConstructionSafetyAuditorSessionCreate(AgenticConstructionSafetyAuditorSessionBase):
    pass

class AgenticConstructionSafetyAuditorSessionResponse(AgenticConstructionSafetyAuditorSessionBase):
    id: str
    status: str
    safety_tier: str
    confidence_score: float
    created_at: datetime
    updated_at: datetime
    items: List[AgenticConstructionSafetyAuditorItemResponse] = []

    class Config:
        from_attributes = True
