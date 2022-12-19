CREATE DATABASE IF NOT EXISTS joy_of_painting;

CREATE TABLE IF NOT EXISTS colors_used (
    ColumnNumber int PRIMARY KEY,
    painting_index int,
    img_src VARCHAR(250),
    painting_title VARCHAR(250),
    season int,
    episode int,
    num_colors int,
    youtube_src VARCHAR(250),
    colors VARCHAR(500),
    color_hex VARCHAR(500),
    Black_Gesso int,
    Bright_Red int,
    Burnt_Umber int,
    Cadmium_Yellow int,
    Dark_Sienna int,
    Indian_Red int,
    Indian_Yellow int,
    Liquid_Black int,
    Liquid_Clear int,
    Midnight_Black int,
    Phthalo_Blue int,
    Phthalo_Green int,
    Prussian_Blue int,
    Sap_Green int,
    Titanium_White int,
    Van_Dyke_Brown int,
    Yellow_Ochre int,
    Alizarin_Crimson int
);

CREATE TABLE IF NOT EXISTS subject_matter (
    ColumnNumber int PRIMARY KEY,
    EPISODE VARCHAR(250),
    TITLE VARCHAR(250),
    APPLE_FRAME int,
    AURORA_BOREALIS int,
    BARN int,
    BEACH int,
    BOAT int,
    BRIDGE int,
    BUILDING int,
    BUSHES int,
    CABIN int,
    CACTUS int,
    CIRCLE_FRAME int,
    CIRRUS int,
    CLIFF int,
    CLOUDS int,
    CONIFER int,
    CUMULUS int,
    DECIDUOUS int,
    DIANE_ANDRE int,
    DOCK int,
    DOUBLE_OVAL_FRAME int,
    FARM int,
    FENCE int,
    FIRE int,
    FLORIDA_FRAME int,
    FLOWERS int,
    FOG int,
    FRAMED int,
    GRASS int,
    GUEST int,
    HALF_CIRCLE_FRAME int,
    HALF_OVAL_FRAME int,
    HILLS int,
    LAKE int,
    LAKES int,
    LIGHTHOUSE int,
    MILL int,
    MOON int,
    MOUNTAIN int,
    MOUNTAINS int,
    NIGHT int,
    OCEAN int,
    OVAL_FRAME int,
    PALM_TREES int,
    PATH int,
    PERSON int,
    PORTRAIT int,
    RECTANGLE_3D_FRAME int,
    RECTANGULAR_FRAME int,
    RIVER int,
    ROCKS int,
    SEASHELL_FRAME int,
    SNOW int,
    SNOWY_MOUNTAIN int,
    SPLIT_FRAME int,
    STEVE_ROSS int,
    STRUCTURE int,
    SUN int,
    TOMB_FRAME int,
    TREE int,
    TREES int,
    TRIPLE_FRAME int,
    WATERFALL int,
    WAVES int,
    WINDMILL int,
    WINDOW_FRAME int,
    WINTER int,
    WOOD_FRAMED int
);

CREATE TABLE IF NOT EXISTS episode_dates (
    ColumnNumber int PRIMARY KEY,
    Title VARCHAR(250),
    Month VARCHAR(250),
    Day VARCHAR(250),
    Year VARCHAR(250)
);
