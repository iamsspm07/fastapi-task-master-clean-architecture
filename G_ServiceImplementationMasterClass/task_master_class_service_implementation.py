from sqlalchemy.orm import Session

from F_ServiceMasterClass.task_msater_class_service import TaskMasterClassService
from C_SchemasMasterClass.request_master_class import (CreateTaskMasterClassRequest, FetchTaskMasterClassRequest,
                                                       DeleteTaskMasterClassRequest, UpdateTaskMasterClassRequest)
from D_RepositoryMasterClass.task_repository_master_class import TaskMasterRepositoryClass

class ServiceImplementationMasterClass(TaskMasterClassService):

    def __init__(self):
        self.repository_task = TaskMasterRepositoryClass()

    def display_task_master_function(self, database: Session):
        display = self.repository_task.display_task(database)
        return display

    def fetch_task_master_function(self, database: Session, fetch_task: FetchTaskMasterClassRequest):
        display = self.repository_task.fetch_task(database, fetch_task)
        return display

    def update_task_master_function(self, database: Session, update_task: UpdateTaskMasterClassRequest):
        display = self.repository_task.update_task(database, update_task)
        return display

    def delete_task_master_function(self, database: Session, delete_task: DeleteTaskMasterClassRequest):
        display = self.repository_task.delete_task(database, delete_task)
        return display

    def create_task_master_function(self, database: Session, create_task: CreateTaskMasterClassRequest):
        display = self.repository_task.create_task(database, create_task)
        return display