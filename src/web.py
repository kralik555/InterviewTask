from flask import Flask, render_template
import psycopg2
import database

app = Flask(__name__)

@app.route('/')
def index():
    ads = database.fetch_ads_data()
    return render_template('index.html', ads=ads)

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
