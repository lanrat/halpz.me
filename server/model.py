import redis

class RedisModel(object):
    
    def __init__(self,host='localhost',port=9000):
        self.r = redis.StrictRedis(host=host,port=port,db=0)
        
    def studentAdd(self,classid,studentinfo):
        self.r.lpush('queue:'+str(classid),studentinfo)
        self.r.sadd('set:'+str(classid),studentinfo)
        
    def getClassSize(self,classid):
        return self.r.llen('queue:'+str(classid))
        
    def popStudent(self,classid):
        studentinfo = self.r.rpop('queue:'+str(classid))
        self.r.sadd('pending:'+str(classid),studentinfo)
        self.r.srem('set:'+str(classid),studentinfo)
        return studentinfo
    
    def removeFromPending(self,classid,studentinfo):
        self.r.srem('pending:'+str(classid),studentinfo)
       
    def pendingBackToClass(self,classid,studentinfo):
        self.r.srem('pending:'+str(classid),studentinfo)
        self.r.rpush('queue:'+str(classid),studentinfo)
        self.r.sadd('set:'+str(classid),studentinfo)
        
    def findIndexOfStudent(self,classid,studentinfo,maxI=99):
        if not self.r.sismember('set:'+str(classid),studentinfo):
            return -1
        l = self.r.lrange('queue:'+str(classid),0,maxI)
        try:
            return l.index(studentinfo)
        except ValueError:
            return maxI+1
