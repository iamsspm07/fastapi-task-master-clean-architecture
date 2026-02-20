# 🚀 FastAPI Task Master API (Clean Architecture)

A production-ready Task Management API built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, following a clean layered architecture approach.

---

## 🏗 Architecture

Controller → Service → Repository → Database

This structured design ensures:

- Clear separation of concerns
- Maintainable and scalable code
- Clean business logic abstraction
- Production-style backend organization

---

## 🛠 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic v2
- Uvicorn
- Dependency Injection
- Custom Exception Handling

---

## 📌 Features

- Create Task
- Update Task
- Delete Task
- Fetch Task by Code
- Display All Tasks
- Clean layered architecture
- Proper database commit & rollback handling
- Structured error management

---

## 📂 Project Structure

```
A_DatabaseConnection/
B_MasterClassTable/
C_SchemasMasterClass/
D_RepositoryMasterClass/
E_CustomExceptionMasterClass/
F_ServiceMasterClass/
G_ServiceImplementationMasterClass/
H_ControllerMasterClass/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-task-master-clean-architecture.git
cd fastapi-task-master-clean-architecture
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Update your database configuration in:

```
A_DatabaseConnection/task_master_database_config.py
```

Or use environment variables for secure configuration.

### 5️⃣ Run the Application

```bash
uvicorn H_ControllerMasterClass.task_master_controller:app --reload
```

Application will run at:

```
http://127.0.0.1:8000
```

Swagger API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🎯 What This Project Demonstrates

- Clean Architecture Principles
- Repository Pattern Implementation
- Service Layer Abstraction
- SQLAlchemy ORM Integration
- RESTful API Design
- Structured Exception Handling
- Production-style backend structuring

---

## 🚀 Future Enhancements

- JWT Authentication
- Role-Based Access Control
- Dockerization
- Alembic Migrations
- Unit & Integration Testing
- CI/CD Integration

---

## 👨‍💻 Author

Sujit Maity  
Backend Developer | Machine Learning Engineer | Data Scientist
