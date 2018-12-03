# do.py

import mysql.connector
import get
import time

# This function generates data, that will be sent to remote mongodb database
# @param mycursor - mysql object class instance that can execute operations such as SQL statements
# @param data - empty python dict to be filled with data and sensor readings
def make_data(mycursor, data):

	mycursor.execute("SELECT street_id, cluster_id, smart_node_id, sensor_id ,sensor_type_id FROM smart_city_281_sensor_dtls")
	fetch_sensor_info = mycursor.fetchall()

	if not fetch_sensor_info:
		pass
	else:
		for x in fetch_sensor_info:
			mydict = {}
			sensor_data = generate_sensor_data(x[4])
			timestamp = time.asctime( time.localtime(time.time()) )
			mydict.update({	'street_id':int(x[0]), 'cluster_id': int(x[1]), 'smart_node_id':int(x[2]), 
							'sensor_id':int(x[3]), 'sensor_data':sensor_data, 'timestamp':timestamp})
			data.append(mydict)

# This function generates random sensor data based on sensor type
# @param sensor_type: 1 - temperature, 2 - pressure, 3 - humidity, 4 - light
def generate_sensor_data(sensor_type):
	if '1' == sensor_type:
		return get.temperature()
	elif '2' == sensor_type:
		return get.pressure()
	elif '3' == sensor_type:
		return get.humidity()
	elif '4' == sensor_type:
		return get.light()