def digital_root(num):
	while num >=10:
		#num equals list of our numbers added together
		num = sum(map(int,str(num)))
		print(num)
	return num
_______________________________________________________________________

def tribonacci(signature, n):
	trib = []
	a,b,c = signature
	for i in range(n):
		trib.append(a)
		a,b,c=b,c,a+b+c
		#think 4th dimensionally. abc = previous b,c, & a plus a + b + c
	return trib

_______________________________________________________________________

def array_diff(a,b): {1,2,3,4,}{4,3,2,1,5}
	for x in b:
		while x in a:
			a.remove(x)
			print(a)
	return a
#better version
def array_diff(a,b):
	return [x for x in a if x not in b]
_______________________________________________________________________
import numpy as np 
#backpack problem
def pack_backpack(scores, weight, capacity):
	m = np.zeros([len(scores), capacity +1])
	for i in range(len(score)):
		for j in range(capacity+1):
			if weights[i] > j:
				m[i,j] = m[i-1,j]
			else:
				m[i,j] = max(m[i-1,j - weights[i]] + scores[i],m[i-1,j])
	return np.max(m)
_______________________________________________________________________
def pack_backpack(S,W,C):
	M= [0] * (1+C)
	for F,V in enumerate(S):
		M= [max(U,M[T-W[F]]+ V if W[F]) <= T else 0) for T,U in enumerate(M)]
	return M[-1]

_______________________________________________________________________


def dirReduc(arr):
	opposing_directions = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
	DR = [] 
	for x in arr:
		if DR and DR[-1] == opposing_directions[x]:
			DR.pop()
		else:
			DR.append(x)
	return DR
_______________________________________________________________________
def score(dice):
	sum = 0 
	counter = [0,0,0,0,0,0]
	points = [1000,200,300,400,500,600]
	extra = [100,0,0,0,50,0]
	for die in dice:
		counter[die-1]+=1
	for (i,count) in enumerate(counter):
		sum+= (points[i] if count>=3 else 0) +extra[i]* (count%3)
	return sum

	_______________________________________________________________________
cities = ['Marseille', 'Amsterdam', 'New York', 'London']
	#the bad way 
i=0
for city in cities:
	print(i, city)
	i+=1

	#THE GOOD WAY
for i, city in enumerate(cities):
	print(i, city)

_______________________________________________________________________
x_list = [1,2,3]
y_list = [2,4,6]

# THE BAD WAY:

for x in range(len(x_list)):
	x = x_list[i]
	y = y_list[i]
	print(x,y)

# THE GOOD WAY

for x,y in zip(x_list, y_list): #this turns into tuples otherwise
	print(x,y)

_______________________________________________________________________
x =10
y = -10
print('Before: x = %d, y = %d' % (x,y))
#the bad way 
tmp =y
y=x
x= tmp
print('After: x = %d, y = %d'  %(x,y))

# the good way

x,y = 10,-10

x,y = y,x #its beautiful!

print('After: x = %d, y = %d'  %(x,y))
_______________________________________________________________________

ages = {'Mary':31, 'Jonathan':28}


#the bad way 
if 'Dick' in ages:
	age = ages['Dick']
else:
	age = 'Unknown'
print('Dick is %s years old' % age)


#the good way

age=ages.get('Dick', 'Unknown')

print('Dick is %s years old' % age)

_______________________________________________________________________

needle = 'd'
haystack = ['a','b','c']

#the bad way

found = False
for letter in haystack:
	if needle = letter :
		print('Found!')
		found = True
		break
if not found:
	print('Not Found')

# The good way

for letter in haystack:
	if needle = letter :
		print('Found!')
		break  #oh yeah you can stop a for loop when you get what you need
else: #no break occured
	print('Not Found')

_______________________________________________________________________

#the bad way

f = open('Pimpin-aint-easy.txt')
text = f.read()
for line in f:
	print(line)
f.close()


# The better way

with open('Pimpin-aint-easy.txt') as f:
	for line in f:
		print(line)

_______________________________________________________________________

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
					  REGEX 2 ELECTRIC BOGALOO
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

Sentence = 'Start a sentence and then bring it to an end'


# BEFORE WRITING OUR FIRST REGEX LETS TALK ABOUT RAW STRING - IT'S A STRING PREFIXED WITH AN R.

EXAMPLE

print('\tTab')
#output
	'Tab'

print(r'\tTab')
#output
'\tTab'

#compile will let us separate out our patters into variables.

#makes it easier to reuse that variable to perform multiple searches

pattern = re.complie(r'abc')

matches = pattern.finditer(text_to_search)

for match in mathes:
	print(match)
#output
<_sre.SRE_Match object; span=(1,4), match='abc'>

print(text_to_search[1:4])
#output
'abc'

#quick note when searching for a period we add the backslash

pattern = re.complie(r'\.')

#this trick needs to be applied in things like searching websites

pattern = re.complie(r'coreyms\.com')

MetaCharacters
# . 	- any character except a new line
# \d 	- Digit (0-9)
# \D 	- Not a Digit
# \w 	- Word Character (a-z, A-Z, 0-9)
# \W 	- Not a Word Character
# \s 	- Whitespace (space, tab, newline)
# \S 	- Not Whitespace (space, tab, newline)

##  ANCHORS - not matching characters but invisible positions before or after characters

# \b 	- Word Boundary 
	 re.complie(r'\bHa') #you get the first ha and part of the second one in
	 # line 193 so be casreful using.
# \B 	- Not a Word Boundary pattern
	 re.complie(r'\BHa') #now we get the second Ha in HaHa 

# ^ 	- Beginning of a String

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
# output will return a place to find if it matches. 

# $ 	- End of a String

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'$end')
matches = pattern.finditer(sentence)
# output will return a place to find if it matches. 


# []	- Matches characters in brackets
# [^]	- Matches characters NOT in brackets
# | 	- Either Or
# ()	- Group

# QUANTIFIERS:

# *		- 0 or more
# +		- 1 or more
# ?		- 0 or One
# {3}	- Exact number
# {3,4}	- Range of numbers (Minimum, Maximum)




# time to get to know metacharacters. lets get those phone numbers
pattern = re.complie(r'\d\d\d.\d\d\d.\d\d\d\d')
		#rememebr the dot alone will accept anything so the . - in phone numbers is picked up as not many other items follow this pattern.

matches = pattern.finditer(text_to_search)

with open('data.txt', 'r', encoding ='utf-8') as f:
	contents = f.read()

	matches = pattern.finditer(contents)

	for match in matches
#this returns all the phone numbers in our imaginary file of contacts.  

#now what if we want the phone #s with only dashes?

# character sets to the rescue! ( square brackets with our desired characters!)

pattern = re.complie(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# lets say we only wanted 800 or 900 numbers. no problem

pattern = re.complie(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# K what about numbers 1 through 5?

pattern = re.complie(r'[1-5]')

#letters?

pattern = re.complie(r'[a-z]') 

#what if i want both lower and uupercase?

pattern = re.complie(r'[a-zA-Z]')

# And if i dont want them because i hate letters suddenly?

pattern = re.complie(r'[^a-zA-Z]')

# what if i want to pit up three letter words ending with at, but not bat because im weird.

#hi werid!

pattern = re.complie(r'[^b]at')

#now we learn about quanitifiers. which can match more than one character at once. back to the phone number example

pattern = re.complie(r'\d{3}.\d{3}.\d{4}')

# so what if we arent sure how many characters we need? like if we are looking up names?

pattern = re.complie(r'Mr\.?\s[A-Z]\w*') #notice when we use word and * we dont need to clairify the use of lowercase!

# HEY what about the ladies?

pattern = re.complie(r'M(r|s|rs)\.?\s[A-Z]\w*')

# lets be kind to our future selves

pattern = re.complie(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# how about emails?

pattern = re.complie(r'[a-zA-Z0-9.]+@[a-zA-Z-]+\.(com|org|net|edu|gov)')

#how about every possible email we could have?

pattern = re.complie(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# ooh OOH! Do Websites now!

pattern = re.complie(r'https?://(www\.)?(\w+)(\.\w+)')

for match in matches:
	print(match.group(0)) #groups(1)(2)(3) also give us choices! 

# Back reference 
# to reference our captured group (shorthand for accessing these group indexes)

#instead of the for loop above do this. 

subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

#this lists off all the captured sites! 

#now we have been using .finditer() this whole time lets try something else

matches = pattern.findall(text_to_search) #returns all the matches as a list of strings. if it's matching groups only groups. finditer is more flexible, but findall is also useful.

pattern = re.complie(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

#when we use it on this, we only get the Mr, Ms, and Mrs nothing else. 

#for the phone number ones we get everything because thats all one group. 

pattern = re.complie(r'\d{3}.\d{3}.\d{4}')


# Now we got the .match() method 

#will determine if the regular expression matches at the beginning of the string. 

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'Start')
matches = pattern.match(sentence)
#THIS WILL NOT RETURN AN ITERABLE. NO FOR LOOPS FOR YOU! 
print(matches)
#output
#<_sre.SRE_Match object; span=(0,5), match='Start'>


# k so what if we tried to match sentence?

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'sentence')
matches = pattern.match(sentence)
#THIS WILL NOT RETURN AN ITERABLE. NO FOR LOOPS FOR YOU! 
print(matches)
#output
None

#it's only seeing if it matches at the beginning of that string. If we are looking deeper we use the .search() method

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'sentence')
matches = pattern.search(sentence)

print(matches)
#output
##<_sre.SRE_Match object; span=(8,16), match='sentence'>


# time to check for Flags! 

#what if you were looking for a word and wanted to see if it was in uppercase, lowercase, or both?
 

 sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'start', re.IGNORECASE) #re.I also works but for the sake of readability we're going to use the longer version. 
matches = pattern.search(sentence)

print(matches)

# take some time to google for other regex flags and other functions there are plenty to go around!



Reeducation of calsses 

class NameOfClass():
	def __init__(self, param1,param2):
		self.param1 = param1
		self.param2 = param2

	def some_method(self):
		#perform some action 
		print(self.param1)


class Dog():

	def __init__(self, breed): #breed here
		#attributes
		#we take in the arguement
		#assign it using the self.attribute_name
		self.breed = breed #<-- is this breed here 


my_dog = Dog(breed = 'Lab')


type(my_dog)
#output
__main__.Dog 

my_dog.breed
#output
'Lab'

#lets add more things to this class

class Dog():

	def __init__(self, breed, name, spots): 
		'''Docstrings are good here. use them.'''

		self.breed = breed #string
		self.name = name #string
		self.spots = spots #boolean True or False

my_dog = Dog(breed = 'lab', name = 'Sammy', spots = False)

my_dog.breed
#out
'lab'

my_dog.name 
#out
'Sammy'

my_dog.spots
#out
False

class Dog():

	#class object attribute
	#same for any instance of a class
	species = 'mammal' # no self.whatever needed in this spot.  

	def __init__(self, breed, name, spots): 
		'''Docstrings are good here. use them.'''

		self.breed = breed #string
		self.name = name #string
		self.spots = spots #boolean True or False

my_dog = (breed ='Lab', name = 'Sammy', spots = False)

my_dog.species
#output
'mammal'


#now for the methods. 


class Dog():

	#class object attribute
	#same for any instance of a class
	species = 'mammal' # no self.whatever needed in this spot.  

	def __init__(self, breed, name, spots): 
		'''Docstrings are good here. use them.'''

		self.breed = breed #string
		self.name = name #string
		self.spots = spots #boolean True or False


	#Methods <- - - - operations/actions
	def bark(self, number):
		print('WOOF! My name is {} and the number is {}.'.format(self.name, number))

my_dog = (breed ='Lab', name = 'Frankie', spots = False)
	
my_dog.species
#out
'mammal'

my_dog.name
#out
'Frankie'

#HOW TO ACTIVATE METHODS:
my_dog.bark(2)
#output
'WOOF! My name is Frankie and the number is 2.'


class Circle():

	#class object attribute
	pi = 3.14

	__init__(slef,radius=1):

		self.radius = radius
		self.area = self.pi * radius**2 #you can also use Circle.pi to show off

	# Method
	def get_circumference(self)
	return self.radius * self.pi * 2


my_circle = Circle()
my_circle.pi
#out 
3.14

my_circle.radius
#out 
1
#wanna change it?

my_circle = Circle(30)
my_circle.radius
#out
30
my_circle.get_circumference()
#out
188.4
my_circle.area
2826.0


#be kind to your future self. 

#Inheritence and polymorphism

#Creating new clasees based on classes already defined.


class Animal(): #This is a base class

	def __init__(self):
		print("ANIMAL CREATED")

	def who_am_i(self):
		print("I am an animal")

	def eat(self):
		print("I am eating")


myanimal = Animal()
#out
ANIMAL CREATED

myanimal.eat()
#out
I am eating

myanimal.who_am_i()
#out
I am an animal


class Dog(Animal): #we inherit Animal to our class

	

	def __init__(self): 
		'''Docstrings are good here. use them.'''
		Animal.__init__(self)
		print("Dog Created")

	def who_am_i(self):
		print("I am a dog!") #this overwriites the previous one in the animal class

	def bark(self):
		print("WOOF!")

	def eat(self):
		print("I am a dog and eating")




mydog= Dog()
#out
ANIMAL CREATED
Dog Created

mydog.eat()
#out
I am a dog and eating

mydog.who_am_i()
#out
I am a dog!

#Polymorphism!

class Dog():

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says woof!"

class Cat():

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says meow!"

niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
#out 
Niko says woof!

print(felix.speak())
#out 
Felix says meow!

for pet in [niko,felix]:
	print(type(pet))
	print(pet.speak())
#out
<class '__main__.Dog'>
niko says woof!
<class '__main__.Cat'>
felix says meow!

def pet_speak(pet):
	print(pet.speak())


pet_speak(niko)
#out
Niko says woof!

pet_speak(felix)
#out
Felix says meow!

#Abstract classes and Inheritence

class Animal():

	def __init__(self,name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method.")

myanimal = Animal('fred')

myanimal.speak()
#output 
NotImplementedError: Subclass must implement this abstract method.

class Dog(Animal):

	def speak(self):
		return self.name+' says woof!'

class Cat(Animal):

	def speak(self):
		return self.name+' says meow!'

fido = Dog('Fido')

isis = Cat('Isis')

print(fido.speak())
#out
Fido says woof!

print(isis.speak())
#out
isis says meow!

#special (Magic/Dunder) methods

mylist = [1,2,3]

len(mylist)
#out
3

class Sample():
	pass

mysample = Sample()
len(mysample)
#output
TYPE ERROR

print(mysample)
#out
<__main__.Sample object at 0x0000015B611B9710>


print(mylist)
#out
[1,2,3]

#how do we get stuff out of classes?

class Book():

	def __init__(self, title,autor,pages):
		
		self.title = title
		self.author = author
		self.pages = pages

b = Book('Python rocks', 'Jose', 200)

#if we tried printing that now..

print(b)
#out
<__main__.Book object at 0x0000015B611D5238>

str(b)
#out
'<__main__.Book object at 0x0000015B611D5238>'


#FIX IT

class Book():

	def __init__(self, title,autor,pages):
		
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author}. {self.pages} pages of cool."

#k now lets try printing our stuff.

print(b)
#out
'Python rocks by Jose. 200 pages of cool.'

#thats cool and all but what about length?


class Book():

	def __init__(self, title,autor,pages):
		
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author}. {self.pages} pages of cool."

	def __len__(self):
		return self.pages


len(b)
#out
200

del b 

b 
#output
#NameError: name 'b' is not defined

#BUT THIS MIGHT NOT BE GOOD ENOUGH!

class Book():

	def __init__(self, title,autor,pages):
		
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author}. {self.pages} pages of cool."

	def __len__(self):
		return self.pages
	
	def __del__(self):
		print("A book object has been deleted")

del b 
#out
# A book object has been deleted

class Line:
		def __init__(self, coor1, coor2):
			self.coor1 = coor1
			self.coor2 = coor2

		def distance(self):
			x1,x2 = self.coor1
			y1,y2 = self.coor2
			return (((x2-x1)**2)+((y2-y1)**2)**0.5)

		def slope(self):
			x1,x2 = self.coor1
			y1,y2 = self.coor2
			return (y2-y1)/(x2-x1)


class Cylinder:
	pi = 3.14

	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return self.pi * self.radius**2 * self.height

	def surface_area(self):
		return (2*self.pi) * self.radius * self.height + (2 * self.pi) * self.radius **2
_______________________________________________________________________

# Instance class, and Static methods and overvview. 

class MyClass:
	def method(self):
		return 'instance method called', self

	@classmethod
	def classmethod(cls):
		return 'class method called', cls

	@staticmethod
	def staticmethod():
		return 'static method called'

#instance methods

#the first Method shown above is a a regular instance mthod. 

	def method(self):
			return 'instance method called', self

# Just a basic type we will use most of the time. like a function, but for classes. 
#it takes the paramater: 
self
#which points to an instance of MyClass when the method is called. can take more than one parameter.

#Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

#Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.


#Class methods 

	@classmethod
	def classmethod(cls):
		return 'class method called', cls

#Let’s compare that to the second method, MyClass.classmethod. I marked this method with a @classmethod decorator to flag it as a class method.

#instead of accepting a self parameter class method take a cls parameter that points to the class and not the object instance when the method is called. 

# Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

Static Methods


	@staticmethod
	def staticmethod():
		return 'static method called'


#The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.

#This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

# Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods. 

________________________________________________________________________________

class Employee:
	pass

emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Corey'
emp_2.last = 'Schafer'
emp_2.email = 'Corey.Schafer@company.com'
emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)

#what if we didnt have to put this crap in manually? THERES GOT TO BE A BETTER WAY!

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

	def fullname(self):
		return "{} {}".format(self.first, self.last)
		#Python 3 way.
		return f"{self.first} {self.last}"


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

#Class variables

#variables that are shared in all instances of a class

# while instance variables are unique for each instance (name, pay, email, etc)

# Class variables will be the same for each instance. (how about everyone gets the same raise!)


class Employee:
	num_of_emps = 0
	raise_ammount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

		Employee.num_of_emps +=1

	def fullname(self):
		return "{} {}".format(self.first, self.last)
		#Python 3 way.
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay*self.raise_ammount)



emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
					CLASS METHODS AND STATIC METHODS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/


#Regular methods in a class automatically take the instance as the first arguement (self). How do we change it so the CLASS is the first arguement? We add a decorator!

class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

		Employee.num_of_emps +=1

	def fullname(self):
		return "{} {}".format(self.first, self.last)
		#Python 3 way.
		return f"{self.first} {self.last}"

	#This changes the amount for a specified employee
	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amt)

	@classmethod
	#THIS CHANGES ALL THE EMPLOYEES NOT JUST ONE
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls,emp_str):
		first, last, pay = emp_str.split('-')
		return cls.(first, last, pay)


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)
new_emp_1 = Employee.from_string(emp_str_1)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
STATIC METHODS 	STATIC METHODS 	STATIC METHODS 	STATIC METHODS 	STATIC METHODS 	
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# REGULAR METHODS AUTOMATICALLY pass the instance as the first arguement (self)

# CLASS METHODS pass the class as the first arguement (cls)

# STATIC METHODS  DO NOT pass anything automatically. 

	# they behave like regular functions except we include them in the class as they are logically connected to them 

	#lets add a static method that takes a date and sees if thats a workday or not. 


class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

		Employee.num_of_emps +=1

	def fullname(self):
		return "{} {}".format(self.first, self.last)
		#Python 3 way.
		return f"{self.first} {self.last}"

	#This changes the amount for a specified employee
	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amt)

	@classmethod
	#THIS CHANGES ALL THE EMPLOYEES NOT JUST ONE
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls,emp_str):
		first, last, pay = emp_str.split('-')
		return cls.(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or if day.weekday() == 6:
			return False
		return True
#pro tip! if you dont need to call the class or the instances, it can be a static method or a function!

#so how would i activate one of these staic methods? 
import datetime

my_date = datetime.date(2019, 4, 29)

print(Employee.is_workday(my_date))


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				CLASS INHERITANCE --- CREATING SUBCLASSES
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

		Employee.num_of_emps +=1

	def fullname(self):
		return "{} {}".format(self.first, self.last)
		#Python 3 way.
		return f"{self.first} {self.last}"

	#This changes the amount for a specified employee
	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amt)

class Developer(Employee):
	raise_amt = 1.10
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) #this is useful!
		self.prog_lang = prog_lang

class Manager(Employee):
	# WARNING  WARNING  WARNING  WARNING  WARNING  WARNING 
	# Never put a [] () or {} in your arguements use None or = number or variable instead.  
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay) #this is useful!
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	def print_emps(self):
		for emp in self.employees:
			print(emp.fullname()) #don't forget the ()!

dev_1 =Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()


isinstance() #tells us if an object is an instance of a class

print(isinstance(mgr_1,Manager))
#out 
True
print(isinstance(mgr_1,Employee))
#out 
True
print(isinstance(mgr_1,Developer))
#out 
False

issubclass(x,y) #tells us if a class is a subclass of another

issubclass(Developer, Employee)
#out
True
issubclass(Manager, Employee)
#out
True
issubclass(Manager, Developer)
#out
False


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

				Special methods AKA Magic/Dunder Methods

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/


 MAJOR KEY ! ! ! ! ! - # Dunder == DOUBLE UNDER == DOUBLE UNDERSCORES

class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

		Employee.num_of_emps +=1

	def fullname(self):
		return "{} {}".format(self.first, self.last)
		#Python 3 way.
		return f"{self.first} {self.last}"

	#This changes the amount for a specified employee
	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amt)

	def __repr__(self):#unambiguous representation of the object (useful for devs)
		return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

	def __str__(self):# readable thing for the end user. 
		return "{} - {}".format(self.fullname(),self.email)
		#note fullname is a method so it needs at least the () 
	
	def __add__(self, other):
		#my my this line of code would have been helpful earlier! 
		return self.pay + other.pay
	
	def __len__(self):
		return len(self.fullname())



emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1)
#out (before using __repr__)
<__main__.Employee object at 0x101b2b0f0>

print(emp_1)
#Out (after using __repr__)
Employee('Corey','Schafer',50000)


print(repr(emp_1)) #AKA print(emp_1.__repr__())
#out
Employee('Corey','Schafer',50000)

print(str(emp_1)) #AKA print(emp_1.__str__())
#out
Employee('Corey Schafer- Corey.Schafer@email.com')

# print(1+2) == print(int.__add__(1,2))

# print(1+2) == print(str.__add__('a','b'))

#print(len('test')) == print('test'.__len__())


//////////////////////////////////////////////////////////////////////////

Javascript events and event handling:

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Events: Notifications that are sent to notify the code that something happened on the webpage 

#examples clicking a button resizing a window, scrolling down or pressing a key.

# Event listener: a function that performs an action based on a certain event. it waits for a specific event to happen.  

# how is is processed?

# First the execution stack. 

# an event can only be processed or handled as soon as the execution stack is empty.

# which means all of the functions have returned 

#from there we deal with the message queue in the javascript engine. 

#this is where all the events that happen in the browswer are put.

#they sit there waiting to be processed. 

#They are only processed AFTER the execution stack is empty 

#next item in message queue now gets processed. 

#remember about the event listener? Listening and waiting for things to happen.

#the message queue is a calling it. since it's a function it gets it's own execution context. 

#which is then put at the top of the EXECUTION STACK which will be handled before going back to the message queue. 

#small victory. 

#how to setup an event handler,

#what a callback function is

#what an anonymous function is 

#another way to select elements by id

#how to change the image in an <img> element 




\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
				EVERYTHING IS AN OBJECT 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#primitives
	#numbers
	#strings
	#booleans
	#undefined
	#null
#everything else....
	#arrays
	#functions
	#objects 
	#dates
	#wrappers for numbers, strings, booleans etc
#...is an object!

#object oriented programming
	#objects interacting with one another through methods and properties;

	#used to store data, structure applications into modules and keeping the code clean. 

#constructors and instances in javascript
_________________ 
|	 Person		|
|---------------|
| yearOfBirth   |
|---------------|
|	   job      |
|---------------|
| calculateAge()|
|---------------|

#they are called classes in other languages but here they are called constructors


#inheritance in general. when one object is based on another object. 

	#The person concstructor could be utilized for an athelete constructor. the athelete constructor... Seriously you know this stuff already. Python does this with classes 

#prototypes and prototype chains

	#inheritance works using prototypes
	#each and every object has a prototype property which is what makes inheritance possible in javascript.  

	#lets say john wants to inherit the calculateAge the person object is a constructor and John is one of the instances. 

	#if we want john to inherit a property from the person object

	#we have to add that method or property to the person's prototype property.

#THE IMPORTANT STUFF

# every javascript object has a PROTOTYPE PROPERTY, which makes inheritance possible in javascript.  

# The prototype property of an object is where we put methods an d properties that we want OTHER OBJECTS TO INHERIT.

#the consturctors prototype property is NOT the prototype constructoe itself, it's the prototype of ALL instances that are created through it.

#when a certain method (or property ) is called, the search starts in the object itself, and if it cannot be found, the search moves on to the object's prototype/ this continues until the method is found: prototype chain.


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
		WEAKNESSES IN PROGRAMMING 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# classes in Python.

# closures in javascript  - An inner function has access to the variable and parameters of its outer function even after the outer function has returned. It's javascript's super power. It also hides those outer variables, paramaters and functions! 



## GET FRIENDLY WITH ARROW FUNCTION 

#What is git?

	#distributed source control system
	#not required to be decentralized
	#open source
	#developed for linux project requirements
	#most operations are local
	#very fast 
	#active community
	#Most popular DVCS, VCS

# Key concepts
	#repository contains files, history, config managed by git
	# history of changes or special configuration
	#three states of git
		
		#working directory 
			#directory or folder on your computer that holds all the application/project files..			
				
		#staging area - pre-commit holding area
			
			#aka git index
			
			#holding area for queing up changes for the next commit 

			#since they are not commited yet, you can move them in and out of the staging area. without impacting the git repository and it's history of changes.
		
		#Commit - Git repository (history) 
			
			#normally with the  working directory is a hidden folder called the .git folder that conatains the actual git repository.
			
			#manages the git commmt history

	#forth unofficial stage GitHub
		#remote repostiory with it's own three states

	#Master Branch
		#branches in git

		#master is the default one. 

#coomand line?

#history

#new features

#online help

#power!

#consistent
	#terminal on Mac Linux
	#git Bash on windows.

#windows
	#git for windows (git-scm.com)
#mac OS X
	# Yosemite or later, easy path: "git version"
#Git Commands will be the same

