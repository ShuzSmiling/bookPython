import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='appdb',
    user='app',
    password='p@ssw0rd'
)

cur = conn.cursor()
cur.execute('SELECT * FROM app_table')
rows = cur.fetchall()

for i in rows:
    print(i[0])

conn.close()