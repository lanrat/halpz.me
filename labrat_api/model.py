import psycopg2

class PgsqlModel(object):
  def __init__(self):
    try:
        self.conn = psycopg2.connect("dbname='labrat' user='labrat' host='localhost' password='f00b@r'")
    except:
        print "I am unable to connect to the database"


