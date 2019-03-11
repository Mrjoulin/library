import psycopg2
from openpyxl import load_workbook


def conect_to_db():
    conn = psycopg2.connect(dbname='d94gubjsid34us', user='bsznwlvcnhqxpv',
                            password='87263473da60733af18f3745dc31ad577df617e932a4c1011554d2441688e3b6',
                            host='ec2-54-247-70-127.eu-west-1.compute.amazonaws.com')

    cursor = conn.cursor()
    return conn, cursor


def create():
    conn, cursor = conect_to_db()

    cursor.execute("CREATE TABLE library (id serial PRIMARY KEY, title varchar, annotations varchar, author varchar, "
                   "EGEDirection varchar, EssayDirection varchar, OGEDirection varchar, is_have_illustration bool, "
                   "number_of_copies integer, number_of_pages integer, section varchar, year_of_publish integer);")

    wb_example = load_workbook('./table.xlsx')
    ws_example = wb_example.active

    for row in ws_example.values:
        if row[6] == '=TRUE()':
            cursor.execute("INSERT INTO library (title, annotations, author, EGEDirection, EssayDirection,OGEDirection,"
                           "is_have_illustration, number_of_copies, number_of_pages, section, year_of_publish) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (row[0], row[1], row[2], row[3], row[4], row[5], True, row[7], row[8], row[9], row[10]))
        else:
            cursor.execute("INSERT INTO library (title, annotations, author, EGEDirection, EssayDirection,OGEDirection,"
                           "is_have_illustration, number_of_copies, number_of_pages, section, year_of_publish) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (row[0], row[1], row[2], row[3], row[4], row[5], False, row[7], row[8], row[9], row[10]))

    cursor.execute('SELECT * FROM library;')
    records = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    return records

