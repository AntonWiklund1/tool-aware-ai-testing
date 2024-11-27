from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class Prompt(BaseModel):
    id: Optional[int]
    prompt: str
    prompt_category: str
    correct_tool: str
    tools_available: List[str]

class TestRun(BaseModel):
    id: Optional[int]
    model_name: str
    instructions: str
    started_at: datetime
    completed_at: Optional[datetime]
    configuration: dict

class Result(BaseModel):
    id: Optional[int]
    prompt_id: int
    test_run_id: int
    tool_calls: List[str]
    time_taken: float
    success_rate: bool
    error_type: Optional[str]
    created_at: datetime