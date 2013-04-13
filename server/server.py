from flask import Flask, session, redirect, url_for, escape, request, render_template
import model

#initialize flask server and redis db
app = Flask(__name__)
#for the sessions
app.secret_key = 'o\xb8~Q>%\xed\x90\xb9A\x84\x8e\xfa\xabD\x01\xf0\xc2#b\x07\xe9*H'
r = model.RedisModel()



#default
@app.route('/')
def index():
    s = r.getSession(session['_id'])
    return render_template('index.html')

@app.route('/tutor/', methods=['POST'])
def tutorhome():
    #changes session to tutor
    s = r.getSession(session['_id'])
    s['type'] = 'tutor'
    r.setSession(s)
    return redirect(url_for('index'))

@app.route('/student/', methods=[ 'POST'])
def studenthome():
    #changes session to student
    s = r.getSession(session['_id'])
    s['type'] = 'student'
    r.setSession(s)
    return redirect(url_for('index'))

@app.route('/with/<classid>', methods=['POST', 'GET'])
def helpwith(classid):
    #get - show their place in the queue, ie 4th on the list(should update in real time)
    # show an ask for help button with autofill name and location field based on Ian's API
    #post - student requests tutor for class
    s = r.getSession(session['_id'])
    if validateclass(classid):
        pass
    return redirect(url_for('index'))

@app.route('/helped/<studentid>/with/<classid>', methods=[ 'POST'])
def helped(studentid,classid):
    #adds student to queue
    s = r.getSession(session['_id'])
    if validatestudent(s,studentid) and validateclass(classid):
        pass
    return redirect(url_for('index'))

@app.route('/helpnext/<classid>', methods=[ 'POST'])
def helpnext(classid):
    #helps next student in classid
    s = r.getSession(session['_id'])
    if validateclass(classid):
        pass
    return redirect(url_for('index'))

@app.route('/cannothelp/<studentid>/with/<classid>', methods=[ 'POST'])
def cannothelp(studentid,classid):
    #puts student back on beginning of queue
    s = r.getSession(session['_id'])
    if validatestudent(s,studentid) and validateclass(classid):
        pass
    return redirect(url_for('index'))
 
@app.route('/queue/<classid>.json', methods=[ 'GET'])
def queue(classid):
    #gets queue for class in json
    s = r.getSession(session['_id'])
    if validateclass(classid):
        pass
    return redirect(url_for('index'))   

@app.route('/index/<studentid>/in/<classid>', methods=[ 'POST'])
def indexedstudent(studentid,classid):
    #gets index of student in class queue
    s = r.getSession(session['_id'])
    if validatestudent(s,studentid) and validateclass(classid):
        pass
    return redirect(url_for('index'))


def validatestudent(session,studentid):
    #first check if session matches student or session is a tutor
    #then make sure student is valid format
    if isinstance(studentid,str) and len(studentid)<50 and (session['type']=='tutor' or session['id']==studentid):
        return True
    return False

def validateclass(classid):
    #make sure class if valid format
    if isinstance(classid,str) and len(classid)<50 and classid[:3]=='cse':
        return True
    return False
    
#achievement idea: over 1 million served(like mcdonalds)
if __name__ == "__main__":
    app.run(debug = True)

