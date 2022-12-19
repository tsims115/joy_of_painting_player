import mysql.connector
f = open("SubjectMatter.csv", "r")
f.readline()
i = 1
catalog = []
for e in f:
    e = e.split(",")
    e[1] = e[1].replace("\"", "")
    e[-1] = e[-1].replace("\n", "")
    catalog.append(e)

sql = "INSERT INTO subject_matter " \
    "(ColumnNumber, " \
    "EPISODE, " \
    "TITLE, " \
    "APPLE_FRAME, " \
    "AURORA_BOREALIS, " \
    "BARN, " \
    "BEACH, " \
    "BOAT, " \
    "BRIDGE, " \
    "BUILDING, " \
    "BUSHES, " \
    "CABIN, " \
    "CACTUS, " \
    "CIRCLE_FRAME, " \
    "CIRRUS, " \
    "CLIFF, " \
    "CLOUDS, " \
    "CONIFER, " \
    "CUMULUS, " \
    "DECIDUOUS, " \
    "DIANE_ANDRE, " \
    "DOCK, " \
    "DOUBLE_OVAL_FRAME, " \
    "FARM, " \
    "FENCE, " \
    "FIRE, " \
    "FLORIDA_FRAME, " \
    "FLOWERS, " \
    "FOG, " \
    "FRAMED, " \
    "GRASS, " \
    "GUEST, " \
    "HALF_CIRCLE_FRAME, " \
    "HALF_OVAL_FRAME, " \
    "HILLS, " \
    "LAKE, " \
    "LAKES, " \
    "LIGHTHOUSE, " \
    "MILL, " \
    "MOON, " \
    "MOUNTAIN, " \
    "MOUNTAINS, " \
    "NIGHT, " \
    "OCEAN, " \
    "OVAL_FRAME, " \
    "PALM_TREES, " \
    "PATH, " \
    "PERSON, " \
    "PORTRAIT, " \
    "RECTANGLE_3D_FRAME, " \
    "RECTANGULAR_FRAME, " \
    "RIVER, " \
    "ROCKS, " \
    "SEASHELL_FRAME, " \
    "SNOW, " \
    "SNOWY_MOUNTAIN, " \
    "SPLIT_FRAME, " \
    "STEVE_ROSS, " \
    "STRUCTURE, " \
    "SUN, " \
    "TOMB_FRAME, " \
    "TREE, " \
    "TREES, " \
    "TRIPLE_FRAME, " \
    "WATERFALL, " \
    "WAVES, " \
    "WINDMILL, " \
    "WINDOW_FRAME, " \
    "WINTER, " \
    "WOOD_FRAMED) " \
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

mydb = mysql.connector.connect(
  host="database-2.c6l5pd13e84v.us-east-1.rds.amazonaws.com",
  port=3306,
  user="root",
  password="rootroot",
  database="joy_of_painting"
)

mycursor = mydb.cursor()
for i in range(len(catalog)):
    val = (i + 1,
        catalog[i][0],
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
        catalog[i][27],
        catalog[i][28],
        catalog[i][29],
        catalog[i][30],
        catalog[i][31],
        catalog[i][32],
        catalog[i][33],
        catalog[i][34],
        catalog[i][35],
        catalog[i][36],
        catalog[i][37],
        catalog[i][38],
        catalog[i][39],
        catalog[i][40],
        catalog[i][41],
        catalog[i][42],
        catalog[i][43],
        catalog[i][44],
        catalog[i][45],
        catalog[i][46],
        catalog[i][47],
        catalog[i][48],
        catalog[i][49],
        catalog[i][50],
        catalog[i][51],
        catalog[i][52],
        catalog[i][53],
        catalog[i][54],
        catalog[i][55],
        catalog[i][56],
        catalog[i][57],
        catalog[i][58],
        catalog[i][59],
        catalog[i][60],
        catalog[i][61],
        catalog[i][62],
        catalog[i][63],
        catalog[i][64],
        catalog[i][65],
        catalog[i][66],
        catalog[i][67],
        catalog[i][68])
    mycursor.execute(sql, val)

mydb.commit()

print("Job Done")

