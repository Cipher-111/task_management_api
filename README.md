Task Management API
📌 Project Overview

The Task Management API is a backend application built with Django REST Framework that allows users to create, manage, and track their tasks.
Each user can securely create tasks, update them, mark them as completed or incomplete, and delete them when no longer needed.

This project was built as a capstone project to demonstrate backend development skills, RESTful API design, authentication, and database relationships using Django.

🚀 Features

User authentication using Token-Based Authentication

Create, read, update, and delete tasks (CRUD)

Mark tasks as completed or incomplete

Each user can only access their own tasks

Task filtering using query parameters

Proper error handling and status codes

Clean and modular project structure

🔐 Authentication

This API uses Token Authentication.

After logging in, the user receives a token which must be included in the request headers for all protected endpoints.

Header format:

Authorization: Token your_token_here

🛠️ Technologies Used

Python

Django

Django REST Framework

SQLite (default Django database)

Git & GitHub

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Cipher-111/task_management_api
cd task-management-api

2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

3️⃣ Install Dependencies
pip install django djangorestframework

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (Optional)
python manage.py createsuperuser

6️⃣ Run the Server
python manage.py runserver

📡 API Endpoints
🔑 Authentication
Method	Endpoint	Description
POST	/auth/login/	Login and receive authentication token
📝 Tasks
Method	Endpoint	Description
GET	/api/tasks/	List all tasks for the authenticated user
POST	/api/tasks/	Create a new task
GET	/api/tasks/{id}/	Retrieve a specific task
PUT	/api/tasks/{id}/	Update a task
DELETE	/api/tasks/{id}/	Delete a task

✅ Custom Actions
Method	Endpoint	Description
POST	/api/tasks/{id}/complete/	Mark task as completed
POST	/api/tasks/{id}/incomplete/	Mark task as incomplete
🔍 Filtering (Query Parameters)
Example	Description
/api/tasks/?is_completed=true	Get completed tasks
/api/tasks/?priority=high	Filter by priority
🧪 Testing with cURL
Create a Task
curl -X POST http://127.0.0.1:8000/api/tasks/ \
-H "Authorization: Token YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "title": "My First Task",
  "description": "Testing task creation",
  "priority": "high",
  "due_date": "2025-12-20"
}'

Mark Task as Completed
curl -X POST http://127.0.0.1:8000/api/tasks/1/complete/ \
-H "Authorization: Token YOUR_TOKEN"

🗂️ Project Structure
task_management_api/
│
├── accounts/        # Authentication logic
├── task/            # Task management logic
├── taskmanager/     # Project configuration
├── venv/
├── manage.py
└── README.md

🧠 Learning Outcomes

Building RESTful APIs using Django REST Framework

Implementing token-based authentication

Structuring Django projects using apps

Using serializers, viewsets, routers, and permissions

Testing APIs using cURL

Version control using Git and GitHub

📌 Author

Sunday
Backend Developer (Django)