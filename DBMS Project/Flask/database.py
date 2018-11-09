import sqlite3
import time
import datetime
import random
import os
from flask_bcrypt import generate_password_hash, check_password_hash

#conn = sqlite3.connect('mydatabase.db') #create the db
#c = conn.cursor()  #set the cursor for the dataset traversal

conn = sqlite3.connect('mydatabase.db')  #connect to the database 
c = conn.cursor() 

def connect():
	conn = sqlite3.connect('mydatabase.db')  #connect to the database 
	c = conn.cursor()  #set the cursor for the dataset traversal
	return conn,c

#conn,c = connect()
#=================================================================================================================================
#create tables	

def create_table_accounts():
	c.execute('CREATE TABLE IF NOT EXISTS accounts(username varchar(50) not null, first_name varchar(20) not null, last_name varchar(20) not null,email_id varchar(320),password varchar(32) not null,login_status boolean,primary key(username,email_id))')

def create_table_movies():
	c.execute('CREATE TABLE IF NOT EXISTS movies(id varchar(12), name varchar(50) not null, nickname varchar(10),service varchar(15), genre varchar(15) not null,imdb_rating decimal(2,2) not null,user_rating decimal(2,2),cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,release_year int(4) not null,duration_minutes int(4) not null,primary key(id,name))')

def create_table_shows():
	c.execute('CREATE TABLE IF NOT EXISTS shows(id varchar(12), name varchar(50) not null, nickname varchar(10), service varchar(15), genre varchar(15) not null,imdb_rating decimal(2,2) not null,user_rating decimal(2,2),cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,start_year int(4) not null,end_year varchar(8) not null,seasons int(3) not null,primary key(id,name))')

def create_table_watchlist():
	c.execute('CREATE TABLE IF NOT EXISTS watchlist(id varchar(12) primary key, user_id varchar(12), movie_id varchar(12), show_id varchar(12),FOREIGN KEY(user_id)REFERENCES accounts(id),FOREIGN KEY(movie_id) REFERENCES movies(id),FOREIGN KEY(show_id) REFERENCES shows(id))')

def create_table_feedback():
	c.execute('CREATE TABLE IF NOT EXISTS feedback(user_id varchar(12) ,movie_id varchar(12),show_id varchar(12),FOREIGN KEY(user_id) REFERENCES accounts(id),FOREIGN KEY(movie_id) REFERENCES movies(id),FOREIGN KEY(show_id) REFERENCES shows(id))')

def create_table_streams():
	c.execute('CREATE TABLE IF NOT EXISTS streams(stream_id varchar(12) primary key,user_id varchar(12),movie_id varchar(12),show_id varchar(12),foreign key(user_id) references accounts(username),foreign key(movie_id) references movies(id),foreign key(show_id) references shows(id))')


#======================================================================================================================================
#insert_queries

def registration(username = 'null', first_name = 'null', last_name = 'null', email_id = 'null', password = 'null', login_status = 'null'):
	conn, c = connect()
	password = generate_password_hash(password)
	password = str(password,"utf-8")
	c.execute('insert into accounts values (?, ?, ?, ?, ?, ?, ?)', [username, first_name, last_name, email_id, password, login_status])
	conn.commit()
	conn.close()

def insert_movies(id1 = 'null', name = 'null', nickname = 'null', service = 'null', genre = 'null',imdb_rating = 'null',user_rating = 'null',cast_1 = 'null' ,cast_2 = 'null',cast_3 = 'null',cast_4 = 'null',cast_5 = 'null',cast_6 = 'null',director = 'null',release_year = 'null',duration_minutes = 'null'):
	conn, c = connect()
	c.execute('insert into movies values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', [id1 , name , nickname , genre , service ,imdb_rating ,user_rating ,cast_1  ,cast_2 ,cast_3 ,cast_4 ,cast_5 ,cast_6 ,director ,release_year ,duration_minutes ])
	conn.commit()
	conn.close()
	
def insert_shows(id1 = 'null', name = 'null', nickname = 'null', service = 'null', genre = 'null',imdb_rating = 'null',user_rating = 'null',cast_1 = 'null' ,cast_2 = 'null',cast_3 = 'null',cast_4 = 'null',cast_5 = 'null',cast_6 = 'null',director = 'null',start_year = 'null', end_year = 'null',seasons = 'null'):
	conn, c = connect()
	c.execute('insert into shows values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', [id1 , name , nickname , genre , service ,imdb_rating ,user_rating ,cast_1  ,cast_2 ,cast_3 ,cast_4 ,cast_5 ,cast_6 ,director ,start_year, end_year ,seasons ])
	conn.commit()
	conn.close()
	

#======================================================================================================================================
#select_all queries

def select_all_accounts():        #selects info of all accounts 
	conn, c = connect()
	c.execute("select * from accounts")
	data = c.fetchall()
	conn.close()
	# for i in data:
	# 	print(i)
	return data

def select_all_movies():       #selects info of all movies
	conn, c = connect()
	c.execute("select * from movies order by imdb_rating ;")
	data = c.fetchall()
	conn.close()
	# for i in data:
	# 	print(i)
	return data

def select_all_shows():   #selects info of all shows
	conn, c = connect()
	c.execute("select * from shows order by imdb_rating ;")
	data = c.fetchall()
	conn.close()
	# for i in data:
	# 	print(i)
	return data


#===============================================================================================================================
#select queries for movies

#how exactly will we know what search criteria will be specified by the user 
#i.e whatif one of it is left blank or something, 
#maybe we will have to write separate functions based on combinations  
#and then write a separate function that calls the suitable one   

def select_movies_all_cri(genre = 'null', director = 'null', actor = 'null', year = 'null') :
#this one is for the case where all search criteria are applied  
	conn, c = connect()


	if genre == 'null' and actor == 'null' and director == 'null':
		que = "select * from movies"


	else:
		que = 'select * from movies where '
		if genre!= 0:
			que += f"genre = '{genre}'"
			que += " and "
		if director!= 0:
			que += f"director = '{director}'"
			que += " and "
		if actor!=0:
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que+=" and "
		if year!=0:
			que += f"release_year = '{year}'"


	if que.split()[-1] == "and":
		que = que[0:-5]		

	que += f" order by imdb_rating"
	que += ' ;'

	c.execute(que)
	data = c.fetchall()
	conn.close()
	#for i in data:
	#	print(i)
	return data

def select_service_movies(service = 'null'):
	conn, c = connect()

	if service == 'null':
		que = "select * from movies;"

	else:
		que = "select * from movies where service = '{service}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	#for i in data:
	#	print(i)
	return data	

def select_service_shows(service = 'null'):
	conn, c = connect()

	if service == 'null':
		que = "select * from shows;"

	else:
		que = "select * from shows where service = '{service}' order by imdb_rating; "

	c.execute(que)
	data = c.fetchall()
	conn.close()
	# for i in data:
	# 	print(i)
	return data	
#=====================================================================================================================================
#show selection queries
#same doubt as movies

def select_shows_all_cri(genre = 'null', director = 'null', actor = 'null', year = 'null') :
#this one is for the case where all search criteria are applied  
	conn, c = connect()


	if genre == 'null' and actor == 'null' and director == 'null':
		que = "select * from shows"


	else:
		que = 'select * from shows where '
		if genre!= 0:
			que += f"genre = '{genre}'"
			que += " and "
		if director!= 0:
			que += f"director = '{director}'"
			que += " and "
		if actor!=0:
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que+=" and "
		if year!=0:
			que += f"'{year}' between start_year and end_year"


	if que.split()[-1] == "and":
		que = que[0:-5]		

	que += f" order by imdb_rating"
	que += ';'

	c.execute(que)
	data = c.fetchall()
	conn.close()
	# for i in data:
	# 	print(i)
	return data



#==============================================================================================================
#Search By Name
def select_show_name(name):
	conn, c = connect()
	que = f"select * from shows where name = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	# for i in data:
	# 	print(i)
	return data



def select_movie_name(name):
	conn, c = connect()
	que = f"select * from movies where name = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	# for i in data:
	# 	print(i)
	return data



#=============================================================================================================
# table creation functions


conn,c = connect()
create_table_accounts()
create_table_movies()
create_table_shows()
create_table_watchlist()
create_table_feedback()
#=============================================================================================================
#triggers


#===========================================================================================================
#views


#=============================================================================================================


#===========================================================================================================
conn.commit() #commit the current transaction		
c.close()   #close the cursor
conn.close()    #close the connection
#==============================================================================================================
