import redis

class RedisModel(object):
    
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost',port=9000,db=0)
        
    def studentAdd(self,classid,studentinfo):
        self.r.ladd(classid,studentinfo)
        
    def getClassSize(self,classid):
        return self.r.llen(classid)
        
    def popStudent(self,classid):
        return self.r.rpop(classid)

