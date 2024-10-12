from flask import Flask, jsonify, request
import psycopg2
from datetime import datetime
from flask_caching import Cache
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest

app = Flask(__name__, static_folder='static')

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

metrics = PrometheusMetrics(app)

def get_db_connection():
    conn = psycopg2.connect(dbname='DB_Project_3', user='postgres', password='postgres', host='db')
    return conn

@app.route('/data', methods=['GET'])
@cache.cached(timeout=60, query_string=True)
def get_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        category = request.args.get('category', None)
        query = "SELECT * FROM data_records"
        
        if category:
            query += " WHERE category = %s"
            cursor.execute(query, (category,))
        else:
            cursor.execute(query)

        data = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/data', methods=['POST'])
def add_data():
    try:    
        conn = get_db_connection()
        cursor = conn.cursor()

        data_value = request.json.get('data_value')
        category = request.json.get('category')
        created_at = datetime.now()

        cursor.execute(
            "INSERT INTO data_records (data_value, category, created_at) VALUES (%s, %s, %s)",
            (data_value, category, created_at)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'status': 'Data added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

@app.route('/stats', methods=['GET'])
def get_stats():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT category, COUNT(*) FROM data_records GROUP BY category")
        stats = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
