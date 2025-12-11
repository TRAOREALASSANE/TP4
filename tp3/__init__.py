
import pymysql

# Active PyMySQL comme pilote MySQL
pymysql.install_as_MySQLdb()

# On triche sur la version pour satisfaire Django 5
import MySQLdb
if hasattr(MySQLdb, 'version_info'):
    MySQLdb.version_info = (2, 2, 2, 'final', 0)
    MySQLdb.version = '2.2.2'