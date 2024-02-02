import web
import database
import time
import subprocess
import os

time.sleep(1)
if os.path.exists('flats.csv'):
    os.remove('flats.csv')

with open('flats.csv', 'w') as f:
    print('Created flats.csv')

mode = os.getenv('MODE', 'web')
if mode == 'scrapy':
    command = ['scrapy', 'crawl', 'srealityspider', '-o', 'flats.csv']
    result = subprocess.run(command, capture_output=True, text=True)
elif mode == 'web':
    time.sleep(6)
    database.insert_data('flats.csv')
    web.main()
