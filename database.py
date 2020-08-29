import mysql.connector
import JarvisListen


mybd = mysql.connector.connect(host = "localhost" , user = "root" , password = "1234" )

mycursor = mybd.cursor()
mycursor.execute("use jarvis")
queslist = ["Speakup your name", "SpeakUp your date of birth", "Speakup your gmail", "tell me your gmail password","Speakup your Phone number"]
anslist = []
def greinsert( word , meaning ):
	sql = "INSERT INTO greword (word, meaning) VALUES (%s, %s)"
	val = (word, meaning)
	mycursor.execute(sql, val)

	mybd.commit()


def dbuserdetail(): 
	sql = "INSERT INTO userdata (name, dob, gmail, gmailpassword, phno) VALUES (%s, %s, %s, %s, %s)"
	val = (anslist[0], anslist[1], anslist[2], anslist[3], anslist[4])
	mycursor.execute(sql, val)

	mybd.commit()



def dbuserdetailshow():
	mycursor.execute("SELECT * FROM userdata")
	myresult = mycursor.fetchall()

	for x in myresult:
	  print(x)


def greselect():
	mycursor.execute("SELECT * FROM greword")
	myresult = mycursor.fetchall()

	for x in myresult:
	  print(x)

def dbcheck():
	mycursor.execute("SELECT * FROM userdata")
	myresult = mycursor.fetchall()
	if myresult is None :
		return "None"
	else :
		return "userexist"

def newstart():
	ix = 0
	for i in queslist:
		JarvisListen.speak(queslist[ix])
		anslist.append(JarvisListen.takeCommand())
		ix += 1 
	for i in anslist :
		print(i)
	dbuserdetail()
	
dbuserdetailshow()
