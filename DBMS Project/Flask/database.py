import sqlite3
import time
import datetime
import random

#conn = sqlite3.connect('mydatabase.db') #create the db
#c = conn.cursor()  #set the cursor for the dataset traversal

def connect():
	conn = sqlite3.connect('mydatabase.db') #create the db
	c = conn.cursor()  #set the cursor for the dataset traversal
	return conn,c

#conn,c = connect()
#=================================================================================================================================
#create tables	

def create_table_accounts():
	c.execute('CREATE TABLE IF NOT EXISTS accounts(id varchar(12), username varchar(50) not null,first_name varchar(20) not null,last_name varchar(20) not null,email_id varchar(320) not null,password varchar(32) not null,primary key(id))')

def create_table_movies():
	c.execute('CREATE TABLE IF NOT EXISTS movies(id varchar(12), name varchar(50) not null,nickname varchar(10),genre varchar(15) not null,imdb_rating decimal(2,2) not null,cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,release_year int(4)not null,duration_minutes int(4) not null,primary key(id,name))')

def create_table_shows():
	c.execute('CREATE TABLE IF NOT EXISTS shows(id varchar(12), name varchar(50) not null,nickname varchar(10),genre varchar(15) not null,imdb_rating decimal(2,2) not null,cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,start_year int(4)not null,end_year varchar(8) not null,seasons int(3) not null,primary key(id,name))')

def create_table_watchlist():
	c.execute('CREATE TABLE IF NOT EXISTS watchlist(id varchar(12) primary key,user_id varchar(12) ,movie_id varchar(12),show_id varchar(12),FOREIGN KEY(user_id)REFERENCES accounts(id),FOREIGN KEY(movie_id) REFERENCES movies(id),FOREIGN KEY(show_id) REFERENCES shows(id))')

def create_table_feedback():
	c.execute('CREATE TABLE IF NOT EXISTS feedback(user_id varchar(12) ,movie_id varchar(12),show_id varchar(12),FOREIGN KEY(user_id)REFERENCES accounts(id),FOREIGN KEY(movie_id) REFERENCES movies(id),FOREIGN KEY(show_id) REFERENCES shows(id))')

#======================================================================================================================================
#insert_queries

def insert_account(id1 = 'null',username1  = 'null', first_name1 = 'null', last_name1 = 'null', email_id1 = 'null', password1 = 'null'):
	conn, c = connect()
	c.execute('insert into accounts values (?, ?, ?, ?, ?, ?)', [id1, username1, first_name1, last_name1, email_id1, password1])
	conn.commit()
	conn.close()
	select_accounts()









#======================================================================================================================================
#select_all queries

def select_all_accounts():        #selects info of all accounts 
	conn, c = connect()
	c.execute("select * from accounts")
	data = c.fetchall()
	conn.close()
	for i in data:
		print(i)
	return data

def select_all_movies():       #selects info of all movies
	conn, c = connect()
	c.execute("select * from movies")
	data = c.fetchall()
	conn.close()
	for i in data:
		print(i)
	return data

def select_all_shows():   #selects info of all shows
	conn, c = connect()
	c.execute("select * from shows")
	data = c.fetchall()
	conn.close()
	for i in data:
		print(i)
	return data


#===============================================================================================================================
#select queries for movies

#how exactly will we know what search criteria will be specified by the user 
#i.e whatif one of it is left blank or something, 
#maybe we will have to write separate functions based on combinations  
#and then write a separate function that calls the suitable one   

def select_movies_all_cri(imdb_rating= null, actor = null, director = null, release_year = null, genre = null) :
#this one is for the case where all search criteria are applied  
	conn, c = connect()
	que = 'select * from movies where '
	if imdb_rating!= 0:
		que += f"imdb_rating >= '{imdb_rating}'"
	if genre!= 0:
		que += f"and genre = '{genre}'"
	if director!= 0:
		que += f"and director = '{director}'"
	if release_year!=0:
		que += f"and release_year = '{release_year}'"
	if actor!=0:
		que += f"and cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
	que += ';'
	c.execute(que)
	data = c.fetchall()
	conn.close()
	for i in data:
		print(i)
	return data




#=====================================================================================================================================
#show selection queries
#same doubt as movies

def select_shows_all_cri(imdb_rating= null, genre = null, actor = null, director = null) :
#this one is for the case where all search criteria are applied  
	conn, c = connect()
	que = 'select * from movies where '
	if imdb_rating!= 0:
		que += f"imdb_rating >= '{imdb_rating}'"
	if genre!= 0:
		que += f"and genre = '{genre}'"
	if director!= 0:
		que += f"and director = '{director}'"
	if actor!=0:
		que += f"and cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
	que += ';'
	c.execute(que)
	data = c.fetchall()
	conn.close()
	for i in data:
		print(i)
	return data


#==============================================================================================================
# table creation functions


#conn,c = connect()
#create_table_accounts()
#create_table_movies()
#create_table_shows()
#create_table_watchlist()
#create_table_feedback()


conn.commit() #commit the current transaction		
c.close()   #close the cursor
conn.close()    #close the connection
