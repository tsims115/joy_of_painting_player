import json
import sys
import logging
import rds_config
import pymysql

rds_host  = "database-2.c6l5pd13e84v.us-east-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name



logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


def lambda_handler(event, context):
    episodes = {}
    sql = "WHERE "
    if event == []:
        sql = ""

    for i in range(len(event)):
        sql = sql + event[i] + '=1'
        if i < len(event) - 1:
            sql = sql + " AND "
    print(sql)
    with conn.cursor() as cur:
        cur.execute('SELECT painting_title, youtube_src FROM colors_used ' + sql)
        conn.commit()
        for row in cur:
            episodes[row[0]] = row[1]
    conn.commit()
    return {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': r'*'
        },
        'statusCode': 200,
        'body': episodes
    }
