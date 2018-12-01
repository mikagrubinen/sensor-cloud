# application.py

from flask import Flask, request
import do
import mysql.connector
import pymongo
from global_vars import data

application = Flask(__name__)
# starttime=time.time()

######################################## MongoDB ######################################################################
def mongo():
	myclient = pymongo.MongoClient("mongodb://sujan:sujansareen1@ds231133.mlab.com:31133/street_table")
	mydb = myclient.street_table
	mycol = mydb["data"]
	#******************************* INSERT MANY #********************************************#	
	# mylist = [
	#   { "sensor_id": "4", "street_id": "2", "cluster_id":"2", "node_id":"3", "sensor_data":10},
	#   { "sensor_id": "5", "street_id": "2", "cluster_id":"3", "node_id":"3", "sensor_data":11},
	#   { "sensor_id": "6", "street_id": "3", "cluster_id":"3", "node_id":"3", "sensor_data":12}
	# ]
	
	# y = mycol.insert_many(data)	
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
	myquery = { "cluster_id": 1, 'sensor_id':2}
	mydoc = mycol.find(myquery)
	for x in mydoc:
		print(x)
	############################################################################################
	data.clear()
####################################################################################################################



####################################################################################################################
def alo():
	connection = mysql.connector.connect(
		host		='rds-mysql-smartcity.cbtogzj0jikw.us-west-1.rds.amazonaws.com',
		database	='smartcityadmin',
	    user		='smartcityadmin',
	    passwd		='smartcityadmin')
	mycursor = connection.cursor()
	##################################### Update table ##############################################
	# if connection.is_connected():
	# 	sql = "UPDATE smart_city_281_sensor_dtls SET cluster_id = 4 WHERE sensor_id = '10'"
	# 	mycursor.execute(sql)
	# 	connection.commit()
	#################################################################################################
	if connection.is_connected():
		do.make_data(mycursor, data)
		mongo()		
		return "success"
	else:
		return "no connection"
####################################################################################################################



####################################################################################################################

@application.route("/", methods=['POST'])
def hello():
	if request.method == 'POST':
		# print (request.form)
		# param1 = request.form['param1']
		# param2 = request.form['param2']
		# return param1 + param2	
		hello1()
	else:
		return "not post"
####################################################################################################################




if __name__ == '__main__':
	alo()
	application.run(debug = True)

print("Application is down!!!")

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









