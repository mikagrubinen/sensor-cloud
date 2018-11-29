# do.py

import mysql.connector
import get

# This function adds cluster information to data dict, that will be sent to remote mongodb database
# @param mycursor - mysql object class instance that can execute operations such as SQL statements
# @param data - empty python dict to be filled with cluster ids
def make_data(mycursor, data):
		
	# fetch all cluster ids from database	
	mycursor.execute("SELECT cluster_id FROM smart_city_281_cluster")
	fetch_clusters = mycursor.fetchall()

	# check if there is any cluster in a system
	if not fetch_clusters:
		pass
	else:
		for x in fetch_clusters:	
			cluster_id = x[0]
			# key is cluster id, value is empty dict
			data[cluster_id] = {}
			# call node() functions to fill data dict with nodes data
			node(mycursor, data, cluster_id)

# This function adds nodes information to data dict
# @param mycursor - mysql object class instance that can execute operations such as SQL statements
# @param data - python dict filled with cluster ids, to be filled with nodes ids
# @cluster - current cluster id from make_data function
def node(mycursor, data, cluster_id):
	# fetch all node ids connected to given cluster
	mycursor.execute("SELECT smart_node_id FROM smart_city_281_smart_node WHERE smart_node_connected_to_cluster_id = %s", (cluster_id,))
	fetch_nodes = mycursor.fetchall()

	if not fetch_nodes:
		pass
	else:
		for y in fetch_nodes:
			node_id = y[0]
			data[cluster_id][node_id] = {}
			sensor(mycursor, data, cluster_id, node_id)

# This function adds sensors information to data dict
# @param mycursor - mysql object class instance that can execute operations such as SQL statements
# @param data - python dict filled with cluster and node ids, to be filled with newely generated sensor data
# @cluster - current cluster id from make_data function
# @node - current node id from node() function
def sensor(mycursor, data, cluster_id, node_id):
	# fetch all sensor ids connected to given node (including sensor type)
	mycursor.execute("SELECT sensor_id, sensor_type_id FROM smart_city_281_sensor_dtls WHERE smart_node_id = %s", (node_id,))
	fetch_sensors = mycursor.fetchall()	

	if not fetch_sensors:
		pass
	else:
		for z in fetch_sensors:
			sensor_id = z[0]
			sensor_type = z[1]
			sensor_data = generate_sensor_data(sensor_type)
			data[cluster_id][node_id][sensor_id] = sensor_data

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