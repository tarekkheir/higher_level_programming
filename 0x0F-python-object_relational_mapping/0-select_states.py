#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""


def main():

    import MySQLdb
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(user=user_name, host="localhost",
                         passwd=password, db=database_name, port=3306)

    copy = db.cursor()
    copy.execute("""SELECT * FROM states ORDER BY id""")
    datas = copy.fetchall()

    for data in datas:
        print(data)

    copy.close()
    db.close()


if __name__ == "__main__":
    main()
