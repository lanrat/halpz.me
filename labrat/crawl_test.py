#!/usr/bin/env python3
import sys
import os
import time
import itertools

class labrat():
  def __init__(self):

    self.ssh_user = 'idfoster'

    self.debug = True


  def finger(self,import_id,server_id, server):
    #code for updating the IP

    #userless, uses current user and keys
    cmd = 'ssh -oConnectTimeout=01 -ostrictHostKeyChecking=no '+self.ssh_user+'@'+server+' finger -lp 2> /dev/null'
    #print(cmd)
    try:
      p = os.popen(cmd)
    except:
      if self.debug:
        print("Error conecting to "+server)
      return
    l = p.readlines(); #list of strings
    p.close()

    if len(l) == 0:
      if self.debug:
        print("No info returned for "+server)
      return

    #check for no users
    if l[0] == 'No one logged on.\n':
      return

    #parse the lines into managable user-chunks
    userChunks = [list(x[1]) for x in itertools.groupby(l, lambda x: x=='\n') if not x[0]]

    existing_users = list()

    for userData in userChunks:
      print("##")
      self.parseChunk(import_id,server_id,userData,existing_users)


  def parseChunk(self,import_id,server_id,userInfoList,existing_users):
    ''' returns the username, real name, and idle time'''
    if len(userInfoList) < 1:
      return

    #print("------parsing Chunk-----")
    
    #split the line
    line1 = userInfoList.pop(0)
    line1parts = line1.split()
    #get the login
    #login = line1parts[1]
    login_start = line1.find(':')+2
    login = line1[login_start:line1.find(' ',login_start)].strip()

    if self.debug:
      print("login: "+login)

    #get the name
    #name = ' '.join(line1parts[3:len(line1parts)])
    name = line1[line1.rfind(':')+1:len(line1)].strip()

    if self.debug:
      print("name: "+name)

    while userInfoList[0][0:8] != 'On since':
      userInfoList.pop(0)

    if len(userInfoList) == 0:
      return


    print("UserInfoList")
    print(userInfoList)

    while userInfoList.pop(0)[0:8] == 'On since':
      #found an idle time
      if self.debug:
        print("parsing idle for: "+name)
      if len(userInfoList) == 0 or self.parseIdle(userInfoList.pop(0).strip()):
        print("User not idle")
        if login not in existing_users:
          #add user to DB
          if self.debug:
            print("-->Adding User: "+login+" with name: "+name)
          existing_users.append(login)
    return


  def parseIdle(self,line):
    if self.debug:
      print("Idle: "+line)
    line = line.split()
    if 'years' in line:
      return False
    if 'year' in line:
      return False
    if 'days' in line:
      return False
    if 'day' in line:
      return False
    if 'hours' in line:
      return False
    if 'hour' in line:
      return False
    if 'minute' in line:
      return True
    if 'minutes' in line:
      #parse the amount of minutes
      idle = int(line[line.index('minutes')-1])
      if idle > 15:
        return False

    return True


  def run(self):


    #self.finger(0,0,'ACS-CSEB210-01')
    #self.finger(0,0,'ACS-CSEB230-03')
    self.finger(0,0,'ACS-CSEB230-25')
    #self.finger(0,0,'ieng6-201')
    #self.finger(0,0,'ieng9')

    

if __name__ == "__main__":
   proc = labrat()
   proc.run()
