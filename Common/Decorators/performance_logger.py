import functools
from datetime import datetime
from time import time
import sqlite3


def performance_logger_decorator(main_function):
    @functools.wraps(main_function)
    def wrapper(*args, **kwargs):
        function_name = main_function.__name__
        call_datetime = datetime.now()

        start_time = time()
        result = main_function(*args, **kwargs)
        stop_time = time()

        execution_time = stop_time - start_time
        with sqlite3.connect("UserManagment.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
                            INSERT INTO PerformanceLogger (
                                                  function_name,
                                                  execution_time,
                                                  call_datetime
                                              )
                                              VALUES (
                                                  '{function_name}',
                                                  {execution_time},
                                                  '{call_datetime}'
                                              );""")

            connection.commit()

        return result

    return wrapper
