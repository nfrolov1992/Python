import sys
import math

def pars_line(line):
	line = (line.replace('sphere', '"sphere"')
                   .replace('center', '"center"')
                   .replace('radius', '"radius"')
                   .replace('line', '"line"')
                   .replace("{[", "([")
                   .replace("]}", "])")
                   .replace(" ", ""))
	return eval(line)

def use_k(center, radius, straight):
	try:
		res = list()
		x0 = center[0]
		y0 = center[1]
		z0 = center[2]
		x1 = straight[0][0]
		y1 = straight[0][1]
		z1 = straight[0][2]
		x2 = straight[1][0]
		y2 = straight[1][1]
		z2 = straight[1][2]
		a = 1 + ((((y2 - y1)**2) + ((z2 - z1)**2)) / ((x2 - x1)**2))
		b = 2 * (((y2 - y1)/(x2 - x1))*(y1 - y0 - ((y2 - y1)/(x2 - x1))) + ((z2 - z1)/(x2 - x1))*(z1 - z0 - ((z2 - z1)/(x2 - x1))) - x0)
		c = (x0 ** 2) + ((y1 - y0 - ((y2 - y1)/(x2 - x1)))**2) + ((z1 - z0 - ((z2 - z1)/(x2 - x1)))**2) - (radius **2)
		d = (b **2) - 4 * a * c
		if d < 0:
			pass
		elif d == 0:
			xp = (b * (-1))/(2 * a)
			res.append(xp)
			yp = (((xp - x1)*(y2 - y1))/(x2 - x1)) + y1
			res.append(yp)
			zp = (((xp - x1)*(z2 - z1))/(x2 - x1)) + z1
			res.append(zp)
			print("coord:\n x1: {0}\n y1: {1}\n z1: {2}\n".format(res[0],
							res[1], res[2]))
		else:
			xp1 = ((b * (-1)) + math.sqrt(d))/(2 * a)
			res.append(xp1)
			yp1 = (((xp1 - x1)*(y2 - y1))/(x2 - x1)) + y1
			res.append(yp1)
			zp1 = (((xp1 - x1)*(z2 - z1))/(x2 - x1)) + z1
			res.append(zp1)
			xp2 = ((b * (-1)) - math.sqrt(d))/(2 * a)
			res.append(xp1)
			yp2 = (((xp2 - x1)*(y2 - y1))/(x2 - x1)) + y1
			res.append(yp1)
			zp2 = (((xp2 - x1)*(z2 - z1))/(x2 - x1)) + z1
			res.append(zp1)
			print("coord:\n x1: {0}\n y1: {1}\n z1: {2}\n x2: {3}\n y2: {4}\n z2: {5}\n".format( res[0],
							res[1], res[2], res[3], res[4], res[5]))
	except ZeroDivisionError:
		print("Уникальные случаи не обработаны")
	return res

nonZero = 0
av = sys.argv
if len(av) != 2:
	print("неверное количество аргументов")
else:
	FILENAME = av[1]
	try:
		f = open(FILENAME)
		for line in f:
			data = pars_line(line)
			sphere = data.get('sphere') #Cфера
			straight = data.get('line') #Прямая
			r = sphere.get('radius')
			center = sphere.get('center')
			res = use_k(center, r, straight)
			if res != []:
				nonZero = 1
		if nonZero == 0:
			print("Коллизий не найдено")
	except FileNotFoundError:
		print("Файл не найден")

