from flask import Blueprint, request, render_template, redirect, session
from db_config import get_db_connection

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customer WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user'] = user
            return redirect('/dashboard')
        return "Login failed"
    return render_template('login.html')
