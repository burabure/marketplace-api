import sqlite3
import html
import time


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def __connect():
    connection = sqlite3.connect('marketplace.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    return [connection, cursor]


def init():
    [connection, cursor] = __connect()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS listings (
            id TEXT primary key,
            title TEXT,
            price TEXT,
            primaryPhotoUrl TEXT,
            sellerLocation TEXT,
            dismissed BOOLEAN,
            seenAt INTEGER
        )""")
    connection.commit()
    connection.close()


def insert_listing(id, name, currentPrice, primaryPhotoUrl, sellerLocation):
    [connection, cursor] = __connect()

    cursor.execute("""INSERT OR IGNORE INTO listings VALUES ("%s", "%s", "%s", "%s", "%s", False, "%s")""" % (
        id, html.escape(name), currentPrice, primaryPhotoUrl, sellerLocation, time.time()))
    connection.commit()
    connection.close()


def all_listings():
    [connection, cursor] = __connect()

    cursor.execute("SELECT * FROM listings ORDER BY seenAt DESC")
    results = cursor.fetchall()
    connection.close()

    return results


def find_listing(id):
    [connection, cursor] = __connect()

    result = cursor.execute(
        "SELECT * FROM listings WHERE id = %s" % id).fetchone()
    connection.close()

    return result[0] if result != None else None
