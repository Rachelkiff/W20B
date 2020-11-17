import mariadb
import dbcreds

print("Welcome!")
username = input("Enter your username: ")
password = input("Enter your password: ")
conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password, host=dbcreds.host,port=dbcreds.port, database=dbcreds.database)
cursor = conn.cursor()
cursor.execute("SELECT * FROM hackers WHERE alias = ?",[username,])
user = cursor.fetchone()
if user:
    if password == user[2]:
        print("Login successful!")
    while 1:
        print("Please choose from the following options: ")
        print("1) Add a new exploit ")
        print("2) View my exploits ")
        print("3) View others exploits ")
        print("4) Exit ")
        option = input("Enter your option: ")
        if option =="1":
            content = input("Enter the exploit content: ")
            cursor.execute("INSERT INTO exploits (content,user_id)VALUES(?,?)",[content,user[0]])
            conn.commit()
            print("Exploit is added!")
        elif option =="2":
            cursor.execute("SELECT * FROM exploits WHERE user_id = ?",[user[0],])
            posts = cursor.fetchall()
            for post in posts:
                print("Exploits id: " + str(post[0]))
                print("Content: " + post[1])
                print("---------------------------------------")
        elif option == "3":
            cursor.execute("SELECT * FROM exploits e INNER JOIN hackers h ON e.user_id=h.id WHERE user_id != ?",[user[0],])
            posts = cursor.fetchall()
            for post in posts:
                print("Alias: " + post[4])
                print("content: " + post[1])
                print("---------------------------------------")
        elif option == "4":
            print("See you, have a nice life!")
            break
        else:
            print("Invalid Entry")
else:
    print("Password is not correct!")



cursor.close()
conn.close()
