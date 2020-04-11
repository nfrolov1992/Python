import sys
import collections

class  ExeptionNb(Exception): pass

def chek_base(baseSrc):
	i = 0
	tmp = baseSrc
	for x in baseSrc:
		for y in tmp:
			if x == y:
				i += 1
			if i > 1:
				print("Некорректная система счисления (повторяющиеся символы)")
				sys.exit()
		i = 0


def itoBase(nb, baseSrc = None, baseDst = None):
	chek_base(baseSrc)
	if baseDst == None:
		baseS = len(baseSrc)
		nb = int(nb)
		d = {}
		res = list()
		for k in range(baseS):
			d[k] = baseSrc[k]
		while nb >= baseS:
			res.append(d[nb % baseS])
			nb = nb // baseS
		else:
			res.append(d[nb % baseS])
			res.reverse()
		return ''.join(res)
	else:
		bs = len(baseSrc)
		l = len(nb) - 1
		lnb = l
		dd = {}
		num = list()
		i = 0
		for k in baseSrc:
			dd[k] = i
			i += 1
		z = 0
		while l >= 0:
			try:
				num.append(dd[nb[z]] * ((i)**l))
			except KeyError:
				print("не соответствие числа и системы счисления")
				sys.exit()
			l -= 1
			z += 1
		num = sum(num)
		res = itoBase(num, baseDst, None)
		if type(res) == str:
			return res

def main():
	av = sys.argv
	res = None
	if len(av) == 3:
		try:
			nb = int(av[1])
			if nb < 0:
				raise ExeptionNb()
			res = itoBase(nb, av[2])
			print(res)
		except ExeptionNb:
			print("Введено число со знаком, НЕ ВЕРНО")
		except ValueError as err:
			print(err + " Введено не число, НЕ ВЕРНО")
	elif len(av) == 4:
		res = itoBase.itoBase(av[1], av[2], av[3])
		print("Число сконвектировано: ", res)
	else:
		print("некоректное число аргументов")

if __name__ == "__main__":
    main()