import math
import sys
import random
import heapq
import web
import json
import csv


urls = (
	'/', 'get_roommates',
	'/names', 'get_names'
)

app = web.application(urls, globals())


class Student: 
	
	def __init__(self, name, gender, attributes):
		self.name = name 
		self.gender = gender
		self.sound = attributes[0]
		self.attributes = attributes				# list of attribute values
		self.floor = None							# a value between 1 and 6
	
	def __str__(self):
		return self.name
		# return "(" + self.name + " : " + str(self.floor) + ")"

	def __repr__(self):
		return str(self)

	def __eq__(self,other):
		return (self.sound == other.sound)	
	def __gt__(self,other):
		return (self.sound > other.sound)
	def __lt__(self,other):
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
	part = math.ceil( (len(stud_list)/6.0) )
	if part % 2:
		part += 1
	for x in range(len(stud_list)):
		stud_list[x].floor = int(x//part) + 1

def euclidean_distance(studA, studB):
	dist=0
	for i in range(len(studA.attributes)):
		dist += (studA.attributes[i]-studB.attributes[i])**2
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
def get_roommate_list (stud_list):
	size = len(stud_list)
	Stud_Matrix = [[sys.maxsize for x in range(size)] for y in range(size)]
	heap = []
	paired_roommates = []
	for i in range(size):
		for j in range(size):
			if i > j and stud_list[i].floor == stud_list[j].floor:
				dist = euclidean_distance(stud_list[i], stud_list[j])
				Stud_Matrix[i][j] = dist
				heapq.heappush(heap,(dist,i,j))
	
	
	paired = set()
	for x in range(len(heap)):
		dist,i,j = heapq.heappop(heap)
		if not (i in paired or j in paired):
			paired_roommates.append((str(stud_list[i]),str(stud_list[j])))
			paired.add(i)
			paired.add(j)
	
	return paired_roommates
	
def run(stud_list):
	male_list, female_list = separate_genders(stud_list)
	separate_floors(male_list)
	separate_floors(female_list)
	# print(male_list,female_list)
	Male =[[] for _ in range(6)]
	Female = [[] for _ in range(6)]
	
	for student in male_list:
		Male[student.floor-1].append(student)
	for student in female_list:
		Female[student.floor-1].append(student)
	# print("***************")
	# print(Male)
	# print(Female) 
	# print("***************")
	FloorList=[[] for _ in range(6)]
	for i in range(6):
		FloorList[i] = get_roommate_list(Male[i])
	for i in range(6):
		FloorList[i] += get_roommate_list(Female[i])
			
	return FloorList	
	
# This function is only for generating dummy data
def generate_data():
	stud_list = []
	NUM_OF_MALES = 28
	NUM_OF_FEMALES = 24
	for x in range(0,NUM_OF_MALES):
		attributes = []
		for i in range(10):
			attributes.append(random.randrange(10))
		student = Student("anthony"+str(x),True,attributes)
		stud_list.append(student)
	for x in range(0,NUM_OF_FEMALES):
		attributes = []
		for i in range(10):
			attributes.append(random.randrange(10))
		student = Student("christine"+str(x), False,attributes)
		stud_list.append(student)
	random.shuffle(stud_list)
	return stud_list

def get_data():
	with open('roomateSpreadsheet.csv',"rb") as f:
		reader = csv.reader(f)
		stud_data = list(reader)
	stud_data.pop(0)
	std_list = []
	for stud in stud_data:
		if stud[1] == 'Female': #changing gender string into boolean values
			stud[1] = False
		else: 
			stud[1] = True
		attributes = []
		for attribute in stud[2:]:
			attributes.append(int(attribute))
		student = Student(stud[0],stud[1],attributes)
		std_list.append(student)
	return std_list

student_list = get_data()
# print("******************")
# print(student_list)
# males, females = separate_genders(student_list)
# separate_floors(males)
# print("******************")
# print(males)
#
#roommates = get_roommate_list(males)
# print("******************")
#for roommate in roommates:
#	print(roommate)
#	
#print len(roommates)


# for i in range(6):
# 	print(str(i+1) + ": ")
# 	for pair in floorList[i]:
# 		print ("\t" + str(pair))
# 	print("")

class get_roommates:
	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		roommates = run(student_list)
		return json.dumps(roommates)

class get_names:
	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		return json.dumps([[('Jaswin','Anthony'),('Jaswin1','Anthony1')],[('Christine','Will'),('Christine','Will')]])

if __name__ == "__main__":
    app.run()
