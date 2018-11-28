# test.py

from flask import Flask, request
import time
import mysql.connector
# from mysql.connector import Error

application = Flask(__name__)
# starttime=time.time()

@application.route("/")
def hello():
	connection = mysql.connector.connect(host='rds-mysql-smartcity.cbtogzj0jikw.us-west-1.rds.amazonaws.com',
	                             database='smartcityadmin',
	                             user='smartcityadmin',
	                             passwd='smartcityadmin')
	if connection.is_connected():
		data = {}
		mycursor = connection.cursor()	
		# fetch all cluster ids from a database	
		mycursor.execute("SELECT cluster_id FROM smart_city_281_cluster")
		myresult = mycursor.fetchall()

		# check if there is any cluster in a system
		if not myresult:
			pass
		else:
			for x in myresult:	
				cluster = x[0]
				# key is cluster id, value is empty dict
				data[cluster] = {}
				# fetch all node ids connected to given cluster
				mycursor.execute("SELECT smart_node_id FROM smart_city_281_smart_node WHERE smart_node_connected_to_cluster_id = %s", (cluster,))
				fetch_nodes = mycursor.fetchall()

				for y in fetch_nodes:
					data[cluster][y[0]] = {}

				# print (fetch_nodes)
		print (data)
		return str(fetch_nodes)

	else:
		return "no connection"


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