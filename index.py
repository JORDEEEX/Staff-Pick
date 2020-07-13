from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
from datetime import datetime
from flask import session

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'us-cdbr-east-02.cleardb.com'
app.config['MYSQL_USER'] = 'b13278bf55e8e3'  
app.config['MYSQL_PASSSWORD'] = '2aba0f5b' 
app.config['MYSQL_DB'] = 'heroku_7482485d225da5a' 
mysql = MySQL(app)



#SETTINGS
app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/homeadmin')
def homeadmin():
    return render_template("homeadmin.html")

@app.route('/testkurtlewin')
def testkurtlewin():
    return render_template("testkurtlewin.html")

@app.route('/testRiesgosL')
def testRiesgosL():
    return render_template("testRiesgos.html")

@app.route('/testInteligenciaE')
def testInteligenciaE():
    return render_template("testInteligenciaEmocional.html")

@app.route('/habilidadessociales')
def habilidades():
    return render_template("habilidades.html")

@app.route('/addanswer', methods = ['POST'])
def addanswer():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        dni = request.form['id']
        age = request.form['age']
        job = request.form['job']
        sex = request.form['sexo']
        e1 = 0
        e2 = 0
        e3 = 0
        for i in range(33):
            s = request.form.get(str(i))
            if s == "true":
                ac = (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31)
                dm = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32)
                lf = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33)
                if i in ac:
                    e1 += 1
                elif i in dm:
                    e2 += 1
                elif i in lf:
                    e3 += 1
        if e1 >= e2 and e1 >= e3:
            puntaje = e1
            estilo = 1
            result = 'NO APTO'
        elif e2 >= e1 and e2 >= e3:
            puntaje = e2
            estilo = 2
            result = 'APTO'
        elif e3 >= e1 and e3 >= e2:
            puntaje = e3
            estilo = 3
            result = 'NO APTO'
       

              #INSERT USERS
        mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (dni, name, lastname, age, job, sex) VALUES (%s, %s, %s, %s, %s,%s)', 
        (dni, name, lastname, age, job, sex))
        mysql.connection.commit()
        
        cur2 = mysql.connection.cursor()
        cur2.execute('SELECT idusers FROM users ORDER BY idusers DESC LIMIT 1')
        data = cur2.fetchall()
        id = data[0]
        date= datetime.now()
        #INSERT SCORE
        cur3 = mysql.connection.cursor()
        cur3.execute('INSERT INTO score (idtest, idusers, idstyle, date, score, resultadotest) VALUES (%s, %s, %s, %s, %s,%s)', 
        (1, id, estilo, date, puntaje, result))
        mysql.connection.commit()
        return redirect(url_for('exito'))

@app.route('/add_answertwo', methods = ['POST'])
def answer2():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        dni = request.form['id']
        age = request.form['age']
        job = request.form['job']
        sex = request.form['sexo']
        total = 0
        for i in range(1,18):
            s = int(request.form.get(str(i)))   
            total = total + s
            if total <= 11:
                cat = 1
                result = 'NO APTO'
            elif total > 11 and total < 24:
                cat = 2
                result = 'NO APTO'
            elif total > 23:
                cat = 3
                result = 'APTO'
            
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (dni, name, lastname, age, job, sex ) VALUES (%s, %s, %s, %s, %s,%s)', 
        (dni, name, lastname, age, job, sex))
        mysql.connection.commit() 

        cur2 = mysql.connection.cursor()
        cur2.execute('SELECT idusers FROM users ORDER BY idusers DESC LIMIT 1')
        data = cur2.fetchall()
        id = data[0]  

        date= datetime.now()        
        #INSERT SCORE
        cur3 = mysql.connection.cursor()
        cur3.execute('INSERT INTO score2 (idtest, idusers, idcategoria, date,  resultadotest) VALUES (%s, %s, %s, %s, %s)', 
        (2, id, cat, date, result))
        mysql.connection.commit()
        return redirect(url_for('exito'))

@app.route('/add_answerthree', methods = ['POST'])
def answer3():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        dni = request.form['id']
        age = request.form['age']
        job = request.form['job']
        sex = request.form['sexo']
        total = 0
        for i in range(1,33):
            s = int(request.form.get(str(i)))
            total = total + s
        if total <= 5:
            riesgo = 1
            result = 'APTO'
        elif total > 5 and total < 30:
            riesgo = 2
            result = 'APTO'
        elif total > 29 and total < 45:
            riesgo = 3
            result = 'NO APTO'
        elif total > 44:
            riesgo = 4
            result = 'NO APTO'
            
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (dni, name, lastname, age, job, sex ) VALUES (%s, %s, %s, %s, %s,%s)', 
        (dni, name, lastname, age, job, sex))
        mysql.connection.commit()   

        cur2 = mysql.connection.cursor()
        cur2.execute('SELECT idusers FROM users ORDER BY idusers DESC LIMIT 1')
        data = cur2.fetchall()
        id = data[0]  

        date= datetime.now()        
        #INSERT SCORE
        cur3 = mysql.connection.cursor()
        cur3.execute('INSERT INTO score3 (idtest, idusers, idriesgo, date, resultadotest) VALUES (%s, %s, %s, %s, %s)', 
        (3, id, riesgo, date, result))
        mysql.connection.commit()
        return redirect(url_for('exito'))

@app.route('/add_answerfour', methods = ['POST'])
def answer4():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        dni = request.form['id']
        age = request.form['age']
        job = request.form['job']
        sex = request.form['sexo']
        total = 0
        for i in range(1,35):
            s = int(request.form.get(str(i))) 
            total = total + s
        if total <= 82:
            categoria = 1 
            result = 'NO APTO'       
        elif total > 82 and total < 90:
            categoria= 2
            result = 'NO APTO'
        elif total > 89:
            categoria = 3
            result = 'APTO'
            
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (dni, name, lastname, age, job, sex ) VALUES (%s, %s, %s, %s, %s,%s)', 
        (dni, name, lastname, age, job, sex))
        mysql.connection.commit()

        cur2 = mysql.connection.cursor()
        cur2.execute('SELECT idusers FROM users ORDER BY idusers DESC LIMIT 1')
        data = cur2.fetchall()
        id = data[0]     

        date= datetime.now()        
        #INSERT SCORE
        cur3 = mysql.connection.cursor()
        cur3.execute('INSERT INTO score4 (idtest, idusers, idcategoria, date, resultadotest) VALUES (%s, %s, %s, %s, %s)', 
        (4, id, categoria, date, result))
        mysql.connection.commit()
        return redirect(url_for('exito'))

@app.route('/exito')
def exito():
    return render_template("exito.html")

@app.route('/historial')
def listado():
        mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cur.execute('SELECT users.*, test.name, concat_ws(", ",style.name, style.description) as "Resultado" , score.date, score.resultadotest FROM users, style, test, score WHERE score.idstyle = style.idstyle and test.idtest = score.idtest and users.idusers = score.idusers')
        data = cur.fetchall()
        return render_template("historial.html", personas = data)

@app.route('/historialhabilidades')
def historialhabilidades():
        mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cur.execute('SELECT users.*, test.name ,concat_ws(", ",categoria.name, categoria.descripcion), score2.date, score2.resultadotest FROM users, categoria, test, score2 WHERE score2.idcategoria = categoria.idcategoria and test.idtest = score2.idtest and users.idusers = score2.idusers')
        data = cur.fetchall()
        return render_template("historial2.html", personas = data)

@app.route('/historialRiesgos')
def historialRiesgos():
        mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cur.execute('SELECT users.*, test.name ,concat_ws(", ",riesgo.name, riesgo.descripcion), score3.date, score3.resultadotest FROM users, riesgo, test, score3 WHERE score3.idriesgo = riesgo.idriesgo and test.idtest = score3.idtest and users.idusers = score3.idusers')
        data = cur.fetchall()
        return render_template("historial3.html", personas = data)

@app.route('/historialInteligencia')
def historialInteligencia():
        mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cur.execute('SELECT users.*, test.name ,concat_ws(", ",categoria.name, categoria.descripcion), score4.date, score4.resultadotest FROM users, categoria, test, score4 WHERE score4.idcategoria = categoria.idcategoria and test.idtest = score4.idtest and users.idusers = score4.idusers')
        data = cur.fetchall()
        return render_template("historial4.html", personas = data)

@app.route('/inicio', methods = ['POST'])
def inicio():
    if request.method == 'POST':
        try:
            session.pop('username', None)
            username = request.form['username']
            password  = request.form['password']
            mysql.connection.cursor()
            cur = mysql.connection.cursor()
            cur.execute("SELECT name FROM login WHERE username = %s and password = %s", (username, password))
            data = cur.fetchone()
            session['username'] = data[0]
            return render_template('homeadmin.html', name = data)  
        except:                   
            flash("Usuario incorrecto!")
            return redirect(url_for('login'))
            
            
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))
# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True, port=3000)
