from flask import Flask
import redis

#initialize flask server and redis db
app = Flask(__name__)
r = redis.StrictRedis(host='ian.ucsd.edu', port=9000, db=0)

#default
@app.route('/')
def index():
    return 'Welcome to Halpzme'

@app.route('/gethelp')
def gethelp():
    return 'You have been added to the queue'

@app.route('/givehelp')
def givehelp():
	return 'Help this person'

@app.route('/tutorlogin')
def tutorlogin():
	#on success go to tutorhome()
	#on fail go to tutorlogin()
	pass

@app.route('/tutorhome')
def tutorhome():
	#verify they are tutor 
	#if they didn't specify which classes they will tutor, and the time they will tutor until:
		#make them specify that
	#else
		#show them how many students need help for each of the classes they are signed up for, and show a button for each class to say help a student from that class
	pass

@app.route('/studenthome')
#look at zach's UI for this
def studenthome():
	#select class they need help for
	#show everyone on the board right now, the tutors tutoring their class right now, maybe an ETA
	#if they not asked for help
		#show an ask for help button with autofill location field based on Ian's API
	#else
		#show their place in the queue, ie 4th on the list(should update in real time)

	pass


if __name__ == "__main__":
    app.run()

