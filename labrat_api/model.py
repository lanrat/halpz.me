import psycopg2
import psycopg2.extras

class PgsqlModel(object):
  def __init__(self):
    self.lastID = None
    try:
        self.conn = psycopg2.connect("dbname='labrat' user='labrat' host='localhost' password='f00b@r'")
    except:
        print "I am unable to connect to the database"

  def query(self,string,args=None):
    cur = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    if args:
      cur.execute(string,args)
    else:
      cur.execute(string)
    return cur.fetchall()


  def getLastImportID(self):
    if not self.lastID:
      q = """select
            id
          from
            imports
          where
            done = true
          order by timestamp desc
          limit 1"""
      rows = self.query(q)
      self.lastID = rows[0]['id']
    return self.lastID


  def getUserFromHost(self,hostname):
      q = """select
            users.name
          from
            hosts,
            users,
            logins
          where
            hosts.hostname = %s and
            hosts.id = logins.host_id and
            users.id = logins.user_id and
            logins.import_id = %s
            ;"""
      rows = self.query(q,(hostname,str(self.getLastImportID())))
      if len(rows) > 0:
        return rows
      else:
        return None


  def findUser(self,user):
    q="""select
          hosts.location,
          hosts.name as terminal
        from
          hosts,
          users,
          logins
        where
          users.login = %s and
          hosts.id = logins.host_id and
          users.id = logins.user_id and
          logins.import_id = %s"""
    rows = self.query(q,(user,str(self.getLastImportID())))
    if len(rows) > 0:
      return rows
    else:
      return None

  def getOnlineUsers(self):
    q = "select count(*) from logins where import_id = %s"
    result = this.query(q,(str(self.getLastImportID())))
    return result[0]['count']

  #def getTopLabUsers

