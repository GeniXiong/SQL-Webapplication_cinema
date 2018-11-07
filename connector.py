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

def check_movie(date, m_type, rate, price):
    m_list = []
    sql = "SELECT M.mname FROM cinema.schedule S, cinema.movie M WHERE M.mid = S.mid and " \
          "S.date = %s and M.type = %s and M.rate > %s and  S.price = %s"
    adr = (date, m_type, rate, price)
    mycursor.execute(sql, adr)
    m_result = mycursor.fetchall()
    for x in m_result:
        m_list.append(x[0])
    return m_list

    
if __name__ == '__main__':
    check_login_movie('fjgj')


    