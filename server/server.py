from flask import Flask
import model

#initialize flask server and redis db
app = Flask(__name__)
#for the sessions
app.secret_key = 'o\xb8~Q>%\xed\x90\xb9A\x84\x8e\xfa\xabD\x01\xf0\xc2#b\x07\xe9*H'
r = model.RedisModel()

#default
@app.route('/')
def index():
    #FOR STUDENTS
    if 'class' in session:
        # the user is in a queue
        # redirect them to the /with/class url for the queue they're in
        return redirect('/with/%s' % escape(session['class']))
    else:
        # select class they need help for(they will just type in the number)
        # goto helpwith
    #FOR TUTORS
    #if they didn't specify which classes they will tutor, and the time they will tutor until:
        #make them specify that(they will type in both)
    #else
        #show them how many students need help for each of the classes they are signed up for, and show a button for each class to say help a student from that class

    return 'Welcome to Halpzme'

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
def helped(student,classid):
    #adds student to queue
    pass

@app.route('/helpnext/<classid>', methods=[ 'POST'])
def helpnext(classid):
    #helps next student in classid
    pass

@app.route('/cannothelp/<studentid>/with/<classid>', methods=[ 'POST'])
def cannothelp(student,classid):
    #puts student back on beginning of queue
    pass
 
@app.route('/queue/<classid>.json', methods=[ 'GET'])
def queue(classid):
    #gets queue for class in json
    pass   

@app.route('/index/<studentid>/in/<classid>', methods=[ 'POST'])
def indexedstudent(student,classid):
    #gets index of student in class queue
    pass

 
    
#achievement idea: over 1 million served(like mcdonalds)
if __name__ == "__main__":
    app.run()

