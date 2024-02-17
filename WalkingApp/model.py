import sqlite3
from contextlib import contextmanager


@contextmanager
def _open_database():
    """
    Provide a database connection and close it after use.
    """
    conn = sqlite3.connect("walking_data.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS WALKS
                    (DAY     CHAR(10)    NOT NULL,
                    KMS       REAL        NOT NULL,
                    DURATION  INT         NOT NULL,
                    KCAL      INT         NOT NULL,
                    STEPS     INT         NOT NULL)''')

    conn.commit()
    yield conn
    conn.close()


def get_recent_walks():
    """
    Return the last 4 walks from the database as a list of tuples (date, kms)
    """
    with _open_database() as conn:
        return [tuple(row) for row in conn.execute("SELECT day, kms FROM WALKS ORDER BY day DESC LIMIT 4")]


def save_to_database(day, kms: float, time, kcal: int, steps: int):
    """
    Insert a new walk into the database.
    :param day: date value in the "%d/%m/%y" format
    :param kms: kilometres
    :param time: duration expressed as the number of minutes
    :param kcal: amount of kcal
    :param steps: amount of steps
    """
    with _open_database() as conn:
        conn.execute("INSERT INTO WALKS VALUES (?, ?, ?, ?, ?)", [day, kms, time, kcal, steps])
        conn.commit()


def calculate_overall_statistics():
    """
    Return the sum of kms, duration, kcal and steps from the database as a tuple.
    """
    with _open_database() as conn:
        return tuple(conn.execute("SELECT SUM(kms), SUM(duration), SUM(kcal), SUM(steps) FROM WALKS").fetchone())


def calculate_monthly_statistics():
    """
    Return the monthly sum of kms, duration, kcal and steps from the database as a tuple.
    """
    with _open_database() as conn:
        return tuple(conn.execute("""SELECT day, CURRENT_DATE, SUM(kms), SUM(duration), SUM(kcal), SUM(steps) FROM WALKS 
                                     WHERE SUBSTR(day, 4, 2) = SUBSTR(CURRENT_DATE, 6, 2)
                                     AND SUBSTR(day, 7, 2) = SUBSTR(CURRENT_DATE, 3,2)""").fetchone())


selected_date = None
