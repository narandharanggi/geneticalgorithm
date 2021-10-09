from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
css = Bundle("src/style.css", output="dist/style.css", filters="postcss")
assets.register("css",css)
css.build()

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'db-algen'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/database")
def table_db():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `bahan_pakan`")
    data = cursor.fetchall()
    return render_template("database.html", data=data)

@app.route("/optimization")
def optimization():
    return render_template("optimization.html")
