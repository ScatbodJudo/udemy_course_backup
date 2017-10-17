import time
from datetime import datetime as dt

#the 'r' before the string in the below variable indicates to python
#that I am passing a row string and do not plan to include any special
#characters, such as \n for new line, etc.  This is more important when
#writing file names in windows, for example.
hosts_path = r"/etc/hosts"
temp_path = "hosts_temp"
redirect = '127.0.0.1'
website_list = ["www.reddit.com", "reddit.com","www.facebook.com","facebook.com"]

#while loops will intriduce 'background' functionality to this program.
#we want it to run always.
while True:
	#set variables for times at which websites are to be blocked
	#these variables are DATETIME OBJECTS, meaning that they can't
	#be compared with integers or strings.  they must be compared
	#with other datetime objects.
	morning = dt(dt.now().year,dt.now().month,dt.now().day,9)
	evening = dt(dt.now().year,dt.now().month,dt.now().day,19)

	if morning < dt.now() < evening:
		print("Time to get to work...")
		with open(hosts_path,'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content: 
					pass
				else:
					file.write(redirect+" "+website+"\n")
	else:
		with open(hosts_path, "r+") as file:
			content = file.readlines()
			#use the .seek() function to place the reading "cursor"
			#back at the beginning of the file
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			#truncate() limits the size of the file.  In this case
			#it prevents this program from copying the hosts file every
			#time the while loop executes.
			file.truncate()

		print("Time to not work or whatever...")



	#this cute little .sleep method makes the program pause for a specified
	#amount of seconds.  We don't want this program to run at processor clock speed.
	time.sleep(5)