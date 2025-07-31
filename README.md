# 🚌 Pandey Tour & Travels

A full-stack Django-based travel and tourism website that allows users to explore tour packages, contact the agency, and book trips easily. This project is designed to provide a seamless user experience and help Pandey Tour & Travels grow digitally.

## 🚀 Features

- 🏠 Homepage with auto-sliding image carousel and call-to-action buttons
- 📦 Popular Packages section with “Book Now” buttons
- 📞 Contact page with form, location map, and social links
- 📧 Form data saved to database and also sent to owner's email
- 📊 Admin dashboard to view all bookings and messages
- 📱 Fully responsive design for mobile users
- 🔐 Secure form submission with CSRF protection

## 🔧 Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Backend:** Python, Django
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)
- **Email Support:** SMTP (Gmail, customizable)
- **Deployment Ready:** Fully functional local Django server

## 📬 Contact Form + Email

- Users can fill in: Name, Email, Phone, and Message.
- Messages are saved to the database **and** sent via email to the admin.
- Admin can manage all contact submissions in the Django admin panel.

## 🧠 What I Learned

- Building dynamic pages using Django templates and views
- Handling form submissions securely with CSRF protection
- Configuring email backend to send real-time messages
- Creating responsive UI using Bootstrap and custom CSS
- Managing a professional project with modular code and folders

## 📸 Project Screenshots

Here are some screenshots from the **Pandey Tour & Travels** Django website:

### 🏠Home Page
![Home](screenshots/home.png)

### 📦Services Page
![Services](screenshots/services.png)

### 📁Packages Page
![Packages](screenshots/packages.png)

### 📬Contact Page
![Contact](screenshots/contact.png)

### 📃About Us Page
![About Us](screenshots/aboutus.png)

## 📌 Setup Instructions

```bash
git clone https://github.com/yourusername/pandey-tour-travels.git
cd pandey-tour-travels
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
