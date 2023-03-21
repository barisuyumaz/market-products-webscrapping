import psycopg2

hostname = "localhost" #enter hostname
database = "" #name of your database
username = "" #postgresql username
pwd = "" #postgresql password
port_id = 1111 #enter your port id(1111 is not real)



def getConnection():
	conn = psycopg2.connect(
	        host = hostname,
	        dbname = database,
	        user = username,
	        password = pwd,
	        port = port_id)
	return conn

def InsertData(tpl_val):

	conn = getConnection()
	cur = conn.cursor()

	insert_script = 'INSERT INTO products (id, product_code, product_name, product_price, product_brand, stock_info, origin, product_category, product_type) \
	VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

	insert_tuple_value = (tpl_val[0], tpl_val[1], tpl_val[2], tpl_val[3], tpl_val[4], tpl_val[5], tpl_val[6], tpl_val[7], tpl_val[8])

	cur.execute(insert_script,insert_tuple_value)
	conn.commit()


	cur.close()
	conn.close()
