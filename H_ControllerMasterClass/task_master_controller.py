from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI, Depends, status
from A_DatabaseConnection.task_master_database_config import BASE, database_connection, ENGINE

from C_SchemasMasterClass.request_master_class import (FetchTaskMasterClassRequest, DeleteTaskMasterClassRequest,
                                                       CreateTaskMasterClassRequest, UpdateTaskMasterClassRequest)
from C_SchemasMasterClass.response_master_class import FetchResponseMasterClass

from G_ServiceImplementationMasterClass.task_master_class_service_implementation import ServiceImplementationMasterClass

app = FastAPI(
    title="Task Master Controller",
    version="1.0",
    description="Task Master Controller"
)

BASE.metadata.create_all(bind=ENGINE)

serviceImplementation = ServiceImplementationMasterClass()

@app.get('/')
def root():
    return {'message': 'Welcome to Task Master Controller!'}

@app.get('/tasks', response_model=List[FetchResponseMasterClass])
def display_tasks_api(database: Session = Depends(database_connection)):
    return serviceImplementation.display_task_master_function(database)

@app.post('/tasks/code')
def fetch_task_api(fetch: FetchTaskMasterClassRequest, database: Session = Depends(database_connection)):
    return serviceImplementation.fetch_task_master_function(database, fetch)

@app.post('/tasks/create', response_model=FetchResponseMasterClass)
def create_task_api(create: CreateTaskMasterClassRequest, database: Session = Depends(database_connection)):
    return serviceImplementation.create_task_master_function(database, create)

@app.put('/tasks/update')
def update_task_api(updates: UpdateTaskMasterClassRequest, database: Session = Depends(database_connection)):
    return serviceImplementation.update_task_master_function(database, updates)

@app.delete('/tasks/delete')
def delete_task_api(deletes: DeleteTaskMasterClassRequest, database: Session = Depends(database_connection)):
    return serviceImplementation.delete_task_master_function(database, deletes)