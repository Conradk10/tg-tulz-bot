import logging
import pymysql
from rich import print
from data.config import mysql_info as db

connection = pymysql.connect(db['host'], db['user'], db['password'], db['db'], cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True, init_command=print("[bold green]🗄  БД успешно подключена!"))


def logger(statement):
    logging.basicConfig(
        level=logging.INFO,
        filename="logs.log",
        format=f"[Executing] [%(asctime)s] | [%(filename)s LINE:%(lineno)d] | {statement}",
        datefmt="%d-%b-%y %H:%M:%S"
    )
    logging.info(statement)


def handle_silently(function):
    def wrapped(*args, **kwargs):
        result = None
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            logger("{}({}, {}) failed with exception {}".format(
                function.__name__, repr(args[1]), repr(kwargs), repr(e)))
        return result

    return wrapped


# Форматирование запроса с аргументами
def update_format_with_args(sql, parameters: dict):
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)
    return sql, tuple(parameters.values())


# Форматирование запроса без аргументов
def get_format_args(sql, parameters: dict):
    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])
    return sql, tuple(parameters.values())


# Получение пользователя
def get_free_sql(query: str, args=None):
    connection.ping()
    with connection.cursor() as cursor:
        cursor.execute(query, args)
        response = cursor.fetchone()
    return response


# Получение пользователей
# def get_free_sqls(**kwargs):
#     with sqlite3.connect(path_to_db) as db:
#         sql = "SELECT * FROM storage_users WHERE "
#         sql, parameters = get_format_args(sql, kwargs)
#         get_response = db.execute(sql, parameters)
#         get_response = get_response.fetchall()
#     return get_response
