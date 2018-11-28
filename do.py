# do.py

import mysql.connector

def make_data(mycursor, data):
		
	# fetch all cluster ids from database	
	mycursor.execute("SELECT cluster_id FROM smart_city_281_cluster")
	fetch_clusters = mycursor.fetchall()

	# check if there is any cluster in a system
	if not fetch_clusters:
		pass
	else:
		for x in fetch_clusters:	
			cluster = x[0]
			# key is cluster id, value is empty dict
			data[cluster] = {}
			node(mycursor, data, cluster)


def node(mycursor, data, cluster):
	# fetch all node ids connected to given cluster
	mycursor.execute("SELECT smart_node_id FROM smart_city_281_smart_node WHERE smart_node_connected_to_cluster_id = %s", (cluster,))
	fetch_nodes = mycursor.fetchall()

	for y in fetch_nodes:
		data[cluster][y[0]] = {}


		############# everything needs to be changed
		sensor(mycursor, data, cluster, node)

def sensor(mycursor, data, cluster, node):
	# fetch all sensor ids connected to given node (including sensor type)
	mycursor.execute("SELECT smart_node_id FROM smart_city_281_smart_node WHERE smart_node_connected_to_cluster_id = %s", (cluster,))
	fetch_nodes = mycursor.fetchall()	