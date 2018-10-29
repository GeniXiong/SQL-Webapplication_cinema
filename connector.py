import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="xw55555"
)
mycursor = mydb.cursor()

def check_login(name, pwd):
    sql = "SELECT pwd FROM cinema.accounts WHERE name = %s"
    adr = (name, )
    mycursor.execute(sql, adr)
    check_pwd = str(mycursor.fetchone()[0])
    print(check_pwd)
    if pwd == check_pwd:
        return True
    else:
        return False

    
#if __name__ == '__main__':
#    mydb = mysql.connector.connect(
#      host="localhost",
#      user="root",
#      passwd="xw55555"
#    )
#    mycursor = mydb.cursor()
#
#    
#    mycursor.execute(sql, adr)