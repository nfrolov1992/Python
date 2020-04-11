import random
FILENAME = "log.log"

f = open(FILENAME, 'w', encoding="utf8")

#2020-02-06T13:15:17.616153Z - [username4] - wanna scoop 76l
#2020-02-06T13:16:07.616410Z - [username7] - wanna top_up 74l
#2020-02-06T13:16:35.616769Z - [username7] - wanna top_up 49l
#2020-02-06T13:17:30.617582Z - [username2] - wanna scoop 21l

f.write("META DATA:\n")
f.write("400\n")
f.write("23\n")
i = 0
while i < 16700:
	hour1 = str(random.randint(0, 2))
	if hour1 == "2":
		hour2 = str(random.randint(1, 3))
	else:
		hour2 = str(random.randint(1, 9))
	min1 = str(random.randint(1, 5))
	min2 = str(random.randint(1, 9))
	sec1 = str(random.randint(1, 5))
	sec2 = str(random.randint(1, 9))
	msec = str(random.randint(600000, 999999))
	name = str(random.randint(1, 9))
	action = str(random.randint(1, 2))
	if action == "1":
		act = "scoop"
	else:
		act = "top_up"
	col = str(random.randint(1, 600))
	s = "2020-04-11T{0}{1}:{2}{3}:{4}{5}.{6}Z - [username{7}] -  wanna {8} {9}l\n".format(hour1, hour2, min1, min2, sec1, sec2, msec, name, act, col)
	f.write(s)
	i += 1
f.close