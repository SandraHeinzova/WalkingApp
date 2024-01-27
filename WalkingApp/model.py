import sqlite3


def _open_database():
    """connect to the database"""
    try:
        conn = sqlite3.connect("walking_data.db")
        conn.execute('''CREATE TABLE WALKS
                    (DATE   CHAR(10)    NOT NULL,
                    KMS     REAL        NOT NULL,
                    TIME    TIME        NOT NULL,
                    KCAL    INT         NOT NULL,
                    STEPS   INT         NOT NULL)''')

        conn.commit()
        return conn

    except sqlite3.OperationalError:
        return sqlite3.connect("walking_data.db")


def get_recent_walks():
    """gets four last walks from database and returns them"""
    conn = _open_database()
    cursor = conn.cursor()

    data = []
    cursor.execute("SELECT * FROM WALKS ORDER BY date DESC LIMIT 4")
    rows = cursor.fetchall()

    for row in rows:
        data.append((row[0], row[1]))

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

    total_km = conn.execute("SELECT SUM(kms) FROM WALKS").fetchone()

    total_time = conn.execute("SELECT time(SUM(strftime('%s', time)),'unixepoch') FROM WALKS").fetchone()

    total_kcal = conn.execute("SELECT SUM(kcal) FROM WALKS").fetchone()

    total_steps = conn.execute("SELECT SUM(steps) FROM WALKS").fetchone()

    conn.close()
    return total_km[0], total_time[0], total_kcal[0], total_steps[0]


selected_date = None
