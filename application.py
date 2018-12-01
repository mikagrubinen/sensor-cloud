# application.py

from flask import Flask, request
import do
import time
import mysql.connector
import pymongo
from global_vars import data

application = Flask(__name__)
# starttime=time.time()


@application.route("/")
def hello():
	connection = mysql.connector.connect(
		host		='rds-mysql-smartcity.cbtogzj0jikw.us-west-1.rds.amazonaws.com',
		database	='smartcityadmin',
	    user		='smartcityadmin',
	    passwd		='smartcityadmin')
	mycursor = connection.cursor()

	if connection.is_connected():

		do.make_data(mycursor, data)
		mongo()		
		return str(data)
	else:
		return "no connection"

	

######################################## MongoDB ####################################################
def mongo():
	myclient = pymongo.MongoClient("mongodb://sujan:sujansareen1@ds231133.mlab.com:31133/street_table")
	mydb = myclient.street_table
	mycol = mydb["data"]

	#******************************* INSERT MANY #********************************************#



	#!!!!!!!!!!!!!!!!!!!   ADD TIMESTAMP     !!!!!!!!!!!!!!!


	
	# mylist = [
	#   { "sensor_id": "4", "street_id": "2", "cluster_id":"2", "node_id":"3", "sensor_data":10},
	#   { "sensor_id": "5", "street_id": "2", "cluster_id":"3", "node_id":"3", "sensor_data":11},
	#   { "sensor_id": "6", "street_id": "3", "cluster_id":"3", "node_id":"3", "sensor_data":12}
	# ]
	
	# y = mycol.insert_many(mylist)
	############################################################################################

	#**************************** DELETE ALL documents in collection **************************#
	# x = mycol.delete_many({})
	# print(x.deleted_count, " documents deleted.")
	############################################################################################

	#************************************ FIND ALL ********************************************#
	# mydoc = mycol.find()
	# for x in mydoc:
	# 	print(x)
	#############################################################################################

	#******************************* FIND ALL with addres *************************************#
	myquery = { "street_id": "2", "node_id":"3"}
	mydoc = mycol.find(myquery)
	for x in mydoc:
		print(x)
	############################################################################################

if __name__ == '__main__':
    application.run(debug = True)

# @application.route("/", methods=['POST'])
# def hello():
# 	if request.method == 'POST':
# 		print (request.form)
# 		param1 = request.form['param1']
# 		param2 = request.form['param2']
# 		return param1 + param2


		# return 'Received !'

	# Ovo vraca svakih 20 sec
	# while True:
 #  		return (time.asctime( time.localtime(time.time()) ))
 #  		time.sleep(20.0 - ((time.time() - starttime) % 20.0))









