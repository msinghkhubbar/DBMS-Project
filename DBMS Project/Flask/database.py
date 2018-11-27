import sqlite3
import time
import datetime
import random
import os
import database

conn = sqlite3.connect('mydatabase.db')  #connect to the database 
c = conn.cursor() 

def connect():
	conn = sqlite3.connect('mydatabase.db')  #connect to the database 
	c = conn.cursor()  #set the cursor for the dataset traversal
	return conn,c

conn,c = connect()

#=================================================================================================================================
#create tables	
def create_table_accounts():
	c.execute('CREATE TABLE IF NOT EXISTS accounts(first_name varchar(20) not null, last_name varchar(20) not null,email_id varchar(320) not null,password varchar(32) not null,primary key(email_id))')

def create_table_movies():
	c.execute('CREATE TABLE IF NOT EXISTS shows(id varchar(12), name varchar(50) not null, nickname varchar(10),service varchar(15) not null, genre varchar(15) not null,imdb_rating decimal(2,2) not null,user_rating decimal(2,2),cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,release_year int(4) not null,duration_minutes int(4) not null,primary key(id))')

def create_table_shows():
	c.execute('CREATE TABLE IF NOT EXISTS shows(id varchar(12), name varchar(50) not null, nickname varchar(10), service varchar(15) not null, genre varchar(15) not null,imdb_rating decimal(2,2) not null,user_rating decimal(2,2),cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,start_year int(4) not null,end_year varchar(8) not null,seasons int(3) not null,primary key(id))')

def create_table_watchlist():
	c.execute('CREATE TABLE IF NOT EXISTS watchlist(email_id varchar(12) not null, movie_id varchar(12), show_id varchar(12), movie_name varchar(50) ,show_name varchar(50),CONSTRAINT uniq UNIQUE(email_id,movie_id,show_id),FOREIGN KEY(email_id) REFERENCES accounts(email_id) on update cascade)')


def create_table_feedback():
	c.execute('CREATE TABLE IF NOT EXISTS feedback(email_id varchar(12) ,movie_id varchar(12),show_id varchar(12),rating decimal(2.2),comments varchar(280),CONSTRAINT uniqs UNIQUE(email_id,movie_id,show_id),FOREIGN KEY(email_id) REFERENCES accounts(email_id) on update cascade,FOREIGN KEY(movie_id) REFERENCES movies(id) on update cascade,FOREIGN KEY(show_id) REFERENCES shows(id) on update cascade )')

def create_table_streams():
	c.execute('CREATE TABLE IF NOT EXISTS streams(stream_id varchar(12) primary key,user_id varchar(12),movie_id varchar(12),show_id varchar(12),foreign key(user_id) references accounts(username),foreign key(movie_id) references movies(id),foreign key(show_id) references shows(id));')

def create_table_recommend():
	c.execute('CREATE TABLE IF NOT EXISTS recommend(movie_name varchar(50), show_name varchar(50))')

#======================================================================================================================================
#insert_queries

def registration(first_name = 'null', last_name = 'null', email_id = 'null', password = 'null'):
	conn, c = connect()
	c.execute('insert into accounts values (?, ?, ?, ?)', [first_name, last_name, email_id, password])
	conn.commit()
	conn.close()

def insert_movies(id1 = 'null', name = 'null', nickname = 'null', service = 'null', genre = 'null',imdb_rating = 'null',user_rating = 'null',cast_1 = 'null' ,cast_2 = 'null',cast_3 = 'null',cast_4 = 'null',cast_5 = 'null',cast_6 = 'null',director = 'null',release_year = 'null',duration_minutes = 'null'):
	conn, c = connect()
	c.execute('insert into movies values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', [id1 , name , nickname ,service , genre ,imdb_rating ,user_rating ,cast_1  ,cast_2 ,cast_3 ,cast_4 ,cast_5 ,cast_6 ,director ,release_year ,duration_minutes])
	conn.commit()
	conn.close()
	
def insert_shows(id1 = 'null', name = 'null', nickname = 'null', service = 'null', genre = 'null',imdb_rating = 'null',user_rating = 'null',cast_1 = 'null' ,cast_2 = 'null',cast_3 = 'null',cast_4 = 'null',cast_5 = 'null',cast_6 = 'null',director = 'null',start_year = 'null', end_year = 'null',seasons = 'null'):
	conn, c = connect()
	c.execute('insert into shows values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', [id1 , name , nickname , genre , service ,imdb_rating ,user_rating ,cast_1  ,cast_2 ,cast_3 ,cast_4 ,cast_5 ,cast_6 ,director ,start_year, end_year ,seasons ])
	conn.commit()
	conn.close()
	
def check_login(email):
	conn,c = connect()
	c.execute(f'select password from accounts where email_id = "{email}" ;')
	data = c.fetchall()
	conn.close()
	return data[0]

def select_users():   #selects info of all shows
    conn, c = connect()
    c.execute("select email_id from accounts")
    data = c.fetchall()
    conn.close()
    result1 = [x[0] for x in data]
    print(result1)
    return result1
#======================================================================================================================================
#select_all queries

def select_all_accounts():        #selects info of all accounts 
	conn, c = connect()
	c.execute("select * from accounts ;")
	data = c.fetchall()
	conn.close()
	return data

def select_all_movies():       #selects info of all movies
	conn, c = connect()
	c.execute("select * from movies order by imdb_rating ;")
	data = c.fetchall()
	conn.close()
	return data

def select_all_shows():   #selects info of all shows
	conn, c = connect()
	c.execute("select * from shows order by imdb_rating ;")
	data = c.fetchall()
	conn.close()
	return data

def select_rec():   
	conn, c = connect()
	c.execute("select distinct * from recommend ;")
	data = c.fetchall()
	conn.close()
	return data	

#=====================================================================================================================
#insert into recommendation	

def rec_submit(idd):      
	conn, cur = connect()
	data1 = ()
	data2 = ()
	data3 = ()
	data4 = ()
	data5 = ()
	data6 = ()
	# cur.execute(f"delete from recommend;")
	if idd[0]=='M':
		cur.execute(f"select genre from movies where movies.id = '{idd}';")
		genre1 = cur.fetchall()
		
		cur.execute(f"select cast_1 from movies where movies.id = '{idd}';")
		actor1 = cur.fetchall()
		
		cur.execute(f"select director from movies where movies.id = '{idd}';")
		direc1 = cur.fetchall()
	else:
		cur.execute(f"select genre from shows where shows.id = '{idd}';")
		genre1 = cur.fetchall()
		
		cur.execute(f"select cast_1 from shows where shows.id = '{idd}';")
		actor1 = cur.fetchall()
		
		cur.execute(f"select director from shows where shows.id = '{idd}';")
		direc1 = cur.fetchall()
	
	if idd[0]=='M':
		cur.execute(f"select name from movies where genre = '{genre1[0][0]}' and id != '{idd}';")
		data1 = cur.fetchall()
		cur.execute(f"select name from movies where cast_1 = '{actor1[0][0]}' and id != '{idd}' ;")
		data2 = cur.fetchall()
		cur.execute(f"select name from movies where director = '{direc1[0][0]}' and id != '{idd}'; ")
		data3 = cur.fetchall()
	else:
		cur.execute(f"select name from shows where genre = '{genre1[0][0]}' and id != '{idd}';")
		data1 = cur.fetchall()
		cur.execute(f"select name from shows where cast_1 = '{actor1[0][0]}' and id != '{idd}' ;")
		data2 = cur.fetchall()
		cur.execute(f"select name from shows where director = '{direc1[0][0]}' and id != '{idd}'; ")
		data3 = cur.fetchall()
	
	insert_qu1 = f"'insert into recommend values (?, ?)',[item,'NA'] "

	for item in data1:
		cur.execute('insert into recommend values (?, ?)', [item[0] ,'NA'])
	for item in data2:
		cur.execute('insert into recommend values (?, ?)', [item[0] ,'NA'])
	for item in data3:
		cur.execute('insert into recommend values (?, ?)', [item[0] ,'NA'])

	conn.commit()
	conn.close()
	
	



def select_movies_all_cri_amazon(genre = 'null',director = 'null', actor = 'null', year = 'null'):
#this one is for the case where all search criteria are applied  
	conn, c = connect()

	que=""

	if genre == 'null' and actor == 'null' and director == 'null' and year == 'null':
		que = "select * from movies where service = 'Prime Video' "


	else:
		que = "select * from movies where service = 'Prime Video' and "
		if genre != 'null':
			que += f"genre = '{genre}'"
			que += " and "
		if director != 'null':
			que += f"director = '{director}'"
			que += " and "	
		if actor != 'null':
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que += " and "
		if year != 'null':
			que += f"release_year = '{year}'"

	
	if que.split()[-1] == "and":
		que = que[0:-5]	

	que += f" order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.commit()
	conn.close()
	return data

def select_movies_all_cri_hotstar(genre = 'null',director = 'null', actor = 'null', year = 'null'):
#this one is for the case where all search criteria are applied  
	conn, c = connect()

	que=""

	if genre == 'null' and actor == 'null' and director == 'null' and year == 'null':
		que = "select * from movies where service = 'Hotstar' "


	else:
		que = "select * from movies where service = 'Hotstar' and "
		if genre != 'null':
			que += f"genre = '{genre}'"
			que += " and "
		if director != 'null':
			que += f"director = '{director}'"
			que += " and "	
		if actor != 'null':
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que += " and "
		if year != 'null':
			que += f"release_year = '{year}'"

	
	if que.split()[-1] == "and":
		que = que[0:-5]	

	que += f" order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.commit()
	conn.close()
	return data

def select_movies_all_cri_netflix(genre = 'null',director = 'null', actor = 'null', year = 'null'):
#this one is for the case where all search criteria are applied  
	conn, c = connect()

	que=""

	if genre == 'null' and actor == 'null' and director == 'null' and year == 'null':
		que = "select * from movies where service = 'Netflix' "


	else:
		que = "select * from movies where service = 'Netflix' and "
		if genre != 'null':
			que += f"genre = '{genre}'"
			que += " and "
		if director != 'null':
			que += f"director = '{director}'"
			que += " and "	
		if actor != 'null':
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que += " and "
		if year != 'null':
			que += f"release_year = '{year}'"

	
	if que.split()[-1] == "and":
		que = que[0:-5]	

	que += f" order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.commit()
	conn.close()
	return data

#==========================================================================================================================	

def select_shows_all_cri_amazon(genre = 'null',director = 'null', actor = 'null', year = 'null'):
#this one is for the case where all search criteria are applied  
	conn, c = connect()

	que=""

	if genre == 'null' and actor == 'null' and director == 'null' and year == 'null':
		que = "select * from shows where service = 'Prime Video' "


	else:
		que = "select * from shows where service = 'Prime Video' and "
		if genre != 'null':
			que += f"genre = '{genre}'"
			que += " and "
		if director != 'null':
			que += f"director = '{director}'"
			que += " and "	
		if actor != 'null':
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que += " and "
		if year != 'null':
			que += f"'{year}' between start_year and end_year"

	
	if que.split()[-1] == "and":
		que = que[0:-5]	

	que += f" order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.commit()
	conn.close()
	return data

def select_shows_all_cri_hotstar(genre = 'null',director = 'null', actor = 'null', year = 'null'):
#this one is for the case where all search criteria are applied  
	conn, c = connect()

	que=""

	if genre == 'null' and actor == 'null' and director == 'null' and year == 'null':
		que = "select * from shows where service = 'Hotstar' "


	else:
		que = "select * from shows where service = 'Hotstar' and "
		if genre != 'null':
			que += f"genre = '{genre}'"
			que += " and "
		if director != 'null':
			que += f"director = '{director}'"
			que += " and "	
		if actor != 'null':
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que += " and "
		if year != 'null':
			que += f"'{year}' between start_year and end_year"

	
	if que.split()[-1] == "and":
		que = que[0:-5]	

	que += f" order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.commit()
	conn.close()
	return data

def select_shows_all_cri_netflix(genre = 'null',director = 'null', actor = 'null', year = 'null'):
#this one is for the case where all search criteria are applied  
	conn, c = connect()

	que=""

	if genre == 'null' and actor == 'null' and director == 'null' and year == 'null':
		que = "select * from shows where service = 'Netflix' "


	else:
		que = "select * from shows where service = 'Netflix' and "
		if genre != 'null':
			que += f"genre = '{genre}'"
			que += " and "
		if director != 'null':
			que += f"director = '{director}'"
			que += " and "	
		if actor != 'null':
			que += f"cast_1 = '{actor}' or cast_2 = '{actor}' or cast_3 = '{actor}' or cast_4 = '{actor}' or cast_5 = '{actor}' or cast_6 = '{actor}'"
			que += " and "
		if year != 'null':
			que += f"'{year}' between start_year and end_year"

	
	if que.split()[-1] == "and":
		que = que[0:-5]	

	que += f" order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.commit()
	conn.close()
	return data	



#==============================================================================================================
#Search By Name
def select_show_name_netflix(name):
	conn, c = connect()
	que = f"select * from show_shows where service = 'Netflix' and name = '{name}' or nickname = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	return data


def select_movie_name_netflix(name):
	conn, c = connect()
	que = f"select * from show_movies where service = 'Netflix' and name = '{name}' or nickname = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	return data

def select_show_name_amazon(name):
	conn, c = connect()
	que = f"select * from show_shows where service = 'Prime Video' and name = '{name}' or nickname = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	return data


def select_movie_name_amazon(name):
	conn, c = connect()
	que = f"select * from show_movies where service = 'Prime Video' and name = '{name}' or nickname = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	return data	

def select_show_name_hotstar(name):
	conn, c = connect()
	que = f"select * from show_shows where service = 'Hotstar' and name = '{name}' or nickname = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	return data


def select_movie_name_hotstar(name):
	conn, c = connect()
	que = f"select * from show_movies where service = 'Hotstar' and name = '{name}' or nickname = '{name}' order by imdb_rating;"

	c.execute(que)
	data = c.fetchall()
	conn.close()
	return data		

#=============================================================================================================
#feedback

def feedback_name(idd):
	conn,c = connect()
	que = f"select name from movies where id = '{idd}' ;"
	que1 = f"select name from shows where id = '{idd}' ;"
	if(idd[0] == 'M'):
		c.execute(que)
	elif(idd[0] == 'S'):
		c.execute(que1)

	data = c.fetchall()
	conn.close()
	return data

def feedback_submit(uid,idd,rating,comment):
	conn, c = connect()
	NA = 'NA'
	print("HELLO")
	print(idd)
	c.execute(f"select * from feedback where email_id = '{uid}' and movie_id = '{idd}' or show_id = '{idd}'; ")
	datac = c.fetchall()
	if not datac:
		if(idd[0] == 'M'):
			c.execute('insert into feedback values (?, ?, ?, ?, ?)', [uid,idd,NA,rating,comment])
		else:
			c.execute('insert into feedback values (?, ?, ?, ?, ?)', [uid,NA,idd,rating,comment])
	
	conn.commit()
	conn.close()
	


#=============================================================================================================
#watchlist

def watchlist_submit(eid,idd):
	conn, c = connect()
	NA = 'NA'

	na_m = f"select name from movies where id = '{idd}';"
	na_s = f"select name from shows where id = '{idd}';"
	c.execute(na_m)
	name_m = c.fetchall()
	c.execute(na_s)
	name_s = c.fetchall()
	print(str(name_s))
	print(str(name_m))
	c.execute(f"select * from watchlist where email_id = '{eid}' and movie_id = '{idd}' or show_id = '{idd}'")
	data1 = c.fetchall()
	print("hello")
	print(idd)
	if not data1:
		if(idd[0] == 'M'):
			c.execute('insert into watchlist values (?, ?, ?, ?, ?)',[eid,idd,'NA',str(name_m),'NA'])
		if(idd[0] == 'S'):
			c.execute('insert into watchlist values (?, ?, ?, ?, ?)',[eid,'NA',idd,'NA',str(name_s)])
	conn.commit()
	conn.close()
	

def watchlist_display(eid):
	conn, c = connect()

	que = f'select movies.name,movies.genre,movies.imdb_rating from watchlist,movies where watchlist.email_id = "{eid}" and watchlist.movie_id = movies.id;'
	que1 = f'select shows.name,shows.genre,shows.imdb_rating from watchlist,shows where watchlist.email_id = "{eid}" and watchlist.show_id = shows.id;'

	c.execute(que)
	data1 = c.fetchall()
	c.execute(que1)
	data2 = c.fetchall()
	print(data1)
	print(data2)
	
	conn.close()
	return (data1,data2)


#==============================================================================================================
#views

def movies_view():

	conn, cur = connect()

	cur.execute('''CREATE VIEW show_movies as SELECT 
				name,
				nickname,
				service,
				genre,
				director,
				imdb_rating,
				user_rating,
				cast_1,
				cast_2,
				release_year
					from movies;''')

	conn.commit()
	conn.close()


def shows_view():

	conn, cur = connect()

	cur.execute('''CREATE VIEW show_shows as SELECT 
				name,
				nickname,
				service,
				genre,
				director,
				imdb_rating,
				user_rating,
				cast_1,
				cast_2,
				start_year as 'from',
				end_year as 'to'
					from shows;''')

	conn.commit()
	conn.close()

conn, cur = connect()
cur.execute(f'drop view show_movies ;')
cur.execute(f'drop view show_shows ;')
movies_view()
shows_view()	
conn.commit() #commit the current transaction		
# c.close()   #close the cursor
conn.close() 


def show_movies_view():

	conn, cur = connect()

	cur.execute('SELECT * from show_movies')
	data = cur.fetchall()
	conn.close()

	for r in data:
		print(r)

	return data


def show_shows_view():

	conn, cur = connect()

	cur.execute('SELECT * from show_shows')
	data = cur.fetchall()
	conn.close()

	for r in data:
		print(r)

	return data

'''
---------------------------------------------------------------------------------------------------------------------
Triggers
'''

def create_trigger_show():

	conn, cur = connect()

	cur.execute('''CREATE trigger update_show_rating
				   
				   after INSERT
				   on feedback
				   WHEN NEW.movie_id == 'NA'
				   
				   BEGIN	 

						update shows set user_rating = (select avg(rating) from feedback where show_id = new.show_id) where id = new.show_id;

				   END;

				''')

	conn.commit()
	conn.close()

def create_trigger_movie():

	conn, cur = connect()

	cur.execute('''CREATE trigger update_movie_rating
				   
				   after INSERT
				   on feedback
				   WHEN NEW.show_id == 'NA'
				   
				   BEGIN	 

						update movies set user_rating = (select avg(rating) from feedback where movie_id = new.movie_id) where id = new.movie_id;

				   END;

				''')

	conn.commit()
	conn.close()