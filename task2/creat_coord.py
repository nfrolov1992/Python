import random
FILENAME = "coords"

f = open(FILENAME, 'w', encoding="utf8")

#{sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}} 
x1 = 0
y1 = 0
z1 = 5
x2 = 2
y2 = 0
z2 = 5
i = 0
while i < 10:
	s1 = "{sphere: {center: [0, 0, 0], radius: 1}, line: {"
	s2 = "[{0}, {1}, {2}], [{3}, {4}, {5}]".format(x1, y1, z1, x2, y2, z2)
	s3 = "}}\n"
	s4 = s1 + s2 + s3
	print(s4)
	#s = "2020-04-11T{0}{1}:{2}{3}:{4}{5}.{6}Z - [username{7}] -  wanna {8} {9}l\n".format(hour1, hour2, min1, min2, sec1, sec2, msec, name, act, col)
	f.write(s4)
	z1 -= 1
	z2 -= 1
	i += 1
f.close