from pydantic import BaseModel, ConfigDict
from datetime import datetime
from datetime import date

class FetchResponseMasterClass(BaseModel):
    task_id: int
    task_code: str
    task_name: str
    task_details: str
    task_created_ts: datetime
    task_created_date: date
    task_status: str

    model_config = ConfigDict(
        from_attributes=True
    )