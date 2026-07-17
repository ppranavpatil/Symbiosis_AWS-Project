from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'punemultiplex-secret-key-2026'

def get_db():
    conn = sqlite3.connect('bookmyshow.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return render_template('home.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie_showtimes(movie_id):
    conn = get_db()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    showtimes = conn.execute('SELECT * FROM showtimes WHERE movie_id = ?', (movie_id,)).fetchall()
    conn.close()
    return render_template('showtimes.html', movie=movie, showtimes=showtimes)

@app.route('/showtime/<int:showtime_id>')
def seat_map(showtime_id):
    conn = get_db()
    showtime = conn.execute('''
        SELECT showtimes.*, movies.title FROM showtimes
        JOIN movies ON showtimes.movie_id = movies.id
        WHERE showtimes.id = ?
    ''', (showtime_id,)).fetchone()
    seats = conn.execute('SELECT * FROM seats WHERE showtime_id = ? ORDER BY id', (showtime_id,)).fetchall()
    conn.close()
    return render_template('seats.html', showtime=showtime, seats=seats)

@app.route('/book', methods=['POST'])
def book_seats():
    showtime_id = request.form['showtime_id']
    seat_ids = request.form.getlist('seat_ids')
    customer_name = request.form['customer_name']
    customer_email = request.form['customer_email']

    if not seat_ids:
        flash('Please select at least one seat.')
        return redirect(url_for('seat_map', showtime_id=showtime_id))

    conn = get_db()
    cursor = conn.cursor()

    for seat_id in seat_ids:
        seat = cursor.execute('SELECT is_booked FROM seats WHERE id = ?', (seat_id,)).fetchone()
        if seat['is_booked'] == 1:
            conn.close()
            flash('Sorry, one of your selected seats was just booked. Please try again.')
            return redirect(url_for('seat_map', showtime_id=showtime_id))

    for seat_id in seat_ids:
        cursor.execute('UPDATE seats SET is_booked = 1 WHERE id = ?', (seat_id,))
        cursor.execute(
            'INSERT INTO bookings (showtime_id, seat_id, customer_name, customer_email) VALUES (?, ?, ?, ?)',
            (showtime_id, seat_id, customer_name, customer_email)
        )

    conn.commit()
    conn.close()
    return render_template('confirmation.html', customer_name=customer_name, seat_count=len(seat_ids))

@app.route('/admin/bookings')
def admin_bookings():
    conn = get_db()
    bookings = conn.execute('''
        SELECT bookings.customer_name, bookings.customer_email, bookings.booking_time,
               movies.title, showtimes.show_date, showtimes.show_time, seats.seat_number
        FROM bookings
        JOIN seats ON bookings.seat_id = seats.id
        JOIN showtimes ON bookings.showtime_id = showtimes.id
        JOIN movies ON showtimes.movie_id = movies.id
        ORDER BY bookings.booking_time DESC
    ''').fetchall()
    conn.close()
    return render_template('admin_bookings.html', bookings=bookings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)s