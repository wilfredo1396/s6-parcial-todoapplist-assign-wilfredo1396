import pymysql.cursors


def createDBConnection():
    pass


def createDBConnection():
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Vela_124#",
        database="specialtodolistdb",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection
