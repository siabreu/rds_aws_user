import json
import pymysql

endpoint = 'db-myapp.crbspiwdqkkr.sa-east-1.rds.amazonaws.com'
username = 'admin'
password = 'admin123456'
database_name = 'PERMISSIONS_DB'

connection = pymysql.connect(host=endpoint, user=username, password=password, db=database_name)

def lambda_handler(event, context):
    cursor = connection.cursor()
    cursor.execute('SELECT user.id, user.email, user.username, role.id AS role_id, role.name AS role_name FROM user JOIN user_roles on (user.id=user_roles.user_id)JOIN role on (role.id=user_roles.role_id) WHERE role.name="USER";')
    rows = cursor.fetchall()
    
    return {
        'statusCode': 200,
        'body': json.dumps(rows)
    }
