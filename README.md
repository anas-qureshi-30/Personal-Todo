
# Personal Todo Flask Application

A **web-based To-Do List application** developed using **Flask** and **MySQL**. This application allows users to manage tasks efficiently by adding, updating, and deleting them.

---

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Tasks are stored in MySQL with timestamps

---

## Prerequisites

* Python 3.x
* MySQL Server
* Python packages:

  * Flask
  * mysql-connector-python

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/anas-qureshi-30/Personal-Todo.git
cd Personal-Todo
```

### 2. Install Dependencies

```bash
pip install flask mysql-connector-python
```

### 3. Create the Database

Login to MySQL and create the database:

```sql
CREATE DATABASE personal_todo;
```

### 4. Configure Database Credentials

Copy `config.example.json` to `config.json`:

* Windows: `copy config.example.json config.json`
* Mac/Linux: `cp config.example.json config.json`

Update `config.json` with your MySQL credentials and a secret key:

```json
{
  "DB_HOST": "host",
  "DB_USER": "userName",
  "DB_PASS": "yourPassword",
  "DB_NAME": "personal_todo",
  "SECRET_KEY": "yourSecretKey"
}
```

### 5. Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Folder Structure

```
Personal-Todo/
│── app.py
│── config.json
│── config.example.json
│── .gitignore
│── templates/
│    ├── index.html
│    └── update.html
│── static/
     ├── style.css
```

---

## Screen Shots:
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/a776578a-3c60-47b7-be11-ba572ad2fffc" />

<img width="1919" height="909" alt="image" src="https://github.com/user-attachments/assets/31f24239-55ad-4a47-99c5-eb693f447678" />

<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/30544767-858b-460b-be55-41dd50dbca4b" />

<img width="1919" height="905" alt="image" src="https://github.com/user-attachments/assets/16bd7375-562e-493f-9b0c-adc347bd6d23" />

## Usage Instructions

1. **Add a Task:** Enter a task and submit.
2. **Update a Task:** Click the update button next to a task.
3. **Delete a Task:** Click the delete button to remove a task.
4. **Database Storage:** All tasks are stored in MySQL with timestamps.

