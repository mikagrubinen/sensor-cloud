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


# @application.before_request
# def before_request():
# 	g.connection = mysql.connector.connect(
# 		host		='rds-mysql-smartcity.cbtogzj0jikw.us-west-1.rds.amazonaws.com',
# 		database	='smartcityadmin',
# 	    user		='smartcityadmin',
# 	    passwd		='smartcityadmin')


@application.route("/", methods=['POST', 'GET'])
def index():

	print("Sending sensor data to a database...")

	while True:

		time.sleep(30.0 - ((time.time() - starttime) % 30.0))
		print (time.asctime( time.localtime(time.time()) ))

		connection = mysql.connector.connect(
			host		='rds-mysql-smartcity.cbtogzj0jikw.us-west-1.rds.amazonaws.com',
			database	='smartcityadmin',
		    user		='smartcityadmin',
		    passwd		='smartcityadmin')
		mycursor = connection.cursor()

		if connection.is_connected():
			do.make_data(mycursor, data)

			myclient = pymongo.MongoClient("mongodb://sujan:sujansareen1@ds231133.mlab.com:31133/street_table")
			mydb = myclient.street_table
			mycol = mydb["data"]

			x = mycol.insert_many(data)
			data.clear()
		else:
			print("Error with connection to a database")
			return "Error with connection to a database"
		
	print("Sending sensor data to database is Stopped")
	return "Sending sensor data to database is Stopped"
			
		  		



if __name__ == '__main__':
	application.run(debug = True)



print("Application is closed")


