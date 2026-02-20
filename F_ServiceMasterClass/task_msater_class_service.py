from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from C_SchemasMasterClass.request_master_class import (CreateTaskMasterClassRequest, FetchTaskMasterClassRequest,
                                                       DeleteTaskMasterClassRequest, UpdateTaskMasterClassRequest)


class TaskMasterClassService(ABC):

    @abstractmethod
    def create_task_master_function(self, database: Session, create_task: CreateTaskMasterClassRequest): pass

    @abstractmethod
    def delete_task_master_function(self, database: Session, delete_task: DeleteTaskMasterClassRequest): pass

    @abstractmethod
    def update_task_master_function(self, database: Session, update_task: UpdateTaskMasterClassRequest): pass

    @abstractmethod
    def fetch_task_master_function(self, database: Session, fetch_task: FetchTaskMasterClassRequest): pass

    @abstractmethod
    def display_task_master_function(self, database: Session): pass