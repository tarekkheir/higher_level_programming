#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    match_name = sys.argv[4]

    db = MySQLdb.connect(user=user_name, host="localhost",
                         passwd=password, db=database_name, port=3306)
    copy = db.cursor()
    copy.execute("""SELECT * FROM states WHERE name='%s'
    ORDER BY id""" % match_name)
    datas = copy.fetchall()

    for data in datas:
        print(data)

    copy.close()
    db.close()
