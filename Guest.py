import psycopg2


class ScriptSQl:
    def __init__(self):
        self.db = DBHelper()

    def create():
        

# Update connection string information
host = "databasefuze.postgres.database.azure.com"
dbname = "guest"
user = "fuze@databasefuze"
password = "147742a@"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed)")


def Uploader():
    
    f = open('persons.csv', 'r' , encoding="utf8")
    cursor.copy_from(f, 'person', sep=',')    
    f.close()
    # with open('01_Subject_attributes.csv', 'r') as f:
    #     # Notice that we don't need the csv module.
    #     next(f) # Skip the header row.
    #     cur.copy_from(f, 'guest', sep=',')

    # conn.commit()

    print("Upload Success")


# Uploader()


def creat_table():
    # Create a table
    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
    print("Finished creating table")

    # Insert some data into the table
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
    print("Inserted 3 rows of data")


    # Fetch all rows from table
    cursor.execute("SELECT * FROM inventory;")
    rows = cursor.fetchall()

    # Print all rows
    for row in rows:
        print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))


# # Delete data row from table
# cursor.execute("DELETE FROM inventory WHERE name = %s;", ("orange",))
# print("Deleted 1 row of data")


# Clean up
conn.commit()
cursor.close()
conn.close()


