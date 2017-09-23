from datetime import datetime
from threading import Timer
import quickstart
import pairRoomate2
import csv
import time

x = datetime.today()
y = x.replace(day = x.day, hour = x.hour, minute = x.minute, second = x.second+1, microsecond = 0)
delta_t = y - x

secs = (delta_t.seconds+1)%60

def hello_world():
    print("hello world")


def get_csv():
    quickstart.main()

def startPair():
    stud_list = []
    with open('Roommate.csv', newline='')as csvfile:
        roommates = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in roommates:
            student = pairRoomate2.Student(row[0], row[1],
                                           [row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                            row[11], row[12], row[13], row[14]])
            stud_list.append(student)
    floorList = pairRoomate2.run(stud_list)
    for i in range(6):
        print(str(i + 1) + ": ")
        for pair in floorList[i]:
            print("\t" + str(pair))
        print("")
    #pairRoomate2.run(stud_list)


t = Timer((secs+1)%60, get_csv)
t.start()


t = Timer((secs+3)%60, startPair)
t.start()