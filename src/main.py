import web
import database
import time

# here we will use spider to get the data
time.sleep(10)
print('Going to insert')
database.insert_data('flats.csv')
print('Starting web')
web.main()
