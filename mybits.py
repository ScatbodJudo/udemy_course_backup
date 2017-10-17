"""
This file is a running list of functions developed through the Udemy python megacourse.
"""
import datetime
from geopy.geocoders import Nominatim
import json

def getType():
	var = input("Variable --> ")
	print ("haha everything is a string with the input() function...")
	return type(var)

def mathThing(x,y):
	result = x**y
	return result

def stringSplit(string):
	list = []
	for i in string: list.append(i)
	print ("list: " + str(list[0:4]))
	print (string[0:4])

def dictionaryMaker(key,index=int()):
	d = {"name":("bob","frank","joe"), "id":(123,456,654,321)}
	print(d[key][int(index)])

def thingThing(thing1 = "#justdefaultthings", thing2 = "are you out of ideas?"):
	print(str(thing1) + str(thing2))

def questionThing():
	color = input("What is your facvorite color? ")
	print ("your favorite color is not " + str(color) + "! You lie!")

def convertTemperature(temp,unit):
	if unit == 'C' and temp > -273.15: 	
		f = temp*9/5+32
		result = [str(f),unit]
		return result
	elif unit == 'F' and temp > -459.67:	
		c = 5/9*(temp-32)
		result = [str(c),unit]
		return result
	else: print("ERROR: please indicate F or C and/or stop breaking the laws of physics.")

def exersize2():
	d = money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
	print( d["under_bed"][1] )

def getAge():
	age = int(input("What is your age? "))
	if age >150: print("Are you a vampire?")
	elif 1 <= age < 5: print("Are you a prodigy?")
	elif age <= 0: print("Okay, this is getting silly...")
	else: print(str(age) + " is a good age to be!") 

def iterator(*things):
	print("Your things in the box:")
	for thing in things:
		if 'b' in thing: print("A "+thing+", really?")
		else: print(thing)

correct_password = "password123"
def whatsThePassword():
	pass_entered = input("please enter password: ")
	while pass_entered != correct_password:
		print ("Wrong password.")
		pass_entered = input("Please enter the correct password.")
	else: print("correct password entered.")

def convertTempList():
	temp = 	[15,20,-20,-27,10,100]
	unit = ['F','C','C','F','C','F']
	result = []
	for t,u in zip(temp,unit):
		result.append(convertTemperature(t,u))
	return result	
		

def writeToFile(mode):
	temperatures = convertTempList()
	with open("bits.txt",mode) as file:
		for temp in temperatures: 
			file.write(temp[0]+temp[1]+"\n")

def dateTime():
	#this_morning = datetime.datetime(2017,8,29,0,0,0,0)
	now = datetime.date.today()
	print(now)

#create new file with date as name of file
def dateTimeFile():
	fileName = str(datetime.date.today())
	with open(fileName+".txt","w+") as file:
		file.write("Today")

def geoCoder():
	geolocator = Nominatim()
	location = geolocator.geocode("1570 Willow st Denver CO 80220")
	print(location.address)

def filesToArray(*files):
	#read text from files and place text into master array
	output = []
	for filename in files:
		with open(filename, 'r') as file:
			output.append(file.read())
	#write array to new file followed by time stamp
	with open('file4.txt','w+') as file:
		for i in output: file.write(str(i)+"\n")
		file.write(str(datetime.datetime.now()))

getType()













