# Task Manager  

*Task Manager* is a web application with gamification designed to help you manage your daily tasks and boost productivity. With a simple and intuitive interface, the app allows you to organize your tasks, track progress, and stay motivated with challenges and rewards.  

## Description  
Task Manager was developed using *Flask* for the backend, *PostgreSQL* for the database, and *HTML/CSS/JS* for the frontend. It provides a clean interface for adding, editing, and deleting tasks, along with a *gamification* feature that rewards users with points and achievements for completing tasks.  

### Features  
- *Task Management*: Create tasks with deadlines and categories.  
- *Gamification*: Earn points by completing tasks and unlock achievements.  
- *Progress Tracking*: Monitor your progress with charts and summaries.  
- *Focus Mode*: Minimize distractions and concentrate only on the current task.  

## Technologies Used  
- *Backend*: Flask (Python)  
- *Database*: PostgreSQL  
- *Frontend*: HTML, CSS, JavaScript  
- *Authentication*: Flask-Login  
- *ORM*: SQLAlchemy  
- *Gamification*: Points and achievements system integrated.  

## Installation and Execution 

This project can be run locally for development purposes. If you want to run the application, follow these steps:  

1. Clone the repository:  
   
   ```bash
   git clone https://github.com/franciscoprimo/TASK_MANAGER.git
   cd TASK_MANAGER

2.	Create a virtual environment 

4.	Install the dependencies:

pip install -r requirements.txt

5.	Configure the database in the config.py file with your PostgreSQL credentials.

6.	Initialize the database:

flask db upgrade

7.	Run the application:

flask run
