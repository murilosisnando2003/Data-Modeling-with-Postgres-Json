# DROP TABLES
"""
    Drops each table using the queries in the list below.
"""

songplay_table_drop = "Drop Table if exists songplays "
user_table_drop = "Drop Table if exists users"
song_table_drop = "Drop Table if exists songs"
artist_table_drop = "Drop Table if exists artists"
time_table_drop = "Drop Table if exists time"

# CREATE TABLES
"""
    Create each table using the queries in the list below.
"""

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS SONGPLAYS(
songplay_id serial NOT NULL PRIMARY KEY,
start_time bigint,
user_id int,
level varchar,
song_id varchar,
artist_id varchar,
session_id int,
location varchar,
user_agent varchar
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id varchar not null primary key,
first_name varchar not null,
last_name varchar not null,
gender char,
level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS SONGS  (
song_id varchar  NOT NULL PRIMARY KEY,
title varchar,
artist_id varchar,
year int,
duration decimal
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS ARTISTS  (
artist_id varchar  NOT NULL PRIMARY KEY,
name varchar,
location varchar,
latitude varchar,
longitude varchar
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS TIME  (
start_time time NOT NULL PRIMARY KEY ,
hour varchar,
day varchar,
week varchar,
month varchar,
year varchar,
weekday varchar);
""")

# INSERT RECORDS
"""
    Insert rows the queries in the list below.
"""
songplay_table_insert = ("""
INSERT INTO SONGPLAYS (
songplay_id, start_time,user_id, level, song_id, artist_id,session_id,location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s) 
ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO USERS (user_id , first_name , last_name , gender , level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level = excluded.level;
""")

song_table_insert = ("""
INSERT INTO SONGS (song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (song_id) DO NOTHING; 
""")

artist_table_insert = ("""
INSERT INTO ARTISTS (artist_id, name, location, latitude, longitude) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (artist_id) DO NOTHING; 
""")

time_table_insert = ("""
INSERT INTO TIME (start_time , hour , day , week , month , year , weekday ) 
values (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING; 
""")

# FIND SONGS
"""
    Select rows in the table songs and artists.
"""

song_select = ("""
SELECT s.song_id,a.artist_id FROM songs s, artists a WHERE s.artist_id = a.artist_id 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]