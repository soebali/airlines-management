from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import flights, users, bookings, User

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user.password == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@main_routes.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@main_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists!', 'danger')
        else:
            users[username] = User(username, password)
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('main.login'))
    return render_template('register.html')

@main_routes.route('/book_flight', methods=['GET', 'POST'])
def book_flight():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        date = request.form['date']
        # Search for flights based on origin and destination
        available_flights = [flight for flight in flights if flight.origin == origin and flight.destination == destination]
        if available_flights:
            return render_template('view_flights.html', flights=available_flights)
        else:
            flash('No flights available for the selected route.', 'warning')
    return render_template('book_flight.html')

@main_routes.route('/view_flights')
def view_flights():
    return render_template('view_flights.html', flights=flights)

@main_routes.route('/book/<flight_number>')
def book(flight_number):
    flight = next((f for f in flights if f.flight_number == flight_number), None)
    if flight:
        bookings.append(flight)
        flash(f'Flight {flight_number} booked successfully!', 'success')
    return redirect(url_for('main.view_flights'))

@main_routes.route('/booking_history')
def booking_history():
    return render_template('booking_history.html', bookings=bookings)  # Display user's booking history