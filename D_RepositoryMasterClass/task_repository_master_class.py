from B_MasterClassTable.task_master_class_table import TaskMasterClassTable
from C_SchemasMasterClass.request_master_class import (CreateTaskMasterClassRequest, DeleteTaskMasterClassRequest,
                                                       UpdateTaskMasterClassRequest, FetchTaskMasterClassRequest)
from E_CustomExceptionMasterClass.exception_handling_master_class import (TaskNotFoundException, TaskAlreadyExistException)
from sqlalchemy.orm import Session

class TaskMasterRepositoryClass:

    def create_task(self, database: Session, task: CreateTaskMasterClassRequest):
        try:
            new_task = TaskMasterClassTable(**task.model_dump())
            database.add(new_task)
            database.commit()
            database.refresh(new_task)
            return new_task
        except Exception:
            database.rollback()
            raise TaskAlreadyExistException(
                f"Task Code: {task.task_code} Already Exists!!"
            )

    def fetch_task(self, database: Session, task: FetchTaskMasterClassRequest):
        fetch = database.query(TaskMasterClassTable).filter(TaskMasterClassTable.task_code == task.task_code).first()
        if not fetch:
            raise TaskNotFoundException(f'Task Code: {task.task_code}, Not Found!')
        return fetch

    def delete_task(self, database: Session, task: DeleteTaskMasterClassRequest):
        try:
            delete_task = database.query(TaskMasterClassTable).filter(
                TaskMasterClassTable.task_code == task.task_code
            ).first()
            database.delete(delete_task)
            database.commit()
            return {
                'status': 'success',
                'message': 'Task deleted!',
                'data': delete_task
            }

        except Exception:
            database.rollback()
            raise TaskNotFoundException(f'Task Code: {task.task_code} not found!')

    def update_task(self, database: Session, task: UpdateTaskMasterClassRequest):
        try:
            update_task = database.query(TaskMasterClassTable).filter(
                TaskMasterClassTable.task_code == task.task_code
            ).first()

            update_task_master = task.dict(exclude_unset=True)
            update_task_master.pop('task_code', None)

            for key, value in update_task_master.items():
                setattr(update_task, key, value)

            database.commit()
            database.refresh(update_task)
            return {
                'status': 'success',
                'message': 'Task updated successfully!',
                'data': update_task
            }

        except Exception:
            database.rollback()
            raise TaskNotFoundException(f'Task Code: {task.task_code} not found!')

    def display_task(self, database: Session):
        try:
            display_task = database.query(TaskMasterClassTable).all()
            return display_task
        except Exception:
            database.rollback()
            raise TaskNotFoundException('Task not found!')

