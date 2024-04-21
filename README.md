[![Python 3.6](https://img.shields.io/badge/python-3.10-yellow.svg)](https://www.python.org/downloads/release/python-360/)
![Django 3.0](https://img.shields.io/badge/Django-4.2.6-green.svg)
# Django Bitrix Contact Handler




**Project Name:** Webhook Contact Handler


**Project Description:**
This program get a contacts, check contact for db existing and response with gender by ID.


# Technologies Used:
- Backend Framework: Django
- Database: PostgreSQL

##Getting Started:

## 1. Clone the Repository:

```
git clone https://github.com/vipdev12/bitrix_handler.git
cd WebhookHandler
```
## 2. Create Virtual Environment:
```
python -m venv venv
```
## 3. Activate Virtual Environment:

Windows:
```
venv\Scripts\activate
```
Linux/Mac:
```
source venv/bin/activate
```
## 4. Install Dependencies:
```
pip install -r requirements.txt
```
## 5. Run Postgresql server

Linux/mac:
```
sudo service postgresql start
```
Windows:
Run postgresql on Windows

## 6. Run Migrations:
```
python manage.py migrate
```
## 7. Create Superuser:
```
python manage.py createsuperuser
```


## 8. Run the development server:
```
python manage.py runserver
```

### Docker Setup:

## 1. Build Docker Image:
```
docker build  .
```
## 2. Run Docker Compose:
```
docker-compose up
```
License:
This project is licensed under the MIT License.
