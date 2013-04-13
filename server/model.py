import redis
import random

class RedisModel(object):
    
    def __init__(self,host='ian.ucsd.edu',port=9000):
        self.r = redis.StrictRedis(host=host,port=port,db=0)
    
    def studentIn(self,classid,studentinfo):
        return self.r.sismember('set:'+str(classid),studentinfo)
    
    def studentAdd(self,classid,studentinfo):
        if not self.studentIn(classid,studentinfo):
            self.r.rpush('queue:'+str(classid),studentinfo)
            self.r.sadd('set:'+str(classid),studentinfo)
        
    def getClassSize(self,classid):
        return self.r.llen('queue:'+str(classid))
        
    def popStudent(self,classid):
        studentinfo = self.r.lpop('queue:'+str(classid))
        self.r.sadd('pending:'+str(classid),studentinfo)
        self.r.srem('set:'+str(classid),studentinfo)
        s = self.r.hgetall("session:"+str(studentinfo))
        return s
    
    def removeFromPending(self,classid,studentinfo):
        self.r.srem('pending:'+str(classid),studentinfo)
       
    def pendingBackToClass(self,classid,studentinfo):
        self.r.srem('pending:'+str(classid),studentinfo)
        self.r.lpush('queue:'+str(classid),studentinfo)
        self.r.sadd('set:'+str(classid),studentinfo)
        
    def findIndexOfStudent(self,classid,studentinfo,maxI=99):
        if not self.r.sismember('set:'+str(classid),studentinfo):
            return -1
        l = self.r.lrange('queue:'+str(classid),0,maxI)
        try:
            return l.index(studentinfo)
        except ValueError:
            return maxI+1
    
    def getStudentList(self,classid,maxI=99):
        l = self.r.lrange('queue:'+str(classid),0,maxI)
        output=[]
        for sid in l:
            d = self.r.hgetall("session:"+str(sid))
            output.append(d)
        return output
    
    def getSession(self,sid):
        s = self.r.hgetall("session:"+str(sid))
        if s:
            return s
        defaults = {'type':'student',
                    'name':'',
                    'tutorclasses':'',
                    'studentlocation':'',
                    'id':str(sid),
                    'profilePicUrl':'/static/profpics/'+str(random.randint(0,22))+'.jpg',
                    }
        for k,v in defaults.iteritems():
            self.r.hset("session:"+str(sid), k,v)
        return defaults
        
    def setSession(self,sid,sess):
        for k,v in sess.iteritems():
            self.r.hset("session:"+str(sid), str(k),str(v))
        return sess
    
    def addCourse(self,classid):
        self.r.sadd("courses",classid)
    
    def getCourses(self):
        return list(self.r.smembers("courses"))
        
    def addTutor(self, classid, tutorid):
        self.r.sadd("tutors:"+str(classid),tutorid)
        
    def getTutors(self,classid):
        self.r.smembers("tutors:"+str(classid))

    def addHostname(self, ip, hostname):
        self.r.set(str(ip), hostname)

    def getHostname(self, ip):
        self.r.get(str(ip))

