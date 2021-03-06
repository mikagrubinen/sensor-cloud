# application.py

from flask import Flask, request, redirect, url_for, g
import do
import mysql.connector
import pymongo
import global_vars
import time
import requests
from global_vars import data


application = Flask(__name__)
starttime=time.time()


@application.route("/", methods=['POST', 'GET'])
def index():

	print("Sending sensor data to a database...")

	connection = mysql.connector.connect(
		host		='rds-mysql-smartcity.cbtogzj0jikw.us-west-1.rds.amazonaws.com',
		database	='smartcityadmin',
	    user		='smartcityadmin',
	    passwd		='smartcityadmin')
	mycursor = connection.cursor()

	while True:
		
		time.sleep(5.0 - ((time.time() - starttime) % 5.0))
		print (time.asctime( time.localtime(time.time()) ))


		if connection.is_connected():
			do.make_data(mycursor, data)

			myclient = pymongo.MongoClient("mongodb://sujan:sujansareen1@ds231133.mlab.com:31133/street_table")
			mydb = myclient.street_table
			mycol = mydb["data"]

			if not data:
				return "There is no sensors in a system"

			x = mycol.insert_many(data)
			data.clear()
		else:
			print("Error with connection to a database")
			return "Error with connection to a database"
		
	print("Sending sensor data to database is Stopped")
	return "Sending sensor data to database is Stopped"
			
		  		



if __name__ == '__main__':
	application.run(port = 5000, debug = True)



print("Application is closed")


