# do.py

import mysql.connector
import get
import time
import datetime

# This function generates data, that will be sent to remote mongodb database
# @param mycursor - mysql object class instance that can execute operations such as SQL statements
# @param data - empty python dict to be filled with data and sensor readings
def make_data(mycursor, data):

	mycursor.execute("SELECT a.cluster_id, a.smart_node_id, a.sensor_id, a.sensor_type_id, a.sensor_status, b.street_no, b.street, b.city, b.client_id \
		FROM smart_city_281_sensor_dtls a, smart_city_281_cluster b WHERE a.cluster_id = b.cluster_id")
	fetch_sensor_info = mycursor.fetchall()

	if not fetch_sensor_info:
		pass
	else:
		for x in fetch_sensor_info:
			if x[4] == 'Active':
				mydict = {}
				sensor_data = generate_sensor_data(x[3])
				date = datetime.datetime.today().strftime('%Y-%m-%d')
				time = str(datetime.datetime.now().time())
				mydict.update({	'cluster_id': x[0], 		'smart_node_id':x[1], 
								'sensor_id':str(x[2]), 		'sensor_data':sensor_data, 		
								'date':date, 				'time':time,	
								'street_no':x[5], 			'street':x[6], 				
								'city':x[7],				'client_id': x[8],
								'sensor_type':x[3]})
				data.append(mydict)

# This function generates random sensor data based on sensor type
# @param sensor_type: 1 - temperature, 2 - pressure, 3 - humidity, 4 - light
def generate_sensor_data(sensor_type):
	if 'Temperature' == sensor_type:
		return get.temperature()
	elif 'Pressure' == sensor_type:
		return get.pressure()
	elif 'Humidity' == sensor_type:
		return get.humidity()
	elif 'Light' == sensor_type:
		return get.light()