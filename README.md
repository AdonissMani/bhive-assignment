# **Mutual Fund Broker Backend**

This project implements a backend application for a mutual fund brokerage firm. It allows users to register, login, fetch mutual fund data via RapidAPI, view their portfolio, and track current investment values.


---

## **Features**
- User registration and login
- Fetch open-ended mutual funds by fund family from RapidAPI
- View user portfolios
- Track portfolio investment values
- Hourly NAV updates via scheduled tasks
- tests scripts to test all end point at once
- POSTMAN collection

---

## **Technologies Used**
- Python 3.8+
- Django 4.x
- Django REST Framework
- SQLite (default database)
- RapidAPI
- Redis (for caching)
- celery (for scheduling tasks)

---
## Prerequisites:
- Python 3.8+
- pipenv
- Redis (its up and running)
- RapidAPI account
---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/AdonissMani/bhive-assignment
cd bhive-assignment
```

### **2. Create a Virtual Environment**
```bash
pipenv shell
```

### **3. Install Dependencies from pipfile**
```bash
pipenv install
```

### **4. Set Up Environment Variables**
Create a `.env` file in the project root directory with the following content:
```
RAPID_API_KEY="52259d75b8msh1ad52fa38fd6d36p105555jsn06a9d70b4cb8" 
```

### **5. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Run the Development Server**
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

---

## **Usage**

### **1. Register a User**
- Endpoint: `POST http://127.0.0.1:8000/api/v1/user/register/`
- Body:
  ```json
  {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "securepassword"
  }
  ```

### **2. Login**
- Endpoint: `POST http://127.0.0.1:8000/api/v1/user/login/`
- Body:
  ```json
  {
    "email": "testuser@example.com",
    "password": "securepassword"
  }
  ```

### **3. Fetch Open-Ended Funds**
- Endpoint: `http://127.0.0.1:8000/api/v1/broker/load/funds/"Aditya Birla Sun Life Mutual Fund"`
- Replace `<Aditya Birla Sun Life Mutual Fund>` with the desired fund family name.

### **4.List all Funds from the rapid api**
- Endpoint: `http://127.0.0.1:8000/api/v1/broker/funds/`

### **5. Add Portfolio**
- Endpoint: `POST http://127.0.0.1:8000/api/v1/broker/portfolio/`
- Body:
  ```json
  {
    "mutual_fund": "108274",  # this is mutual fund scheme id
    "units": 10
  }
  ```

### **6. View Portfolio**
- Endpoint: `GET http://127.0.0.1:8000/api/v1/broker/portfolios/`

---
## running the hourly task
1. Running celery worker
```bash
celery -A main.celery worker --loglevel=info   
```

2. Running celery beats
```bash
celery -A main.celery beat --loglevel=info    
```
---
## Running Tests
```bash
python manage.py test
```
---
