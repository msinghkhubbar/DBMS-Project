import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('myda.db') #create the db
c = conn.cursor()  #set the cursor for the dataset traversal

def connect():
	conn = sqlite3.connect('myda.db') #create the db
	c = conn.cursor()  #set the cursor for the dataset traversal
	return conn,c




def create_table_mo():
	c.execute('CREATE TABLE IF NOT EXISTS mo(id varchar(12), name varchar(50) not null,nickname varchar(10),genre varchar(15) not null,imdb_rating decimal(2,2) not null,cast_1 varchar(50) not null,cast_2 varchar(50) not null,cast_3 varchar(50),cast_4 varchar(50),cast_5 varchar(50),cast_6 varchar(50),director varchar(50) not null,release_year int(4)not null,duration_minutes int(4) not null,primary key(id))')

#create_table_mo()

def insert_mo1():
	conn, c = connect()
	c.execute("insert into mo values('1231','fury',null,'action',8.5,'brad pitt','logan lerman',null,null,null,null,'abcd',2014,134)")
	conn.commit()
	conn.close()
	

def insert_mo2():
	conn, c = connect()
	c.execute("insert into mo values('1232','inglorious bastards',null,'action',8.9,'brad pitt','Abc',null,null,null,null,'tarantino',1994,138)")
	conn.commit()
	conn.close()
	

def insert_mo3():
	conn, c = connect()
	c.execute("insert into mo values('12345','rtyu',null,'action',8.7,'brad pitt','dfgh',null,null,null,null,'david ayer',2014,134)")
	conn.commit()
	conn.close()
	

def insert_mo4():
	conn, c = connect()
	c.execute("insert into mo values('1234','mmm',null,'action',8.2,'brad pitt','logan lerman',null,null,null,null,'david ayer',2014,134)")
	conn.commit()
	conn.close()
	

def select_col(director = 'tarantino',release_year = 1994):
	conn, c = connect()
	que = 'select * from mo where '
	if director!= 0:
		que += f"director = '{director}'"
	if release_year!=0:
		que += f"and release_year = '{release_year}'"
	que += ';'
	c.execute(que)



# insert_mo4()
# insert_mo3()
# insert_mo2()
# insert_mo1()

select_col()

conn.commit() #commit the current transaction		
c.close()   #close the cursor
conn.close() #close the connection