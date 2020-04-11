import sys

def strcmp(s1, s2):
	if s2.find('*') == -1:
		if s1 == s2:
			print("OK")
		else:
			print("KO")
	else:
		tmp = s2.split('*')
		for x in tmp:

			if x == '':
				pass
			elif s1.find(x) != -1:
				s1 = s1[(s1.find(x) + len(x)):]
			else:
				print("KO")
				return None
		print("OK")

av = sys.argv
if len(av) != 3:
	print("Введено не верное количество строк")
else:
	strcmp(av[1], av[2])