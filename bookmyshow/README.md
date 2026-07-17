# 🎬 BookMyShow Clone - Pune Multiplex

A full-stack cinema seat booking web application built with **Python Flask**, deployed on **AWS EC2** — inspired by BookMyShow.

![Python](https://img.shields.io/badge/Python-3.14-blue) ![Flask](https://img.shields.io/badge/Flask-3.1.3-green) ![AWS](https://img.shields.io/badge/AWS-EC2-orange) ![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue) ![Nginx](https://img.shields.io/badge/Server-Nginx-brightgreen)

## 🌐 Live Demo
http://65.2.172.127:5000

## 📌 Project Overview
This project is a single-theater movie booking system similar to BookMyShow. Users can browse movies, select showtimes, pick seats on an interactive seat map, and confirm bookings. An admin panel shows all customer bookings in real time.

## ✨ Features
- 🎥 4 Movies with multiple showtimes per day
- 🕑 4 Showtimes Daily per movie (10:00, 14:00, 18:30, 22:00)
- 💺 Interactive Seat Map with real-time availability (5 rows × 8 seats = 40 seats per show)
- ✅ Double-Booking Prevention via server-side validation
- 🎟️ Booking Confirmation Page with customer details
- ⚙️ Admin Dashboard to view all bookings
- 🌙 Dark Theme UI inspired by BookMyShow
- 📱 Responsive Design for mobile and desktop

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Backend | Python 3.14, Flask 3.1.3 |
| Database | SQLite (4 tables: movies, showtimes, seats, bookings) |
| Frontend | HTML5, CSS3, JavaScript, Jinja2 Templates |
| Cloud | AWS EC2 t3.micro (ap-south-1, Mumbai) |
| Web Server | Nginx (reverse proxy) |
| WSGI Server | Gunicorn |
| OS | Ubuntu 26.04 LTS |

## 📁 Project Structure
bookmyshow/
│
├── app.py # Flask backend (5 routes)
├── create_db.py # Database setup script
├── requirements.txt # Python dependencies
│
├── templates/ # Jinja2 HTML templates
│ ├── home.html # Movie listing page
│ ├── showtimes.html # Showtime selection page
│ ├── seats.html # Seat map + booking form
│ ├── confirmation.html # Booking confirmation page
│ └── admin_bookings.html # Admin dashboard
│
└── static/ # Static files
└── posters/ # Movie poster images

## 🗄️ Database Schema
movies → id, title, description, poster_url, duration_minutes
showtimes → id, movie_id, show_date, show_time, screen
seats → id, showtime_id, seat_number, is_booked
bookings → id, showtime_id, seat_id, customer_name, customer_email, booking_time

## 🚀 How to Run Locally
git clone https://github.com/ppranavpatil/bookmyshow-clone-aws.git
cd bookmyshow-clone-aws
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 create_db.py
python3 app.py

Visit: http://localhost:5000

## ☁️ AWS Deployment Steps
1. Launch EC2 instance (t3.micro, Ubuntu, ap-south-1)
2. Configure Security Group (ports 22, 80, 443, 5000)
3. SSH into instance and install Python, Nginx
4. Create virtual environment and install Flask, Gunicorn
5. Upload project files via SCP
6. Run database setup script (python3 create_db.py)
7. Start Flask app (python3 app.py)

## 🔗 Flask Routes
| Route | Method | Description |
|---|---|---|
| / | GET | Home page — movie listing |
| /movie/<id> | GET | Showtimes for a movie |
| /showtime/<id> | GET | Seat map for a showtime |
| /book | POST | Process seat booking |
| /admin/bookings | GET | Admin — view all bookings |

## 👨‍💻 Author
**Pranav Patil**
- GitHub: [@ppranavpatil](https://github.com/ppranavpatil)
- Email: pranavpatil1594@gmail.com
- Location: Pune, Maharashtra, India

## 📄 License
This project is open source and available under the MIT License.

## 🙏 Acknowledgements
- Inspired by BookMyShow (https://www.bookmyshow.com)
- Deployed on AWS EC2 (https://aws.amazon.com/ec2/)
- Built as a portfolio project for cloud computing learning

cd C:\Users\prana\OneDrive\Desktop\bookmyshow
git add README.md
git commit -m "Add README"
git push