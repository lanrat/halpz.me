import psycopg2
import psycopg2.extras

class PgsqlModel(object):
  def __init__(self):
    self.lastID = None
    try:
        self.conn = psycopg2.connect("dbname='labrat' user='labrat' host='localhost' password='f00b@r'")
    except:
        print "I am unable to connect to the database"
    DEC2FLOAT = psycopg2.extensions.new_type(
        psycopg2.extensions.DECIMAL.values,
        'DEC2FLOAT',
        lambda value, curs: float(value) if value is not None else None)
    psycopg2.extensions.register_type(DEC2FLOAT)

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

  def getUserFromIP(self,addr):
      q = """select
            users.name
          from
            hosts,
            users,
            logins
          where
            hosts.ip = %s and
            hosts.id = logins.host_id and
            users.id = logins.user_id and
            logins.import_id = %s
            ;"""
      rows = self.query(q,(addr,str(self.getLastImportID())))
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
    result = self.query(q,(str(self.getLastImportID()),))
    return result[0]['count']

  def getTopLabUsers(self,limit=10):
      query = """select
              users.login,
              div(count(distinct logins.import_id), 4) as hours
          from
              users,
              logins,
              imports,
              hosts
          where
              hosts.id = logins.host_id and
              (imports.timestamp > (now() - interval '1day')) and
              imports.id = logins.import_id and users.bot = false and
              users.id = logins.user_id and
              hosts.location <> 'server'
          group by
              users.login
          having
              div(count(distinct logins.import_id), 4) < 24
          order by hours desc
          limit %s;"""
      return self.query(query,(str(limit),))


  def getTopUsers(self,limit=10):
      query = """select
              users.login,
              div(count(distinct logins.import_id), 4) as hours
          from
              users,
              logins,
              imports
          where
              (imports.timestamp > (now() - interval '1day')) and
              imports.id = logins.import_id and users.bot = false and
              users.id = logins.user_id
          group by
              users.login
          having
              div(count(distinct logins.import_id), 4) < 24
          order by hours desc
          limit %s"""
      result = self.query(query,(str(limit),))
      return result

  def getNumberOfLabOccupants(self):
      q = """select count(logins.host_id) from hosts, logins
          where logins.import_id = %s and hosts.id = logins.host_id and hosts.location <> 'server'"""
      result = self.query(q,(str(self.getLastImportID()),))
      return result[0]['count']


  def getLabOccupants(self):
        query = """select
                users.name,
                users.login,
                hosts.location as room,
                hosts.name as terminal
            from
                hosts,
                users,
                logins
            where
                hosts.id = logins.host_id and
                logins.import_id = %s and
                logins.user_id = users.id and
                hosts.location <> 'server'
            order by hosts.location, hosts.name""";
        return self.query(query,(str(self.getLastImportID()),))



