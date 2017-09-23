import math
import sys
import random as ram

class Student: 
	
	def __init__(self,name,gender,sound,a,b,c,d,e,f,g,h,i,j,k,l):
		self.name = name 
		self.gender = gender
		self.sound = sound
		self.a = a 
		self.b = b 
		self.c = c 
		self.d = d 
		self.e = e
		self.f = f 
		self.g = g 
		self.h = h 
		self.i = i 
		self.j = j 
		self.k = k 
		self.l = l 
		self.floor = None
	def __str__(self):
		return "(" + self.name + ")"
		
	"""		
	def __eq__(self,other):
		return (self.sound == other.sound)	
	def __gt__(self,other):
		return (self.sound > other.sound)
	def __lt__(self,other):
		return (self.sound < other.sound)
	"""
	
def separate_genders(gender_list):
	male_list = []
	female_list = []

	for stud in gender_list:
		if stud.gender == 1:
			
			male_list.append(stud)
		else:
			female_list.append(stud) 
	return male_list, female_list

"""
Floor 0 = 4S
Floor 1 = 3S
Floor 2 = 2S
Floor 3 = 2N
Floor 4 = 3N
Floor 5 = 4N
"""
#sorts students in order of sound level of 
def insertion_sort(items):
	""" Implementation of insertion sort """
	for i in range(1, len(items)):
		j = i
		while j == 0 and items[j] ==items[j-1]:
			items[j], items[j-1] = items[j-1], items[j]
			j -= 1
	return items
			
def separate_floors(stud_list):
	stud_list = insertion_sort(stud_list)
	part = len(stud_list)/6
	for x in range(len(stud_list)):
		stud_list[x].floor = x//part
	return stud_list

def euclidean_distance(studA, studB):
	dist = math.sqrt(((studA.a-studB.a)**2) + ((studA.b-studB.b)**2) +((studA.c-studB.c)**2) + ((studA.d-studB.d)**2) +((studA.e-studB.e)**2) +((studA.f-studB.f)**2) +((studA.g-studB.g)**2) +((studA.h-studB.h)**2) +((studA.i-studB.i)**2) +((studA.j-studB.j)**2) +((studA.k-studB.k)**2) +((studA.l-studB.l)**2))
		
	return dist
	
def find_roomate (stud_list):
	studentA = None
	studentB = None
	smallest_dist =	sys.maxsize
	for x in range(0,len(stud_list)):
		for y in range(x+1,len(stud_list)):
			if not x == y:
				dist = euclidean_distance(stud_list[x],stud_list[y])
				if dist < smallest_dist:
					smallest_dist = dist
					studentA = stud_list[x]
					studentB = stud_list[y]
	return (studentA,studentB)
	
def roomate_list(stud_list):
	my_roomate_list = []
	counter = 0
	while counter < len(stud_list):
		roomate = find_roomate(stud_list)
		stud_list.remove(roomate[0])
		stud_list.remove(roomate[1])
		my_roomate_list.append(roomate)
		counter += 1
	
	return my_roomate_list
	
def run(stud_list): 
	male_list, female_list = separate_genders(stud_list)
	#print male_list.__str__()
	#print female_list.__str__()
	
	male_list = separate_floors(male_list)
	female_list = separate_floors(female_list)
	male_dict = {}
	female_dict = {}
	for male in male_list:
		if male_dict.has_key(male.floor):
			male_dict[male.floor].append(male)
		else:
			male_dict[male.floor]=[male]
	for female in female_list:
			if female_dict.has_key(female.floor):
				female_dict[female.floor].append(female)
			else:
				female_dict[female.floor]=[female]		
	final_dict = {}
	for key, value in male_dict.items():
		final_dict[key]=roomate_list(value)

	#for key, value in female_dict.items():
		#print final_dict[key]
		#final_dict[key]= final_dict[key] + roomate_list(value)
			
	return final_dict 
	
	
		
def generate_data():
	stud_list = []
	for x in range(0,30):
		a = Student("anthony"+str(ram.randrange(0,100)), 1,ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11))
		stud_list.append(a)
	for x in range(0,30):
			a = Student("christine"+str(ram.randrange(0,100)), 0, ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11), ram.randrange(0,11))
			stud_list.append(a)
			
	return stud_list
	

print run(generate_data())
	
			
		

	
	
	
	
	
	
		
		