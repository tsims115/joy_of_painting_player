import mysql.connector
f = open("EpisodeDates.csv", "r")
f.readline()
i = 1
catalog = []
for e in f:
    e = e.split(" (")
    e[0] = e[0].replace("\"", "")
    e[1] = e[1].replace(",", "")
    e[1] = e[1].replace(")", "")
    e[1] = e[1].replace("\n", "")
    e[1] = e[1].split(" ")
    catalog.append(e)

mydb = mysql.connector.connect(
  host="database-2.c6l5pd13e84v.us-east-1.rds.amazonaws.com",
  port=3306,
  user="root",
  password="rootroot",
  database="joy_of_painting"
)

mycursor = mydb.cursor()
sql = "INSERT INTO episode_dates (ColumnNumber, Title, Month, Day, Year) VALUES (%s, %s, %s, %s, %s)"
for i in range(len(catalog)):
    val = (i + 1, catalog[i][0], catalog[i][1][0], catalog[i][1][1], catalog[i][1][2])
    mycursor.execute(sql, val)

mydb.commit()

print("Job Done")
