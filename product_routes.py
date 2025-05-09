from flask import Blueprint, render_template
from db_config import get_db_connection

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', products=products)
