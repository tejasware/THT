import pymysql as con

def insert():
    mydb = con.connect(host = "localhost", user="root", passwd = "A18saiapartment", database= "thehightable")
    cursor = mydb.cursor()
    print('-'*30)
    unique_id = input("Unique id:")
    print('-'*30)
    name = input("Name of target:")
    print('-'*30)
    money = input("Money to be paid:")

    insert_query = "Insert into contracts(Unique_ID,Name,Money) values('{}','{}',{})".format(unique_id,name,money)
    cursor.execute(insert_query)
    mydb.commit()
    print('*'*30)
    print("Contract generated")
    print('*'*30)

def printmyContracts():
    mydb = con.connect(host = "localhost", user="root", passwd = "A18saiapartment", database= "thehightable")
    cursor = mydb.cursor()
    print('-'*30)
    unique_id = input("Please enter your id:")
    printCon = "Select*from contracts where Unique_ID = '{}'".format(unique_id)
    cursor.execute(printCon)
    result = cursor.fetchall()
    print('*'*30)
    print("These are contracts by you:")
    for i in result:
        print(i)
    print('*'*30)


def login(id, password):
    try:
        mydb = con.connect(host = "localhost", user="root", passwd = "A18saiapartment", database= "thehightable")
        cursor = mydb.cursor()
        login_query = "Select*from login where Unique_ID = '{}' and password = '{}'".format(id,password)
        cursor.execute(login_query)
        result = cursor.fetchall()
        return result

    except:
        print("Incorrect credentials")


def printContracts():
    mydb = con.connect(host = "localhost", user="root", passwd = "A18saiapartment", database= "thehightable")
    cursor = mydb.cursor()
    printCon = "Select*from contracts where Taken_by is null"
    cursor.execute(printCon)
    result = cursor.fetchall()
    print('*'*30)
    print("These are all available contracts:")
    for i in result:
        print(i)
    print('*'*30)

def apply():
    mydb = con.connect(host = "localhost", user="root", passwd = "A18saiapartment", database= "thehightable")
    cursor = mydb.cursor()
    print('-'*30)
    unique_id = input("Enter Unique id of contractor:")
    print('-'*30)
    name = input("Name of target:")
    print('-'*30)
    hitman_id = input("Your hitman id:")

    apply_query = "Update contracts set Taken_by = '{}' where name = '{}' and Unique_ID = '{}'".format(hitman_id,name,unique_id)
    cursor.execute(apply_query)
    mydb.commit()
    print('*'*30)
    print("You have taken contract, now kill {}".format(name))
    print('*'*30)