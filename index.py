import sqlite3

connect = sqlite3.connect('hotel.db')
cursor = connect.cursor()


def search_db():
    cursor.execute("SELECT * FROM contacts_page")
    all_results = cursor.fetchall()
    print(all_results[0],all_results[1])

search_db()