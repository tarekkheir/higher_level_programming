#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
    copy.execute("""SELECT cities.name FROM cities
    LEFT JOIN states ON states.id = cities.state_id
    WHERE states.name = '%s' ORDER BY cities.id""" % match_name)
    datas = copy.fetchall()

    print(", ".join([data[0] for data in datas]))

    copy.close()
    db.close()
