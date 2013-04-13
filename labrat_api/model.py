import psycopg2

class PgsqlModel(object):
  def __init__(self):
    self.lastID = None
    try:
        self.conn = psycopg2.connect("dbname='labrat' user='labrat' host='localhost' password='f00b@r'")
    except:
        print "I am unable to connect to the database"

  def getLastImportID(self):
    if not self.lastID:
      q = "select id from imports where done = true order by timestamp desc limit 1"
      cur = conn.cursor()
      cur.execute(q)
      rows = cur.fetchall()
      self.lastID = rows[0][0]
    return self.lastID


  def getUserFromHost(self,hostname):
    try:
      id = self.lastID
      cur = self.conn.cursor()
      cur.execute("""select users.name from hosts, users, logins where hosts.name = %s and hosts.id = logins.host_id and users.id = logins.user_id;""", (hostname,))
      rows = cur.fetchall()
      if len(rows) > 0:
        return rows[0][0]
      else:
        return None
    except:
      cur.clear()
