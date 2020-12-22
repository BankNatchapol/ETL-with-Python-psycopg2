# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
    create table if not exists songplays (
        songplay_id SERIAL primary key,
        start_time float not null,
        user_id integer not null,
        song_id varchar(255),
        artist_id varchar(255),  
        level varchar(255),
        session_id integer not null,
        location varchar(255),
        user_agent varchar(255),
        foreign key (start_time) 
            references time (start_time),
        foreign key (user_id) 
            references users (user_id),
        foreign key (song_id)
            references songs (song_id),
        foreign key (artist_id)
            references artists (artist_id)
    )
""")

user_table_create = ("""
    create table if not exists users (
        user_id integer primary key,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        gender char(1),
        level varchar(255) not null
    )
""")

song_table_create = ("""
    create table if not exists songs (
        song_id varchar(255) primary key,
        artist_id varchar(255) not null,
        title varchar(255) not null,
        year integer,
        duration float not null
        )
""")

artist_table_create = ("""
    create table if not exists artists (
        artist_id varchar(255) primary key,
        name varchar(255),
        location varchar(255),
        latitude float,
        longitude float
    )
""")

time_table_create = ("""
    create table if not exists time (
        start_time float primary key,
        hour integer not null,
        day integer not null,
        week integer not null,
        month integer not null,
        year integer not null,
        weekday integer not null
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplays ( 
        start_time,
        user_id,
        song_id,
        artist_id, 
        level,
        session_id,
        location,
        user_agent
    ) values ( %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    insert into users (
        user_id,
        first_name,
        last_name,
        gender,
        level
    ) values (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO 
        update set user_id = users.user_id 
""")

song_table_insert = ("""
    insert into songs (
        song_id,
        artist_id,
        title,
        year,
        duration
    ) values (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
    insert into artists (
        artist_id,
        name,
        location,
        latitude,
        longitude
    ) values (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

time_table_insert = ("""
    insert into time (
        start_time,
        hour,
        day,
        week,
        month,
        year,
        weekday
    ) values (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    select s.song_id, a.artist_id from songs as s 
        join artists as a on a.artist_id = s.artist_id
        where s.title=%s and a.name=%s and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]