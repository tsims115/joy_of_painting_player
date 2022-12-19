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
    print('================')
    print(event)
    print('================')
    sql = "WHERE "
    if event == []:
        sql = ""

    for i in range(len(event)):
        if event[i] == "Fall":
            sql = sql + 'Month="September"' + ' OR ' + 'Month="October"' + ' OR ' + 'Month="November"'
        if event[i] == "Summer":
            sql = sql + 'Month="June"' + ' OR ' + 'Month="July"' + ' OR ' + 'Month="August"'
        if event[i] == "Winter":
            sql = sql + 'Month="January"' + ' OR ' + 'Month="February"' + ' OR ' + 'Month="December"'
        if event[i] == "Spring":
            sql = sql + 'Month="March"' + ' OR ' + 'Month="April"' + ' OR ' + 'Month="May"'
        if i < len(event) - 1:
            sql = sql + " OR "
    print(sql)
    with conn.cursor() as cur:
        cur.execute('SELECT episode_dates.Title, colors_used.youtube_src FROM episode_dates INNER JOIN colors_used ON episode_dates.ColumnNumber = colors_used.ColumnNumber ' + sql)
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
