import mysql.connector
f = open("ColorsUsed.csv", "r")
f.readline()
i = 1
catalog = []
for e in f:
    new_episode = []
    if (i == 201):
        episode = e.split(",")
        catalog.append(episode)
        i += 1
        continue
    i += 1
    episode = e.split(",", 8)
    for j in range(0,8):
        new_episode.append(episode[j])
    colors_used_list = episode[8].split('",')[0][1:]
    new_episode.append(colors_used_list)
    colors_used_list_hex = episode[8].split('",')[1][1:]
    new_episode.append(colors_used_list_hex)
    colors_used_by_color = episode[8].split('",')[2].split(",")
    for j in colors_used_by_color:
        new_episode.append(j)
    catalog.append(new_episode)
for i in range(len(catalog)):
    for j in range(len(catalog[i])):
        catalog[i][j] = catalog[i][j].replace(r'\r', "")
        catalog[i][j] = catalog[i][j].replace(r'\n', "")
        catalog[i][j] = catalog[i][j].replace('\n', "")

sql = "INSERT INTO colors_used " \
    "(ColumnNumber, " \
    "painting_index, " \
    "img_src, " \
    "painting_title, " \
    "season, " \
    "episode, " \
    "num_colors, " \
    "youtube_src, " \
    "colors, " \
    "color_hex, " \
    "Black_Gesso, " \
    "Bright_Red, " \
    "Burnt_Umber, " \
    "Cadmium_Yellow, " \
    "Dark_Sienna, " \
    "Indian_Red, " \
    "Indian_Yellow, " \
    "Liquid_Black, " \
    "Liquid_Clear, " \
    "Midnight_Black, " \
    "Phthalo_Blue, " \
    "Phthalo_Green, " \
    "Prussian_Blue, " \
    "Sap_Green, " \
    "Titanium_White, " \
    "Van_Dyke_Brown, " \
    "Yellow_Ochre, " \
    "Alizarin_Crimson) " \
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

mydb = mysql.connector.connect(
  host="database-2.c6l5pd13e84v.us-east-1.rds.amazonaws.com",
  port=3306,
  user="root",
  password="rootroot",
  database="joy_of_painting"
)

mycursor = mydb.cursor()
for i in range(len(catalog)):
    val = (catalog[i][0],
        catalog[i][1],
        catalog[i][2],
        catalog[i][3],
        catalog[i][4],
        catalog[i][5],
        catalog[i][6],
        catalog[i][7],
        catalog[i][8],
        catalog[i][9],
        catalog[i][10],
        catalog[i][11],
        catalog[i][12],
        catalog[i][13],
        catalog[i][14],
        catalog[i][15],
        catalog[i][16],
        catalog[i][17],
        catalog[i][18],
        catalog[i][19],
        catalog[i][20],
        catalog[i][21],
        catalog[i][22],
        catalog[i][23],
        catalog[i][24],
        catalog[i][25],
        catalog[i][26],
        catalog[i][27])
    mycursor.execute(sql, val)

mydb.commit()

print("Job Done")
