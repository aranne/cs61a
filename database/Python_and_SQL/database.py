import sqlite3

db = sqlite3.Connection("n.db")   # connect with n.db through db
db.execute("CREATE TABLE nums AS SELECT 2 UNION SELECT 3;")
db.execute("INSERT INTO nums VALUES (?), (?), (?);", range(4, 7))   # This python range will be passed into SQL statement.
print(db.execute("SELECT * FROM nums;").fetchall()) # fetch all the values out from n.db
db.commit()  # all values python put into database n.db will be committed. That is to say, you have writen values into database n.db through Python 
