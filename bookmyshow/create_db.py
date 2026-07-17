import sqlite3

conn = sqlite3.connect('bookmyshow.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    poster_url TEXT,
    duration_minutes INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS showtimes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER NOT NULL,
    show_date TEXT NOT NULL,
    show_time TEXT NOT NULL,
    screen TEXT DEFAULT 'Screen 1',
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS seats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    showtime_id INTEGER NOT NULL,
    seat_number TEXT NOT NULL,
    is_booked INTEGER DEFAULT 0,
    FOREIGN KEY (showtime_id) REFERENCES showtimes(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    showtime_id INTEGER NOT NULL,
    seat_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    customer_email TEXT,
    booking_time TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (showtime_id) REFERENCES showtimes(id),
    FOREIGN KEY (seat_id) REFERENCES seats(id)
)
''')

movies = [
    ("Kabir Singh", "A passionate surgeon spirals into self-destruction.", "/static/posters/kabirsingh.jpg", 172),
    ("RRR", "Two revolutionaries fight against British colonial rule.", "/static/posters/rrr.jpg", 187),
    ("Pushpa", "A laborer rises in the world of red sandalwood smuggling.", "/static/posters/pushpa.jpg", 179),
    ("3 Idiots", "Three engineering students navigate life and friendship.", "/static/posters/3idiots.jpg", 170),
]
cursor.executemany("INSERT INTO movies (title, description, poster_url, duration_minutes) VALUES (?, ?, ?, ?)", movies)

cursor.execute("SELECT id FROM movies")
movie_ids = [row[0] for row in cursor.fetchall()]

showtimes_data = []
for mid in movie_ids:
    showtimes_data.append((mid, "2026-07-10", "10:00", "Screen 1"))
    showtimes_data.append((mid, "2026-07-10", "14:00", "Screen 1"))
    showtimes_data.append((mid, "2026-07-10", "18:30", "Screen 1"))
    showtimes_data.append((mid, "2026-07-10", "22:00", "Screen 1"))

cursor.executemany("INSERT INTO showtimes (movie_id, show_date, show_time, screen) VALUES (?, ?, ?, ?)", showtimes_data)

cursor.execute("SELECT id FROM showtimes")
showtime_ids = [row[0] for row in cursor.fetchall()]

seats_data = []
for sid in showtime_ids:
    for row in "ABCDE":
        for num in range(1, 9):
            seats_data.append((sid, f"{row}{num}"))

cursor.executemany("INSERT INTO seats (showtime_id, seat_number) VALUES (?, ?)", seats_data)

conn.commit()
conn.close()

print("Database created successfully!")
print(f"Movies inserted: {len(movie_ids)}")
print(f"Showtimes inserted: {len(showtime_ids)}")
print(f"Seats inserted: {len(seats_data)}")