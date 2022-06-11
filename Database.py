import sqlite3
import html


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
            id VARCHAR(255) primary key,
            title VARCHAR(255),
            price VARCHAR(255),
            primary_photo_url VARCHAR,
            seller_name VARCHAR(255),
            dismissed BOOLEAN
        )""")
    connection.commit()
    connection.close()


def insert_listing(id, name, currentPrice, primaryPhotoUrl, sellerName):
    [connection, cursor] = __connect()

    cursor.execute("""INSERT OR IGNORE INTO listings VALUES ("%s", "%s", "%s", "%s", "%s", False)""" % (
        id, html.escape(name), currentPrice, primaryPhotoUrl, sellerName))
    connection.commit()
    connection.close()


def all_listings():
    [connection, cursor] = __connect()

    cursor.execute("SELECT * FROM listings")
    results = cursor.fetchall()
    connection.close()

    return results


def find_listing(id):
    [connection, cursor] = __connect()

    result = cursor.execute(
        "SELECT * FROM listings WHERE id = %s" % id).fetchone()
    connection.close()

    return result[0] if result != None else None
