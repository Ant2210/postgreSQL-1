from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    MetaData,
)
from postgres_settings import postgres_settings1 as settings

# Executing the instruction from our localhost "chinook" db
db = create_engine(
    f"postgresql://{settings['user']}:{settings['pass']}@{settings['host']}:{settings['port']}/{settings['db']}"
)

meta = MetaData(db)

# Create variable for "Artist" table
artist_table = Table(
    "Artist",
    meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String),
)

# Create variable for "Album" table
album_table = Table(
    "Album",
    meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId")),
)

# create variable for "Track" table
track_table = Table(
    "Track",
    meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float),
)


# Making the connection
with db.connect() as connection:
    """
    Compare queries to how they are laid out in sql-psycopg2
    """

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(artist_table.c.Name)

    # Query 3 - Select only "Queen" from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - Select only by "ArtistId" #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - Select all the tracks where the composer is "Queen" from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
