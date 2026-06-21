# FoodFolio

FoodFolio is a Django-based healthy food ordering platform that helps users achieve their fitness goals by providing nutritious meal options based on their dietary preferences such as Weight Loss, Weight Gain, and Balanced Diet plans.

The platform connects customers, food suppliers, and delivery personnel through a role-based system, ensuring a seamless food ordering and delivery experience.

---

## Features

### User Module
- User Registration & Login
- Browse Healthy Food Items
- Filter Foods by Fitness Goal
  - Weight Loss
  - Weight Gain
  - Balanced Diet
- Add Items to Cart
- Online Order Placement
- Order Tracking
- Monthly Purchase Reports
- Submit Ratings & Feedback
- Access Diet Guidance Materials

### Supplier Module
- Supplier Registration & Login
- Add Healthy Food Items
- Upload Product Images
- Manage Food Listings
- View Customer Orders
- Assign Delivery Personnel
- Upload Diet Guidance Documents

### Delivery Module
- Delivery Staff Registration & Login
- Manage Availability Status
- Accept Assigned Orders
- Update Delivery Status
- Mark Orders as Delivered

### Admin Module
- Approve Users, Suppliers, and Delivery Staff
- Manage Food Listings
- Approve Food Products
- View Sales Reports
- Monitor Platform Activities

---

## Technology Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Database
- SQLite (Development)
  - Can be migrated to MySQL/PostgreSQL

### Other Technologies
- Django Authentication
- Session Management
- File Upload Handling
- Role-Based Access Control

---

## Project Workflow

1. User registers and gets approval from Admin.
2. Supplier adds healthy food products.
3. Admin approves food items.
4. User browses and orders food based on fitness goals.
5. Supplier assigns a delivery partner.
6. Delivery partner accepts and delivers the order.
7. User provides ratings and feedback.
8. Admin can generate sales reports.

---

## User Roles

| Role | Responsibilities |
|--------|----------------|
| Admin | Manage users, suppliers, deliveries, foods, reports |
| User | Order healthy food and provide feedback |
| Supplier | Add foods and manage orders |
| Delivery Partner | Deliver assigned orders |

---

## Screenshots

### Home Page
<img width="1897" height="870" alt="Screenshot 2026-06-21 203816" src="https://github.com/user-attachments/assets/7f20d5c2-1ac0-4727-ae24-af6492a4cf61" />

### Registration Pages
<img width="1898" height="852" alt="Screenshot 2026-06-21 203841" src="https://github.com/user-attachments/assets/68167446-5067-4603-bfc4-733c9b434b97" />
<img width="1895" height="837" alt="Screenshot 2026-06-21 203906" src="https://github.com/user-attachments/assets/e0653cd7-7c46-496e-ad4d-e6e55bbe2662" />
<img width="1896" height="860" alt="Screenshot 2026-06-21 203929" src="https://github.com/user-attachments/assets/01810da9-377d-4b06-98f4-aa601bab3e2f" />

### Login Page
<img width="1902" height="797" alt="Screenshot 2026-06-21 203950" src="https://github.com/user-attachments/assets/01e799a4-0f63-44e9-b588-a1de17d39f06" />

### Food Listing
<img width="1588" height="862" alt="Screenshot 2026-06-21 204125" src="https://github.com/user-attachments/assets/36a3c10b-fa6f-442d-840c-4280be8da917" />

---

## Installation

### Clone Repository

```bash
git clone https://github.com/akshaykv03/FoodFolio
cd foodfolio
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Future Enhancements

- Online Payment Gateway Integration
- Email Notifications
- Real-time Order Tracking
- Nutrition Analytics Dashboard
- Mobile Application
- AI-Based Diet Recommendations

---

## Author

**Akshay K V**

Python Django Developer

GitHub: https://github.com/akshaykv03

---

## License

This project is developed for educational and portfolio purposes.
