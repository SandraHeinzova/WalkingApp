import sqlite3


def _open_database():
    """connect to the database"""
    conn = sqlite3.connect("walking_data.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS WALKS
                    (DATE     CHAR(10)    NOT NULL,
                    KMS       REAL        NOT NULL,
                    DURATION  INT         NOT NULL,
                    KCAL      INT         NOT NULL,
                    STEPS     INT         NOT NULL)''')

    conn.commit()
    return conn


def get_recent_walks():
    """gets four last walks from database and returns them"""
    conn = _open_database()

    data = [tuple(row) for row in conn.execute("SELECT date, kms FROM WALKS ORDER BY date DESC LIMIT 4")]

    conn.close()
    return data


def save_to_database(date, kms: float, time, kcal: int, steps: int):
    """gets checked data as params and save them into database
    :param date: date value in required format
    :param kms: kilometres, float value
    :param time: time value in required format
    :param kcal: amount of kcal, int value
    :param steps: amount of steps, int value"""
    conn = _open_database()

    conn.execute("INSERT INTO WALKS VALUES (?, ?, ?, ?, ?)", [date, kms, time, kcal, steps])
    conn.commit()
    conn.close()


def calculate_statistics():
    """receives data from database, calculates statistics and returns them"""
    conn = _open_database()

    totals = tuple(conn.execute("SELECT SUM(kms), SUM(duration), SUM(kcal), SUM(steps) FROM WALKS").fetchone())

    conn.close()
    return totals


selected_date = None
