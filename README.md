# Django Modular Entity Mapping API's
## Project Overview:
This project implements modular Djnago REST framework for managing the entities:
- Vendors
- Products
- Courses
- Certifications
and their relationships using mapping entities.
The API's are built using **APIView** only.

---

## Project Architecture
### Master Entities:
- Vendor
- Product
- Course
- Certification
### Mapping Entities:
- VendorProductMapping
- ProductCourseMapping
- CourseCertificationMapping
These mapping entities represent the relationship between the master entities.

---

## Technology Stack
- Python
- Django
- Django REST framework
- drf-yasg(Swagger documentation)

---

## Project Structure:

```
DRF_Assignment
├─ certification
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ course
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ course_certification_mapping
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ drf_main
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
├─ product
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ product_course_mapping
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ README.md
├─ requirements.txt
├─ vendor
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
└─ vendor_product_mapping
   ├─ admin.py
   ├─ apps.py
   ├─ migrations
   │  ├─ 0001_initial.py
   │  └─ __init__.py
   ├─ models.py
   ├─ serializers.py
   ├─ tests.py
   ├─ urls.py
   ├─ views.py
   └─ __init__.py

```

---

## Project Set Up Instructions:
### 1 Install Dependencies
pip install -r requirements.txt

### 2 Apply migrations
python manage.py makemigrations
python manage.py migrate

### 3 Run the server
python manage.py runserver

### 4 API Documentation
For viewing the swagger UI : (http://127.0.0.1:8000/swagger/)

Redoc:
(http://127.0.0.1:8000/redoc/)

---

## API Endpoints for each Entities:
### Vendors:
- GET /api/vendors/
- POST /api/vendors/
- GET /api/vendors/{id}/
- PUT /api/vendors/{id}/
- PATCH /api/vendors/{id}/
- DELETE /api/vendors/{id}/

### Products:
- GET /api/products/
- POST /api/products/
- GET /api/products/{id}/
- PUT /api/products/{id}/
- PATCH /api/products/{id}/
- DELETE /api/products/{id}/

### Courses:
- GET /api/courses/
- POST /api/courses/
- GET /api/courses/{id}/
- PUT /api/courses/{id}/
- PATCH /api/courses/{id}/
- DELETE /api/courses/{id}/

### Certifications:
- GET /api/certifications/
- POST /api/certifications/
- GET /api/certifications/{id}/
- PUT /api/certifications/{id}/
- PATCH /api/certifications/{id}/
- DELETE /api/certifications/{id}/

### Filtering API end poins:
- GET /api/products/?vendor_id={id}
- GET /api/courses/?product_id={id}
- GET /api/certifications/?course_id={id}

---

## Validation Rules Implemented

- Required fields validation
- Unique `code` for master entities
- Duplicate mapping prevention
- Foreign key validation
- Only one `primary_mapping=True` per parent entity

---





