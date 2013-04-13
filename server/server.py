from flask import Flask
import model

#initialize flask server and redis db
app = Flask(__name__)
r = model.RedisModel()

#default
@app.route('/')
def index():
    return 'Welcome to Halpzme'

@app.route('/tutorhome/')
def tutorhome():
	#if they didn't specify which classes they will tutor, and the time they will tutor until:
		#make them specify that(they will type in both)
	#else
		#show them how many students need help for each of the classes they are signed up for, and show a button for each class to say help a student from that class
	pass

@app.route('/studenthome/')
#look at zach's UI for this
def studenthome():
	#select class they need help for(they will just type in the number)
		#goto helpwith
	#show everyone on the board right now, the tutors tutoring their class right now, maybe an ETA
	#if they not asked for help
		#show an ask for help button with autofill name and location field based on Ian's API
	#else
		#show their place in the queue, ie 4th on the list(should update in real time)

	pass

@app.route('/with/<classid>')
def helpwith(classid):
	pass

#achievement idea: over 1 million served(like mcdonalds)
if __name__ == "__main__":
    app.run()

