import math
import sys
import random
import heapq


class Student:
    def __init__(self, name, gender, attributes):
        self.name = name
        self.gender = gender
        self.sound = attributes[0]
        self.attributes = attributes  # list of attribute values
        self.floor = None  # a value between 1 and 6

    def __str__(self):
        return self.name

    #		return "(" + self.name + " : " + str(self.floor) + ")"

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

        dist += ((int)(studA.attributes[i]) - (int)(studB.attributes[i])) ** 2
    return math.sqrt(dist)


"""
def find_roomate (stud_list):
	studentA = []
	studentB = []
	smallest_dist =	sys.maxsize
	for x in range(0,len(stud_list)):
		for y in range(x+1,len(stud_list)):
			if not x == y:
				dist = euclidean_distance(stud_list[x],stud_list[y])
				if dist < smallest_dist:
					smallest_dist = dist
					studentA = stud_list[x]
					studentB = stud_list[y]
					print(studentA,studentB)
	return (studentA,studentB)
"""


def find_roommate(stud_list):
    size = len(stud_list)
    Stud_Matrix = [[sys.maxsize for x in range(size)] for y in range(size)]
    heap = []
    paired_roommates = []
    for i in range(size):
        for j in range(size):
            if i > j and stud_list[i].floor == stud_list[j].floor:
                dist = euclidean_distance(stud_list[i], stud_list[j])
                Stud_Matrix[i][j] = dist
                heapq.heappush(heap, (dist, i, j))

    paired = set()
    for x in range(len(heap)):
        dist, i, j = heapq.heappop(heap)
        if not (i in paired or j in paired):
            paired_roommates.append((stud_list[i], stud_list[j]))
            paired.add(i)
            paired.add(j)

    return paired_roommates


# def roomate_list(stud_list):
#	my_roomate_list = []
#	while 0 < len(stud_list):
#		roomate = find_roomate(stud_list)
#		print(roomate)
#		stud_list.remove(roomate[0])
#		stud_list.remove(roomate[1])
#		my_roomate_list.append(roomate)
#
#	return my_roomate_list

def run(stud_list):
    male_list, female_list = separate_genders(stud_list)
    separate_floors(male_list)
    separate_floors(female_list)
    print(male_list, female_list)
    Male = [[] for _ in range(6)]
    Female = [[] for _ in range(6)]

    for student in male_list:
        Male[student.floor - 1].append(student)
    for student in female_list:
        Female[student.floor - 1].append(student)
    print("***************")
    print(Male)
    print(Female)
    print("***************")
    FloorList = [[] for _ in range(6)]
    for i in range(6):
        FloorList[i] = find_roommate(Male[i])
    for i in range(6):
        FloorList[i] += find_roommate(Female[i])

    return FloorList


def generate_data():
    stud_list = []
    for x in range(0, 36):
        attributes = []
        for i in range(10):
            attributes.append(random.randrange(10))
        student = Student("anthony" + str(x), True, attributes)
        stud_list.append(student)
    for x in range(0, 30):
        attributes = []
        for i in range(10):
            attributes.append(random.randrange(10))
        student = Student("christine" + str(x), False, attributes)
        stud_list.append(student)
    random.shuffle(stud_list)
    return stud_list


#student_list = generate_data()
# print(student_list)
# males, females = separate_genders(student_list)
# separate_floors(males)
# print("******************")
# print(males)
#
# roommates = find_roommate(males)
# print("******************")
# for roommate in roommates:
#	print(roommate)
#
# print len(roommates)

#floorList = run(stud_list)
#for i in range(6):
#    print(str(i + 1) + ": ")
#    for pair in floorList[i]:
#        print("\t" + str(pair))
#    print("")