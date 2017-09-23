import math
import sys
import random


class Student:
    def __init__(self, name, gender, attributes):
        self.name = name
        self.gender = gender
        self.sound = attributes[0]
        self.attributes = attributes  # list of attribute values
        self.floor = None  # a value between 1 and 6

    def __str__(self):
        return "(" + self.name + " : " + str(self.floor) + ")"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.sound == other.sound)

    def __gt__(self, other):
        return (self.sound > other.sound)

    def __lt__(self, other):
        return (self.sound < other.sound)


# we are assuming that gender is a boolean
def separate_genders(student_list):
    male_list = []
    female_list = []

    for student in student_list:
        if student.gender == True:
            male_list.append(student)
        else:
            female_list.append(student)
    return male_list, female_list


"""
	Floor 0 = 4S
	Floor 1 = 3S
	Floor 2 = 2S
	Floor 3 = 2N
	Floor 4 = 3N
	Floor 5 = 4N
"""


def separate_floors(stud_list):
    sorted(stud_list)
    part = len(stud_list) / 6
    for x in range(len(stud_list)):
        stud_list[x].floor = int(x // part) + 1


def euclidean_distance(studA, studB):
    dist = 0
    for i in range(len(studA.attributes)):
        dist += (studA.attributes[i] - studB.attributes[i]) ** 2
    return math.sqrt(dist)

'''
def find_roomate(stud_list):
    studentA = []
    studentB = []
    smallest_dist = sys.maxsize
    for x in range(0, len(stud_list)):
        for y in range(x + 1, len(stud_list)):
            if not x == y:
                dist = euclidean_distance(stud_list[x], stud_list[y])
                if dist < smallest_dist:
                    smallest_dist = dist
                    studentA = stud_list[x]
                    studentB = stud_list[y]
                    print(studentA, studentB)

    return (studentA, studentB)
'''
def find_roomate(stud_list):
    studentA = None
    studentB = None
    smallest_dist = 60
    x = 0
    while x < (len(stud_list)):
        y = x + 1
        while y < (len(stud_list)):
            dist = euclidean_distance(stud_list[x],stud_list[y])
            if dist < smallest_dist:
                smallest_dist = dist
                studentA = stud_list[x]
                #print(studentA)
                studentB = stud_list[y]

                #print ("hi1")
            #print (studentA)
            #print("hi2")
        #print(studentA)
        print(studentA,studentB)
        #print(stud_list[len(stud_list)-1])
        #print("hi3")

    return (studentA, studentB)

def roomate_list(stud_list):
    my_roomate_list = []
    while len(stud_list)>0:
        roomate = find_roomate(stud_list)
        #print(roomate)
        stud_list.remove(roomate[0])
        stud_list.remove(roomate[1])
        my_roomate_list.append(roomate)

    return my_roomate_list


def run(stud_list):
    male_list, female_list = separate_genders(stud_list)

    separate_floors(male_list)
    separate_floors(female_list)
    #print(male_list, female_list)
    Male = [[] for _ in range(6)]

    Female = [[] for _ in range(6)]
    for student in male_list:
        Male[student.floor - 1].append(student)
    for student in female_list:
        Female[student.floor - 1].append(student)
    #print(Male)
    #print(Female)
    FloorList = [[] in range(6)]
    for i in range(len(Male)):
        FloorList[i] = roomate_list(Male[i])
    for i in range(len(Female)):
        FloorList[i] = FloorList + roomate_list(Female[i])

    return FloorList


def generate_data():
    stud_list = []
    for x in range(0, 30):
        attributes = []
        for i in range(10):
            attributes.append(random.randrange(10))
        student = Student("anthony" + str(random.randrange(0, 100)), True, attributes)
        stud_list.append(student)
    for x in range(0, 30):
        attributes = []
        for i in range(10):
            attributes.append(random.randrange(10))
        student = Student("christine" + str(random.randrange(0, 100)), False, attributes)
        stud_list.append(student)
    random.shuffle(stud_list)
    return stud_list


student_list = generate_data()
run(student_list)
