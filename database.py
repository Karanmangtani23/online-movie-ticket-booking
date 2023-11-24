import mysql.connector
mydb = mysql.connector.connect(
 host="localhost", user="root", password="", database="online_movie_ticket_booking",auth_plugin='mysql_native_password')
c  = mydb.cursor()

def login(userid,passwd):
    c.execute(f"SELECT password,aname from pes1ug21cs268_289_admin where aid = {userid}")
    data = c.fetchall()
    if(passwd==data[0][0]):
        return True,data[0][1]
    else:
        return False,None

def values(value):
    c.execute(f"select * from {value}")
    data = c.fetchall()
    return data
    
def view(value):
    c.execute(f"SELECT * FROM pes1ug21cs268_289_booked_tickets as b natural join pes1ug21cs268_289_shows as s WHERE s.date = '{value}'") 
    data = c.fetchall()
    return data

def add_movie(movieID,movie_name,movie_length,language,show_start,show_end):
    c.execute('insert into pes1ug21cs268_289_movies(movie_id,movie_name,length,language,show_start,show_end) values (%s,%s,%s,%s,%s,%s)',(movieID,movie_name,movie_length,language,show_start,show_end))
    mydb.commit()

def get_movie():
    c.execute('select movie_name from pes1ug21cs268_289_movies')
    data = c.fetchall()
    ans = []
    for i in data:
        ans.append(i[0])
    return ans

def del_movie(movie_name):
    c.execute(f'delete from pes1ug21cs268_289_movies where movie_name= "{movie_name}"')
    mydb.commit()

def update_movie(movieID,movie_name,movie_length,language,show_start,show_end):
    c.execute('update pes1ug21cs268_289_movies set movie_id=%s, movie_name=%s, length=%s, language=%s, show_start = %s, show_end= %s',(movieID,movie_name,movie_length,language,show_start,show_end))
    mydb.commit()

def view_screenid():
    c.execute('SELECT screen_id from pes1ug21cs268_289_screens')
    data = c.fetchall()
    ans = []
    for i in data:
        ans.append(i[0])
    return ans

def view_movieid():
    c.execute('SELECT movie_id from pes1ug21cs268_289_movies')
    data = c.fetchall()
    ans = []
    for i in data:
        ans.append(i[0])
    return ans

def view_priceid():
    c.execute('SELECT price_id from pes1ug21cs268_289_price_list')
    data = c.fetchall()
    ans = []
    for i in data:
        ans.append(i[0])
    return ans

def del_priceid(price_id):
    c.execute(f'delete from pes1ug21cs268_289_price_list where price_id = {price_id}')
    mydb.commit()

def get_show():
    c.execute('select show_id from pes1ug21cs268_289_shows')
    data = c.fetchall()
    ans = []
    for i in data:
        ans.append(i[0])
    return ans

def add_shows(show_id,type,time,date,screen_id,movie_id,price_id):
    c.execute('insert into pes1ug21cs268_289_shows(show_id,type,time,date,screen_id,movie_id,price_id) values (%s,%s,%s,%s,%s,%s,%s)',(show_id,type,time,date,screen_id,movie_id,price_id))
    mydb.commit()

def update_shows(show_id,type,time,date,screen_id,movie_id,price_id):
    c.execute(f'update pes1ug21cs268_289_shows set show_id = "{show_id}",type = "{type}",time = "{time}",date = "{date}",screen_id = "{screen_id}",movie_id = "{movie_id}",price_id = "{price_id}"')
    mydb.commit()

def del_shows(show_id):
    c.execute(f'delete from pes1ug21cs268_289_shows where show_id = {show_id}')
    mydb.commit()

def add_price(price_id,type,day,price):
    c.execute('insert into pes1ug21cs268_289_price_list(price_id,type,day,price) values (%s,%s,%s,%s)',(price_id,type,day,price))
    mydb.commit()

def view_price_list():
    c.execute('select * from pes1ug21cs268_289_price_list')
    data = c.fetchall()
    return data

def update_price(price_id,type,day,price):
    c.execute(f'update pes1ug21cs268_289_price_list set type="{type}", day="{day}", price="{price}" where price_id = "{price_id}"')
    mydb.commit()

def add_screen(screen_id,class_s,capacity):
    c.execute('insert into pes1ug21cs268_289_screens values(%s,%s,%s)',(screen_id,class_s,capacity))
    mydb.commit()

def update_screenid(screen_id,class_s,capacity):
    c.execute('update pes1ug21cs268_289_screens set screen_id=%s, class=%s, no_od_seats=%s',(screen_id,class_s,capacity))
    mydb.commit()

def del_screenid(screen_id):
    c.execute(f'delete from pes1ug21cs268_289_screens where screen_id={screen_id}')
    mydb.commit()

def execute_queries(query):
    c.execute(f"{query}")
    data = c.fetchall()
    mydb.commit()
    return data

# Function to execute SQL queries
def execute_query(query):
    cursor.execute(query)
    conn.commit()

