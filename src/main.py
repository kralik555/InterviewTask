import web
import database
import time
import subprocess

time.sleep(5)
command = ['scrapy', 'crawl', 'srealityspider', '-o', 'flats.csv']
result = subprocess.run(command, capture_output=True, text=True)
print(result)
database.insert_data('flats.csv')
web.main()
