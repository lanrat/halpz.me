import redis

class RedisModel(object):
    
    def __init__(self,host='localhost',port=9000):
        self.r = redis.StrictRedis(host=host,port=port,db=0)
        
    def studentAdd(self,classid,studentinfo):
        self.r.lpush('queue:'+str(classid),studentinfo)
        
    def getClassSize(self,classid):
        return self.r.llen('queue:'+str(classid))
        
    def popStudent(self,classid):
        studentinfo = self.r.rpop('queue:'+str(classid))
        self.r.sadd('pending:'+str(classid),studentinfo)
        return studentinfo
    
    def removeFromPending(self,classid,studentinfo):
        self.r.srem('pending:'+str(classid),studentinfo)
       
    def pendingBackToClass(self,classid,studentinfo):
        self.r.srem('pending:'+str(classid),studentinfo)
        self.r.rpush('queue:'+str(classid),studentinfo)

