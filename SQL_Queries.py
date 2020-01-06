
# Create queries to ask the following three questions of the data
#  1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
#  2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
#  3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

# Available attributes
# artist
# firstName of user
# gender of user
# item number in session
# last name of user
# length of the song
# level (paid or free song)
# location of the user
# sessionId
# song title
# userId


# Since we have 3 queries, we can create 3 different tables to answer the queries.

CREATE_TABLE_SONG_DETAILS = """ 
CREATE TABLE IF NOT EXISTS song_details(
session_id INT,
item_in_session INT,
artist TEXT,
song_title TEXT,
song_length FLOAT,
PRIMARY KEY(session_id,item_in_session)
)
"""

SONG_DETAIL_SELECT = """SELECT artist, song_title, song_length FROM song_details
                    	 WHERE session_id = %s 
                    	 AND item_in_session = %s"""

INSERT_SONG_DETAILS = """INSERT INTO song_details(session_id, item_in_session, artist, song_title, song_length)
						  VALUES (%s, %s, %s, %s, %s)"""


CREATE_TABLE_ARTIST_DETAILS = """ 
CREATE TABLE IF NOT EXISTS artist_details(
user_id INT,
session_id INT,
item_in_session INT,
artist_name TEXT,
song_title TEXT,
user_first_name TEXT,
user_last_name TEXT,
PRIMARY KEY((user_id, session_id), item_in_session)
)
"""

ARTIST_DETAIL_SELECT = """SELECT artist_name, song_title, user_first_name, user_last_name FROM artist_details
                    WHERE user_id = %s
                    AND session_id = %s"""

INSERT_ARTIST_DETAILS = """INSERT INTO artist_details(user_id, session_id, item_in_session, artist_name,
							song_title, user_first_name, user_last_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

CREATE_TABLE_USER_DETAILS = """ 
CREATE TABLE IF NOT EXISTS user_details(
song_title TEXT, 
user_id INT, 
user_first_name TEXT,
user_last_name TEXT, 
PRIMARY KEY ((song_title), user_id)
)
"""

USER_DETAIL_SELECT = """SELECT user_first_name, user_last_name FROM 
						user_details WHERE song_title = %s"""


INSERT_USER_DETAILS = """ INSERT INTO user_details(song_title, user_id, user_first_name, user_last_name)
							VALUES (%s, %s, %s, %s)"""




CREATE_KEYSPACE = """
CREATE KEYSPACE IF NOT EXISTS SparkifyDB WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1}
"""

DROP_KEYSPACE = "DROP KEYSPACE sparkifydb"

DROP_SONG_DETAILS = "DROP TABLE IF EXISTS sparkifydb.song_details"

DROP_ARTIST_DETAILS = "DROP TABLE IF EXISTS sparkifydb.artist_details"

DROP_USER_DETAILS = "DROP TABLE IF EXISTS sparkifydb.user_details"

