from flask import Flask, session, redirect, url_for, escape, request, render_template
import socket
import model
import json
import requests
import uuid

#initialize flask server and redis db
app = Flask(__name__)
#for the sessions
app.secret_key = 'o\xb8~Q>%\xed\x90\xb9A\x84\x8e\xfa\xabD\x01\xf0\xc2#b\x07\xe9*H'
r = model.RedisModel()



#default
@app.route('/')
def index():
    s = session_init()
    return render_template('index.html')

@app.route('/tutor/', methods=['POST'])
def tutorhome():
    #changes session to tutor
    s = session_init()
    s['type'] = 'tutor'
    r.setSession(s['id'],s)
    return redirect(url_for('index'))

@app.route('/student/', methods=[ 'POST'])
def studenthome():
    #changes session to student
    s = session_init()
    s['type'] = 'student'
    r.setSession(s['id'],s)
    return redirect(url_for('index'))

@app.route('/with/<classid>', methods=['POST', 'GET'])
def helpwith(classid):
    #get - show their place in the queue, ie 4th on the list(should update in real time)
    # show an ask for help button with autofill name and location field based on Ian's API
    #post - student requests tutor for class
    s = session_init()
    classid = str(classid)
    if validateclass(classid):
        if request.method == 'POST':
            dic = {}

            dic['name']=request.form.get('name')
            dic['studentlocation']=request.form.get('studentlocation')
            r.setSession(s['id'],dic)
            r.studentAdd(classid,s['id'])
        return render_template('class.html',currStudent=s,classId=classid)
    return redirect(url_for('index'))

@app.route('/helped/<studentid>/with/<classid>', methods=[ 'POST'])
def helped(studentid,classid):
    #adds student to queue
    s = session_init()
    classid = str(classid)
    if validatestudent(s,studentid) and validateclass(classid):
        r.removeFromPending(classid,studentid)
    return redirect(url_for('index'))

@app.route('/helpnext/<classid>', methods=[ 'POST'])
def helpnext(classid):
    #helps next student in classid
    s = session_init()
    classid = str(classid)
    if validateclass(classid):
        student = r.popStudent(classid)
        return json.dumps(student)
    return json.dumps([])

@app.route('/cannothelp/<studentid>/with/<classid>', methods=[ 'POST'])
def cannothelp(studentid,classid):
    #puts student back on beginning of queue
    s = session_init()
    classid = str(classid)
    studentid = str(studentid)
    if validatestudent(s,studentid) and validateclass(classid):
        r.pendingBackToClass(classid,studentid)
    return redirect(url_for('index'))
 
@app.route('/queue/<classid>.json', methods=[ 'GET'])
def queue(classid):
    #gets queue for class in json
    s = session_init()
    classid = str(classid)
    if validateclass(classid):
        l = r.getStudentList(classid)
        return json.dumps(l)
    return json.dumps([])   

@app.route('/courses.json', methods=[ 'GET'])
def courses():
    return json.dumps(r.getCourses())

@app.route('/tutors/<classid>.json',methods=['GET'])
def tutors(classid):
    return json.dumps(r.getTutors(classid))
    
@app.route('/addtutor/<classid>',methods=['POST'])
def tutor(classid):
    s = session_init()
    classid = str(classid)
    if validateclass(classid):
        json.dumps(r.setTutor(classid,s['id']))
        return json.dumps([True])
    return json.dumps([])
    
def session_init():
    if 'uid' not in session:
        session['uid'] = uuid.uuid4()
    s = r.getSession(session['uid'])
    return s
    
def validatestudent(session,studentid):
    #first check if session matches student or session is a tutor
    #then make sure student is valid format
    if isinstance(studentid,str) and len(studentid)<500 and (session['type']=='tutor' or session['id']==studentid):
        return True
    return False

def validateclass(classid):
    #make sure class if valid format
    if isinstance(classid,str) and len(classid)<7 and classid[:3]=='cse':
        r.addCourse(classid)
        return True
    return False

"""def magic_shit(ip):
    result = redis_lookup(ip)
    #if you didn't find it in cache 
    if not result: 
        actually do the ssh bullshit, then put it in the cache
        result = bull
    else:
        return result
"""


#achievement idea: over 1 million served(like mcdonalds)
if __name__ == "__main__":
    app.run(debug = True)

