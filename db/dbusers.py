from db.dbconnection import createDBConnection
from models.user import User


from db.dbconnection import createDBConnection
from models.user import User


def selectAllUsers():
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.users;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


def insertNewUser(user: User):
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = (
                "INSERT INTO `specialtodolistdb`.`users` (`id`,`user`)VALUES (%s, %s);"
            )
            cursor.execute(sql, (0, user.user))
        connection.commit()


def selectUserById(id) -> dict:
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.users where id=%s;"
            cursor.execute(sql, id)
            result = cursor.fetchone()
            return result


def updateUser(user: User):
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `specialtodolistdb`.`users` SET `user` = %s WHERE `id` = %s;"
            cursor.execute(sql, (user.user))
        connection.commit()


def deleteUser(id: int):
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `specialtodolistdb`.`users` WHERE id=%s;"
            cursor.execute(sql, id)
        connection.commit()
