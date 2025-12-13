# Task Management API

## Project Overview
The Task Management API is a backend RESTful service built with Django and Django REST Framework.  
It allows users to securely register, authenticate, and manage personal tasks.

Each user can create, view, update, and delete their own tasks, as well as mark tasks as completed or incomplete.  
The API follows REST best practices and demonstrates proper backend architecture, authentication, and database relationships.

This project was developed as a backend capstone project to showcase skills in Django REST Framework, authentication, and API design.

---

## Project Goals
- Build a real-world backend API using Django REST Framework
- Implement authentication and permissions
- Design a clean relational database schema
- Follow RESTful API conventions
- Demonstrate proper Git and documentation practices

---

## Features
- User registration and login
- Token-based authentication
- Create, read, update, and delete tasks
- Tasks are user-specific and protected by permissions
- Mark tasks as complete or incomplete
- Clean and modular project structure

---

## Authentication & Authorization
The API uses token-based authentication.

- Users must register and log in to receive an authentication token
- All task-related endpoints require authentication
- Users can only access and modify their own tasks

---

## Database Design
The application uses a relational database with the following core entities:

- User  
  Represents registered users of the system

- Task  
  Represents tasks created by users  
  Each task belongs to a single user (One-to-Many relationship)

This design ensures data integrity and security.

---

## API Overview
The API provides endpoints for:

- User registration and login
- Task creation, retrieval, updating, and deletion
- Marking tasks as completed or incomplete

All endpoints follow RESTful conventions and return appropriate HTTP status codes.

---

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite (development database)
- Git & GitHub for version control

---

## Project Structure
The project is organized into multiple Django apps:

- accounts – Handles user authentication and registration
- tasks – Handles task management logic
- docs – Contains planning documents and ERD diagrams

This structure improves readability, maintainability, and scalability.

---

## Future Improvements
- Add filtering and searching for tasks
- Improve error handling and logging
- Add API documentation using Swagger or Postman
- Deploy the API to a cloud platform

---

## Testing
API endpoints are tested using tools such as Postman to ensure correct behavior and authentication handling.

---

## Author
This project was developed as part of a backend capstone project to demonstrate Django REST Framework skills.

---

## Project Status
This project is currently in development.
