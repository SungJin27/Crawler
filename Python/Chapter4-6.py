import feedparser
import MySQLdb

#connect to DATABASE
connection = MySQLdb.connect(
    user="scrapingman",
    passwd="sungjin0127",
    host="localhost",
    db="scrapingdata",
    charset="utf8")

#generate cursor
cursor = connection.cursor()

#delete table
cursor.execute("DROP TABLE IF EXISTS books")

#generate table
cursor.execute("CREATE TABLE books (title text, url text)")

#
rss = feedparser.parse("http://www.aladin.co.kr/rss/special_new/351")

#
print(rss.version)

#
print(rss["feed"]["title"])

#
for content in rss["entries"]:
    cursor.execute("INSERT INTO books VALUES(%s, %s)", (content["title"], content["link"]))

#commit
connection.commit()

#close
connection.close()
