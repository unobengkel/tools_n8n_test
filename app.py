from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'data.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         nama TEXT NOT NULL, 
                         email TEXT NOT NULL)''')

@app.route('/users', methods=['GET'])
def get_users():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        # Ubah data ke format list of dict agar mudah dibaca n8n
        users = [{"id": r[0], "nama": r[1], "email": r[2]} for r in rows]
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'nama' not in data or 'email' not in data:
        return jsonify({"error": "Data tidak lengkap"}), 400
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("INSERT INTO users (nama, email) VALUES (?, ?)", 
                              (data['nama'], data['email']))
        new_id = cursor.lastrowid
    
    return jsonify({"message": "User berhasil dibuat", "id": new_id}), 201

if __name__ == '__main__':
    init_db()
    # Host 0.0.0.0 agar bisa diakses dari luar VPS
    app.run(host='0.0.0.0', port=5000)
