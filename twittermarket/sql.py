import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'lcenci',
    password = 'root',
    database = 'hack_db'
)

mycursor = db.cursor()

rname = 'jhon'
rusername = 'meyer' 
remail = 'jhon_meyer@gmail.com' 
hashed_password = '28d821812dUDSHADHUSADHU'
rproduct = 'wine'
rlocation = 'atlanta'

#*****UNCOMMENT EACH ONE PER TIME AND RUN THEM IN ORDER*******

# mycursor.execute("CREATE DATABASE hack_db")
# mycursor.execute("CREATE TABLE User(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(60), username VARCHAR(20), email VARCHAR(120), password VARCHAR(60), product VARCHAR(20), city VARCHAR(20)")

# mycursor.execute("INSERT INTO Users(name, username, email, password, product, city) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (rname, rusername, remail, hashed_password, rproduct, rlocation))
# db.commit()

# q = "SELECT * FROM USER WHERE email = {} AND password = {}".format(lemail, lpassword)
# mycursor.execute(q)
# db.commit()

#check q and see if returns none or something, it should return something