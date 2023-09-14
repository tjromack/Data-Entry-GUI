from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Set up database connection
conn = psycopg2.connect(
    dbname="DBNAME",
    user="USERNAME",
    password="PASSWORD",
    host="localhost",
    port=5433
)

@app.route('/')
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM players")
    players = cur.fetchall()
    cur.close()
    return render_template('index.html', players=players)

@app.route('/add_player', methods=['POST'])
def add_player():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pdga_number = request.form['pdga_number']

    # Check if player with same PDGA number exists
    cur = conn.cursor()
    cur.execute("SELECT * FROM players WHERE pdga_number = %s", (pdga_number,))
    existing_player = cur.fetchone()
    cur.close()

    if existing_player:
        # Return a response that player already exists
        return jsonify({"status": "error", "message": "Player with this PDGA number already exists!"})
    
    # Insert new player since they don't exist
    cur = conn.cursor()
    cur.execute("INSERT INTO players (first_name, last_name, pdga_number) VALUES (%s, %s, %s)",
                (first_name, last_name, pdga_number))
    conn.commit()
    cur.close()

    return jsonify({"status": "success", "message": "Player added successfully!"})

@app.route('/search', methods=['POST'])
def search():
    term = request.form['search_term']
    cur = conn.cursor()
    cur.execute("SELECT * FROM players WHERE first_name ILIKE %s OR last_name ILIKE %s", (f"%{term}%", f"%{term}%"))
    players = cur.fetchall()
    cur.close()
    return jsonify(players)

if __name__ == '__main__':
    app.run(debug=True)
