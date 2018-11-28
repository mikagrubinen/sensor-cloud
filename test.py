# test.py

from flask import Flask, request
import do
import time
import mysql.connector
# from mysql.connector import Error

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

		data = {}
		do.make_data(mycursor, data)
		print (data)		
		return str(data)
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