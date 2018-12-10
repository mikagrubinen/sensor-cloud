# do.py

import mysql.connector
import get
import time
import datetime

# This function generates data, that will be sent to remote mongodb database
# @param mycursor - mysql object class instance that can execute operations such as SQL statements
# @param data - empty python dict to be filled with data and sensor readings
def make_data(mycursor, data):

	mycursor.execute("SELECT a.cluster_id, a.smart_node_id, a.sensor_id, a.sensor_type_id, a.sensor_status, b.street_no, b.street, b.city \
		FROM smart_city_281_sensor_dtls a, smart_city_281_cluster b WHERE a.cluster_id = b.cluster_id")
	fetch_sensor_info = mycursor.fetchall()

	# print(fetch_sensor_info)

	if not fetch_sensor_info:
		pass
	else:
		for x in fetch_sensor_info:
			if x[4] == 'active':
				mydict = {}
				sensor_data = generate_sensor_data(x[3])
				date = datetime.datetime.today().strftime('%Y-%m-%d')
				time = str(datetime.datetime.now().time())
				mydict.update({	'cluster_id': int(x[0]), 	'smart_node_id':int(x[1]), 
								'sensor_id':int(x[2]), 		'sensor_data':sensor_data, 		'date':date, 'time':time,
								'street_no':int(x[5]), 		'street':x[6], 'city':x[7]})
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