import MySQLdb, sys
from sys import argv

# get the arguments and assign them to variables (host defaults to 127.0.0.1 because mysql ignores port if you specify localhost)
if len(sys.argv) == 3:
    script, first, second = argv
    regionName = first
    shouldExist = second
    url = "127.0.0.1:3306"
elif len(sys.argv) == 4:
    script, first, second, third = argv
    regionName = first
    shouldExist = second
    url = third
else:
    print "Incorrect number of arguments. Please use this format for arguments: 'region name' 'yes|no' [hostname:port]"
    sys.exit(2)

# Open database connection using specified or default host
try:
    db = MySQLdb.connect(
        user = 'root',
        passwd = 'coolpass',
        host = url.split(':')[0],
        port = int(url.split(':')[1]),
        db = 'testdb')

except (MySQLdb.Error, MySQLdb.Warning) as e:
    print(e)
    sys.exit(2)

# Prepare a database cursor object
cursor = db.cursor()

# Execute sql statement
try:
    cursor.execute("SELECT EXISTS(SELECT * FROM region WHERE name LIKE '" + regionName + "')")

except (MySQLdb.Error, MySQLdb.Warning) as e:
    print(e)
    sys.exit(2)

# Close the database connection
db.close()

# Get the exists field
for row in cursor.fetchall():
    regionExists = row[0]

# Determine desired outcome from shouldExist, then give outcome based on regionExists
if shouldExist == "yes":
    if regionExists:
        print "Success, \"" + regionName + "\" exists in this table"
        sys.exit(0)
    else:
        print "Failure, \"" + regionName + "\" does not exist in this table"
        sys.exit(1)

if shouldExist == "no":
    if regionExists:
        print "Failure, \"" + regionName + "\" exists in this table"
        sys.exit(1)
    else:
        print "Success, \"" + regionName + "\" does not exist in this table"
        sys.exit(0)



