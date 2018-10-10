import sqlite3

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

def create_table_accounts():
	c.execute('CREATE TABLE IF NOT EXISTS accounts(id varchar(12), username varchar(50) not null,first_name varchar(20) not null,last_name varchar(20) not null,email_id varchar(320) not null,password varchar(32) not null,primary key(id))')

def create_table_movies():
	c.execute('CREATE TABLE IF NOT EXISTS movies(id varchar(12), name varchar(50) not null,nickname varchar(10) not null,genre varchar(15) not null,imdb_rating decimal(2,2) not null,cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,release_year int(4)not null,duration_minutes int(4) not null,primary key(id,name))')

def create_table_shows():
	c.execute('CREATE TABLE IF NOT EXISTS shows(id varchar(12), name varchar(50) not null,nickname varchar(10) not null,genre varchar(15) not null,imdb_rating decimal(2,2) not null,cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,start_year int(4)not null,end_year varchar(8) not null,seasons int(3) not null,primary key(id,name))')

def create_table_watchlist():
	c.execute('CREATE TABLE IF NOT EXISTS watchlist(user_id varchar(12) ,movie_id varchar(12),show_id varchar(12),user_id varchar(12) FOREIGN KEY REFERENCES accounts(id),movie_id varchar(12) FOREIGN KEY REFERENCES movies(id),show_id varchar(12) FOREIGN KEY REFERENCES shows(id))')

def data_entry():
	c.execute("INSERT INTO accounts values('1234','asdf','asdfg','asdfgh','asdf@gmail.com','add')")
	conn.commit()
	c.close()
	conn.close()


create_table_accounts()
create_table_movies()
create_table_shows()
#create_table_watchlist()
data_entry()	
