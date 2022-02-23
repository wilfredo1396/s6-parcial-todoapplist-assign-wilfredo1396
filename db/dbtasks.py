from db.dbconnection import createDBConnection
from models.task import Task


from db.dbconnection import createDBConnection
from models.task import Task


def selectAllTasks():
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.tasks;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


def selectAllTasksByUser(iduser):
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.tasks where iduser=%s;"
            cursor.execute(sql, iduser)
            result = cursor.fetchone()
            return result


def insertNewTask(task: Task):
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `specialtodolistdb`.`status` (`id`,`iduser`,`description`,`idstatus`)VALUES (%s, %s,%s,%s);"
            cursor.execute(sql, (0, task.iduser, task.description, task.idstatus))
        connection.commit()


def selectTaskById(id) -> dict:
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.tasks where id=%s;"
            cursor.execute(sql, id)
            result = cursor.fetchone()
            return result


def updateTask(task: Task):
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `specialtodolistdb`.`task` SET `iduser` = %s, `description` = %s, `idstatus`= %s WHERE `id` = %s;"
            cursor.execute(sql, (task.iduser, task.description, task.idstatus))
        connection.commit()


def deleteTask(id: int):
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `specialtodolistdb`.`tasks` WHERE id=%s;"
            cursor.execute(sql, id)
        connection.commit()
