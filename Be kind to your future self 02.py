#one more time on step ten

#while loop to keep running the game
print('welcome to tic tac toe!')

while True:
	#play the game
	#set everything up (board, whos first, choose markers x,o)
	board = [' ']*10 #blank spaces
	player1_marker,player2_marker = player_input()
	turn = choose_first()
	print(turn,' goes first!')
	play_game = input("Ready??? 'Y' or 'N'?: ")
	if play_game.upper()[0] == 'Y':
		game_on = True
	else:
		game_on = False
	#gameplay
	while game_on:
		##player 1 turn
		if turn == 'Player 1':
			#display the board
			display_board(board)
			#chose position
			position = player_choice(board)
			place_marker(board,player1_marker,position)
			#check for win
			if win_check(board,player1_marker):
				display_board(board)
				print("Player 1 wins!")
				game_on = False
			#check tie.
			else:
				if full_board_check(board):
					display_board(board)
					print("Draw!")
					game_on = False
					#else player 2 turn
				else:
					turn ='Player 2'
		##Player 2 turn
		else:
			if turn == 'Player 2':
				#display the board
				display_board(board)
				#chose position
				position = player_choice(board)
				place_marker(board,player2_marker,position)
				#check for win
				if win_check(board,player2_marker):
					display_board(board)
					print("Player 2 wins!")
					game_on = False
				#check tie.
				else:
					if full_board_check(board):
						display_board(board)
						print("Draw!")
						game_on = False
						#else player 2 turn
					else:
						turn ='Player 1'
	if not replay():
		break
	#break out of the while loop on replay() fuction

#lessons learned:
	#know exactly what your functinos do and where to put them. 

	# Dont panic (preferrably in friendly red letters)
	
	#INDENTATIONS 

	# LURN 2 SPEL
#100k job
#Be Kind To Your Future Self

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
					OBJECT ORIENTED PROGRAMMING
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

~~~~~INTRODUCTION~~~~~~~~

	# Object oriented programming (OOP) allows programmers to create their own objects that have methods and attributes. 

	# recall that after defining a string, list, dictionary, or other objects, you were able to call methods off of them with the .method_name() syntax.

	#These methods act as functions that use information about the object, as well as the object itself to return results or change the current object. 

	#for example this includes appending to a list, or counting the occurances of an element in a tuple. 

	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>>### OOP allows users to create their own objects. 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# the general format is often confusing when first encountered because of the use of a self keyword and it's usefullnes may not be completely clear first. 

	# in general OOP allows us to create code that is repeatable and organized. 

	#for much larger scripts of python code, functions by themselves arent enough for organization and repeatability.

	#commonly repeated tasks and objects can be defined with OOP to create code that is more useable. 

	#lets check out the syntax.

	~~~~~~~~~~~~~~~EXAMPLE~~~~~~~~~~~~~~~~~
	#class keyword is how we usually define an object.
	class NameOfClass(): #CamelCasing
		def _init_(self,param1,param2):
			self.param1 = param1
			self.param2 = param2

		def some_method(self):
			#perform some action 
			print(self.param1)

		#BREAK IT DOWN.
	#class keyword is how we usually define an object.
	#CamelCasing. do this for classes not variables or methods
	class NameOfClass():
		#this is a method bellow not a function
		#_init_ method allows you to create an instance of this object.
		def _init_(self,param1,param2):

			self.param1 = param1
			self.param2 = param2 #assign it to an attribute of a function.

		def some_method(self): #self is an indicationit's a method and not a function. 
			#perform some action 
			print(self.param1)

#don't worry if this doesnt make sense right away. We're going to keep doing more code examples. Take five. 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
					ATTRIBUTES AND CLASS KEYWORD 
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#attributes are a characteristic of an object.

#mylist = [1,2,3]

#myset = set()

#type(myset)
#output
set

#type(mylist)
#output
list

class Dog():
    def __init__(self,breed):
        
        self.breed = breed

########################
my_dog = Dog(breed='Lab')

type(my_dog)
#output
__main__.Dog

my_dog.breed
#output
'lab'


#Break it down

__init__ #constructor for a class called automatically when u construct an instance of a class. 

#class Dog():
    def __init__(self #instance of the object itself.
)
# 
class Dog():
    def __init__(self,breed): # Breed = 
        #attributes 
        # we take n the arguement
        #assign it using self.attribute_name
        self.breed = breed

class Dog():
    def __init__(self,breed,name,spots):
        #attributes
        # we take in arguement
        #assign it to using self.attribute_name
        self.breed = breed
        self.name = name
        #expect boolean T/F
        self.spots = spots

my_dog = Dog(breed = 'lab', name = 'Sammy', spots = False)

my_dog.breed
#output
'lab'
my_dog.name
#output
'Sammy'
my_dog.spots
#output
False
 
 #Documentation strings are a must in these cases. especially now that programs are getting more complex

#to review
#use the class keyword

#capitalized names and camelcasing

#first method is __init__ method acts as a constructor

# self keyword as reference to the instance of the class

# follow the rest with attributes.
# paramaters and attributes assigned to the assignment call all have same names used to simplify

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				CLASS OBJECT ATTRIBUTES AND METHODS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#User defined objects are created using the class keyword. The class is a blueprint that defines the nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. For example, above we created the object lst which was an instance of a list object.

class Dog():
    def __init__(self,breed,name,spots):
        #attributes
        # we take in arguement
        #assign it to using self.attribute_name
        self.breed = breed
        self.name = name
        #expect boolean T/F
        self.spots = spots

my_dog = Dog(breed = 'lab', name = 'Sammy', spots = False)

type(my_dog)

#WE CAN DEFINE AN ATTRIBUTE AT A CLASS OBJECT LEVEL. 


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  PRO TIP !  PRO TIP !  PRO TIP !  PRO TIP !  PRO TIP !  PRO TIP !  
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 #An attribute is a characteristic of an object.

 # A method is an operation we can perform with the object.
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  PRO TIP !  PRO TIP !  PRO TIP !  PRO TIP !  PRO TIP !  PRO TIP !  
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class Dog():

	#class object attribute
	#same for any instance of a class.
	species = 'mammal'

    def __init__(self,breed,name,spots):
        #attributes
        # we take in arguement
        #assign it to using self.attribute_name
        self.breed = breed
        self.name = name
        #expect boolean T/F
        self.spots = spots

#this attribute will work regardless of what changes you make bellow. such is the way of python indentation.

~~~~METHODS~~~~~~~~~~

#functions defined inside the body of the class and they are used to perform operations that sometimes utilize actual attributes of the object we made. 
0

# A method is an operation we can perform with the object.


class Dog():

    #class object attribute
    #same for any instance of a class.
    species = 'mammal'
    def __init__(self,breed,name):
        #attributes
        # we take in arguement
        #assign it to using self.attribute_name
        self.breed = breed
        self.name = name

    
    #OPERATIONS/Actions ----> Methods
    def bark(self): 
        print("Woof!")

my_dog.bark() # note the ()
#output
"Woof!"
#this is a method. it's an action the object can take! 

#lets get fancy. lets have the dog bark its name! 

class Dog():

    #class object attribute
    #same for any instance of a class.
    species = 'mammal'
    def __init__(self,breed,name):
        #attributes
        # we take in arguement
        #assign it to using self.attribute_name
        self.breed = breed
        self.name = name

    
    #OPERATIONS/Actions ----> Methods
    def bark(self): 
        print("Woof! My name is {}".format(self.name))
#self in bark is there in case we reference it. 

my_dog.bark()
#output
Woof! My name is Frankie

#cool huh? lets add more stuff
##############################################
||||||||||||||||||||||||||||||||||||||||||||||
##############################################
class Dog():

    #class object attribute
    #same for any instance of a class.
    species = 'mammal'
    def __init__(self,breed,name):
        #attributes
        # we take in arguement
        #assign it to using self.attribute_name
        self.breed = breed
        self.name = name

    
    #OPERATIONS/Actions ----> Methods
    def bark(self, number): 
        print("Woof! My name is {} and the number is {}".format(self.name,number))

 #no extra self needed when we add number to the method. we can add one in the parenthesis. 

 my_dog.bark(10) #we add the number in here. 

#output
#Woof! My name is Frankie and the number is 10

#see we can either pull up ones in the attributes, or we can add out own input when needed.  

#lets make a new class


class Circle():
    
    #class object attribute.
    pi = 3.14 
    
    
    def __init__(self,radius = 1):
        
        self.radius = radius
        
    #method
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)
my_circle.get_circumference()
#output
188.4

#one more cool trick

class Circle():
    
    #class object attribute.
    pi = 3.14 
    
    
    def __init__(self,radius = 1):
        
        self.radius = radius
        self.area = radius*radius*self.pi #or Circle.pi (casing matters)
    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi
    #method for circumfrence
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)

my_circle.area
#output
2826.0



#In the __init__ method above, in order to calculate the area attribute, we had to call Circle.pi. This is because the object does not yet have its own .pi attribute, so we call the Class Object Attribute pi instead.

#In the setRadius method, however, we'll be working with an existing Circle object that does have its own pi attribute. Here we can use either Circle.pi or self.pi.

my_circle.setRadius(2)

print('Radius is: ',c.radius)
print('Area is: 'c.area)
print('Circumfrence is: ',c.get_circumference)

#output #output #output #output #output #output #output

#Radius is:  2
#Area is:  12.56
#Circumference is:  12.56




#you can pull up class object attributes by using class name instead of the self. Example Circle.pi 


#awesome work. You understood this. One step closer to 100k a year. Take five. 


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
					INHERRITANCE AND POLYMORPHISM 
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/



#Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
#notice you can override inherrited attributes by simply rewriting them in your class. 
    def whoAmI(self): 
        print("Dog")
#and since this is a new class you can add other attributes as well
    def bark(self):
        print("Woof!")

#Test

d = Dog()
#output.
Animal created
Dog created

d.whoAmI()
#output
Dog


#now lets get into 

~~~~~~~~~~~POLYMORPHISM~~~~~~~~~~~~~~~~~~

#We've learned that while functions can take in different arguments, methods belong to the objects they act on. In Python, polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in. The best way to explain this is by example:

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

#output

Niko says Woof!
Felix says Meow!



#Here we have a Dog class and a Cat class, and each has a .speak() method. When called, each object's .speak() method returns a result unique to the object.

#There a few different ways to demonstrate polymorphism. First, with a for loop:

for pet in [niko,felix]:
    print(pet.speak())

#output
Niko says Woof!
Felix says Meow!

#how about with functions?

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
#output
Niko says Woof!
Felix says Meow!

#In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.

#A more common practice is to use abstract classes and inheritance. An abstract class is one that never expects to be instantiated. For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:


class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method") #We put in an intentional error to inform us and other devs this is meant to be an inherited method. 


class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

#output
Fido says Woof!
Isis says Meow!



#Real life examples of polymorphism include:

    #opening different file types - different tools are needed to display Word, pdf and Excel files
    #adding different objects - the + operator performs arithmetic and concatenation


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				SPECIAL METHODS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example let's create a Book class:

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self): #see a pattern here?
        return self.pages

    def __del__(self):
        print("A book is destroyed")



book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book

#output
#A book is created
#Title: Python Rocks!, author: Jose Portilla, pages: 159
#159
#A book is destroyed

The __init__(), __str__(), __len__() and __del__() methods

#These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class.

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Homework assignment! Homework assignment! Homework assignment! 

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

~~~~~~~~~~~~~~~~~~~~~~~~PROBLEM 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

#Slope = (y2-y1) / (x2-X1)

#distance sqare root of sqrt(((y2-y1)**2) + ((x2-X1)**2))

#my guess

class Line:
    
    def __init__(self,coor1,coor2):
    	#must be tuples
        self.coor1 =coor1
        self.coor2= coor2
    
    def distance(self):
        return sqrt(((coor1[0]-coor1[1])**2) + ((coor2[0]-coor2[1])**2))
    
    def slope(self):
        return (coor2[1]-coor2[0])/(coor1[1]-coor1[0])

#answer

class Line:
    
    def __init__(self,coor1,coor2):
        #must be tuples
        self.coor1 =coor1
        self.coor2= coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2        
        return (((x2-x1)**2) + ((y2-y1)**2))**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2        
        return (y2-y1)/(x2-x1)

#almost got this. didnt think to incorporate x1 and y1 and was thinking with indexing. 

~~~~~~~~~~~~~~~~~~~~~~~~~PROBLEM TWO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



class Cylinder:
	pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
    	self.volume = pi * radius**2 * height
        
    
    def surface_area(self):
    	self.surface_area = (2*pi)*radius*height+ (2*pi)*radius**2
        
#correct answer

class Cylinder:
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * self.radius**2 * self.height
        
    
    def surface_area(self):
        return (2*self.pi)*self.radius*self.height+ (2*self.pi)*self.radius**2

#close again. we just needed to swap the attributes as methods and utilize return methods. the formulas were correct you just needed to write them with the .self. 


~~~~~~~~~~~~~~~~~~~~~~~~~CHALLENGE ONE~~~~~~~~~~~~~~~~~~~~~~~~~~~

#For this challenge, create a bank account class that has two attributes:

    #owner
    #balance

#and two methods:

    #deposit
    #withdraw

#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f"Account Name {self.owner}. Current balance is {self.balance}"
    def deposit(self,x):
        self.balance += x
        if self.balance > 100000:
            return f"Deposit Accepted. Your balance is now {self.balance}.\n Looks like you landed that 100k job!"
        else:
            return f"Deposit Accepted. Your balance is now {self.balance}."
    def withdraw(self,y):
        if self.balance >= y:
            self.balance -= y
            return f"Withdraw Accepted. Your balance is now {self.balance}."
        else:
            return "You don't have that kind of money wiseguy."

#lessons learned
#f string literals are our friends. 
#when in doubt, add self.whatever 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				  USING PYPI WITH PIP INSTALL
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#PyPi is a repository for open source third part python packages

#similar to RubyGems in Ruby world, php's packagist, CPAN for Pearl, and NPM for Node.js

#so far we only used libraries that come internally with python.

#there are amny other libraries availible that poeple have open-sourced and shared on PyPi.

#We can use pip install at command line to install these packages. 

#by installing Python from python.org of through Anaconda distribution you also installed pip

#pip is a simple way to download packages at your command line directly from the PyPi repository.

#there are packages already created for almost any use casse you can think of!

#a quick google search will usually help you discover a link to the PyPi page for the package, or for the package documentation. 

#lets quickly show you how to downlaod and install external packages.

	#Windows Users: Command Prompt
	#MacOS/Linux users: Terminal





|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
			WRITING YOUR OWN MODULES AND PACKAGES
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/


#Now that we understand how to install external packages, lets explore how to create our own modules and packages.

#modules are just .py scripts that you call in another .py scripts 

#packages are a collection of modules. 

#lets create some examples.

#you did it!

#100k job. prove everyone wrong. 



~~~~~~~~~~~~~~~~__name__ & "__main__" ~~~~~~~~~~~~~~~~~

# an often confusing part of python is a mysterious line of code: 
 	# if __name__ == "__main__":

#sometimes when you are importing from a module, you would like to know whehter a modules function is being used as an import, or if you are using a the original .py file of the module. 
# lets explore this some more, but make sure to check out the full explanatory text file that is in the part's folder. 

#video finished. Review these practices tonight. Be kind to your future self. 100K job. 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				ERRORS AND EXCEPTION HANDLING
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# Errors are bound to happen in your code!

# especially when someone else ends up using it in an unexpected way.

# we can use error handling to  attempt to plan for possible errors.

#for example a user may try to write a file that was only opened in mode='r'
#currently if there is any type of error in your code, the entire script will stop. 
#we can use Error Handling to let the script continue with other code, even if there is an error.

#We can use three keywords for this:
	# try: This is the block of code to be attempted (may lead to an error.)

	# except: Blick of code will execute in case there is an error in try block.

	# finally: a final block of code to be executed, regardless of error.  

def add(n1,n2):
    print(n1+n2)

add(10,20)

#output
30


number1 = 10
number2 = input("Please provide a number:")
# we put in 20

add(number1,number2)
print("Something Happened")
#output tldr
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    #want to attempt code but may have an error.
    
    result = 10 + "10"

except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print('add went well!')
    print(result)
#output
#'Hey it looks like you aren't adding correctly!'

try:
    f= open('testfile','r')#set to read instead of write.
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except:
    print('all other exceptions')
finally:
    print("I always run")
#output
#all other exceptions
#I always run

def ask_for_int():
    try: 
        result = int(input("Please provide a number: "))
    except:
        print("whoops!")
    finally:
        print("End of try/except/finally")

ask_for_int()

#output
#Please provide a number: 20
#End of try/except/finally

#now lets mess up

#output
#Please provide a number: fish
#whoops!
#End of try/except/finally


def ask_for_int():
    
    while True:
        try: 
            result = int(input("Please provide a number: "))
        except:
            print("whoops! That's not a number!")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")

ask_for_int()
# if i enter 'q'

#output

#Please provide a number: y
#whoops! That's not a number!
#End of try/except/finally
#I will always run at the end
#Please provide a number:__________

#if i enter a number

#Please provide a number: 5
#Yes thank you
#End of try/except/finally
#I will always run at the end




#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
    	try:
    		result = int(input("Please provide a number: "))
    	except:
    		print('An error occured. please try again.')
    		continue
    	else:
    		break
    print('Thank you, your number squared is: ',result**2)


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
			PYLINT OVERVIEW AND UNIT TESTING
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# as you begin to expand to larger multi-file projects it becomes important to have tests in place.

# this way as you make changes or update your code, you can run your test files to make sure previous code still runs as expected. 

# There are several testing tools, we will focus on two of them:

	# pylint - this is a library that looks at your code and reports back possible issues.

	# unittest:  this built-in library will allow to test your own programs and check you are getting desired outputs. 
# were going to begin by showing you how to sue pylint to check your code for possible errors and styling. 

	#python as a set of style convention rules known as "PEP 8".
	#afterwards we will explore how to test our code with the built-in unittest library

# for this lecture we will be creating .py scripts in sublime.

# you can still use the associated notebook for code using the %%writefile magic jupyter command.

# Lets do this 100k job

pip install pylint

pylint myscript.py -r y #-r y gives us more data to work with.

#we look for its returned errors and score it gives us for help

	#dont freak out getting a 10/10 isnt necessarily the right way to code think of it like the windows rating

~~~~~~~~~~~~~~~~~~unittest library~~~~~~~~~~~~~~~~~~~~~

#cap.py
def cap_text(text):
	'''
	input a string
	output the string capitalized
	'''
	return text.title()
################################################
#testcap.py
import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
if __name__ == '__main__':
    unittest.main()
################################################
#in cmd.

python test_cap.py


#to sum up:

#write your code 

#import it to your testing script. 
#import along with unittest


#write a class that tests your various code in the methods.

#test out the various methods of and functions and classes

#check with self.assertEqual()

#check the python documentation!



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				Blackjack Project
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/




    #1. Create a deck of 52 cards
    #Assign a value of cards and put them in a list? tuple? 
    #four of each
    #ace might need to ask if you want it as 1 or 11
import random
#tuple of suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#tuple of ranks 2-ace
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#dictionary to store values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
#playing will control big while loop
playing = True


#######################################################
#Class Definitions

#Consider making a Card class where each Card object has a suit and a rank, then a Deck class to hold all 52 Card objects, and can be shuffled, and finally a Hand class that holds those Cards that have been dealt to each player from the Deck.

#Step 2: Create a Card Class
#A Card object really only needs two attributes: suit and rank. You might add an attribute for "value" - we chose to handle value later when developing our Hand class.
#In addition to the Card's __init__ method, consider adding a __str__ method that, when asked to print a Card, returns a string in the form "Two of Hearts"

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank +' of '+ self.suit

#########################################################
#Step 3: Create a Deck Class
#Here we might store 52 card objects in a list that can later be shuffled. First, though, we need to instantiate all 52 unique card objects and add them to our list. 

#So long as the Card class definition appears in our code, we can build Card objects inside our Deck __init__ method. Consider iterating over sequences of suits and ranks to build out each card. This might appear inside a Deck class __init__ method:

#for suit in suits:
    #for rank in ranks:

#In addition to an __init__ method we'll want to add methods to shuffle our deck, and to deal out cards during gameplay.

#OPTIONAL: We may never need to print the contents of the deck during gameplay, but having the ability to see the cards inside it may help troubleshoot any problems that occur during development. With this in mind, consider adding a __str__ method to the class definition.

class Deck:

    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''#start witht the empty deck
        for card in (self.deck):
        	#add each card's print string
        	deck_comp += '\n'+card.__str__()
        return "The deck has: "+ deck_comp 

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
    	#how do we remove a card from the list? we pop it from the list!
        single_card = self.deck.pop()
        return single_card


#Step 4: Create a Hand Class
#In addition to holding Card objects dealt from the Deck, the Hand class may be used to calculate the value of those cards using the values dictionary defined above. It may also need to adjust for the value of Aces when appropriate.


class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


#Step 5: Create a Chips Class
#In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings. This could be done using global variables, but in the spirit of object oriented programming, let's make a Chips class instead!

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += (self.bet)
        return f"You win! Your total is now {self.total}."    
    def lose_bet(self):
        self.total -= (self.bet)
        return f"You lose. Your total is now {self.total}." 
#######################################################

#Function Defintions

#A lot of steps are going to be repetitive. That's where functions come in! The following steps are guidelines - add or remove functions as needed in your own program.

#Step 6: Write a function for taking bets
#Since we're asking the user for an integer value, this would be a good place to use try/except. Remember to check that a Player's bet can be covered by their available chips.
#######################################################

 

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How much are you willing to bet?: "))    		
        except ValueError:
            print("We're betting with chips, and nothing else. Give me a number.")
        else:
            if chips.bet > chips.total:
                print("Sorry chungus, your bet can't exceed",chips.total)
            else:
                break

########################################################
#Step 7: Write a function for taking hits
	#Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21.

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


########################################################
#Step 8: Write a function prompting the Player to Hit or Stand

#This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.

#If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of a while loop later on in our code.

def hit_or_stand(deck,hand):
    global playing # to control the upcoming while loop.
    while True:
        x = input("hit or stand? Enter 'H' or 'S' ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("player stands. Dealer is playing")
            playing = False
        else:
            print("You should read directions.")
            continue
        break

#######################################################


#Step 9: Write functions to display cards
#When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible. At the end of the hand all cards are shown, and you may want to show each hand's total value. Write a function for each of these scenarios.

def show_some(player,dealer):
	print("\nDealer's hand:")
	print("<CARD HIDDEN>")
	print(" ",dealer.cards[1])
	print("\nPlayer's Hand:", *player.cards, sep='\n ') #forgot the comma also learn what the * is for. 
def show_all(player,dealer):
	print("\nDealer's hand: ",*dealer.cards, sep='\n')
	print("Dealer's hand = ", dealer.value)
	print("\nPlayer's Hand: ", *player.cards, sep='\n')
	print("Player's hand = ", player.value)

#####################################################
#Step 10: Write functions to handle end of game scenarios


#Remember to pass player's hand, dealer's hand and chips as needed.

def player_wins(player,dealer,chips):
	print("Player wins!")
	chips.win_bet()
def player_busts(player,dealer,chips):
	print("Player BUSTED!")
	chips.lose_bet()
def dealer_wins(player,dealer,chips):
	print("Dealer wins!")
	chips.lose_bet()
def dealer_busts(player,dealer,chips):
	print("Dealer Busted!")
	chips.win_bet()
def push(player,dealer):
	print("PUSH! It's a tie!")
##################################################

#now onto the game!

from IPython.display import clear_output

while True:
    clear_output()
    # Print an opening statement
    print("welcome to Blackjack! Rules are hit or stand to 21. Play against the dealer. Dealer hits until 17. Aces count as 1 or 11")

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
        
    # Set up the Player's chips
    player_chips = Chips() #default value is 100
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
        
    
    # Inform Player of their chips total 
    print("Your chips stand currently at ",player_chips.total,".")
    
    # Ask to play again
    new_game = input("again? y or n? : ")
    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print("Thanks for playing.")
        break


#awesome. tomroow we're going to try writing all this again so you git gud. You werent as panicked as tic tac toe, but you can do better. We're going to ace tech academy! got it? good!`

import random
suits= ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 
values = {'Two':2,'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True


#--------------------------

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit # commas caused you problems use +s instead of ,

#-------------------

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#------------------

#In addition to holding Card objects dealt from the Deck, 
#the Hand class may be used to calculate the value of those
#cards using the values dictionary defined above. 
#It may also need to adjust for the value of Aces when appropriate.

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        #card passed in from Deck.deal() -->single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank] #look above for clues. Dont panic that you missed this. 
        #track aces
        if card.rank == 'Ace':
            self.aces +=1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces: #theres a while loop here. not an if while the ace is in your hand.
            self.value -=10
            self.aces -=1

#aces value works off truthiness in python. google that nao.

#-----------------------------------            

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        return f"Player 1 wins. Your total is {self.total}."
        
    
    def lose_bet(self):
        self.total -= self.bet
        return f"Player 1 wins. Your total is {self.total}."

#---------------------------------------

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("how much are you going to bet?:"))
        except ValueError:
            print("try putting a number in.")
        else:
            if chips.bet > chips.total:
                print("try something you can afford chungus.")
            else:
                break

#-----------------------------------------

def hit(deck,hand):	
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
	
#----------------------------------------
def hit_or_stand(deck,hand):
    global playing #we dont bring these in normally 
    #Hit or stand
    while True:#while it's the playing turn. 
        #ask hit or stand
        x = input("Hit or Stand? press 'h' or 's':")
        #if they hit use the hit function we just wrote. 
        if x[0].lower() == 'h':
            hit(deck,hand)
        #elif they stand, leave a witty response and put false on the loop.
        elif x[0].lower() == 's':
            print("player stands. Dealer is playing")
            playing = False #break the loop here.
        #else tell them to try again and continue the loop
        else:
            print("You should read directions.")
            continue
        break
#----------------------------------------
def show_some(player,dealer):
    print("Dealer's Hand:")
    print("<HIDDEN>")
    print(dealer.cards[1])
    print("\n")
    print("Player's Hand:")
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player's Hand:")
    for card in player.cards:
        print(card)
#-----------------------------------------
def player_busts(player,dealer,chips):
    print("Player BUSTS!")
    chips.lose_bet

def dealer_busts(player,dealer,chips):
    print("Dealer BUSTS!")
    chips.win_bet

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet

def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet
def push(player,dealer):
    print("PUSH! It's a tie!")

#-----------------------------------------
#put it together. Follow along no matter what. Be kind to your future self
#---------------------------------------------

while True:
    # Print an opening statement
    print('welcome to blackjack!')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
 
        show_some(player_hand,dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
    
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if deaseler_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        else: 
            push(player_hand,dealer_hand)

    
    # Inform Player of their chips total 
    print(f"you have {player_chips.total} chips.")
    # Ask to play again
    new_game = input("again? y or n? : ")
    
    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print("Thanks for playing.")
        break



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
						DECORATORS IN Python
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# lets discuss a more advanced Python topic: Decorators.

# Decorators allow you to "decorate" a function, lets discuss what that means in this context. 

#Imagine you created a function:

def simple_func():
	#Do simple stuff 
	#return something

# Now you want to add some new capabilites to the function:

def simple_func():
	#Want to do more stuff!
	#Do simple stuff 
	#return something

# You have two options:
	#Add that extra code(functuality) to your old function.

	#create a brand new function that contains the old code, and then add new code to that.
 # But what if then you want to remove that extra "functuality"?

 # you would need to delete it manually, or make sure you have that old function.

 #is there a better way? Maybe an on/off switch to quickly add this functionality

 ////////// INTRODUCING DECORATORS!////////////

 # Python has decorators that allow you to tack on extra functionality to an already existing function. 

 #they use an @ operator and are then placed on top of of an origional function.

 # Now you can easily add on extra functionality with a decorator:

 @some_decorator
 def simple_func():
	#Want to do more stuff!
	#Do simple stuff 
	#return something

# Tis idea is pretty abstract in practice with Python syntax, so we will fo through the steps manually building out a decorator ourselves, to show what @ operator is doing behind the scenes.

def func():
    return 1
func()
#out
1
#
func
#out
<function __main__.func()>

#

def hello():
    return "Hello!"

hello()
#out
'Hello!'
#

greet = hello

greet()
#out
'Hello!'
#

hello()
#out
'Hello!'
#

del hello

greet()
#out
'Hello!'
#

# So despite deleting hello function the greet still works like the function we wrote earlier.

# Its important to know that functions are object that can be passed to other objects.

# now lets show an example of passing in a function within another function or calling functions within another function.


def hello (name='Jose'):
    print('The hello() function has been executed!')

hello()
#out
#The hello() function has been executed!

def hello (name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello.'

hello()
#out
#The hello() function has been executed!

def hello (name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello.'
    print(greet())

hello()
#out
#The hello() function has been executed!
#	 This is the greet() func inside hello.

def hello (name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello.'
    def welcome():
        return '\t This is welcome() inside hello'
    print(greet())
    print(welcome())

hello()
#out
#The hello() function has been executed!
	 #This is the greet() func inside hello.
	 #This is welcome() inside hello
#

def hello (name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello.'
    def welcome():
        return '\t This is welcome() inside hello'
    print(greet())
    print(welcome())
    print('This is the end of the hello function')

hello()
#out
#The hello() function has been executed!
#	 This is the greet() func inside hello.
#	 This is welcome() inside hello
#This is the end of the hello function

#in this example the welcome and greet can only be called inside the hello function, and not outside. lets fix that

def hello (name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello.'
    def welcome():
        return '\t This is welcome() inside hello'
    print("I am going to return a function!")
    
    if name == 'Jose':
        return greet 
    else:return welcome

my_new_func = hello('Jose')
#output
# The hello() function has been executed!
# I am going to return a function!

my_new_func
#out
#<function __main__.hello.<locals>.greet()>
#
my_new_func()
#out
#'\t This is the greet() func inside hello.'
#
print(my_new_func())
#out
#	This is the greet() func inside hello.'

def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool

some_func = cool()
some_func()
#out
#'I am very cool!'

# Yo dawg I heard u like functions. so we put a function (as an arguement) inside a function so you can function whiile you function. 

def hello():
    return 'Hi Jose!'
def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())
    
other(hello)
#output
#Other code runs here!
#Hi Jose!

#now lets work with decorators.


def new_decorator(original_func):
    
    def wrap_func():
        
        print('some extra code, before original function')
        
        original_func()
        
        print('some extra code AFTER original function')
        
    return wrap_func #return is the last step for decorators
#################
def func_needs_decorator():
    print('I want to be decorated!!')
#################
decorated_func = new_decorator(func_needs_decorator)
#################
decorated_func()
#some extra code, before original function
#I want to be decorated!!
#some extra code AFTER original function

#BUT WAIT THERES A BETTER WAY


@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')
func_needs_decorator()

#output
#some extra code, before original function
#I want to be decorated!!
#some extra code AFTER original function



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							  GENERATORS 
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# We've learned how to create functions with def and the return statement

# generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off.

# this type of function is a generator in Python, allowing us to generate a sequence of values over time.

# the main difference in syntax will be the use of a yield statement. 

# when a generator function is compiled they become an object that supposrts an iteration protocol.

# that means when they are called in your code, they dont actually return a value and then exit. 

# instead generator functions will automatically suspend and resume their execution and state around the last point of value generation.

# The advantage is that instead of having to compute an entire series of values upfront, the generator computes one value waits until the next value is called for. 

# for example the range function doesn't produce a list in memory for all values from start to stop 

# it simply keeps track of the last number and the step size to provide a flow of numbers. 

# if the user did need the list, they have to transform the generator to a list with list(range(0,10))

# lets explore how to create our own generators!

~~~~~~~~ONLY WAY TO LEARN CODE IS TO CREATE CODE! 100K JOB~~~~~~~

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

create_cubes(10)
#output
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

#this is useful if you *need* the list, but somes you just want to print them.

for x in create_cubes(10):
	print(x)
#output
0
1
8
27
64
125
216
343
512
729
 
#To accomplish this we didnt need the whole list we just needed the next number, previous one, and whatever step to get to the next (every third number, exponent, mathmatical variable, what have you). so how can we get to this result but more efficiently?

def create_cubes(n):
    for x in range(n):
        yield x**3
#lot less code, lots more memory saved.
for x in create_cubes(10):
	print(x)
#output
0
1
8
27
64
125
216
343
512
729
#oh and this trick still works! 

#calling on create_cubes by itself will only produce a generator object. You can make it a list by doing the list() function, but then you are wasting memory. granted we're no longer working on windows xp, but it helps. 

#okay fibinocci sequence time!

# a+b = the sum of the last two numbers

# 1 1 2 3 5 8 13 21 etc

def gen_fibon(n):
    a = 1
    b = 1 
    for i in range(n):
        yield a
        a,b = b,a+b #reset 'a' to be equal to 'b'. 'b' will be equal to the sum of the previous 'a' and 'b'

for number in gen_fibon(10):
    print(number)
#output
1
1
2
3
5
8
13
21
34
55

# key to fully understanding generators is the 'next' function, and the 'iter' function. 

def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

#output
0
1
2

g = simple_gen()

g
#output
<generator object simple_gen at 0x0000
01BCA08AAED0>

print(next(g))
#out
0

print(next(g))
#out
1

print(next(g))
#out
2

#getting it? its looking at the next number based on the rules we put in the generator. if we go any further it will produce an error because we reached the end of our specified generated range. 

# iter function time

s = "hello"

for letter in s:
    print(letter)
#output
h
e 
l 
l 
o 

#if we try using next(s) we will get an error. iter() to the rescue!

s_iter = iter(s) #assign it
next(s_iter) # NOW you can use next!
#output
h 
next(s_iter) 
#output
e 
next(s_iter) 
l 
next(s_iter) 
#output 
l 
next(s_iter) 
#output
o 


yield, next(), iter(),

#sweet you got all this. take five. 100k job.

#so apparently we made it through the course and a lot of this is bonus material. three more sections and we can accelerate to the bigger leagues.

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
						ADVANCED PYTHON MODULES
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

~~~~~~~~~~~~~~~~~~~~~~~~COLLECTIONS MODULE~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~COUNTER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# BUILT in module that uses specialized that ives us more options that dictionaries, lists, sets, and tuples.

# counter is a dictionary subclass which helps us count hashable objects. elements are stored as dictionary keys, and the counts of the objects are stored as the value.

from collections import Counter

#Counter() with lists

1 = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

Counter(lst)
#output
Counter({1: 6, 2: 6, 3: 4, 12: 1, 21: 1, 32: 1, 223: 1})


\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Counter() with strings. 
\\\\\\\\\\\\\\\\\\\\\\\\\\\


Counter('aabsbsbsbhshhbbsbs')
#output
Counter({'a': 2, 'b': 7, 'h': 3, 's': 6})


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Counter with words in a sentence. 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

Counter(words)
#output#############
Counter({'How': 1,
         'does': 1,
         'each': 3,
         'in': 1,
         'many': 1,
         'sentence': 1,
         'show': 1,
         'this': 1,
         'times': 2,
         'up': 1,
         'word': 3})
#####################
#methods with Counter()
c = Counter(words)
c.most_common(2)
#output
[('each', 3), ('word', 3)]

||||||||||||||||||||||||||||||||||||||||||||||||
Common patterns when using the Counter() object
||||||||||||||||||||||||||||||||||||||||||||||||

sum(c.values()) #Total of all counts
c.clear() #reset all counts
list(c) #list unique elemenets
set(c) #convert to a set.
dict(c) #convert to a regular dictionary
c.items() #convert to a list of (elem,cnt(elements & count)) pairs
Counter(dict(list_of_pairs)) # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1] #n least common elements
c += Counter() #remove zero and negative counts

~~~~~~~~~~~~~~~~~~~~~~~~~~~defaultdict~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a dictionary like object that provides all methods provided by a dictionary but takes a first arguement (default_factory) as a default data type for the dictionary. Using defaultdict is faster than doing the same using dict.set_default method. 

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

from collections import defaultdict

d = {}
d['one']
#out
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-8-924453a5f45e> in <module>()
----> 1 d['one']

KeyError: 'one'
---------------------------------------------------------------------------

d = defaultdict(object)
d['one']
#output
<object at 0x1792df202e0>

for item in d:
	print(item)
#output
one

#we can also initialize with default values!

d = defaultdict(lambda: 0)
d['one']
#ouput
<object at 0x1792df202e0>

for item in d:
	print(item)
#output
one

# you can also initialize with default values:

d = defaultdict(lambda: 0)
d['one']
#output
0

d['two'] = 2

d
#output

#defaultdict(<function<lambda> at 0x000000042144AC8>, {'two':2,'one:':0})

#TL;DR defaultdict automatically assigns the VALUE of a dictionary's object 


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~OrderedDict~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# OrderedDict is a dictionary that rememebrs the order you put things in.

#Example heres a normal dictionary:

print('Normal dictionary:')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

#output
Normal dictionary:
a A
b B
c C
d D
e E
######################
#now here's an ordered dictionary:

from collections import OrderedDict

print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

#output
OrderedDict:
a A
b B
c C
d D
e E

\\\\\\\\\\\\\
  IMPORTANT!
\\\\\\\\\\\\\

#A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.

#in a normal dictionary:

print('Dictionaries are equal?')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)

#######################
 #ouput #ouput #ouput 
#######################
Dictionaries are equal?
True

#Now heres an ordered dictionary!

print('Dictionaries are equal?')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)

#######################
 #ouput #ouput #ouput 
#######################
Dictionaries are equal?
False

#even though both dictionaries have the same stuff in them for ordereddictionaries it isnt true unless they are in the same order


#HEADS UP THIS ALL LOOKS LIKE PYTHON 2 STUFF. LOOKS LIKE PYTHON 3 REMEDIES THIS BY DEFAULT BE CAREFUL USING THIS.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~namedtuple~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#normal tuples use number index to get it's stuff.

t = (12,13,14)

t[0]

#output
12

# namedtuples it assigns a name as well as the numerical index to help you know whats what in bigger code.

#each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. the arguements are the name of the new class and a string containing the names of the elements.

# basically think of namedtuples as a very quick way of creating a new object/class type with some attribute fields.

from collections import namedtuple


Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")


#get some rest. practice a few of those exercises and try to do a few class objects next time you open your laptop. 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
								datetime
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# Python has date and time modules to help with timestamps in code. Time Values are represented with the time class. We use hour minute second and microsecond attributes. We also got timezones. arguements to initialize a time instance are optional, but default of 0 is not likely what u want. 

#time

# we can creat a timestamp by specifying datime.time(hour,minute,second,microsecond)

import datetime
t= datetime.time(4, 20, 1)

#let show different time components

print(t)
print('hour :',t.hour)
print('minute :',t.minute)
print('second :',t.second)
print('microsecond :',t.microsecond)
print('tzinfo :',t.tzinfo)
#out
04:20:01
hour  : 4
minute: 20
second: 1
microsecond: 0
tzinfo: None

#Note: A time instance only holds values of time, and not a date associated with the time.

#We can also check the min and max values a time of day can have in the module:

print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
# Output
Earliest  : 00:00:00
Latest    : 23:59:59.999999
Resolution: 0:00:00.000001

# min and max class attributes reflect the valid range of times in a single day.


|||||||||||
|||DATES|||
|||||||||||

#datetime lets us work with dates timestamps. calander date values are represented by date class. attributes for year month and day. we make a date using the today() class method. 

today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

# output
# 2018-02-05
# ctime: Mon Feb  5 00:00:00 2018
# tuple: time.struct_time(tm_year=2018, tm_mon=2, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=36, tm_isdst=-1)
# ordinal: 736730
# Year : 2018
# Month: 2
# Day  : 5

# we can use min max attributes here too for the date values. 
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)
#output
# Earliest  : 0001-01-01
# Latest    : 9999-12-31
# Resolution: 1 day, 0:00:00

# we can also use replace() on an existing date to change it. like just changing the year and leaving everything else alone:

d1 = datetime.date(2015, 3, 11)
print('d1:', d1)

d2 = d1.replace(year=1990)
print('d2:', d2)

#output
# d1: 2015-03-11
# d2: 1990-03-11

#since programming does lots of math we can apply that to dates as well

d1-d2
#output
datetime.timedelta(9131)

#thats the differnece in days! use the timedelta method to further specify (day, months, weeks, hours for all I care.)

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							PYTHON DEBUGGER
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# pdb module implements an interactive debugging enviornment. 

# lets you pause, look at the variables, watch program execution step by step. 
_______________________________________________________________________
 IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT 
 ======================================================================
  This will be hard to show on notes. check video worst case. 

 #lets create an error on purpose. adding a list to an int

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)
result2 = y+x
print(result2)

#output gives us an error. lets play dumb (that parts easy :p ) 

# lets implement a set_trace() using the pbd module. It lets us pause the code  and check if anything is wrong.

import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)

# awesome we can check the code better this way. also press 'q' to quit debugging. https://docs.python.org/3/library/pdb.html Documentation link here. read it chungus. 



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							TIMING YOUR CODE
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# time = resources. this applies to coding. longer it takes = poor code. Find out WHERE it's taking forever will help you land that 100k job. Luckily pythons got your back. In both command line interface as well as a callable one. it avoids a number of common traps for measuring execution times. 

# timeit

import timeit

# we're going to use this to time various ways to create a string of numbers. 

# For loop
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
#out
0.21865416520477374

# List comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
#output
0.19484614421698643

# Map()
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
#output
0.15291817337139246


#okay we see time differences between these. map() (which in case you didnt remember helps you put a fuction to an iterable object like a list of numbers) being the clear winner. 

#now time for the special sauce %timeit (note this works specifically with jupyter notebooks.)

# iPython's %timit will try the same code lines several times and return the fastest.

Example:

%timeit "-".join(str(n) for n in range(100))
#output
# 20.4 µs ± 269 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%timeit "-".join([str(n) for n in range(100)])

#18.1 µs ± 56.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit "-".join(map(str, range(100)))

#14.4 µs ± 64.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# awesome map is still the fastest and it wasnt a fluke. #please note timeit will adjust the number of loops if things are taking too long. it will tell you if it does and if you're not seeing many loops that alone should be a clear indication you need to fix some code. 


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							REGULAR EXPRESSIONS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

Regular Expressions # are text-matching patterns described in a formal syntax. AKA regex, regexp when talking to other coders. regex can include a varietey of rules, from finding repeition, to text-matching, and much more. as youadvance in python you'll see that al ot of you parsing problems can be solved with regex. (COMMON INTERVIEW QUESTION. STUDY THIS.)

#we will be using the re module with python for this. 

#one of the most common uses for re module is for finding patterns in text. Lets do a quick example of using the search method in the re module to find some text: 

import re 

# list of patterns to search for
patterns = ['term1', 'term2']

#text to parse

text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
	print('Searching for "%s" in:\n "%s"\n' %(pattern,text))

	#check for match
	if re.search(pattern,text):
		print('Match was found. \n')
	else:
		print('no match was found. \n')
#output
#Searching for "term1" in:
# "This is a string with term1, but it does not have the other term."

#Match was found. 

#Searching for "term2" in:
# "This is a string with term1, but it does not have the other term."

#No Match was found.
-------------------------------------------------------------------------

# now we see that re.search() will take the pattern, scan the text and return a match object. If nothing is found nothing returned. Check below:

# List of patterns to search for
pattern = 'term1'

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

match = re.search(pattern,text)

type(match)
#output
_sre.SRE_Match

#the MATCH onject returned by the search() method is more than just a Boolean or None it contains information about the match, including the original input string, the regular expression that was used and the location of the match. Lets see the methods we can use on the match object:

#show the start of the match
_sre.start() 
#output
22

#show end
math.end()
#output 
27

 ~~~~~~~~~SPLIT WITH REGULAR EXPRESSIONS
# lets see how we can split with the re syntax. This should look similar to how you used the split() method with strings.

# Term to split on
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Split the phrase
re.split(split_term,phrase)
#out
['What is the domain name of someone with the email: hello', 'gmail.com']

#Note how re.split() returns a list with the term to split on removed and the terms in the list are a split up version of the string. Create a couple of more examples for yourself to make sure you understand!

#done and done. 

~~~~~~~~~~~FINDING ALL INSTANCES OF A PATTERN.

# we can use the re.findall() to find all the instances of a pattern in a string. Example

#returns a list of all matches. 

re.findall('match',' this phrase has match in the middle')
#output
['match']

~~~~~~~~~~~~re Pattern Syntax 

#this will be the bulk of the lecture on using re with python.

ARE YOU LISTENING???? THIS IS IMPORTANT RIGHT HERE.

# regex supports a huge varietey of patterns beyond just simply finding where a single string occured. 

#We can use METACATCHERS along with with re to find specific types of patterns

# since we will be testing multiple re syntax forms, lets create a function that will print out results given a list of various regular expressions and a phrase to parse. 

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')

||||||||||||||||||||||||
~~~~repeition syntax~~~~
||||||||||||||||||||||||

#there are five ways to express repeition in a pattern:

#1. repeition followed by a meta-character * is repeated zero or more times. 

# 2. Replace the  * with + and the pattern must appear at least once. 

# 3. using ? means the pattern appears zero or one time. 

# 4. For a specific number of occurances, use {m} after the pattern, where ''n'' is the maximum. Leaving out n {m,} means tha value appears at least M times with no maximum. 

#Now we will see an example of each of these using our multi_re_find fuction:

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

#OUTPUT (THIS IS A BIG ONE)

#Searching the phrase using the re check: 'sd*'
#['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 'sdddd']


#Searching the phrase using the re check: 'sd+'
#['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sdddd']


#Searching the phrase using the re check: 'sd?'
#['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 'sd']


#Searching the phrase using the re check: 'sd{3}'
#['sddd', 'sddd', 'sddd', 'sddd']


#Searching the phrase using the re check: 'sd{2,3}'
#['sddd', 'sddd', 'sddd', 'sddd']


~~~~~~~~CHARACTER SETS

# character sets are used when you wish to match any one of a group of characters at a point in the input. Brackets are used to construct character set inputs. For example: the input [ab] searches for occurances of either a or b. lets see some examples. 

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)

#output
#Searching the phrase using the re check: '[sd]'
#['s', 'd', 's', 'd', 's', 's', 's', 'd', 'd', 'd', 's', 'd', 'd', 'd', 's', 'd', 'd', 'd', 'd', 's', 'd', 's', 'd', 's', 's', 's', 's', 's', 's', 'd', 'd', 'd', 'd']


#Searching the phrase using the re check: 's[sd]+'
#['sdsd', 'sssddd', 'sdddsddd', 'sds', 'sssss', 'sdddd']
----------------------------------------------------------------------
#It makes sense that the first input [sd] returns every instance of s or d. Also, the second input s[sd]+ returns any full strings that begin with an s and continue with s or d characters until another character is reached.

~~~~~~~~~~~~EXCLUSION

# we can use  ^ to exclude terms by incorporating it into the bracket syntax notation. For example: [^...] will match any single character NOT in the brackets. lets see some examples:

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

#Use [^!.? ] to check for matches that are not a !,.,?, or space. Add a + to check that the match appears at least once. This basically translates into finding the words.
re.findall('[^!.? ]+',test_phrase)

#OUTPUT (LONG LIST)
['This',
 'is',
 'a',
 'string',
 'But',
 'it',
 'has',
 'punctuation',
 'How',
 'can',
 'we',
 'remove',
 'it']
---------------------
~~~~~~~~~~~~CHARACTER RANGES 

#As character sets grow larger, typing every character that should (or should not) match could become very tedious. A more compact format using character ranges lets you define a character set to include all of the contiguous characters between a start and stop point. The format used is [start-end].

#common cases are to search for a specific range of letters in the alphabet. For instance , [a-f] for letters 'a' through 'f' 

# EXMAPLES:

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)

#Searching the phrase using the re check: '[a-z]+'
#['his', 'is', 'an', 'example', 'sentence', 'ets', 'see', 'if', 'we', 'can', 'find', 'some', 'letters']


#Searching the phrase using the re check: '[A-Z]+'
#['T', 'L']


#Searching the phrase using the re check: '[a-zA-Z]+'
#['This', 'is', 'an', 'example', 'sentence', 'Lets', 'see', 'if', 'we', 'can', 'find', 'some', 'letters']


#Searching the phrase using the re check: '[A-Z][a-z]+'
#['This', 'Lets']


~~~~~~~~~~~~~ESCAPE CODES 

#You can use special escape codes to find specific types of patterns in your data, such as digits, non-digits, whitespace, and more. For example:

# CODE | MEANING
#______|_________________
#\d    |a digit
#\D    |a non digit
#\s    |whitespace (tab, space,newline,etc)
#\S    |non-whitespace
#\w    |alphanumeric
#\W    |non-alphanumeric

#Escapes are indicated by prefixing the character with a backslash \. Unfortunately, a backslash must itself be escaped in normal Python strings, and that results in expressions that are difficult to read. Using raw strings, created by prefixing the literal value with r, eliminates this problem and maintains readability.

HEY LISTEN UP! HEY LISTEN UP! HEY LISTEN UP! HEY LISTEN UP! HEY LISTEN UP! 

#Personally, I think this use of r to escape a backslash is probably one of the things that block someone who is not familiar with regex in Python from being able to read regex code at first. Hopefully after seeing these examples this syntax will become clear.

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)
#output

#Searching the phrase using the re check: '\\d+'
#['1233']


#Searching the phrase using the re check: '\\D+'
#['This is a string with some numbers ', ' and a symbol #hashtag']


#Searching the phrase using the re check: '\\s+'
#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


#Searching the phrase using the re check: '\\S+'
#['This', 'is', 'a', 'string', 'with', 'some', 'numbers', '1233', 'and', 'a', 'symbol', '#hashtag']


#Searching the phrase using the re check: '\\w+'
#['This', 'is', 'a', 'string', 'with', 'some', 'numbers', '1233', 'and', 'a', 'symbol', 'hashtag']


#Searching the phrase using the re check: '\\W+'
#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']


\\\\\\\\\\\\\\TO SUM UP 
# This is important stuff

http://www.tutorialspoint.com/python/python_reg_expressions.htm

Study this ^ ^ ^ ^ ^ ^


https://docs.python.org/3/library/re.html#regular-expression-syntax

This too ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 


#okay rest your brain. watch the videos in a bit. 



\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
							STRING I/O 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# We have opened files that exist outside of python, and streamed their contents into an in-memory file object. 

# We can also create in-memory file-like objects within your program that Python treats the same way. 

# Text data is stored in a StringIO object, while binary data would be stored in a BytesIO object. 

# This object can then be used as input or output to most functions that would expect a standard file object.

import io

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)

###  Now we have an object f that we will be able to treat just like a file. For example:


f.read()
#output
'This is just a normal string.'


### we can also write to it.

f.write(' Second line written to file like object')
#output 
40
# Reset cursor just like you would a file
f.seek(0)
#output
0
# Read again
f.read()
#output
'This is just a normal string. Second line written to file like object'


# Close the object when contents are no longer needed
f.close()

# Great! Now you've seen how we can use StringIO to turn normal strings into in-memory file objects in our code. This kind of action has various use cases, especially in web scraping cases where you want to read some string you scraped as a file.

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							ADVANCED NUMBERS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#Convert to hexidecimal

hex()

#convert to binary
bin()

#Exponents 
pow() == x^y or (x^y)%z

#Absolute value

abs() #returns everything positive. 

#Round a number to a given precision decimal digit. DOES NOT CONVERT INTEGERS TO FLOATS

round(3,2)
#output
3

round(395,-2)
#out
400

round(3.1415926535,2)
#out
3.14

#Remember code is made of math chances are the language will have quite a few options for you dealing with the numbers. 


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							ADVANCED STRINGS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#lets start with a regular string

s = 'hello world'

#you better know that one. now lets change the casing. 

s.capitalize()
#output
'Hello World'

s.upper()
#out
'HELLO WORLD'

#Not so loud!
#fine then

s.lower()
#out
'hello world'

#remember these things only MODIFY the existing original string. Not change it. To do that we gotta reassign. 

s = s.upper()
s
#out
'HELLO WORLD'

s= s.lower()
s
#out
'hello world'

~~LOCATION AND COUNTING 
#lets count how many times o is in the variable s:
s.count('o')
#out
2
#cool lets get the index of the first time we see o:
s.find('o')
#out
4

~~FORMATTING 

#lets get weird. say after a night of drinking we decide to put our string centered in between a string of a certain length. Our glorious developers got our backs!

s.center(20,'z')
#out
'zzzzhello worldzzzzz'

#and .explandtabs() will expand tab notations \t into spaces. Don't know why we need this, but apparently it was on the to-do list! 

'hello\thi'.expandtabs()
#out
'hello    hi'

~~~IS CHECK METHODS

#These various methods below check if the string is some case. Let's explore them:

s = 'hello'

#isalnum() will return True if all characters in s are alphanumeric
s.isalnum()
#out
True

#islower() will return True if all cased characters in s are lowercase and there is at least one cased character in s, False otherwise.
s.islower()
#out
True

#isspace() will return True if all characters in s are whitespace.
s.isspace()
#out
False

#istitle() will return True if s is a title cased string and there is at least one character in s, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. It returns False otherwise.
s.istitle()
#out
False

#isupper() will return True if all cased characters in s are uppercase and there is at least one cased character in s, False otherwise.
s.isupper
#out
False

#Another method is endswith() which is essentially the same as a boolean check on s[-1]
s.endswith('o')
#out
True

~~~~~Built-in Reg. Expressions
#Strings have some built-in methods that can resemble regular expression operations. We can use split() to split the string at a certain element and return a list of the results. We can use partition() to return a tuple that includes the first occurrence of the separator sandwiched between the first half and the end half.

s.split('e')
#out
['h','llo']

s.partition('l')
#out
('he', 'l', 'lo')




|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							ADVANCED SETS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/


# In this lecture we will learn about the various methods for sets that you may not have seen yet. We'll go over the basic ones you already know and then dive a little deeper.

s=set() 


~~~~Add
#add elements to a set. Remember, a set won't duplicate elements; it will only present them once (that's why it's called a set!)

s.add(1)
s.add(2)
s
#out
{1, 2}

~~~clear

#removes all elemenets from a set

s.clear()
s
#out
set()

~~~copy 

#returns a copy of a set. note it is a copy, so changes to the original dont effect the copy

s = {1,2,3}
sc = s.copy()
sc
#out
{1,2,3}

s
#out
{1,2,3}

s.add(4)

s
#out
{1,2,3,4}

sc
#out
{1,2,3}

~~~~~~~~difference 
#difference of two or more sets Syntax is

set1.deffiernce(set2)

#example
s.difference(sc)
#out
{4}

~~~~~difference_update
#like the reverse of differnece. it returns set 1 after removing the elements in set 2. syntax is 

set1.difference_update(set2)

s1={1,2,3}

s2 = {1,4,5}

s1.difference_update(s2)

s1
#output
{2,3}


~~~discard

#removes an element froma a set if it is a member. if the element is not a member, do nothing. 

s
#out
{1,2,3,4}

s.discard(2)
s
#out
{1,3,4}

~~~~intersection and intersection_update

#returns intersection of two or more sets as a new set (elements that are common to all of the sets)
s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection(s2)
#output
{1,2}

s1
#out
{1,2,3}


# intersection_update will update a set with the intersection of itself and another
s1.intersection_update(s2)
s1 
#out
{1,2}


~~~isdisjoint
#will return true if two sets have a null intersection. 

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
s1.isdisjoint(s2)
False

~~issubset
#This method reports whether another set contains this set.

s1
#out
{1,2}
s2
#out
{1,2,4}

s1.issubset(s2)
#out
True

~~issuperset
#reports whether this set contains another set.

s2.issuperset(s1)
#out
True

s1.issuperset(s2)
#out
False

~~~symmetric_difference and symmetric_update

#Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)

s1
#out
{1, 2}


s2
#Out
{1, 2, 4}

s1.symmetric_difference(s2)
#out
{4}


~~Union
#Returns the union of two sets (i.e. all elements that are in either set.)

s1.uniion.(s2)
s1
#out
{1,2,4}

~~Update
#Update a set with the union of itself and others.

s1.update(s2)
s1
#out
{1,2,4}


#Great! You should now have a complete awareness of all the methods available to you for a set object type. This data structure is extremely useful and is underutilized by beginners, so try to keep it in mind!






|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
						ADVANCED DICTIONARIES
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#Unlike some of the other Data Structures we've worked with, most of the really useful methods available to us in Dictionaries have already been explored throughout this course. Here we will touch on just a few more for good measure:

~~~~Dictionary Comprehensions

#Just like List Comprehensions, Dictionary Data Types also support their own version of comprehension for quick creation. It is not as commonly used as List Comprehensions, but the syntax is:

{x:x**2 for x in range(10)}
#output
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#not often used as structring key names as not usually based off the values.

{k:v**2 for k,v in zip(['a','b'],range(2))}
#output
{'a': 0, 'b': 1}

~~~Iteration over keys, values, and items

#Dictionaries can be iterated over using the keys(), values() and items() methods. For example:

d = {'k1':1,'k2':2}

for k in d.keys():
    print(k)
#out
k1
k2
for v in d.values():
    print(v)
#out
1
2
for item in d.items():
    print(item)
#out
('k1', 1)
('k2', 2)

~~~Viewing keys, values and items

#By themselves the keys(), values() and items() methods return a dictionary view object. This is not a separate list of items. Instead, the view is always tied to the original dictionary.

key_view = d.keys()

key_view
#output
dict_keys(['k1', 'k2'])

-------------------------

d['k3'] = 3

d
#output
{'k1': 1, 'k2': 2, 'k3': 3}

--------------------

key_view
#output
dict_keys(['k1', 'k2', 'k3'])



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
							ADVANCED LISTS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#In this series of lectures we will be diving a little deeper into all the methods available in a list object. These aren't officially "advanced" features, just methods that you wouldn't typically encounter without some additional exploring. It's pretty likely that you've already encountered some of these yourself!

#Let's begin!

list1 = [1,2,3]


~~~append
# You will definitely have used this method by now, which merely appends an element to the end of a list:

list1.append(4)

list1
#output
[1, 2, 3, 4]

~~~~count 

#We discussed this during the methods lectures, but here it is again. count() takes in an element and returns the number of times it occurs in your list:

list1.count(10)
#output
0
------------------------
list1.count(2)
#output
1


~~~~~~~~~~~~extend

#Many times people find the difference between extend and append to be unclear. So note:
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
append: appends whole object at end:
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

x = [1, 2, 3]
x.append([4, 5])
print(x)
#out
[1, 2, 3, [4, 5]]

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||extend: extends list by appending elements from the iterable:|||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
x = [1, 2, 3]
x.extend([4, 5])
print(x)
#output
[1, 2, 3, 4, 5]

# Note how extend() appends each element from the passed-in list. That is the key difference.

~~~~~~~INDEX 

# index() will return the index of whatever element is placed as an argument. Note: If the the element is not in the list an error is raised.

list1.index(2)
#output
1

list1.index(12)
#output
VALUE ERROR! 12 IS NOT IN LIST

~~~~~~~~INSERT 

# insert() takes in two arguments: insert(index,object) This method places the object at the index supplied. For example:

list1
#output
[1, 2, 3, 4]




# Place a letter at the index 2
list1.insert(2,'inserted')

list1
# out
[1, 2, 'inserted', 3, 4]

~~~~~~~~pop

#You most likely have already seen pop(), which allows us to "pop" off the last element of a list. However, by passing an index position you can remove and return a specific element.

ele = list1.pop(1)  # pop the second element
list1
#output
[1, 'inserted', 3, 4]


ele
#output
2

~~~~~~~remove
#The remove() method removes the first occurrence of a value. For example:

list
#output
[1, 'inserted', 3, 4]

list1.remove('inserted')
list1
#output
[1, 3, 4]


list2 = [1,2,3,4,3]
list2.remove(3)
list2
#output
[1, 2, 4, 3]

~~~~~~~~~~~reverse
#As you might have guessed, reverse() reverses a list. Note this occurs in place! Meaning it affects your list permanently.

list2.reverse()
list2
#outut
[3, 4, 2, 1]


~~~~~~~~~~~~~~sort
# The sort() method will sort your list in place:

list2
#output
[3, 4, 2, 1]


list2.sort()
list2
#output
[1, 2, 3, 4]

#The sort() method takes an optional argument for reverse sorting. Note this is different than simply reversing the order of items.

list2.sort(reverse=True)
list2
#output
[4, 3, 2, 1]


\\\\\\\\\\\\\Be Careful With Assignment!


#A common programming mistake is to assume you can assign a modified list to a new variable. While this typically works with immutable objects like strings and tuples:

x = 'hello world'
y = x.upper()
print(y)
#ouput
HELLO WORLD

#This will NOT work the same way with lists:

x = [1,2,3]
y = x.append(4)
print(y)
#output
None

#What happened? In this case, since list methods like append() affect the list in-place, the operation returns a None value. This is what was passed to y*. In order to retain *x you would have to assign a copy of x** to **y, and then modify y:

x = [1,2,3]
y = x.copy()
y.append(4)
print(x)
#output
[1, 2, 3]
print(y)
#output
[1, 2, 3, 4]


#Great! You should now have an understanding of all the methods available for a list in Python!




|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				With Statement Context Managers
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# When you open a file using f = open('test.txt'), the file stays open until you specifically call  f.close(). Should an exception be raised while working with the file, it remains open. This can lead to vulnerabilities in your code, and inefficient use of resources.

# A context manager handles the opening and closing of resources, and provides a built-in try/finally block should any exceptions occur.

# The best way to demonstrate this is with an example.
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
~~~~~Standard open() procedure, with a raised exception:
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
p = open('oops.txt','a')
p.readlines()
p.close()

#output
--->2 p.readlines()
UnsupportedOperation: not readable

#Let's see if we can modify our file:

p.write('add more text')
#out
13

#Ouch! I may not have wanted to do that until I traced the exception! Unfortunately, the exception prevented the last line, p.close() from running. Let's close the file manually:

p.close()

~~~~~~~~~~~~PROTECT FILE WITH TRY/EXCEPT/FINALLY 

#A common workaround is to insert a try/except/finally clause to close the file whenever an exception is raised:

p = open('oops.txt','a')
try:
    p.readlines()
except:
    print('An exception was raised!')
finally:
    p.close()
#out
An exception was raised!

# lets see if we can modify our file this time.

p.write('add more text')
#output
ValueError: I/O operation on closed file.


#excellent the file is still safe.

~~~~~~~~~~SAVE STEPS WITH with

# Now we'll employ our context manager. The syntax follows with [resource] as [target]: do something

with open('oops.txt','a') as p:
    p.readlines()
# output
UnsupportedOperation: not readable

# Can we modify the file? 

p.write('add more text')
#output
ValueError: I/O operation on closed file.


# Great! With just one line of code we've handled opening the file, enclosing our code in a try/finally block, and closing our file all at the same time.

# Now you should have a basic understanding of context managers.



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
				ADVANCED OBJECT ORIENTED PROGRAMMING
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# In the regular section on Object Oriented Programming (OOP) we covered:

# Using the class keyword to define object classes
# Creating class attributes
# Creating class methods
# Inheritance - where derived classes can inherit attributes and methods from a base class
# Polymorphism - where different object classes that share the same method can be called from the same place
# Special Methods for classes like __init__, __str__, __len__ and __del__

# In this section we'll dive deeper into:

# Multiple Inheritance
# The self keyword
# Method Resolution Order (MRO)
# Python's built-in super() function

~~~~Inheritance Revisited

# Recall that with Inheritance, one or more derived classes can inherit attributes and methods from a base class. This reduces duplication, and means that any changes made to the base class will automatically translate to derived classes. As a review:


class Animal:
	def __init__ (self, name): # Constructor of the class
		self.name = name

	def speak(self): # Abstract method, defined by convention only
		raise NotImplementedError("subclass must implement abstract method")

class Dog(Animal):
	def speak(self):
		return self.name+' says Woof!'

class Cat(Animal):
	def speak(self):
		return self.name+' says Meow!'
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak)
print(isis.speak)
#output
Fido says Woof!
Isis says Meow!



# In this example, the derived classes did not need their own __init__ methods because the base class __init__ gets called automatically. However, if you do define an __init__ in the derived class, this will override the base:

class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        self.name = name
        self.legs = legs
        self.hibernate = hibernate


# This is inefficient - why inherit from Animal if we can't use its constructor? The answer is to call the Animal __init__ inside our own __init__.



class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        Animal.__init__(self,name,legs) #THIS RIGHT HERE! ! ! ! ! ! ! ! ! ! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.hibernate = hibernate
        
yogi = Bear('Yogi')
print(yogi.name)
print(yogi.legs)
print(yogi.hibernate)
#output
yogi
4
yes


~~~~MULTIPLE INHERITANCE 

# Sometimes it makes sense for a derived class to inherit qualities from two or more base classes. Python allows for this with multiple inheritance.

class Car:
    def __init__(self,wheels=4):
        self.wheels = wheels
        # We'll say that all cars, no matter their engine, have four wheels by default.

class Gasoline(Car):
    def __init__(self,engine='Gasoline',tank_cap=20):
        Car.__init__(self)
        self.engine = engine
        self.tank_cap = tank_cap # represents fuel tank capacity in gallons
        self.tank = 0
        
    def refuel(self):
        self.tank = self.tank_cap
        
    
class Electric(Car):
    def __init__(self,engine='Electric',kWh_cap=60):
        Car.__init__(self)
        self.engine = engine
        self.kWh_cap = kWh_cap # represents battery capacity in kilowatt-hours
        self.kWh = 0
    
    def recharge(self):
        self.kWh = self.kWh_cap




#So what happens if we have an object that shares properties of both Gasolines and Electrics? We can create a derived class that inherits from both!

class Hybrid(Gasoline, Electric):
    def __init__(self,engine='Hybrid',tank_cap=11,kWh_cap=5):
        Gasoline.__init__(self,engine,tank_cap)
        Electric.__init__(self,engine,kWh_cap)
        
        
prius = Hybrid()
print(prius.tank)
print(prius.kWh)
#output
0
0

prius.recharge()
print(prius.kWh)
#output
5


~~~~~~Why do we use self?

# We've seen the word "self" show up in almost every example. What's the deal? The answer is, Python uses self to find the right set of attributes and methods to apply to an object. When we say:

prius.recharge()

# What really happens is that Python first looks up the class belonging to prius (Hybrid), and then passes prius to the Hybrid.recharge() method.

# It's the same as running:

Hybrid.recharge(prius)

# but shorter and more intuitive!

~~~~~~~~~ Method Resolution Order (MRO)
# Things get complicated when you have several base classes and levels of inheritance. This is resolved using Method Resolution Order - a formal plan that Python follows when running object methods.

# To illustrate, if classes B and C each derive from A, and class D derives from both B and C, which class is "first in line" when a method is called on D?
Consider the following:

class A:
    num = 4
    
class B(A):
    pass

class C(A):
    num = 5
    
class D(B,C):
    pass

#Schematically the relationship looks like this:
     A
   num=4
  /     \
 /       \
 B       C
pass   num=5
#\       /
 #\     /
     D
    pass

#Here num is a class attribute belonging to all four classes. So what happens if we call D.num?

D.num
#output
5

# You would think that D.num would follow B up to A and return 4. Instead, Python obeys the first method in the chain that defines num. The order followed is [D, B, C, A, object] where object is Python's base object class.

# In our example, the first class to define and/or override a previously defined num is C.


~~~~~~~~~~~~super()


super()

# Python's built-in super() function provides a shortcut for calling base classes, because it automatically follows Method Resolution Order.

# In its simplest form with single inheritance, super() can be used in place of the base class name :

class MyBaseClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
class MyDerivedClass(MyBaseClass):
    def __init__(self,x,y,z):
        super().__init__(x,y) ## < < < < - - - R I G H T - H E R E < < <
        self.z = z



# Note that we don't pass self to super().__init__() as super() handles this automatically.

# In a more dynamic form, with multiple inheritance like the "diamond diagram" shown above, super() can be used to properly manage method definitions:


class A:
    def truth(self):
        return 'All numbers are even'
    
class B(A):
    pass

class C(A):
    def truth(self):
        return 'Some numbers are even'

class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()
            
d = D()
d.truth(6)
#OUTPUT
'All numbers are even'

d.truth(5) 
#output
'Some numbers are even'

# In the above example, if we pass an even number to d.truth(), we'll believe the A version of .truth() and run with it. Otherwise, follow the MRO and return the more general case.


## super() IS EXTREMELY USEFUL FOR CLASSES! USE THEM. STUDY THEM. MEANTIME TAKE 5. 



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
						INTRODUCTION TO GUIS
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

					PYTHON GUIS WITH IPYWIDGETS

# We can build simple GUIs with jupyter!

# Explore how to build out these interactive elemenets.

# Keep the lecture notebooks handy, there is a lot of reference code and info there for you. 

#Be kind to your future self. 

# In this lecture we will begin to learn about creating dashboard-type GUI with iPython widgets!

# The interact function (ipywidgets.interact) automatically creates user interface (UI) controls for exploring code and data interactively. It is the easiest way to get started using IPython's widgets.



# DONT GET LAZY. YOU ARE ONLYA MONTH IN THIS BE KIND TO YOUR FUTURE SELF. 

# Start with some imports!

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


~~~~~~~~~~~Basic interact

# At the most basic level, interact auto-generates UI controls for function arguments, and then calls the function with those arguments when you manipulate the controls interactively. To use interact, you need to define a function that you want to explore. Here is a function that prints its only argument x.


# Very basic function
def f(x):
    return x

#When you pass this function as the first argument to interact along with an integer keyword argument (x=10), a slider is generated and bound to the function parameter. Note that the semicolon here just prevents an out cell from showing up.

# Generate a slider to interact with
interact(f, x=10,);
 


#When you move the slider, the function is called, which prints the current value of x.

# If you pass True or False, interact will generate a check-box:

# Booleans generate check-boxes
interact(f, x=True);


#If you pass a string, interact will generate a text area.


# Strings generate text areas
interact(f, x='Hi there!');


# interact can also be used as a decorator. This allows you to define a function and interact with it in a single shot. As this example shows, interact also works with functions that have multiple arguments.

# Using a decorator!
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)


~~~~~~~~~~~Fixing arguments using fixed

# There are times when you may want to explore a function using interact, but fix one or more of its arguments to specific values. This can be accomplished by wrapping values with the fixed function.


# Again, a simple function
def h(p, q):
    return (p, q)

# When we call interact, we pass fixed(20) for q to hold it fixed at a value of 20.


interact(h, p=5, q=fixed(20));



#Notice that a slider is only produced for p as the value of q is fixed.
~~~~~~~Widget abbreviations

#When you pass an integer-valued keyword argument of 10 (x=10) to interact, it generates an integer-valued slider control with a range of [-10,+3\times10]. In this case, 10 is an abbreviation for an actual slider widget:

IntSlider(min=-10,max=30,step=1,value=10)

#In fact, we can get the same result if we pass this IntSlider as the keyword argument for x:
_____________________________________________________________________

# Can call the IntSlider to get more specific
interact(f, x=widgets.IntSlider(min=-10,max=30,step=1,value=10));



#This examples clarifies how interact processes its keyword arguments:

#  1.)  If the keyword argument is a Widget instance with a value attribute, that widget is used. Any widget with a value attribute can be used, even custom ones.
#  2.)  Otherwise, the value is treated as a widget abbreviation that is converted to a widget before it is used.

#google for your widgets. 


# Note that a dropdown is used if a list or a dict is given (signifying discrete choices), and a slider is used if a tuple is given (signifying a range).

#You have seen how the checkbox and text area widgets work above. Here, more details about the different abbreviations for sliders and drop-downs are given.

# If a 2-tuple of integers is passed (min,max), an integer-valued slider is produced with those minimum and maximum values (inclusively). In this case, the default step size of 1 is used.

# Min,Max slider with Tuples
interact(f, x=(0,4));



#If a 3-tuple of integers is passed (min,max,step), the step size can also be set.


# (min, max, step)
interact(f, x=(0,8,2));


# A float-valued slider is produced if the elements of the tuples are floats. Here the minimum is 0.0, the maximum is 10.0 and step size is 0.1 (the default).

interact(f, x=(0.0,10.0));


# The step size can be changed by passing a third element in the tuple.

interact(f, x=(0.0,10.0,0.01));


#For both integer and float-valued sliders, you can pick the initial value of the widget by passing a default keyword argument to the underlying Python function. Here we set the initial value of a float slider to 5.5.

@interact(x=(0.0,20.0,0.5))
def h(x=5.5):
    return x

#Dropdown menus are constructed by passing a list of strings. In this case, the strings are both used as the names in the drop-down menu UI and passed to the underlying Python function.

interact(f, x=['apples','oranges']);

#If you want a drop-down menu that passes non-string values to the Python function, you can pass a dictionary. The keys in the dictionary are used for the names in the drop-down menu UI and the values are the arguments that are passed to the underlying Python function.

interact(f, x={'one': 10, 'two': 20});

#Failed to display Jupyter Widget of type interactive.


~~~~Using function annotations with interact

#You can also specify widget abbreviations using function annotations.

#Define a function with a checkbox widget abbreviation for the argument x.




def f(x:True):  # Python 3 only
    return x

# Then, because the widget abbreviation has already been defined, you can call interact with a single argument.


interact(f);

~~~~~~~interactive

# In addition to interact, IPython provides another function, interactive, that is useful when you want to reuse the widgets that are produced or access the data that is bound to the UI controls.

# Note that unlike interact, the return value of the function will not be displayed automatically, but you can display a value inside the function with IPython.display.display.

# Here is a function that returns the sum of its two arguments and displays them. The display line may be omitted if you don’t want to show the result of the function.

from IPython.display import display

def f(a, b):
    display(a + b)
    return a+b

# Unlike interact, interactive returns a Widget instance rather than immediately displaying the widget.

w = interactive(f, a=10, b=20)

# The widget is an interactive, a subclass of VBox, which is a container for other widgets.

type(w)
#out
ipywidgets.widgets.interaction.interactive

# The children of the interactive are two integer-valued sliders and an output widget, produced by the widget abbreviations above.

w.children
#output
(IntSlider(value=10, description='a', max=30, min=-10),
 IntSlider(value=20, description='b', max=60, min=-20),
 Output())




#To actually display the widgets, you can use IPython's display function.

display(w)



# At this point, the UI controls work just like they would if interact had been used. You can manipulate them interactively and the function will be called. However, the widget instance returned by interactive also give you access to the current keyword arguments and return value of the underlying Python function.

# Here are the current keyword arguments. If you rerun this cell after manipulating the sliders, the values will have changed.


w.kwargs
#output
{'a': 10, 'b': 20}

#Here is the current return value of the function.
w.result
#output
30

#### okay so we finished the lesson today. and honestly future me this is looking like its nboth hard to really write down for notes and just syntax lessons so this stuff can be googled later. w'ell just foollow along and go back to notes once we start ML. 

#Past you here. Hopefully the codes to all the exercises confusing you here will help you later. Lets eark that 100k 


#Starting with the braces exercise. We learned about stack that day. 
def validBraces(string):
    #dictionary of the opened and closed brackets.
    braces = {"(":")","[":"]","{":"}"} 
    #empty list to fill up
    stack = []
    for character in string: #now we for loop
        if character in braces:#if theres a opening bracket in the string...
            stack.append(character) #add it to the list
        else:
            # if the stack is empty or the last item on the stack 
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False #it's wrong
                

                braces[stack.pop()] #this is clever

                #just like subscripting a list with an index, we can grab a value from a dictionary with a key using the same syntax
                >>> d = {'foo':1, 'bar':2}
                >>> d['foo']
           #out: 1
                >>> d['bar']
           #out: 2
# the pop is removing the last item on the list, then checking it to see if it works. 
------------------------------------------------------------------------------
#say you were given the string '([])'

#you'll first see the open parenthesis, and add it to your stack, as that opening parenthesis will need to be closed at some point

#now we see the open square bracket, we also add this to our stack because that also needs to be closed at some point, but it has to be closed BEFORE the parenthesis is

# so our stack currently looks like this: ['(', '[']

# now we see the closing square bracket, and since this is not an opening brace, it's not in our dictionary
# so now that we know that this must be a closing brace, we need to make sure it matches up with the last opening brace we saw

# so we pop the stack, giving us our opening square bracket

# and we pass this to our dictionary, so find out what the valid closing brace for this character is, which is a closing square bracket

# now we check to see if the bracket we got back (]) is different from the current bracket we're looking at (also ])

# since they're the same, we don't return False, because this string is still valid so far

# so now our stack looks like this: ['(']
# now we reach the last character in our string, which is the ')'
# again, this isn't in our dictionary, so we know it's a closing brace of some kind
# so we pop the stack, giving us (, and we pass it to our dictionary to get it's corresponding closing brace which is )
# then we again compare, they are also the same, so we don't return false, and now we've finished reading the string, so we know the string has valid braces


def digital_root(num):
    while num >=10:
        num = sum(map(int, str(num))) # maps rule. Function followed by iterable. can be built in function.
    return num


_____________________________________________________________________

def tribonacci(signature, n):
    trib = []
    a,b,c = signature
    for i in range(n):
        trib.append(a)
        a,b,c = b,c,a+b+c 
        # a, b, and c equals previous b and c and a PLUS b Plus c
    return trib
    
_____________________________________________________________________

def array_dif(a,b):
    for x in b:
        while x in a:
            a.remove(x)
            print(a)
    return a

#better version
def array_diff(a, b):
    return [x for x in a if x not in b]
_____________________________________________________________________
#unique number in arrangement 

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
    #this programmer was clever. used the counter function. you were focused on the for loop and possibly utilizing the mean.  


_____________________________________________________________________

#STUDY THIS RELIGIOUSLY 

import numpy as np

def pack_bagpack(scores, weights, capacity):
    m = np.zeros([len(scores), capacity + 1])

    for i in range(len(scores)):
        for j in range(capacity + 1):
            if weights[i] > j:
                m[i,j] = m[i-1,j]
            else:
                m[i,j] = max(m[i-1,j - weights[i]] + scores[i], m[i-1,j])
                
    return np.max(m)

#another one

def pack_bagpack(S,W,C) :
    M = [0] * (1 + C)
    for F,V in enumerate(S) :
        M = [max(U,M[T - W[F]] + V if W[F] <= T else 0) for T,U in enumerate(M)]
    return M[-1]

#another one

def pack_bagpack(scores,weights,capacity):
    sols=[[0 for j in range(capacity+1)] for i in range(len(scores)+1)]
    scores.insert(0, 0)
    weights.insert(0, 0)
    for y,iy in enumerate(sols[1:],1):
        for x,ix in enumerate(iy[1:],1):
            if weights[y]<=x:
                sols[y][x]=max(scores[y]+sols[y-1][x-weights[y]],sols[y-1][x])
            else:
                sols[y][x]=sols[y-1][x]
    return sols[-1][-1]

_____________________________________________________________________

#This is the redundant directions exercise. notice the [-1] trick. this is a lot more straightforward than the evil brackets exercise. 

def dirReduc(arr):
    opposing_directions = {"NORTH":"SOUTH","SOUTH":"NORTH", "EAST":"WEST","WEST":"EAST"}
    DR = [] #the all mighty blank list
    for x in arr:
        if DR and DR[-1] == opposing_directions[x]:
            DR.pop()
        else:
            DR.append(x)
    return DR

    _____________________________________________________________________

def next_bigger(n):
    #break apart numbers into a list.
    nums = list(str(n)) 

    for i in reversed(range(len(nums[:-1]))):
        for j in reversed(range(i, len(nums))):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return int(''.join(nums))
    return -1

_____________________________________________________________________

#you need to git gud with regex lots of automation to be had here


import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

_____________________________________________________________________

#all combinations of letters

def permutations(string):
    import itertools
    #we let itertools make all the combinations from the string. 
    x = list(map("".join, itertools.permutations(string)))
    #remove all duplicates and put them in a new list to return. 
    blank = list(set(x)) 
    return blank

#best code here

import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

#my refined code
def permutations(string):
    import itertools
    return list(map("".join, set(itertools.permutations(string))))
_____________________________________________________________________

#function calculator exercise


def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y

_____________________________________________________________________

# greed is good dice game

#my Code:

def score(dice):
    one=0
    two=0
    three=0
    four =0 
    five=0
    six=0
    score = 0
    for n in dice:    
        if n==1:
            one+=1
        elif n==2:
            two+=1
        elif n==3:
            three+=1
        elif n==4:
            four+=1
        elif n==5:
            five+=1
        elif n==6:
            six+=1            
    if one == 1:
        score +=100
    if one == 2:
        score+=200
    if five ==1:
        score+=50  
    if five ==2:
        score+=100
    if two >=3:
        score +=200
    if three >= 3:
        score+=300
    if four >= 3:
        score+=400
    if five == 3:
        score+=500
    if five == 4:
        score+=550
    if five ==5:
        score+=600
    if six >= 3:
        score+=600
    if one == 3:
        score+=1000
    if one == 4:
        score=+1100
    if one == 5:
        score+=1200
    
    return score

#ooof lets look at the smart code. 

def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 

#also this one. 

def score(dice):
    #the really smart move this guy does is the // returns 0 if there are decimals.
    return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
           + dice.count(2)//3 * 200 \
           + dice.count(3)//3 * 300 \
           + dice.count(4)//3 * 400 \
           + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
           + dice.count(6)//3 * 600 \

#notice the count fuction in this one

def score(dice):
    #seperate rules for one and five
    sum, c1, c5 = 0, dice.count(1), dice.count(5)
    if c1 >= 3:
        c1 -= 3
        sum += 1000
    sum += 100 * c1
    
    if c5 >= 3:
        c5 -= 3
        sum += 500
    sum += 50 * c5
    #greater than or equal rules here. Again wish i used the counter function. 
    if dice.count(6) >= 3: sum += 600
    if dice.count(4) >= 3: sum += 400
    if dice.count(3) >= 3: sum += 300
    if dice.count(2) >= 3: sum += 200
    return sum
_____________________________________________________________________

#given a string see if two differnt strings have all the letters necessary to make it and in a sequential order if they are picked off the first of their respective indexes. 

#my version was alsmost there but i couldnt quite get the indexing right. 

def is_merge(s, part1, part2):
    for l in list(s):
        part1= list(part1)
        part2= list(part2)
        
        if l in part1:
            part1.remove(l)
        elif l in part2:
            part2.remove(l)
        else: 
            return False
    if part1 == []: 
        if part2 == []:
            return True
    else: return False


#best code from kita:
def is_merge(s, part1, part2):
    if not part1:
        return s == part2
    if not part2:
        return s == part1
    if not s:
        return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
        return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False
# if it gets called on a big string
# it divides up the input
# and calls itself on a smaller part of the string
# if the smaller part of the string is still too big
# it does the same
# eventually it finds one of the top 3 if statements and returns a concrete value on a tiny part of the string

# and then the code that called it on the tiny part can return as well
# and then the code that called it on the smaller part can return
# and a whole lot of returns happen until the first call on the total string can figure out what it should return
# a divide and conquer strategy
_______________________________________________________________________________

    #LAMBDA REFRESH

def func(x,y):
    return x + y


#is the same as saying:

x = lambda x,y: x+y
x(3,4)
#out
7


#more advanced lambda in function

def greetings():
    start_word = "Hello "
    greet = lambda x, y: start_word+"Mr. "+ str(x) if y == 'M' else start_word+"Miss. "+ str(x)
    return greet

result = greetings()
print(type(result))
print(result("Lenin", "F"))
#output
#<class 'function'>
#Hello Miss. Lenin

#IF ALL ELSE FAILS REMEMBER THIS TRICK:

if a:
    b
else:
    c
    
#a better way

b if a else c

#TAKE OUT THE TRASH IF ITS EMPTY ELSE LEAVE IT ALONE

_______________________________________________________________________________


#spiral array code thats been bugging you all day

def snail(array):
    blank = []
    while len(array) > 0:
        #go right
        blank += array[0] #new alternative to append. 
        del array[0]

        if len(array) > 0:
            # go down
            for x in array: 
                blank += [x[-1]]
                del x[-1]

            # go left    
            if array[-1]: 
                blank += array[-1][::-1]
                del array[-1]

            # go up
            for x in reversed(array):
                blank +=[x[0]]
                del x[0]
    return blank    

#the best code:

def snail(array):
    return list(array[0]) + snail(list(zip(*array[1:]))[::-1]) if array else [] 

    #AWESOME SOMEONE EXPLAINED THIS!

# my implementation/explanation of the solution by foxxyz
def snail(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    print(top_row)
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    print(rotated_array)
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    print(rotated_array)
    return top_row + snail(rotated_array)
  else:
    return []

#still a little convoluted heres a more straightforward approach using the key concepts:

def snail(array):
    #blank list
    a = []
    #while the array still has items in it
    while array:
        #we use extend rather than append to deal with less headache.
        #we add the first index of the array to a
        a.extend(list(array.pop(0)))
        #we zip together the two remaining lists 
        array = list(zip(*array))
        print(array)
        #finally we reverse the arrangement so that the first index we pop is the right set of numbers to grab
        array.reverse()
    return a

#what we learned:

# Filling a blank list while removing the array in the while loop was the right call.

# the zip tool was a key player to this. we couldnt see it before. 

# conditionals worked, but were not necessary as there is no deviation from the pattern. Unecessary checking was done in our original code. 

_______________________________________________________________________________

# Hashtag Creator:

#my code

import re #<-<-<-< - - - YOU FORGOT TO DELETE THIS!!!!
def generate_hashtag(s):
    s = s.title()
    s= s.strip()  #this could be better too many lines
    s= s.replace(" ", "")
    if (len(s) < 139) and ('#' not in s) and (s !=''):
        return '#'+s
    else:
        return False


#best code:

def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False #returns a little hard to read

# a mix of the two

def generate_hashtag(s):
    return '#'+s.title().replace(' ','') if 0<len(s)<=140 else False

_______________________________________________________________________________

# Return last digit from the exponential values of two random numbers:

# my code. gotta love built in functions.  

def last_digit(n1, n2): return pow(n1, n2, 10) 

_______________________________________________________________________________

#remove all the markers in the string 

#best readable answer. 

import re

def solution(string,markers):
    for marker in markers:
        string = re.sub(' *\\' + marker + '.*\n', '\n', string)
        string = re.sub(' *\\' + marker + '.*', '', string)
    return string

#better code:

import re

def solution(string,markers):
    for marker in markers:
        string = re.sub(' *\\' + marker + '.*', '', string)
    return string


#https://regex101.com/ is our new favorite tool

# ' *\\' = blank character 0-unlimited times followed by a \

# whatever the current marker is 

# followed by any character between 0-unlim times

# replace all that with ''

# make these replacements in the string

_______________________________________________________________________________

#the longest slide pyramid problem not hard, but hard to understand what the math rule was supposed to be. 

# first i thought they simply wanted me to sum up the largest numbers in each list.

def longest_slide_down(pyramid):
    blank = []
    for list in pyramid:
        blank.append(max(list))
    return sum(blank)

#but that wasnt it so i then thought they meant add the next proceeding item from each list's index. so return index 0 of list 1, 1 of 2, 2 of 3 etc. again pretty easy

def longest_slide_down(pyramid):   
    #blank list to fill up soon
    blank = []    
    # For every list inside the pyramid list;
    for list in pyramid:        
        #if the list's length is greater than 1 add the add the second to last number to our blank list
        if len(list) > 1: blank.append(list[-2])        
        #else just append the first item to the list.
        else: blank.append(list[0])        
    #add all those numbers up in our now filled blank list and return the total.
    return sum(blank) 

#but that wasnt it either. 
# Finally i caved and skiped to the solutions after the discussions were not much help either. 

# [3], [7, 4], [2, 4, 6], [8, 5, 9, 3] should get us 23 if we are doing things right.

_______________________________________________________________________________

#this one took me all day. my brain just didnt kick in until now.... and i still didnt get it all the way. 


def dbl_linear(n):
    u = [1]
    for x in u:
        u.sort()
        num = 2*x+1,3*x+1
        u.extend(num)
        if len(u) > n+1:
            break
    print(u)
    return u[n]

#my original code was almost there but I kept running into problems holding the pattern leaving me to think i got the equation wrong. I also kept getting doubles no matter what i did. I could google to look for the function that would have gotten rid of the duplicates, but i thought it had more to do with the equation being wrong and would lead me down the wrong path. 


#best code i liked

def dbl_linear(n):
    num_list = [1]
    for i in num_list:
        #two separeate equations 
        num_list.append((i * 2) + 1)
        num_list.append((i * 3) + 1)
        if len(num_list) > n *10: #multiplier seems to be needed because the pattern gets hard to hold the longer the number req. 
        break
    #sort them out at the end. so simple.     
    return sorted(list(set(num_list)))[n] #list(set()) helps us remove the doubles. 


_______________________________________________________________________________

#this next one was a rather difficult grid exercise i could not interperet: new rule if i dont get the code i gotta manually write a few of the answers, break them down and reverse engineer them. 

#best code 

def interpereter(code, iterations, width, height):
    code = ''.join(c for c in code if c in "[News]*")
    canvas = [ [0] * width for _ in range(height) ]
    row = col = step = count = loop = 0 #all these start at zero lemme try this

    while step < len(code) and count < iterations:
        command = code[step] #so it looks like here in the wihle loop, we iterate using this variable assignment and that way bypas the for loop stuff. 

        if loop:
            if command == '[': loop +=1
            elif command == ']': loop -= 1 #ooh this is clever he is using the string to turn on and off a boolean. 

        elif command == 'n': row = (row -1 ) % height
        elif command == 's': row = (row +1 ) % height
        elif command == 'w': col = ( col-1 ) % width
        elif command == 'e': col = ( col+1 ) % width
        elif command == '*': canvas[row][col] ^= 1 # a^=4 is the same as a = a^4
        elif command == '[' and canvas[row][col] ==0: loop+=1
        elif command == ']'and canvas[row][col] !=0: loop-=1

        step += 1 if not loop else loop // abs(loop)
        count += 1 if not loop else 0

    return "\r\n".join("".join(map(str,row)) for row in canvas)
_______________________________________________________________________________

#roman numerals

#my code

def to_roman(var):
    blank = ''
    while var > 0:
        
        if var== 0:
            break
        elif var>=1000:
            var -= 1000
            blank+=str('M')
            
        elif var<1000:
            var -= 500
            blank+=str('D')
            
        elif var<500:
            var -= 100
            blank+=str('C')
        
        elif var<100:
            var -= 50
            blank+=str('L')
            
        elif var<50:
            var -= 10
            blank<str('X')
            
        elif var<10:
            var -= 5
            blank+=str("V")
            
        elif var<5:
            var -= 1
            blank+=str("I")
            
    
    return blank
def from_roman(var):
    num=0
    for l in var:
        if l == 'M': num+=1000
        elif l == 'D': num+=500
        elif l == 'M': num+=100
        elif l == 'L': num+=50
        elif l == 'X': num+=10
        elif l == 'V': num+=5
        elif l == 'I': num+=1
    return num

def RomanNumerals(var):
    
    if var == int(var):
        to_roman(var)
    elif var== str(var):
        from_roman(var)


#best code (note this was setup for older python)

import string
from collections import OrderedDict

class RomanNumerals:
  @classmethod
  def to_roman(self, num):
    conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),
                               ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
    out = ''
    for key, value in conversions.iteritems():
      while num >= value:
        out += key
        num -= value
    return out
  
  @classmethod
  def from_roman(self, roman):
    conversions = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500),
                               ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
    out = 0
    for key, value in conversions.iteritems():
      out += value * roman.count(key)
      roman = string.replace(roman, key, "")
    return out

#couple things apparently i can use class objects in kata, ordered dictionaries was a nice touch, and guy here used way more numerals.

class RomanNumerals:
    @staticmethod
    def from_roman(s):
        #Zip the list of numbers as we for loop the string. From there turn it into a dictionary
        X=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s]

        return int(sum((x,-x)[x<y]for x,y in zip(X,X[1:]))+X[-1])
    @staticmethod
    def to_roman(i,o=' I II III IV V VI VII VIII IX'.split(' ')):
        r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC','XLCDM'))[c]for c in r(n//10))+o[n%10]
        return r(i)

#This one is both compact and clean

#so it looks like i borked the exercise by using only functions instead of a class. oh well. gottta learn sometime.

_______________________________________________________________________________

#failed the calculator exercise. Gotta write this three times. 

import operator 

class Calculator(object):
    operands = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    def __init__(self):
        self.result = []


    def evaluate(self, string):
        self.result = string.split(' ')
        self._loop('*/')
        self._loop('+-')
        return float(self.result[0])

    def _loop(self, operators):
        i = 1 
        while i < len(self.result) - 1:
            if self.result[i] in operators:
                self.result[i - 1] = str(self.__class__.operands[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))
                self.result.pop(i+1)
                self.result.pop(i)
                continue
            i += 1

import operator

class Calculator(object):
    opperands = {'+':operator.add,'-':operator.sub,'*': operator.mul,'/':operator.div}
    def __init__(self):
        self.result = []

    def evaluate(self, string):
        self.result = string.split(' ')
        self._loop('*/')
        self._loop('+-')
        return float(self.result[0])
    def _loop(self, operators):
        i= 1 
        while i < len(self.result) - 1:
            if self.result[i] in operators:
                self.result[i - 1] = str(self.__class__.operands[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))
                self.result.pop(i-1)
                self.result.pop(i)
                continue
            i += 1



_______________________________________________________________________________

#time i get better with classes

from collections import Counter
class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        a = []
        for x in digits_list:
            #this line was hard. I made it unecessarily harder by trying to return it in a zip function. Colons and commas. Remember you colons and commas.
            a.append((x, int(str(integers_list).count(str(x)))))
        return a

_______________________________________________________________________________

class List(object):
    def remove_(self, integer_list, values_list):
        for x in values_list:
            while x in integer_list:
                integer_list.remove(x)
        return integer_list




#smartest shoe right here.
class List(object):
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]
_______________________________________________________________________________

#boxing match 

#dear future me. At this point we picked up on the fact the class exercises don't provide the full code to study from. So past you will copy paste the URL from now on.

https://www.codewars.com/kata/two-fighters-one-winner/train/python

#your code

def declare_winner(fighter1, fighter2, first_attacker):
    attacks1 = float(fighter2.health)/fighter1.damage_per_attack
    attacks2 = float(fighter1.health)/fighter2.damage_per_attack
    if attacks1==attacks2: return first_attacker
    if attacks1 < attacks2: return fighter1.name
    else: return fighter2.name

#fancy pants coder

from math import ceil #we really didnt need to import. 
from operator import attrgetter #this we had to


def declare_winner(fighter1, fighter2, first_attacker):
    fighter1.turns = ceil(fighter1.health / float(fighter2.damage_per_attack))
    fighter2.turns = ceil(fighter2.health / float(fighter1.damage_per_attack))
    if fighter1.turns == fighter2.turns:
        return first_attacker
    return max(fighter1, fighter2, key=attrgetter('turns')).name

_______________________________________________________________________________


https://www.codewars.com/kata/class-conundrum-bug-fixing-number-7/train/python

#whats wrong with this code? also you are in python 2.7.6 for this ... fun

class List:
    def __init__(self,type): #change type here and bellow. 
        self.type=type #type needs to be replaced as type is a built in function
        self.items=[]
        self.count=0
    
    def add(self,item):
        if type(item)!=self.type:
            item_type="str" if self.type==str else "int" if self.type==int else "float" #needless if else checking.
            return "This item is not of type: %s" %(item_type) #needs f string literal and need to return the name of the self.type.
        self.items+=[item]
        self.count+=1
        return item #must return self not item


#Fix it

class List:
    def __init__(self,item_type):
        self.type=item_type 
        self.items=[]
        self.count=0
    
    def add(self,item):
        if type(item)!=self.type:
            return "This item is not of type: {}".format(self.type.__name__)
        self.items+=[item]
        self.count+=1
        return self


#Fixed code

class List:
    def __init__(self,item_type):
        self.type=item_type
        self.items=[]
        self.count=0
    
    def add(self,item,):
        if type(item)!=self.type:
            return "This item is not of type: {}".format(self.type.__name__)
        self.items+=[item]
        self.count+=1
        return self

_______________________________________________________________________________

#So @classmethod is a decorator that turns a method into a class method.  What that means is that you don't have to make an instance (object) of the class in order to call or use that method

# @classmethod mostly just makes it so that you don't have to pass an object argument, so you don't need self

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

new = MyClass()
print(new.method())
print(new.classmethod())
print(new.staticmethod())

001 | ('instance method called', <__main__.MyClass object at 0x7f583fa7d8d0>)
002 | ('class method called', <class '__main__.MyClass'>)
003 | static method called

#HOKAY, so
#I'm an idiot
#What the @classmethod decorator does is instead of passing the object, it passes the class
# So it'd be something like... Class.method(Class)


class Dog:
    def __init__(self, name, breed, age, sex):
        self.name = name
        self.breed = breed
        self.age = age #number plz
        self.sex = sex
    def __str__(self):
        return 'My name is' + self.name + '. I am a ' + self.breed + '. I am ' + self.age + ' and a very good ' +self.sex '! Woof!'

x = Dog('Chibbi','Golden', 5,'girl')

print(x)

arr = [1,2,3,4]
def double_up(list): 
    blank = []
    for x in list:
        blank.append(x*2)
    return blank
