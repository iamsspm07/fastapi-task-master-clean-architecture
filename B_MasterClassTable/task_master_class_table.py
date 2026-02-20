from A_DatabaseConnection.task_master_database_config import BASE
from sqlalchemy import Column, Integer, String, DateTime, Date
from datetime import datetime
from sqlalchemy.sql import func

class TaskMasterClassTable(BASE):
    __tablename__ = 'task_master'

    task_id = Column(Integer, primary_key=True, index=True)
    task_code = Column(String, unique=True, nullable=False)
    task_name = Column(String, unique=False, nullable=False)
    task_details = Column(String, unique=False, nullable=False)
    task_created_ts = Column(DateTime, default=datetime.utcnow)
    task_created_date = Column(Date, server_default=func.current_date())
    task_status = Column(String, unique=False, default='Pending')