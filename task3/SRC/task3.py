import sys
import datetime as dt
import csv

FILENAME = "res.csv"

class Action:
    def __init__(self, action, dtime, col):
        self.action = action
        self.dtime = dt.datetime.fromisoformat(dtime)
        self.col = col

class Bulk:
    def __init__(self, BulkStart, actual, FreeBulk, BusyBulk):
        self.BulkStart = BulkStart
        self.actual = actual
        self. FreeBulk = FreeBulk

av = sys.argv
if len(av) != 4:
    print("неверное количество аргументов")
    sys.exit()
#если не верное количество аргументов, обработать!!!!!!!
timeStart = dt.datetime.fromisoformat(av[2])
timeEnd = dt.datetime.fromisoformat(av[3])

CountIn = 0 # количество попыток налить воду
ErrIn = 0 # процент ошибок при попытке налить воду
BulkIn = 0 # объем воды налит в бочку
NonBulkIn = 0 # Объем воды не налит в бочку

CountOut = 0 # количество попыток забрать воду
ErrOut = 0 # процент ошибок при попытке Забрать воду
BulkOut = 0 # объем воды забрали в бочку
NonBulkOut = 0 # Объем воды не забрали в бочку

BulkStart = 0 # сколько всего было в бочке в начале
BulkEnd = 0 # сколько стало объема в конце

FreeBulk = 0
BusyBulk = 0

i = 0

def parse_line(line):
    dtime = line[:line.find('Z')]
    action = "scoop" if "scoop" in line else "top_up"
    if action == "scoop":
        col = int(line[line.find("scoop") + 6: line.find("l")])
    else:
        col = int(line[line.find("top_up") + 6: line.find("l")])
    return Action(action, dtime, col)


log_file = open(av[1], 'r')
log_file.readline()
bulk = Bulk
bulk.BulkStart = int(log_file.readline())
bulk.actual = int(log_file.readline())
BulkStart = bulk.actual
bulk.FreeBulk = bulk.BulkStart - bulk.actual

for line in log_file:
    dataPars = parse_line(line)
    if timeStart <= dataPars.dtime <= timeEnd:
        if dataPars.action == "scoop": # вылить
            CountOut += 1
            if bulk.actual >= dataPars.col:
                # выливаем
                bulk.actual -= dataPars.col
                BulkOut += dataPars.col
            else:
                NonBulkOut += dataPars.col
                ErrOut +=1
        elif dataPars.action == "top_up": # налить
            CountIn += 1
            if (bulk.BulkStart - bulk.actual) >= dataPars.col:
                # наливаем
                bulk.actual += dataPars.col
                BulkIn += dataPars.col
            else:
                NonBulkIn += dataPars.col
                ErrIn += 1
    else:
        pass
BulkEnd = bulk.actual
try:
    ErrIn = ErrIn * 100 // CountIn
    ErrOut = ErrOut * 100 // CountOut
except ZeroDivisionError:
    print("введен не верный диапазон времени поиска, уточните время")
res = [ ["Количество попыток налить воду", CountIn],
        ["Процент неудач при Наливании", ErrIn],
        ["Сколько было налито воды", BulkIn],
        ["Сколько было воды НЕ налито", NonBulkIn],        
        ["Количество попыток вылить воду", CountOut],
        ["Процент неудач при ВЫливании", ErrOut],
        ["Сколько было вылито воды", BulkOut],
        ["Сколько было воды НЕ вылито", NonBulkOut],
        ["Сколько было в начале", BulkStart],
        ["Сколько стало в конце", BulkEnd],]
with open(FILENAME, 'w', newline="", encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter="-")
    writer.writerows(res)