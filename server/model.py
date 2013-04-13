import redis

class RedisModel(object):
    
    def __init__(self,host='localhost',port=9000):
        self.r = redis.StrictRedis(host=host,port=port,db=0)
        
    def studentAdd(self,classid,studentinfo):
        self.r.ladd('queue:'+str(classid),studentinfo)
        
    def getClassSize(self,classid):
        return self.r.llen('queue:'+str(classid))
        
    def popStudent(self,classid):
        studentinfo = self.r.rpop('queue:'+str(classid))
        self.r.sadd('pending',studentinfo)
        return studentinfo
    

