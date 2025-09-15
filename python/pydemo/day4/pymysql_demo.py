import pymysql as ps
import pymysql.cursors

config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "db": "jdmall",
    "charset": "utf8",
    "cursorclass": pymysql.cursors.DictCursor
}

conn = ps.connect(**config)
cur = conn.cursor()
sql = "SELECT * FROM products"

result = cur.execute(sql)

data = cur.fetchall()
for row in data:
    print("{}\t{}\t{}\t".format(row["product_name"], row["brand"], row["price"]))

insertSql = "INSERT INTO products(product_name,brand,price) VALUES('%s','%s','%s');" % ("p1", "b1", 166)
cur.execute(insertSql)
conn.commit()

insertSql2 = "INSERT INTO products(product_name,brand,price) VALUES(%s,%s,%s);"
args = ("p2", "b2", 266)
cur.execute(insertSql2, args)
conn.commit()

updateSql1 = "UPDATE products set product_name=%s WHERE product_name=%s"
args = ("p1", "p11")
cur.execute(updateSql1, args)
conn.commit()

conn.close()
