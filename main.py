from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

#INITIALIZATION
app = Flask(__name__)

#MYSQL CONECTION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sg_bd'
mysql = MySQL(app)

#SETTINGS
app.secret_key = "mysecretkey"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form1')
def form1():
    return render_template('index.html')

@app.route('/enlace')
def enlace():
    return render_template('enlace.html')

@app.route('/tabla_incidentes')
def tabla_incidentes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sg_bd.incidente')
    data = cur.fetchall()
    cur.close()
    return render_template('tabla_incidentes.html',datos = data)

if __name__ == "__main__":
    app.run(port=8000 ,debug=True)

