from flask import Flask, render_template, request
import datetime
import psycopg
from psycopg.rows import dict_row

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4g')
def page_4g():
    return render_template('4g.html')

# @app.route('/ont')
# def page_ont():
#     return render_template('ont.html')


@app.route("/ont")
def page_ont_search():
    user = request.args.get('user')
    print(user)

    table_data = []
    with psycopg.connect("postgresql://postgres:postgres@localhost:5432/postgres") as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM data_ont_4 where telnum='{}' LIMIT 30".format(str(user))) # type: ignore
            result = cur.fetchall()
            table_data =result
            print(table_data)
    return render_template("ont.html", table_data=table_data, user=user)

@app.route('/hello')
def hello():
    return 'Hello, World!'