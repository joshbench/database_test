Prerequisites:

Must have MySQL and Python installed, as well as the MySQLdb module (run "pip install mysqldb")

Prep:

Create and populate the database and table with create_testdb.sql

Run:

Run the script in this format:

	python database_test.py 'region name' 'yes|no' ['hostname:port']

For example:

	python database_test.py 'North America' 'yes' '127.0.0.1:3306'