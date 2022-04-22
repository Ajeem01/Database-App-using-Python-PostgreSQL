def create():
    import psycopg2
    conn = psycopg2.connect(dbname='postgres',user='postgres',password='abcde56789',port='5432',host='localhost')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student(ID SERIAL, NAME TEXT, AGE TEXT,ADDRESS TEXT);''')
    print("TABLE CREATED")
    conn.commit()
    conn.close()

def insert_data():
    import psycopg2
    conn = psycopg2.connect(dbname='postgres',user='postgres',password='abcde56789',port='5432',host='localhost')
    cur = conn.cursor()
    name = input('Enter the name: ')
    age = input('Enter the age: ')
    address = input('Enter the address: ')
    query = '''INSERT INTO student(NAME, AGE, ADDRESS) VALUES(%s,%s,%s);'''
    cur.execute(query,(name,age,address))
    print("INSERTED")
    conn.commit()
    conn.close()

insert_data()

