import sqlite3
import html


def __connect():
    connection = sqlite3.connect('marketplace.db')
    cursor = connection.cursor()
    return [connection, cursor]


def init():
    [connection, cursor] = __connect()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS seen_listings (
            id VARCHAR(255) primary key,
            title VARCHAR(255),
            price VARCHAR(255),
            primary_photo_url VARCHAR,
            seller_name VARCHAR(255)
        )""")
    connection.commit()
    connection.close()


def insert_seen(id, name, currentPrice, primaryPhotoUrl, sellerName):
    [connection, cursor] = __connect()

    cursor.execute("""INSERT OR IGNORE INTO seen_listings VALUES ("%s", "%s", "%s", "%s", "%s")""" % (
        id, html.escape(name), currentPrice, primaryPhotoUrl, sellerName))
    connection.commit()
    connection.close()


def all_seen():
    [connection, cursor] = __connect()

    count = cursor.execute("SELECT COUNT(*) FROM seen_listings").fetchone()[0]
    print('SEEN IDS:', count)

    for row in cursor.execute("SELECT * FROM seen_listings"):
        print(row)

    connection.close()


def find_seen(id):
    [connection, cursor] = __connect()

    result = cursor.execute(
        "SELECT * FROM seen_listings WHERE id = %s" % id).fetchone()
    connection.close()

    return result[0] if result != None else None
