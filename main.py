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

#ROUTES LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        if(request.form['usuario'] == "admin" and request.form['clave'] == "admin"):
            return render_template('enlace.html')
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enlace')
def enlace():
    return render_template('enlace.html')

@app.route('/tablas')
def tablas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sg_bd.incidente')
    data = cur.fetchall()
    cur.close()
    return render_template('tablas.html',datos = data)

@app.route('/tablas2')
def tablas2():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sg_bd.incidente LIMIT 3')
    data = cur.fetchall()
    cur.close()
    return render_template('tablas2.html',datos = data)

@app.route('/detalle')
def detalle():
    return render_template('detalle.html')

@app.route('/requerimientos')
def requerimientos():
    return render_template('requerimientos.html')



if __name__ == "__main__":
    app.run(port=9000 ,debug=True)



