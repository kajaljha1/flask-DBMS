import pymysql

con = None
cursor = None

def dbconnect():
    global con, cursor
    con = pymysql.connect(host='localhost',
                    user='root',
                    password='',
                    database='hospital')
    cursor = con.cursor()    

def dbdisconnect():
    cursor.close()
    con.close()

def insertrecord(id,name,age,location,gender):
    dbconnect()
    query = f'insert into hospital_records values({id},"{name}",{age},"{location}","{gender}")'
    cursor.execute(query)
    con.commit()
    dbdisconnect()

def readall():
    dbconnect()
    query = 'select * from hospital_records'
    cursor.execute(query)
    data = cursor.fetchall()
    #print(data)
    dbdisconnect()
    return data

def readbyid(id):
    dbconnect()
    query = f'select * from hospital_records where id={id}'
    cursor.execute(query)
    data = cursor.fetchone()
    dbdisconnect()
    return data

def updaterecord(data):
    dbconnect()
    query = f'update hospital_records set name="{data[1]}", age={data[2]}, location="{data[3]}",gender="{data[4]}" where id={data[0]}'
    cursor.execute(query)
    con.commit()
    dbdisconnect()

def deleterecord(id):
    dbconnect()
    query = f'delete from hospital_records where id={id}'
    cursor.execute(query)
    con.commit()
    dbdisconnect()

def dbconnect():
    global con, cursor
    con = pymysql.connect(host='localhost',
                    user='root',
                    password='',
                    database='hospital')
    cursor = con.cursor()    

def dbdisconnect():
    cursor.close()
    con.close()

def readall():
    dbconnect()
    query = 'select * from amount_pending_records'
    cursor.execute(query)
    data = cursor.fetchall()
    #print(data)
    dbdisconnect()
    return data


