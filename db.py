import yaml
from peewee import Model, MySQLDatabase, SqliteDatabase

# DbLoadError exception
class DbLoadError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Attempt to load the settings.yaml file
try:
    conf_file = open('settings.yaml')
    conf = yaml.load(conf_file)
    conf_file.close()
except:
    raise DbLoadError('Error loading settings.yaml')

# Check the database driver
if conf['database']['driver'] == 'mysql':
    mydb = MySQLDatabase(conf['database']['db'], user=conf['database']['user'], passwd=conf['database']['pass'])
elif conf['database']['driver'] == 'sqlite':
    mydb = SqliteDatabase(conf['database']['db'])
else:
    raise DbLoadError('Unknown database driver: ' + str(conf['database']['driver']))

# Used to send the mydb connection to models
class Db():
    database = mydb