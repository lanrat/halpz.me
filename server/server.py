from flask import Flask, render_template
import model

#initialize flask server and redis db
app = Flask(__name__)
#for the sessions
app.secret_key = 'o\xb8~Q>%\xed\x90\xb9A\x84\x8e\xfa\xabD\x01\xf0\xc2#b\x07\xe9*H'
r = model.RedisModel()

def init_session():
    # just assume the current user is a student initially
    if not 'type' in session:
        session['type'] = 'student'
        session['name'] = ''
        session['tutor_classes'] = []
        session['student_location'] = None

#default
@app.route('/')
def index():
    init_session()
    #FOR STUDENTS
    if session['type'] == 'student':
        if False:
            # the user is in a queue
            # redirect them to the /with/class url for the queue they're in
            return redirect('/with/%s' % escape(session['class']))
        else:
            # select class they need help for(they will just type in the number)
            # goto helpwith
            return render_template('index.html')
    #FOR TUTORS
    else if session['type'] == 'tutor':
        return render_template('tutor_home.html')
    return render_template('index.html')

@app.route('/tutor/', methods=['POST'])
def tutorhome():
    #changes session to tutor
    pass

@app.route('/student/', methods=[ 'POST'])
def studenthome():
    #changes session to student
    pass

@app.route('/with/<classid>', methods=['POST', 'GET'])
def helpwith(classid):
    #get - show their place in the queue, ie 4th on the list(should update in real time)
    # show an ask for help button with autofill name and location field based on Ian's API
    #post - student requests tutor for class
    pass

@app.route('/helped/<studentid>/with/<classid>', methods=[ 'POST'])
def helped(studentid,classid):
    #adds student to queue
    pass

@app.route('/helpnext/<classid>', methods=[ 'POST'])
def helpnext(classid):
    #helps next student in classid
    pass

@app.route('/cannothelp/<studentid>/with/<classid>', methods=[ 'POST'])
def cannothelp(studentid,classid):
    #puts student back on beginning of queue
    pass
 
@app.route('/queue/<classid>.json', methods=[ 'GET'])
def queue(classid):
    #gets queue for class in json
    pass   

@app.route('/index/<studentid>/in/<classid>', methods=[ 'POST'])
def indexedstudent(studentid,classid):
    #gets index of student in class queue
    pass


def validatestudent(session,studentid):
    #first check if session matches student or session is a tutor
    #then make sure student is valid format
    pass

def validateclass(classid):
    #make sure class if valid format
    pass
    
#achievement idea: over 1 million served(like mcdonalds)
if __name__ == "__main__":
    app.run(debug = True)

