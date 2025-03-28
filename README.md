# 🚗 Parking Reservation System

This is a **Django-based Parking Reservation System** that allows users to **reserve parking spots**, view availability, and make payments. The project uses **Django REST Framework**, **PostgreSQL**, and **React (Vite) for the frontend**.

---

## 📌 Features
- 🏢 **Admin Dashboard**: Monitor parking spots and reservations.
- 📍 **User Dashboard**: View available/reserved spots, search, and reserve.
- 💳 **Payments**: Integrate with a payment gateway (Future work).
- 🗺 **Map Integration**: Uses **OpenStreetMap + Leaflet.js** to visualize parking spots.
- 🔄 **REST API**: Provides endpoints for frontend interaction.
- 🏗 **Built with Django + React (Vite) + PostgreSQL**.

---

## ⚡ Quick Start

### 1️⃣ **Clone the Repository**
```bash
# Clone the project
git clone https://github.com/PranjaliSachan/parking-reservation.git
cd parking-reservation
```

### 2️⃣ **Create a Virtual Environment & Install Dependencies**
```bash
# Create a virtual environment
python -m venv venv

# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ **Set Up Environment Variables**
Create a **.env** file in the root of your Django project and add:
```env
DB_NAME=parking_db
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 4️⃣ **Run Database Migrations**
```bash
python manage.py migrate
```

### 5️⃣ **Create a Superuser (for Admin Panel)**
```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

### 6️⃣ **Run the Development Server**
```bash
python manage.py runserver
```
Your API will be available at **http://127.0.0.1:8000**

---

## 🚀 Deployment Instructions

### **Deploy to Render (Recommended for Backend)**
1. **Create a PostgreSQL database** on Render or Railway.
2. **Set environment variables**.
3. **Push your code to GitHub and link Render to the repository**.
4. **Configure Web Service:**
   - **Build Command:** `pip install -r requirements.txt && python manage.py migrate`
   - **Start Command:** `gunicorn parking_backend.wsgi:application`
   - **Environment Variables:** Add `DB_NAME`, `DB_NAME`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.
5. **Deploy!** 🚀

---

## 🔥 API Endpoints
| Method | Endpoint              | Description |
|--------|----------------------|-------------|
| GET    | `/spots`        | Get all parking spots |
| POST   | `/reserve`      | Reserve a parking spot |

---

## 🛠 Technologies Used
- **Backend:** Django, Django REST Framework, PostgreSQL
- **Frontend:** React (Vite), TailwindCSS, Material UI
- **Deployment:** Render, Vercel
- **APIs:** OpenStreetMap, Leaflet.js

---

## 🤝 Contributing
Feel free to contribute! Fork the repository and submit a pull request.

---

## 📜 License
MIT License. Free to use and modify!
