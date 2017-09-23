import math
import sys
import random

class Student: 
	
	def __init__(self, name, gender, attributes):
		self.name = name 
		self.gender = gender
		self.sound = attributes[0]
		self.attributes = attributes				# list of attribute values
		self.floor = None							# a value between 1 and 6
	
	def __str__(self):
		return "(" + self.name + " : " + str(self.floor) + ")"

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
	part = len(stud_list)/6
	for x in range(len(stud_list)):
		stud_list[x].floor = int(x//part) + 1

def euclidean_distance(studA, studB):
	dist=0
	for i in range(len(0, studA.attributes)):
		dist += (studA.attributes[i]-studB.attributes[i])**2
	return math.sqrt(dist)
	
def find_roomate (stud_list):
	mat = [[sys.maxsize for x in range(len(stud_list))] for y in range(len(stud_list))]
	for x in range(0,len(stud_list)):
		for y in range(x+1,len(stud_list)):
			if not x == y:
				dist = euclidean_distance(stud_list[x],stud_list[y])
				if dist < smallest_dist:
					smallest_dist = dist
					studentA = stud_list[x]
					studentB = stud_list[y]
	return (studentA,studentB)
	
# def roomate_list(stud_list):
# 	my_roomate_list = []
# 	counter = 0
# 	while counter < len(stud_list):
# 		roomate = find_roomate(stud_list)
# 		stud_list.remove(roomate[0])
# 		stud_list.remove(roomate[1])
# 		my_roomate_list.append(roomate)
# 		counter += 1
	
# 	return my_roomate_list
	
# def run(stud_list): 
# 	male_list, female_list = separate_genders(stud_list)
# 	#print male_list.__str__()
# 	#print female_list.__str__()
	
# 	male_list = separate_floors(male_list)
# 	female_list = separate_floors(female_list)
# 	male_dict = {}
# 	female_dict = {}
# 	for male in male_list:
# 		if male_dict.has_key(male.floor):
# 			male_dict[male.floor].append(male)
# 		else:
# 			male_dict[male.floor]=[male]
# 	for female in female_list:
# 			if female_dict.has_key(female.floor):
# 				female_dict[female.floor].append(female)
# 			else:
# 				female_dict[female.floor]=[female]		
# 	final_dict = {}
# 	for key, value in male_dict.items():
# 		final_dict[key]=roomate_list(value)

# 	#for key, value in female_dict.items():
# 		#print final_dict[key]
# 		#final_dict[key]= final_dict[key] + roomate_list(value)
			
# 	return final_dict 
	
	
def generate_data():
	stud_list = []
	for x in range(0,30):
		student = Student("anthony"+str(random.randrange(0,100)),True,random.randrange(0,10)+1, random.randrange(0,10)+1)
		stud_list.append(student)
	for x in range(0,30):
		student = Student("christine"+str(random.randrange(0,100)), False, random.randrange(0,10)+1, random.randrange(0,10)+1)
		stud_list.append(student)
	random.shuffle(stud_list)
	return stud_list
		

list_of_students = generate_data()
print (list_of_students)
print ("***************")
# print (sorted(list_of_students))
x,y = separate_genders(list_of_students)
print (x)
print (y)
separate_floors(x)
print(x)
