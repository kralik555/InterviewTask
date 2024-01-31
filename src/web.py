from flask import Flask, render_template
import psycopg2
import pandas

app = Flask(__name__)

@app.route('/')
def index():
    #connection = psycopg2.connect('dbname=flats user=kraljak password=123456')
    #cursor = connection.cursor()
    #cursor.execute("SELECT title, image_url FROM ads")
    #ads = cursor.fetchall()
    #cursor.close()
    #connection.close()
    ads = pandas.read_csv('flats.csv')
    ads_dict = ads.to_dict(orient='records')
    return render_template('index.html', ads=ads_dict)

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
