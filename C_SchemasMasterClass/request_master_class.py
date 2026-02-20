from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import date

class CreateTaskMasterClassRequest(BaseModel):
    task_code: str
    task_name: str
    task_details: str

class UpdateTaskMasterClassRequest(BaseModel):
    task_code: str # need to delete in update function
    task_name: Optional[str]
    task_details: Optional[str]
    task_created_ts: Optional[datetime]
    task_created_date: Optional[date]
    task_status: Optional[str]

class DeleteTaskMasterClassRequest(BaseModel):
    task_code: str

class FetchTaskMasterClassRequest(BaseModel):
    task_code: str