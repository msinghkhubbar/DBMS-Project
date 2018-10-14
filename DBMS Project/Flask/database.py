import sqlite3

conn = sqlite3.connect('mydatabase.db') #create the db
c = conn.cursor()  #set the cursor for the dataset traversal


def create_table_accounts():
	c.execute('CREATE TABLE IF NOT EXISTS accounts(id varchar(12), username varchar(50) not null,first_name varchar(20) not null,last_name varchar(20) not null,email_id varchar(320) not null,password varchar(32) not null,primary key(id))')

def create_table_movies():
	c.execute('CREATE TABLE IF NOT EXISTS movies(id varchar(12), name varchar(50) not null,nickname varchar(10) not null,genre varchar(15) not null,imdb_rating decimal(2,2) not null,cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,release_year int(4)not null,duration_minutes int(4) not null,primary key(id,name))')

def create_table_shows():
	c.execute('CREATE TABLE IF NOT EXISTS shows(id varchar(12), name varchar(50) not null,nickname varchar(10) not null,genre varchar(15) not null,imdb_rating decimal(2,2) not null,cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,start_year int(4)not null,end_year varchar(8) not null,seasons int(3) not null,primary key(id,name))')

def create_table_watchlist():
	c.execute('CREATE TABLE IF NOT EXISTS watchlist(id varchar(12) primary key,user_id varchar(12) ,movie_id varchar(12),show_id varchar(12),FOREIGN KEY(user_id)REFERENCES accounts(id),FOREIGN KEY(movie_id) REFERENCES movies(id),FOREIGN KEY(show_id) REFERENCES shows(id))')

def create_table_feedback():
	c.execute('CREATE TABLE IF NOT EXISTS feedback(user_id varchar(12) ,movie_id varchar(12),show_id varchar(12),FOREIGN KEY(user_id)REFERENCES accounts(id),FOREIGN KEY(movie_id) REFERENCES movies(id),FOREIGN KEY(show_id) REFERENCES shows(id))')




create_table_accounts()
create_table_movies()
create_table_shows()
create_table_watchlist()
create_table_feedback()



conn.commit() #commit the current transaction		
c.close()   #close the cursor
conn.close()    #close the connection
