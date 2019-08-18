#Be kind to your future self. No one else will help you.

#first if statement!

if 3>2:
    print('IT\'S TRUE')

##second if statement

hungry = False
if hungry:
    print('feed me')
else:
    print('No thanks. I\'m good.')


#first elif code

loc = 'Bank'

if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Every line of code you write is one step closer to freedom.")
elif loc == 'Store':
	print("Welcome to the store")
else:
    print("I do not know much.")

#second elif

name  = 'Sammy'
if name == 'Frankie':
    print("Hey Frankie!")
elif name == 'Sammy':
    print("Hello Sammy")
else:
    print("what is your name?")


#End of video on if, elif and else statements. 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/

# Beginning of For Loops in Python:

# Many Objects in python are iterable, meaning it can be operated or be applied repeatedly, as a linguistic rule or mathematical formula.

#We can iterate over every element in the object.

# Every element in a list or a string. Every item in a list. Every key in a dicitonary. And every value to every key in the dictionary. 

#We can use for loops to execute a block of code for every iteration. 

# Syntax of a for loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
my_iterable = [1,2,3]
for item_name in my_iterable:
	print(item_name):
>>1
>>2
>>3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#for loop examples!
~~~~~~~~~~~~~~~~~~~~
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist: #num can be LITERALLY ANYTHING! it wont change the outcome
	print(num)
#output
1
2
3
4
5
6
7
8
9
10
~~~~~~~~~~~~~~~~~~~~
#look what happens if we change the print
~~~~~~~~~~~~~~~~~~~~
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print('100k job')
#output
100k job
100k job
100k job
100k job
100k job
100k job
100k job
100k job
100k job
100k job
~~~~~~~~~~~~~~~~~~~~
#try and print only the even numbers in the list:
~~~~~~~~~~~~~~~~~~~~
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num%2 == 0:
        print(num)
    else:
        print(f'100k job: {num}') #The f is an f string literal
#output
100k job: 1
2
100k job: 3
4
100k job: 5
6
100k job: 7
8
100k job: 9
10
~~~~~~~~~~~~~~~~~~~~
#keep some sort of running tally durring multiple loops
~~~~~~~~~~~~~~~~~~~~
mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0

for num in mylist: 
    list_sum = list_sum +num
    
print(list_sum)
#output:
55
~~~~~~~~~~~~~~~~~~~~
#K now same code, only we indent the print on line 138 bellow
~~~~~~~~~~~~~~~~~~~~~
list_sum = 0

for num in mylist:
    list_sum = list_sum +num
    
    print(list_sum)
#output:
1
3
6
10
15
21
28
36
45
55
#it shows the result from every addition made until it goes through mylist. 

# Be kind to your future self
~~~~~~~~~~~~~~~~~~~~~
#using for loops with strings
~~~~~~~~~~~~~~~~~~~~~
mystring = 'Hello World'
for letter in mystring:
    print(letter)
#output
H
e
l
l
o
 
W
o
r
l
d
~~~~~~~~~~~~~~~~
#this works too! 
~~~~~~~~~~~~~~~~
for letter in 'Hello World':
    print(letter)
#output
H
e
l
l
o
 
W
o
r
l
d
~~~~~~~~~~~~~~~~~~~
#now watch this
~~~~~~~~~~~~~~~~~~~

for literally_anything_can_be_put_here in 'Hello World':
	print('100k job, here I come.')


#output:
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.
100k job, here I come.

~~~~~~~~~~~~~~~~~~~~~~~~~~
#for tuples!
~~~~~~~~~~~~~~~~~~~~~~~~~~
tup = (1,2,3)
for num in tup:
    print(num)

#output
1
2
3
~~~~~~~~~~~~~~~~~~~~~~~~~~
#FOR LOOPS WITH TUPLES
#if you are iterating through a sequence that contains itself tuples, the item can be used with tuple unpacking.
#EXAMPLE
~~~~~~~~~~~~~~~~~~~~~~~~~~
mylist=[(1,2),(3,4),(5,6),(7,8)]
len(mylist)
#output
###4 
###each item is a tuple pair. Lets print those items out
for item in mylist:
    print(item)
#output
(1, 2)
(3, 4)
(5, 6)
(7, 8)
#now lets unpack these tuples!
for (a,b) in mylist:
	print(a)
	print(b)
#output:
1
2
3
4
5
6
7
8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#if you only printed 'a' you would have gotten the odd numbers. 'b' evens.
# YOU WILL DO A LOT OF TUPLE UNPACKING YOU ARE GOING TO USE IT WITH A LOT OF BUILT IN PYTHON FUNCTIONS
~~~~~~~~~~EXAMPLE~~~~~~~~~~~~~~
mylist = [(1,2,3),(5,6,7),(8,9,10)]
for item in mylist:
	print(item)
#output
(1, 2, 3)
(5, 6, 7)
(8, 9, 10)
#now lets have fun with this

mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist:
	print(a)
#output
1
5
8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~HOW TO ITERATE A DICTIONARY~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~BE KIND TO YOUR FUTURE SELF~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)
#output
k1
k2 #keys output by default!
k3
#lets include the items not just the keys
d = {'k1':1,'k2':2,'k3':3}

for item in d.items(): 
    print(item)
#output
('k1', 1)#gotta use .items(): DONT FORGET THE COLON
('k2', 2)
('k3', 3)
#lets try that tuple trick from earlier
for key,value in d.items(): 
	print(value)
#output
1
2 #NOTICE THE ',' in key,value. THATS IMPORTANT
3
#REMEMBER THIS. BE KIND TO YOUR FUTURE SELF.
#
~~~~~~~~~~~~~IF YOU ONLY NEED VALUES~~~~
~~~~USE .values(): ~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
d = {'k1':1,'k2':2,'k3':3}

for value in d.values():
    print(value)
#output
1
2 #THIS WILL NOT GIVE KEYS. ABOVE EXAMPLES WILL. 
3
### ALSO REMEMBER DICTIONARIES ARE UNORDERED.

#end of for loops in python video
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~WHILE LOOPS IN PYTHON ~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\


#Be kind to your future self.

 # while loops in python continue to execute a blocl of code while some condition remains true. 
	# While my pool is not full, keep filling my pool with water. 

	#or while my dogs are hungry, keep feeding my dogs. 

#syntax of while loop
	while some_boolean_condition: #<---- NOTE THE COLON
		do something
#you can combine with else if you want or need to. 
	while some_boolean_condition: #<---- NOTE THE COLON
		do something
	else: #again notice the colon
		do something different



~~~~~~~EXAMPLES!~~~~~~~~~~

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x+1

#output:
The current value of x is 0
The current value of x is 1
The current value of x is 2
The current value of x is 3
The current value of x is 4
#notice it only goes to four and will not output 5. lets fix that.
x = 0

while x <= 5: # All we did is change = to <=
    print(f'The current value of x is {x}')
    x = x+1

#output:
The current value of x is 0
The current value of x is 1
The current value of x is 2
The current value of x is 3
The current value of x is 4
The current value of x is 5

~~~~~~~~REMEMBER THE += SIGN!~~~~~~

x = 0

while x <= 5: 
    print(f'The current value of x is {x}')
    x += 1 #LOOK AT THIS MAGNIFICAENT += SIGN! ALL HAIL += SIGN! ALL HAIL += SIGN! ALL HAIL += SIGN! ALL HAIL += SIGN! ALL HAIL += SIGN!

#output:
The current value of x is 0
The current value of x is 1
The current value of x is 2
The current value of x is 3
The current value of x is 4
The current value of x is 5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~time for an else statement!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 0

while x < 5: #NOTE WE GOT RID OF <= for this demonstration
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X IS NOT LESS THAN 5")

#output:

The current value of x is 0
The current value of x is 1
The current value of x is 2
The current value of x is 3
The current value of x is 4
X IS NOT LESS THAN 5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Lets make it jump to else on purpose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = 50 # We make x = 50 at the start!

while x < 5: 
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X IS NOT LESS THAN 5")

#output:
X IS NOT LESS THAN 5
# Else statements in cases like this could be useful for finding mistakes in your code. Everyone makes them, its good to plan for them.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~CONTINUE BREAK & PASS ~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BREAK - # Breaks out of the current closing loop. 

CONTINUE - # Goes to the top of the closest enclosing loop.

PASS - # Does ABSOLUTELY NOTHING AT ALL! 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~EXAMPLES!~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~ PASS EXAMPLE ~~~~~~~~~~


x = [1,2,3]
for item in x:
	# comment
    pass

#output will produce nothing when normally even if you left a comment it would otherwise leave you with an error!

x = [1,2,3]
for item in x:
    pass
print('end of my script')

#output
end of my script
# Notice how here it simply moves to the print statement, bypassing the for loop. Without the pass....
##############~~~~~~~~~~~~~~~~~~~~~~~~##############
############## WE GET A SYNTAX ERROR! ##############
##############~~~~~~~~~~~~~~~~~~~~~~~~##############

~~~~~~~ CONTINUE EXAMPLE ~~~~~~~~~~

mystring = 'Sammy' 

for letter in mystring:
    if letter == 'a': # USE TWO '='s not one. Should be '=='. AND DONT FORGET THE COLONS!  : : : : : : : : : : : : : : : : : : : : : : :
        continue
    print(letter)
#output
S
m
m
y
# We dismissed the 'a', and "continue" to the top of the loop.

~~~~~~~~~~ BREAK EXAMPLE ~~~~~~~~~~

mystring = 'Sammy' 

for letter in mystring:
    if letter == 'a': # USE TWO '='s not one. Should be '=='. AND DONT FORGET THE COLONS!  : : : : : : : : : : : : : : : : : : : : : : :
        break
    print(letter)
#output
S
#with the power of the break statement, we stop printing after 's'. remember when it reaches a, the code is asking in this case "we reached the 'a', what do we do?" and the code is saying break out of the loop instead of continuing. 

# Break is super useful when used with a while statement! 

~~~~~~~~~~~~~ EXAMPLE ~~~~~~~~~~~~~

x = 0 

while x <5:
	if x = 2:
		break
    print(x)
    x += 1

#output 
0
1
# once again if you are looking at outputs, it won't print the 2

# review!

	# While loops are useful
		#While something is true, keep doing something until it's false. 

	# pass is going to do nothing

	# continue continues the loop by skiping one step. 

	# break stops everything to break out of the loop. 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~USEFUL OPERATORS IN PYTHON ~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\

#are you tired of writing lists? "There's got to be a better way," you say?

~~~~~~~~~~~~~~~~~~~PRO TIP!~~~~~~~~~~~~~~~~~~~~
SHIFT TAB IN JUPITER FOR HELP!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for num in range(10): #Shift-tab here for help when using jupiter! AND DON'T FORGET YOUR COLON!
	print(num)
#output
0
1
2
3
4
5
6
7
8
9


# Cool, how about getting me numbers 3-9?
for num in range(3,10): #this is how slicing works. when indexing in this case it only goes up to 9 REMEMBER THAT NEXT TIME YOU SLICE!!! ADD +1 OF WHATEVER NUMBER YOU REALLY WANT! 
    print(num)
#output
3
4
5
6
7
8
9

# Awesome. I was having trouble with that earlier. How do I make it only print every two numbers? I hate odd numbers. except 5. five is cool. but lets just worry about evens for now. 

 for num in range(0,10,2): #Third slice counts the steps. in this case prints every two numbers giving you the evens.
    print(num)
#output
0
2
4
6
8
# I WANT TEN ON THAT LIST!

for num in range(0,11,2): #good you remebered the colon! and you get slicing finally. see you're not fucked after all. You're one step closer to landing that 100k job. 
	print(num)
#output!
0
2
4
6
8
10
#YAY! 

~~~~PRO TIP!~~~~~

# writing range(0,11,2) on it's own won't work. 

# WHAT DO I EVER DO?
#Easy you put it under list operator and you don't need to colon thinge
list(range(0,11,2))

#output
[0,2,4,6,8,10]

#Hooray!

#later on we'll learn more about list generators in detail. Just remember this in the meantime. A generator is just a special type or function that will generate info instead of saving it to memory. 
#K

~~~~~ NOW WE LEARN ENUMERATE! ~~~~~
# this is a lot of code. lets break it down.
index_count = 0 #set our counter to zero

for letter in 'abcde': # each letter in the string
    print('at index {} the letter is {}'.format(index_count,letter))#print a fill in the blank sentence. .format is used here to specify what to fill in with. 
    index_count += 1 #every time this loops, +1 to the index_count 

#same code bellow minus the comments so you can see it more clearly

index_count = 0
for letter in 'abcde':
    print('at index {} the letter is {}'.format(index_count,letter))
    index_count += 1

#output
at index 0 the letter is a
at index 1 the letter is b
at index 2 the letter is c
at index 3 the letter is d
at index 4 the letter is e

# We do this sort of thing so constantly we have a better way to do it!

# ENUMERATE FUNCTION TO THE RESCUE! 

index_count = 0
word = 'abcde'
for letter in word: #remember letter can be written as anything it's talking about whatever is filling that current index. 
    print(word[index_count])
    index_count += 1

#once again same code minus the comments getting in the way

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1  
#output
a
b
c 
d 
e

# this still looks messy and lots of code to write. and i want both the letter AND index printed! IN TUPLES!

#okay this is how we do it!

word = 'abcde'

for item in enumerate(word):
    print(item)


#output
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
# Enumereate brings all of this stuff to you in tuple form. Also if you put a comma after your iterable in the enumerate operator, whatever number you put in will start at that index!

#oh cool thats right i learned that by Shift tabbing in jupiter! 

#BUT WAIT THERS MORE! Since this is a tuple we can pull off a few more tricks!  Lets unpack these tuples!

word = 'abcde'

for index,letter in enumerate(word):
	print(index)
	print(letter)
	print('\n')
#output
0
a


1
b


2
c


3
d


4
e
#cool! so that's what enumerate does! it takes any iterable object and returns an index counter(the 0,1,2,3,4 in this example) and the object itself! (the letters in the string above)

~~~~~~~~~~~~~~ ZIP FUNCTION ~~~~~~~~~~~~~~~~~

# zip puts together two lists! like an a,b,c and a 1,2,3! 

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

zip(mylist1,mylist2) #USING THIS BY ITSELF WONT LET YOU DO JACK!

## YOU GOTTA ITERATE !

for item in zip(mylist1,mylist2):
	print(item)

#output
(1, 'a')
(2, 'b')
(3, 'c')
#it puts them together into tuples!

# AND WE CAN PUT MORE LISTS IN THE ZIP!
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
    print(item)
#output
(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)

#hey what happens if one list is bigger than the others?
# it will only print up to the shortest list. watch.

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
    print(item)
#output
(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)

#makes sense. 
#it better you need to understand this for the big bucks. 

#it won't give you an error it will just ignore the extra. 

#what if I want just the list itself?

#use list() like this:

list(zip(mylist1,mylist2))

# output
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

#awesome


#also since these are tuples we can upack them too!
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d']
mylist3 = [100,200,300]

for a,b,c in zip(mylist1,mylist2,mylist3):
    print(a)
#output
1
2
3

~~~~~~~~~~~~~IN OPERATOR~~~~~~~~~~~

#The Ctrl+F of python operators

mylist1 = [1,2,3,4,5]

3 in mylist1

#output 
True 

#it will return a boolean:

'x' in 3
#output
False

# great for checking if something is in a list. also great for if statements. if theres a x in xyz print else continue or something. 

#use it to check strings 

'a' in 'lama'

#output
True

# GREAT FOR DICTIONARY KEY FINDING TOO! 

'mykey' in {'mykey':345}
#output
True

#this works too!

d = {'mykey':345}

345 in d.values() #remember value checks the number part of dictionary
#output
True

d = {'mykey':345}

345 in d.keys() #remember keys checks for the key in the dictionary
#output
False

# .keys() the first half, .values() the second half when refernecing dictionary. Very useful because dictionaries will not be organized. 

~~~~~~~~~~~~ min() AND max() ~~~~~~~~~~~~~

mylist = [1,2,3,4,5,6,7,8,9,10]

min(mylist)
#output 
1
max(mylist)
#output
10
#Really hope i dont have to explain this one to you. Don't make these into keywords

~~~~~~~~~IMPORTING LIBRARIES~~~~~~~~~~~

#importing functions

from random import #hit tab here in jupiter at this point and you will get a lot of choices

from random import shuffle
#no output it presumably imported it now lets try it out. 
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
mylist
#output
[2, 7, 6, 3, 5, 10, 9, 4, 8, 1]

~~~~WARNING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~ YOU CAN NOT ASSIGN A VARIABLE TO SHUFFLE ~~~~
~~~~~~~~~~~~~~~ IT WONT RETURN ANYTHING~~~~~~~~~
~~ WE CALL THAT AN IN PLACE OPERATION ~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# at least my list is still shuffled!

mylist
#output
[2, 7, 6, 3, 5, 10, 9, 4, 8, 1]

~~~GRABBING A RANDOM INTERGER~~~~

from random import randint

randint(0,100)

#output 
79

randint(0,100)

#output 
38

# since this retuns stuff without any additional information you can assign a variable to this! 

rannumber = randint(0,100)

rannumber
#output 
47
# its going to keep whatever first outputs. Don't expect a random number every time the variable is used. 


~~~~~~~~Inuput function ~~~~~~~~~~~


input('Enter a number here: ')
#Output will have a place you can type in! lets put in 50

#output 
'50'

#it's good to use these as results.

result = input('Enter a number here: ')
#when you enter the number result will be assigned to it!

result
#output
'50'

#only catch is it turns whatever you put in it as a string. can't have it all...OR CAN WE?

float(result)

#output
50.0
#or even better!

int(result)
#output
50

#lets put it all together! 

result = int(input('Enter a number here: '))
#this will return it as an int!

type(result)
#output
int



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~ LIST COMPREHENSIONS IN PYTHON ~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\


# list comprehensions are a unique way of quickly making a a litst in python.

#if you find yourself using a for loop along with .append() to create a list, list comprehensions are a good alternative!

mystring = 'hello' 

mylist =[]
for letter in mystring:
    mylist.append(letter)

mylist 
#output
['h', 'e', 'l', 'l', 'o']

#theres got to be a better way!

#There is. Let's break it down

mystring = 'hello' 

mylist =[]
for letter in mystring

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mystring = 'hello'

mylist =[]
letter for letter in mystring

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mystring = 'hello'

mylist =[letter for letter in mystring]

mylist
#output
['h', 'e', 'l', 'l', 'o']

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~another example ~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mylist = [x for x in 'word']
print(mylist)

#output
['w', 'o', 'r', 'd']

~~~~~ #REMEMBER the x in the for loop can be ANYTHING. 
~~~~~ # all it is doing is breaking up the string or iterarble object.

mylist = [x for x in range(0,11)] 
print(mylist)
#output
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### Is this all i can do is just make lists of things? 

# Nope! we are just scratching the surface! check this out: 

#what's happening here? 

mylist = [x%2 for x in range(0,11)] 
print(mylist)

#output
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Now what about here? 

mylist = [x+2 for x in range(0,11)] 
print(mylist)

#output
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#this?

mylist = [x+2**2 for x in range(0,11)] 
print(mylist)
#output
[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# k now how about this one? lets get crazy with it.


mylist = [((x+2)**2 + (x**3)) for x in range(0,11)] 
print(mylist)
#output
[4, 10, 24, 52, 100, 174, 280, 424, 612, 850, 1144]

# as you can see you can play around with the first part of the x. just not the second 'x' after the for. 

#menatal note it looks like you understand the math parts of this, but the strings throw you off. Try to tackle more string and character problems to improve yourself. 

#lets make sure you get this 

# THIS ....

mylist = [((x+2)**2 + (x**3)) for x in range(0,11)] 
print(mylist)

# ....is the same as writing this:

mylist =[]
for x in range(0,11): #colons! remember this! 
    mylist.append((x+2)**2 + (x**3))
mylist

# the first half is basically an append instruction. 

#okay you got another thing figured out here. it looks like the built in  functions are something you will need to commit to remembering. 

~~~~~~~~~~~ADDING IF STATEMENTS~~~~~~~~

# we tack on the if statement after the x for x in y part)

mylist = [x for x in range(0,11) if x%2 == 0]
mylist

#output
[0, 2, 4, 6, 8, 10]


# remember we can still play around with the first x! 

mylist = [x**2 for x in range(0,11) if x%2 == 0]
mylist
#output 
[0, 4, 16, 36, 64, 100]


celcius = [0,10, 15, 25, 30]

fahrenheit = [(temperature*(9/5)+32) for temperature in celcius]

#or you can write 
celcius = [0,10, 15, 25, 30]
fahrenheit= [] #GOTTA PUT YOUR LISTS IN! AND MIND YOUR PARENTHESIS
for temperature in celcius:
    fahrenheit.append(temperature*(9/5)+32) #remember your .append()


~~~~~~~~~~~~~~~~~~ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
~~~~~~~~~~~~~~~~~~ STUDY THIS RELIGOUSLY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~ CAN YOU DO IF-ELSE STATEMENTS IN THE LIST COMPREHENSIONS? ~~~~~

# Yup! But it's not exactly the best thing you should be doing. It makes your code harder to read. Remember be kind to your future self! 

#but can you show me anyway? 

#yup the order is going to be different

# REMEMBER READABILITY AND REPRODUCABILITY is the most important thing in python. Save the slick one liners for those who are compensating for something. 

results = [x if x%2 ==0 else 'ODD' for x in range (0,11)] #the slick way. notice the three x's instead of the two. 


#now for the proper way.

mynumbers= range(0,11)
results= []
for num in mynumbers:
    if num%2==0:
        results.append(num)
    else:
        results.append('ODD')


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 # Break it down so you get it. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mynumbers = range(0,11)# assign the variable. remember slicing rules
results = [] #the list we are adding to. You gotta leave it blank to fill in the iterables. this is the bucket. fill up the bucket with appends. 

for x in mynumbers: #colons x means the number in the list in this case. Numbers can be iterated. 
    if x%2==0: #if the remainder when divided by 2 is zero (even) 
        results.append(x) #print the number on the list. 
    else:
        results.append('ODD') #otherwise add the string 'ODD' in it's place.

mynumbers = range(0,11)
results = []

for num in mynumbers:
    if num%2==0:
        results.append(num)
    else: 
        results.append('ODD')
results

#got it on your first try awesome.

#back to the lesson. This is a nested loop. you paying attention?


mylist = [] 

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
mylist
#output
[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

#yo dawg i heard u like lists. so we put a list in your list so you can multiply them up. NOTE THE PATTERN. one index of x goes through the whole list of y, then it moves on from there. lets make it a clear as crystal pepsi:

mylist = [] 

for x in [2,4,6]:
    for y in [1,100,1000]:
        mylist.append(x*y)
mylist
#output:
[2, 200, 2000, 4, 400, 4000, 6, 600, 6000]
# see it now? 

#can i do this in list comprehension?

#yes but again we dont recommend it. YOU GOTTA BE ABLE TO READ THE CODE.

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
mylist
#output:
[2, 200, 2000, 4, 400, 4000, 6, 600, 6000]
#smaller footprint. larger headache unless you ABSOLUTELY know what you're doing. 


#okay that sums up this lesson. Now be a good student and review this stuff. really make sure you understand how for loops work before you move on. 

#small victory. I had a few hiccups on the test, but for the most part i knew what i was doing with a few looks here and there. Im getting better. Going to do some small walking and little bit of celebrating before i go back to work.

#review your stuff first and then save your test progress. 

Assessment test answers

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)
    else:
        continue

 # remember you can test stuff like .split() incrementally   
 
 #also note capital S would not work unless you add a .lower() to word[0]

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)
    else:
        continue


 # OR use or 

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's' or word[0] == 'S'
        print(word)
    else:
        continue

##########################################
list(range(0,11,2))

#another way 

for num in range(0,11,2):
    print(num)

# now append it in a list 

myevens = [] 

for num in range(0,11,2):
    myevens.append(num)
myevens

##########################################
#easy way
mylist=[]

for num in range(1,51):
    if num%3 == 0:
        mylist.append(num)
mylist

#hard way 

[num for num in range(1,51) if num%3 == 0]


###########################################
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word+' is even!')
    

###########################################

#the fizzbuzz REMEMBER THIS ONE!

mylist=[]

for num in range(1,101):
    if (num%3 == 0) and (num%5 == 0):
        print('FizzBuzz')
    elif num%5 == 0:
        print('buzz')
    elif num%3 == 0:
        print('fizz')
    else: 
        print(num)


###########################################


st = 'Create a list of the first letters of every word in this string'
mylist = []
for word in st.split():
    mylist.append(word[0])
mylist

#more fancy way of writing it

[word[0] for word in st.split()] #study this method too. 

############################################

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~METHODS AND FUNCTIONS PYTHON DOCUMENTATION~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\

 # built in objects in python have a varietey of methods you can use!

 # let's explore in a bit more detail how to find methods and how to get information about them! 

 mylist = [1,2,3]

~~~~Appending adds to lists ~~~~

 mylist.append(4)

 mylist

 #output 
 [1,2,3,4]

~~~~~pop removes the last item on lists ~~~

mylist.pop()

#output
4

mylist

#output

[1,2,3]


~~~~~~~~~~~~~~~INSERT~~~~~~~~~~~~~~~~
#insert lets you add stuff in by index and object!
mylist.insert(0,0) 

#output
[0,1,2,3]

#don't forget about shift +tab in jupiter and also use the built in help in python!

#Example

help(mylist.insert)

#output
#Help on built-in function insert:

#insert(index, object, /) method of builtins.list instance
 #   Insert object before index.

 #python documentation helps too!

 https://docs.python.org

 stack overflow

 google

 youtube

 https://docs.python.org/3/library/index.html
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 ~~~~~~~ KEEP THIS UNDER YOUR PILLOW ~~~~~~~~



|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~ FUNCTIONS IN PYTHON ~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\


The big leap!

# Creating clean repeatable code is a key part of becoming an effective programmer. 

# functions allow us to create blocks of code that can be easily exectued many times, without needing to constantly rewrite the entire block of code. 

# The syntax 
def name_of_function():
    '''
    Docstring explains function.
    '''
    print("Hello")
>>name_of_function()
>>Hello

#another example

def name_of_function(name):
    '''
    Docstring explains the function
    '''
>>name_of_function("Jose")
>>Hello Jose

# typically we use the 'return' keyword to send back the result of the function, instead of simply printing it out. 

# 'return' allows us to assign the output of the function to a new variable. 

#example

def add_function(num1,num2):
    return num1+num2

>>result = add_funtion(1,2)
>>
>>print(result)
>>3

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def name_function():
    print('Hello')
###IMPORTANT

~~~~#Your newly made functions will NOT have anything useful in it unless you write up a docstring. Be kind to your future self so you can use help() or shift+tab to know what you wrote. 

#how do i make those? 

# three pairs of quotes either single or double along with "Docstring:" like in the example bellow:

def name_function():
    '''
    Docstring: This will print 'Hello' when you run it with empty brackets. 
    Input: no input...
    Output: Hello
    '''
    print('Hello')

# okay now that we have the very basics established, lets add some arguements. 

def say_hello(name):
    '''
    Put a defined name in the () and it will say Hello with the name given.
    '''
    print('Hello '+name)

#if we leave the code like this without a defined name ('Jose' for example) we will get an error. Lets put in a default one in case one isn't put in. And for giggles lets make it painfully obvious you should have put something in the function. 

def say_hello(name = 'INSERT NAME HERE'):
    '''
    Put a name in the () and it will say Hello with the name given.
    '''
    print('Hello '+ name + '!')

#again this will only print 'INSERT NAME HERE' if you don't put in anything in the brakets given. 

#now these are the very basics and typically we want to get the results back to save to a variable. If we try to assign a varible to the current function it will not return anything. It will just give you a NoneType.

#example

result = say_hello('Dolly')
#output
Hello nurse!
#now when we use result nothing returns
result
#output

#here we check for it's type
type(result)
#output
NoneType

#oh no! how do we fix this?

#return to the rescue!

def say_hello(name = 'INSERT NAME HERE'):
    '''
    Put a name in the () and it will say Hello with the name given.
    '''
    return 'Hello '+ name + '!'

result = say_hello('Rodger')
###
result
#output
'Hello Rodger!'

# another example!

def add(n1,n2):
    return n1+n2

result = add(20,30)

result 
#output 
50

#think of return as a way of saving your work. your variable you assign it to then works like a save file.

#now that we know the basics we can go on to using functions for problem solving. 

#find out if the word dog is in a string

def dog(string):
    if 'dog' in string:
        return True
    else:
        return False

My refined version which includes capitals        

def dog_check(string):
        if 'dog' in string:
            return True
        elif 'Dog' in string:
            return True
        else:
            return False

Better version still

def dog_check(string):
        if 'dog' in string.lower():
            return True
        else:
            return False

BUT WE CAN DO BETTER!

def dog_check(string):
        return 'dog' in string.lower()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pig Latin exercise: #lets see if we can do this
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#rules of pig latin

# if word starts with a,e,i,o,u, add 'ay' to end

#if word does not start with a,e,i,o,u, put first letter at end, then we  add 'ay'

#my attempt

def pig_latin(word):
    if word[0] == ('a'or'e'or'i'or'o'or'u'):
        return word + 'ay'
    else:
        return word[1:]+word[0]+'ay'

#IT WORKS! 

#Pros
    #less code
#cons 
    #multiple return functions
    #vowel equals is not very elegant. would not be practical for a larger list of words. 

#How the video did it 

def pig_latin(word):
    first_letter = word[0]

    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word

#pros
    # in function
    # one return not two.
#cons
    #needed to add a variable for the first letter. 

# can we put the two together? 

def pig_latin(word):
    '''
    Input: Any word of your choosing.
    output: returns word translated to pig latin. 

    '''
    #check if vowel
    if word[0] in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'
    
    return pig_word

#Cool this works and does both well! Don't forget to write a docstring!

 # be kind tp your future self. review this stuff and makes sure you get it. 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~ *ARGS AND **KWARGS IN PYTHON ~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\

# *args and **kwargs are basically stand ins  

# when u work in python long enough you're going to want a way to accecpt an arbitrary number of arguements and key word arguements without having to to predefine a bunch of paramaters in your function calls. 

~~~~~~~~~~~~~~~~~Example~~~~~~~~~~~~~~~~~~~

def myfunc(a,b):
    #returns 5% of sum a and b
    return sum((a,b)) * 0.05
myfunc(40,60)
#output
5.0

#the function works fine like this, but what if we wanted more paramaters to pass in? in this case more than two numbers

def myfunc(a,b,c=0,d=0,e=0): #you could have extra paramaters and set them to zero if you needed them, but thats not always a permenant fix.
    #returns 5% of sum a and b
    return sum((a,b,c,d,e)) * 0.05#also add the paramaters here too.
myfunc(40,60)

#this works, but is not an easy fix and will quickly make things tedious. 

#THERE'S GOT TO BE A BETTER WAY! *args TO THE RESCUE!



def myfunc(*args):
    return sum(args)*0.05 # no * after placing in function also note no need for extra set of () unlike other script

#now we can add as many numbers to this function as we want! 

myfunc(40,60,100,1,34)
#output
11.75

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
Just to make sure we understand this.
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

def myfunc(*args) :
    print(args)
myfunc(1,2,3)

#output
(1,2,3) 

~~~~ARGS ARE TUPLES~~NOT LISTS~~NOT DICTIONARIES~~~~
args
#whatever this paramater is the user can pass in as many as they want and it's going to be treated as a tuple inside of the function.

#args can be written as anything  like *this or *that, but it's a good standard practice to write *args and **kwargs (which we are getting to in a minute) as just their original names to avoid confusion.  

def myfunc(*args):
    for item in args:
        print(item)
myfunc(40,60,100,1,34)
#output
40
60
100
1
34


#now we're gonna talk about KEY WORD ARGUEMENTS or **kwargs !

# we use **kwargs They give us Key Word arguements the gives us
#a dictionary of key value pairs items!

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I didn\'t find any fruit here.')



myfunc(fruit='Apple', veggie = 'lettuce')
#output
#{'fruit': 'Apple', 'veggie': 'lettuce'}
#My fruit of choice is Apple

# THE **s MAKE A DIFFERENCE! ~insert Bill Wurtz tune.

~~~~~ **KWARGS MAKE DICTIONARIES ~~~~~

#LETS USE THE TOGETHER!

def myfunc(*args,**kwargs):
    print(args) #PRO TIP HAVE THESE BABYS UP WHILE WRITING CODE TO KEEP TRACK OF THINGS.
    print(kwargs)
    print('I would like {} {}.'.format(args[0],kwargs['food']))


myfunc(10,20,30, fruit='orange',food='bread',item='toilet paper')

#output
(10, 20, 30)#args
{'fruit': 'orange', 'food': 'bread', 'item': 'toilet paper'} #kwargs
I would like 10 bread.

## MIND THE ORDER YOU ASSIGN ARGS AND KWARGS. IT WILL FOlLOW THAT ORDER.

## dont just see errors, read them!
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
~~CHECK THE NOTEBOOK FOR EXTRA STUFF 
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

Study the uppercase problem and review the notes you took. NEVER QUIT

BE KIND TO YOUR FUTURE SELF. 

def myfunc(string):
    word='' #word is a blank string NOT A LIST. Lists get the append. We let the for loop fill in the blank
    for index,letter in enumerate(string): #with enumerate we can use two parts to the for statement. Remember enumerate lets us unpack the tuple
        if index%2==0:
            word += letter.upper() #we are adding to the STRING, **NOT** adding to a list. 
        else:
            word += letter.lower()
    return word #The string has been added to, and stitched together. no need to join it. 


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
  PRACTICE PRACTICE PRACTICE PRACTICE PRACTICE PRACTICE PRACTICE PRACTICE
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/


def myfunc(string):
    word = ''  
    for index,letter in enumerate(string): 
        if index%2==0:
            word += letter.upper()
        else:
            word += letter.lower()
    return word 

def myfinc(string):
    word = ''
    for index,letter in enumerate(string):
        if letter%2==0:
            word += letter.lower()
        else:
            word += letter.upper()
        return word



def myfunc(string):
    word = ''
    for letter,index in enumerate(sting):
        if letter%2==0:
            word += letter.lower()
        else:
            word += letter.upper()
    return word



def myfunct(string):
    mylist = []
    for letter in range(len(string)):
        if word%2 == 0:
            mylist.append(string[letter].lower())
            mylist.append(string[letter].lower())
            mylist.append(string[letter].lower())
            mylist.append(string[letter].lower())
            mylist.append(string[letter].lower())
        else:
            mylist.append(string[letter].upper())
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)
    return ''.join(mylist)


def myfunc(string):
    mylist = []
    for letter in range(len(string)):
        if letter%2==0:
            mylist.append(string[letter].lower())
        else:
            mylist.append(string[letter].lower())
    retun ''.join(mylist)

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
      END PRACTICE END PRACTICE END PRACTICE END PRACTICE END PRACTICE 
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

## answer given in the books

def myfunc(string):
    mylist = []
    for letter in range(len(string)):
        if letter%2==0:
            mylist.append(string[letter].lower())
        else:
            mylist.append(string[letter].upper())
    return ''.join(mylist)

def myfunc(string):
    mylist = []
    for letter in range(len(string)):
        if letter%2 == 0:
            mylist.append(string[letter].lower())
        else:
            mylist.append(string[letter].upper())
    return ''.join(mylist) #the .join always needs to specify what it's joining in the list. in this case any string. 


#NOTES

def myfunc(string):
    mylist = [] # the list is empty, it will need a string in it later.
    for letter in range(len(string)): #string cant return a range alone which is what we need. the length gives the proper number for us to use to make the range function work! THIS IS HUGE! IT'S BASICALLY A CHEAT CODE! YOU NEED THE LENGTH OF WHATEVER WORD FOR A RANGE! 
        if letter%2==0:
            mylist.append(string[letter].lower()) #we add individual letters as single character strings into the blank list.
        else:
            mylist.append(string[letter].upper()) #same here
    return ''.join(mylist) #we join any strings in mylist with this command

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~ FUNCTION PRACTICE EXERCISES ~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\



#learning python function increases your python skills exponentially

# this also means the difficulties of problems you can solve also increases drastically.

#lets get some practice converting problem statements into python code. 

# we'll go through a series of function practice exercises. 

#after this lecture we will go through the solutions. 

# There are two options for this material:
    # try out the exercises yourself, then go through the solutions. 
    
    #treat the solutions as code-along lecture for more guided practicce. 

~~~~~~~~~~WARMUP SECTION~~~~~~~~~~~~~~


~~~~~~~~LESSER OF TWO EVENS~~~~~~~~~~~

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

# my attempt: (no google)

def lesser_of_two_evens(a,b):
    for num in (a,b):
        if a%2==0 and b%2==0:
            return 
#FAILED. You were trying to provide an uncessary for loop. Think of the nature of the problem. not simply what you did last.

#answer

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0: #if both are even return the lesser
        return min(a,b)
    else:                 #otherwise return the larger.
        return max(a,b)

#a simpler to break down answer
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        #both numbers even
        if a<b:
            result = a
        else:
            result = b
    else:
        #one or more numbers are odd! 
        if a>b:
            result = a
        else:
            result = b

    return result



#################################
~~~~~~~ ANIMAL CRACKERS~~~~~~~~~~

#Write a function takes a two-word string and returns True if both words begin with same letter

# sketch:
#if word1[0] == word2[0]: INDEXING NOT JUST THE LETTERS BUT ITEMS ON THE LIST
#   reuturn true

#my attempt no google.

def animal_crackers(text):
    words = text.split()
    if words[0][0]==words[1][0]
        return True
    else:
        return False
#testing....
success!

#book answer

def animal_crackers(text):
    wordlist = text.lower().split() # ADD LOWERCASE as a habbit for string related questions. 
    return wordlist[0][0] == wordlist[1][0]
#Note this is useful. no need for the if statement. only need the else if there is another key stipulation 

#follow along

def animal_crackers(text):
    wordlist = text.split()
    first = wordlist[0]
    second= wordlist[1]
    return first[0] == second[0]


~~~~~~~~~~~~MAKES TWENTY~~~~~~~~~~~~~~

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

#my attempt (you got this right last time. use your brain and no peeking)

def makes_twenty(*args): #colon you doink!
    return (sum(args) == 20) or (20 in args)
# SUCCESS! You still got it and i think you did better than last time! 

#book answer

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20


#follow along version
def makes_twety(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 or n2 == 20:
        return True
    else:
        return False
#remember if its a ture or false boolean, it can be one lined with a lot of ORs

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
 ~~~~~~~~~~~~LEVEL 1 PROBLEMS~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

#my attempt


def old_macdonald(name):
    firstletter = name[0]
    inbetween = name[1:3]
    forth= name[3] 
    restof = name[4:]
    return firstletter.upper()+inbetween+forth.upper()+restof

#almost. you had the idea close. only your output added extra characters.


|\\\\\\\\\\\\\\\\.capitalize() //////use it or lose it!//////////

def old_macdonald(name):
    firsthalf = name[:3] #learn 2 slice noob
    secondhalf = name[3:]
    return firsthalf.capitalize()+secondhalf.capitalize()
#book answer

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

#Master Yoda

#Given a sentence, return a sentence with the words reversed

my attempt:

def master_yoda(text):
    text.split()[-1::]

#book answer

def master_yoda(text):
    return ' '.join(text.split()[::-1])



#follow along version

def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)

#HOW TO USE .JOIN()

mylist = ['a','b','c']
'--'.join(mylist)
#output
'a--b--c'
#we take away the commas and concatonate! 


#ALMOST THERE

#Given an integer n, return True if n is within 10 of either 100 or 200

|\\\\\\\\\Again you should have read directions more closely. they told you to use .abs

#my attempt
def almost_there(n):
    return (range(90,111) == n) or (range(190,211) == n)
#wrong


#book answer
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
#abs() returns negatives as positives. useful here. We are telling n in these cases to subtract from 100 and two hundered given the two problems. if it's less than ten then we get a true. BUT, if we get a -1 to -10, the abs command will turn these positive! 

#follow along version

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <=10)

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
 ~~~~~~~~~~~~LEVEL 2 PROBLEMS~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/



#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#my attempt 

def find_33(ints):
    for number in len(ints):
        if [num:num+2] == 3:
            return True
        else
        return False

#it's a mess


#book answer

def has_33(nums):
    for i in range(0, len(nums)-1): #range(len()) seems to be a dynamic duo in python. Study that more. 
    
        if nums[i:i+2] == [3,3]: #you forgot the [3,3] when writing your script.
            return True  
    
    return False

#this is the one that tripped you up last time dont worry. let's break it down again.

#range and len work best in for statements. Keep that in mind. 

#follow along video

def has_33(nums):
    for index in range(0,len(nums)-1):
        if nums[index] == 3 and  nums[index+1] == 3:
            return True
    return False


PAPER DOLL

#Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    result = '' #we are filling the blank in for a string.
    for letter in text:
        result += letter*3 # much simpler than you were thinking. Try keeping it simple. 
    return result
#follow along

def paper_doll(text): #word = wwwooorrrddd
    result=''
    for letter in text:
        result += letter*3 #concatinating is the key
    return result


BLACKJACK

#Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST

#My attempt

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c)) #needed two () for some reason for sum. not sure why
    elif 11 in (a,b,c):
        if (sum((a,b,c)) - 10) <= 21:
            return sum((a,b,c)) - 10
        else:
            return 'BUST'
    elif sum((a,b,c)) > 21:
        return 'BUST'
#Small victory. almost got it you needed to peek at the book to understand you needed double() for some reason. Figure out why. Okay close as i can tell it needs the second () becase the first thing that needs to be placed is an iterable. a single number is not iterable.


#book answers

def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

#follow along version

def blackjack(a,b,c):
    if sum([a,b,c]) <=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
   #elif 11 in [a,b,c] and sum([a,b,c]) - 10 <= 21:  also works
        return sum([a,b,c]) - 10
    else:
        return 'BUST'

SUMMER OF 69
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

#my attempt:

def summer_69(arr):
total = 0

#book 

#While conditions were needed. thats where u were absent minded. 

def summer_69(arr):
    total = 0
    add = True #adding condition
    for num in arr: #usual for loop
        while add: #while conditions
            if num != 6: #if the number isnt 6
                total += num #add the number to the total
                break #stop looping
            else: #but if it is a six
                add = False #don't add it.
        while not add: #when you arent adding
            if num != 9: #if the number isn't 9
                break #dont add
            else: #if it is a 9
                add = True #add is set back to true
                break #stop looping
    return total
#you should look at textbook for while loops until its drilled into your skull.

#follow along:
def summer_69(arr):
    total= 0
    add = True
    for num in arr:
        while add:
            if num!=6:
                total+=num
                break #from the WHILE LOOP. NOT THE WHOLE LOOP
            else:
                add False
        while not add:
            if num != 9 :
                break
            else:
                add = True
                break
    return total




|\/|\/|\/|\/|\/|\/|\/|\/
~~CHALLENGING PROBLEMS~~
|\/|\/|\/|\/|\/|\/|\/|\/

#SPY GAME
#Write a function that takes in a list of integers and returns True if it contains 007 in order
#follow along



#book aanswer
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1


#follow along

def spy_game(nums):
    code = [0,0,7,'x']
    #[0,7,'x'] the code is removing one index at a time when it matches
    #[7,'x']
    #['x'] length =1
    for num in nums:
        if num == code[0]:
            code.pop(0) #code.remove(num) also works
    return len(code) == 1



#COUNT PRIMES:
#Write a function that returns the number of prime numbers that exist up to and including a given number


#follow along:
def count_primes(num):
    #check for 0 or 1 input
    if num < 2:
        return 0
    ##############    
    # 2 or greater
    ##############

    # store our prime numbers
    primes = [2]
    # counter going through every number up to input num
    x = 3 #keep adding to x until we reach num.
    while x <= num: 
        #check if x is prime
        for y in range(3,x,2):
            print(y)
            if x%y==0:
                X+=2
                break #break at for loop not while loop
            else:
                primes.append(x)
                x += 2
        print(primes)
        return len(primes)

#book
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2): #range(start,stop,[step])  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

#out
y=3 x=3 
y=3 x=5
y=5 x=7
y=3 x=3
y=3 x=5
y=5 x=7
y=7 x=9
y=9 x=11
[2, 3, 5, 7, 11]

#another faster version.

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

~~~~PYTHON RANGE~~~~~~~
range(start,stop,[step])


|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
YOU MESSED UP BECAUE YOU DONT FULLY UNDERSTAND RANGE FUNCTIONS STUDY THOSE
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

euler project. DO IT

~~~~PRINT BIG~~~~~~~~~~~~~

#Write a function that takes in a single letter, and returns a 5x5 representation of that letter

#book answer


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

#follow along

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4],'F':[4,9,4,9,9]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
~~~~~~~~~~~~~LAMBDA EXPRESSIONS, MAP, AND FILTER FUNCTIONS~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#you got this. you can do this. These questions were hard even for the instructor. Take ten. 

# map function
#first we get a function. if we dont have one, make one.
def square(num):
    return num**2
#then lets make a quick list
my_nums=[1,2,3,4,5]
#now we use the map function

#We could create a for loop for this, but in this case using a mapfunction would be faster! 
#map (func, *iterables)
map(square,my_nums)
#output
<map at 0x24500d02eb8>
# ? ? ? ? ? we still gotta do stuff. 

#you can iterate through it with a for loop

for item in map(square,my_nums):
    print(item)
#output
1
4
9
16
25
# oh cool

#another way you can use this. we can list.

list(map(square,my_nums))
#output
[1,4,9,16,25]

#lets try something else. Something more challenging. 

#lets try mapping a string instead of numbers. 

def splicer(mystring):
    if len(mystring)%2==0: #we will check if the string is even 
        return 'EVEN' # it will say even if it is. 
    else:
        return mystring[0] #or it will just return the first letter. 
#now for the list of names.

names = ['Andy','Eve','Sally']

#lets map it
list(map(splicer,names)) #no need to add the () to your functions in map. 
#output
['EVEN', 'E', 'S']

~~~~~~~FILTER FUNCTION!~~~~~~~~~~~~

#filter by a function that returns true or false. Filter returns the selected items not the entire thing. Maps in contrast would and would return literal true and flase in some cases if you're not specific enough.

REMEMBER #Map does it all, filter filters the unwanted garbage! 

#lets make one real quick

def check_even(num):
    return num%2==0

mynums = [1,2,3,4,5,6]
filter(check_even,mynums)
#output
<filter at 0x24500cad4a8>
#once again we gotta use it with something else not just use filter alone.
list(filter(check_even,mynums)) 
#output
[2,4,6]
#we can iterate through the results
for n in filter(check_even,mynums):
    print(n)
#Output
2
4
6


#now that we know about map and filter, we can learn about...
~~~~~~~~LAMBDA EXPRESSIONS~~~~~~~~~
#and why the filter and map functions are useful!

#We're going to explain the lambda expression by converting a function step by step into a lambda expression. 

Our function:

def square(num):
    result = num**2
    return result
square(3)
#output
9

#converting time
def square(num):
    return num**2
square(3)
#output
9
#we can write this on one line!
def square(num): return num**2
sqaure(3)
#output
9
#simpler!

square(num): num**2

# Now let's turn it into a lambda now AKA:

\\\ANONYMOUS FUNCTION\|/

square = lambda num: num**2 
square(3)
#output
9

# we will typically use these with maps and functions. lambdas take up less code and are easier to write. good for one time functions. 

mynums = [1,2,3,4,5,6]
list(map(lambda num:num**2,mynums))
#output
[1,4,9,16,25,36]

#lets try on the check evens from before. 
mynums = [1,2,3,4,5,6]
list(filter(lambda num:num%2 == 0, mynums))

#now the names
names = ['Andy','Eve','Sally']
list(map(lambda name:name[0],names)) #you dont have to use name. it's like for loops. anything can be put in there we do it for readability.
#output
['A','E','S']
#k lets reverse the names now. 
list(map(lambda name:name[::-1],names))
#output
['ydnA', 'evE', 'yllaS']

#not every function can be translated into a lambda expression. Use them when you can still easily read them. 

#small victory. you finished the lesson. But you dont fully get it yet. lets make sure you do by taking a breather and coming back to this. 

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
~~~~~~~~~~~~~~~~~~~NESTED STATEMENTS AND SCOPE~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

#take a look a look at this code


x = 25

def printer():
    x = 50
    return x
#what do you imagine the output of printer() is? 25 or 50?
print(x)
#output 
25

#okay what about print(printer(x))? 
#output
50

#Interesting! But how does Python know which x you're referring to in your code? This is where the idea of scope comes in. 

#scope can be described by 3 general rules
    #1. Name assignments will create or change local names by default.
    #2. Name references search (at most) four scopes, these are:
        #Local
        #Enclosing function locals
        #Global
        #Built-in python
    #3.Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
#LEGB Rule:

#L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

#E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

#G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

#B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

EXAMPLE:

range(0,10) # Built-in

name = 'This is a global name' #global

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        NAME = 'IM A LOCAL' #local
        print('Hello '+name) 
    
    hello()

greet()

# If you want to assign a value to a name defined at the top level of the program (i.e. not inside any kind of scope such as functions or classes), then you have to tell Python that the name is not local, but it is global. We do this using the global statement. It is impossible to assign a value to a variable defined outside a function without the global statement.

#You can use the values of such variables defined outside the function (assuming there is no variable with the same name within the function). However, this is not encouraged and should be avoided since it becomes unclear to the reader of the program as to where that variable’s definition is. Using the global statement makes it amply clear that the variable is defined in an outermost block.

Example:


x = 50

def func():
    global x #this move right here.
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)

#now x = 50 inside the function. But seriously dont do this. It's up there with saving in the root directory.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#bunch of problems we solved then we compare them with what the lecture gives. Looks like they were lazy and he just talks about them. pay attention closely and copy paste answers. This is a good day for us. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Sphere volume

def vol(rad):
    return ((4/3) * 3.14) * rad **3

#lecture answers

def vol(rad):
    return (4/3)*(3.14)*(rad**3) #better parenthesis usage than me here.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#check for a number in a range.

def ran_check(num,low,high):
        if num in range(low,high+1): #if the number is in the given range of the low and high numbers. always add +1 in range functions. 
             print(f'{num} is in the range between {low} and {high}.') # use the f'{x} sentences' to include your variables in a print function
        else: #otherwise if the number isnt in the range
            print('Sorry, wrong number.') #wise guy remark.


#book answer

def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
# .isupper() and .islower() are useful here. 

# write out the sentence and make it into a string.
# have two counters at zero for counting uppercase and lowercase. 
# for every lowercase in the string add one
# otherwise add one to uppercase.

def up_low(s):
    uppercase = 0 #start upper and lowercase at zero 
    lowercase = 0
    for letter in s: #Check each letter in the words.
        if letter.islower(): #if it's a lowercase letter
            lowercase += 1 #add one to the tally of lowercase letters
        elif: #if it isn't
            uppercase += 1 #we add a tally to the uppercase.
        else:
            pass #needed to add a pass in case it runs a space, or non alphabetical character. 
    print("Total no of uppercase character : ",uppercase) #we tell it to tell up the totals at the end. 
    print("Total no of lower case character : ",lowercase)

#Else needed for non alphabetic characters. 



# book answer


def up_low(s):
    d={"upper":0, "lower":0} #Book used Dictionary to store both the uppercase and lowercase. Nice touch. gotta remember that next time. 
    for c in s:
        if c.isupper(): #uppercase check
            d["upper"]+=1
        elif c.islower(): #lowercae check.
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]


#setup a new list
#check the original list.
# if its something new that isnt already on the new list, add the thing.
#otherwise move onto the next thing on the list. 
# return the new list when it's done checking. 

sample_List = [1,1,1,1,2,2,3,3,3,3,4,5] #list we are checking
def unique_list(lst): #define the function
    uni_list = []#blank list we will fiil unique items to
    for thing in lst: #check item in the list 
        if thing in uni_list: #if it's already in the unique items list 
            continue #check the next item. we don't want anything we already have
        else: #if it isn't in the unique list..
            uni_list.append(thing) # we add it to the unique list!
    return uni_list #when we are done checking the list, bring up the unique list to see what we have.

#Small Victory! First try and we returned no errors!

#book answer

def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x: #not in keyword used which saves a lot of writing, but they did the exact same approach! We're thinking like programmers! 
            x.append(a)
    return x
~~~~~~~~~~~~~~~~~~~~

#Write a Python function to multiply all the numbers in a list.

#Sample List : [1, 2, 3, -4]
#Expected Output : -24

# Start with a variable that equals one.
# check each number on the list one at a time. 
# multiply by the current value of the variable.
#return the variable when the list reaches it's end.

sample_List = [1, 2, 3, -4]
def multiply(nums):
    total = 1 # Start with a variable that equals one.
    for num in nums:# check each number on the list one at a time. 
        total *= num# multiply by the current value of the variable.
    return total#return the variable when the list reaches it's end.

# TWO FOR TWO! WOOT!

#book answer is the same as ours!  woot! 

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#lets try the almost there function exercise again.
#Given an integer n, return True if n is within 10 of either 100 or 200
#abs(num) returns the absolute value of a number
# it's true if the number equals anywhere between 90 and 110
#it's also true if the number is between 190 and 210
#no loops are needed here. we are checking if it is or isnt between those numbers. 

#the way i came up with.
def almost_there(n):
    if n in range(90,111):
        return True
    elif n in range(190,211):
        return True
    else:
         return False

#the way i came up with.

# the cool textbook version.

def almost_there(n):
    return (abs(n) == range(90,111)) and (abs(n)== range(190,211))
# mind the parenthesis abs is definitely a shortcut to writing a lot of code. 

~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python function that checks whether a passed in string is palindrome or not.

#if the word equals the word backwards 
#return true
def palindrome(s):
    return s.lower() == s.lower()[::-1] #[::-1] means reversing the string! .lower() for good measure!
#video version. Guy was lazier than me! he didnt put in anything other than the reverse index.

#book version 

#.replace function is a nice touch. I was wondering about that, and should have googled to see if there was a way to do that. 

def palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]   # Check through slicing

~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python function to check whether a string is pangram or not.

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"

#lecture provides an aplabet string. for the hell of it, im going to try and do without it! 

#create a variable list with the entire alphabet in it.

# check each letter one at a time. split up the string into letters.

#if the letter (in lowercase) is in the variable list 

#we remove it from the list. 

#if its not in there, continue on. 

#once the loop is finished if the variable list is empty return as true! 
def ispangram(s):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #list containing entire alphabet.
    for letter in s.split(): # check each letter one at a time. split up the string into letters.
        if letter.lower() in alphabet:#if the letter (in lowercase) is in the variable list 
            alphabet.remove(letter.lower())#we remove it from the list. 
        else: #if it's not in there 
            continue #move on. 
    print(aplabet) # Print the list just in case we miss any letters for good measure!
    if alphabet == []: #if the alphabet list is empty
        return True # return as true
    else: # otherwise
        return False # it's no bueno.

#Got it! I'm getting the hang of this! 

#Book answer  I'll need to watch the videos to better understand. But we got it!  


import string #imports a string to give us an alphabet to work off of.  

def ispangram(str1, alphabet=string.ascii_lowercase):  #adds the variable and sets it to lowercase. 
    alphaset = set(alphabet)  #uses set to say the alphaset is equal to the alphabet. 
    return alphaset <= set(str1.lower()) #check to see if the string is greater than or equal to alphabet. 

string.ascii_lowercase # this is the string all lowercased. 
#output
'abcdefghijklmnopqrstuvwxyz'


#check collections module tonight.

|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
~~~~~~~~~~~~~~~~~~~FIRST MILESTONE PROJECT~~~~~~~~~~~~~~~~~~~~~
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/
|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/

# You now know enough to create a real program!

# for your first milestone project, you will create a tic tac toe game for two human players.

# lets describe what the game will be like. 

#two players should be able to play the game (both sitting at the same computer)

# the board should be printed out every time a player makes a move

# You should be able to accept input of the player position and then place a symbol on the board. 

#we will use the numpad to match numbers to the grid on the tic tac toe board

#creating the first program is always a big leap, but you will come out the other end a much better programmer! 

#we've set up a walkthrough notebook for you to help guide you along with the functions you will need to  create. 

# lets explore what the game will look like once it's done.

#we'll also cover a few useful functions and go through the walkthrough notebook.

#let's get started. 


~~~~~~~STEP 1~~~~~~~
 #Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
   |   |   
{7}|{8}|{9}  #make this grid appear. Try and hide the numbers.
___|___|___  #make each position start as a ' ' in a dictionary.
   |   |     
{4}|{5}|{6}  
___|___|___
   |   |   
{1}|{2}|{3} 
   |   |   

   #spaces={' ':1,' ':2,' ':3,' ':4,' ':5,' ':6,' ':7,' ':8,' ':9} #maybe something like this. 

   #s={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',}
    #this is probably better 

    #fill these values in the print statement for the grid.

   |   |   
 s[7] | s[8] | s[9] 
___|___|___
   |   |   
 s[4] | s[5] | s[6] 
___|___|___
   |   |   
 s[1] | s[2] | s[3] 
   |   |   

   #thinking 4th dimmensionally here. leave the spaces for when it's returning blank. Ill do one better and change the value of 5 to x. now that i did that in jupiter im going to try and make a print statement out of this mess before i celebrate. concatonate and putting new lines in. 

   print('   |   |   \n'+' '+s[7]+' | '+s[8]+' | '+s[9]+' \n'+'___|___|___\n'+' '+s[4]+' | '+s[5]+' | '+s[6]+' \n'+'___|___|___\n'+'   |   |   \n'+' '+s[1]+' | '+s[2]+' | '+s[3]+' \n'+ '   |   |   \n')

   #output looks good. I was worried that it might create unintentional spacing issues. Small victory. hitting up inversion table for twenty mins. 

   #Lots of pain today. need to keep going. book uses a list index to generate the results. smarter move. Dictionary doesnt keep order unless I call speific terms but in my case it still would have worked. They also use the print command in every line to make it legible rather than use the newline function. That will make things easier on me. Ill adopt that.  100 k job.

# get your head in the game. 

#cleaned up print lines


from IPython.display import clear_output

def display_board(s):
    clear_output() #only works in jupiter

    print('   |   |   ')
    print(' '+ s[7]+' | '+s[8]+' | '+s[9])
    print('___|___|___')
    print(' '+s[4]+' | '+s[5]+' | '+s[6])
    print('___|___|___')
    print('   |   |   ')
    print(' '+s[1]+' | '+s[2]+' | '+s[3])
    print('   |   |   ')



# test the board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.


#player1 = input("Please pick a marker 'X' or 'O'")

#make a marker that we will assign later. its blank for now.

#while it is blank, ask the player if you want to be 'x' or 'o'

#if it's x, assign player 1 X, and player 2 as O
#if it's the other way around just assign them backwards. 

def player_input():
    marker = ''
    while marker == '':
        marker = input("Please pick a marker 'X' or 'O'").upper()
    if marker == 'x'.upper():
        return ("Player 1 is 'X', Player 2 is 'O'.")
    else:
        return ("Player 1 is 'O', Player 2 is 'X'.")  
# this works but if you input literally anything else. player 1 is o and 2 is x. the while not illustrated works better in this case. 

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'): #while not is more efficient of code. covers all bases in this instance.
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O') #returning these as tuples to unpack later
    else:
        return ('O', 'X')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                               Step 3:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

#board list
#marker (x or o)
#position

 def mark_board(board, marker,position):
    board[position]=marker #on the board the position works like an index whhich is where we assign our marker. 


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Step 4:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# write a function that checks to see if someone won. 

# three in a row top, middle, bottom accross. Then three down. then diagonally.

# 789,456,123,741,852,963,753,159

#good thing we arent playing chess right now. 


def win_check(s,mark):
    return ((s[7] == mark and s[8] == mark and s[9] == mark) or (s[4] == mark and s[5] == mark and s[6] == mark) or (s[1] == mark and s[2] == mark and s[3] == mark) or (s[7] == mark and s[4] == mark and s[1] == mark) or (s[8] == mark and s[5] == mark and s[2] == mark) or (s[9] == mark and s[6] == mark and s[3] == mark) or (s[7] == mark and s[5] == mark and s[3] == mark) or (s[1] == mark and s[5] == mark and s[9] == mark)) 


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Step 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

def turnxoro():
    % = random.randint('X','O')
    print("it's" + % +"'s turn")

    #this didn't work. 

#books way

import random

def choose_first():
    if random.randint(0, 1) == 0: #randint needs to be number
        return 'Player 2'
    else:
        return 'Player 1'

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#write a function that returns a boolean letting us know whether a space on the board is freely availible.
def space_check(s, position):
    return s[position] == ' '

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(s):
    for i in range(1,10):
        if space_check(s,i):
            return False
    return True





~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP 8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.
def player_choice(s):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(s,position): #while the position is not filled in yet with an x or o
        position = int(input('choose your next position: (1-9) '))
    return position #choose a number between 1-9 to enter the x or o

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP 9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    return input('again? yes or no: ').lower().startswith('y')


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Here comes the hard part! Use while loops and the functions you've made to run the game!

print ('welcome to tic tac toe')

while True:
    #reset the board
    theboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on: 
        if turn == 'Player 1':
            #player 1's turn

            display_board(theboard)
            position = player_choice(theboard)
            mark_board(theboard, player1_marker, position)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print('congratulations! You won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('the game is a draw! >:C')
                else:
                    turn = 'Player 2'
        else:
            #player 2's turn

            display_board(theboard)
            position = player_choice(theboard)
            mark_board(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('player 2 has won!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('the game is a draw! >:C')
                else:
                    turn = 'Player 1'
    if not replay():
        break


#gotta be kind to my future self and learn all this. From the start you tried doing all this without reading directions. Had you read step one you would have noticed they said to use a list when you were hung up on dictionaries. On that note try to remember other options not just the one you are currently fixated on. You were aware of this. 

#using the != in a while loop is another way can use the not function. 

#tuple unpacking. refresh your memory

#player1_marker , player2_marker = player_input() #this is tuple unpacking. you can check ask what player one and two assigned themselves as x or o

#when reviewing go back to tic tac toe. this is the right of passage for every programmer. 
def sum20():
    mylist = [2,4,1,6,5,40,-1,8,3,5,7,9,10]
    pairsOfNums = [] #list we will return our numbers in         
    for num in mylist: #check each number in our given list.
        if (20//num) in mylist: #if twenty divided by that number is in our list
            if num not in pairsOfNums: #and that number isn't in our return list yet 
                if (20//num) not in pairsOfNums: #and neither is twenty divided by number 
                    pairsOfNums.append(num) #add the numbers to the 
                    pairsOfNums.append(20//num)
    return pairsOfNums

    #cool you almost figured this out but the  // removes the decimals meaning you returned a few flase flags. maybe utilizing the remainder can help, but you gotta finish todays. lectures. 



#display the list 

# for every number in the list 


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Take 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           STEP ONE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

#write a function (board)

# set it up as a list. 
    #1-9 matches a number on the numpad. 

# 3x 3 board
from IPython.display import clear_output#works in jupiter only. 
def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    print(board[7]+' | '+board[8]+' | '+board[9]) #these were missing quotes
    print('---------')#fancy lines! Call crytek. 
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3]) 

#we can make this pretty later lets just make sure it works. 

#test the board. 
test_board = ['win','x','o','x','o','x','o','x','o','x']

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        STEP TWO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

#make an input function. 
    #assigns maker as an 'X' or an 'O'
    #use a while loop until its assigned


# start with an empty variable named marker we will fill it in ina sec. 

#while it's not equal to 'X' or 'O'
    #create input "do you wanna be X or O?"
#if the marker = x
    #player one is X, player 2 is O    
#else
    #player one is O, player two is X

def player_input():
    marker = ''# start with an empty variable named marker we will fill it in ina sec. 
    while not (marker == 'X' or marker == 'O'):#while it's not equal to 'X' or 'O'

        #create input "do you wanna be X or O?"
        marker = input('Player 1. Do you want to be \'X\' or \'O\'? ').upper() #this will capitalize regardless of input. 
    #if the marker = x
    if marker == 'X':
        #player one is X, player 2 is O    
        return ('X','O') #these are tuples we can uppack later! You should study tuple unpacking until you get it. 
    else:
        #player one is O, player two is X
        return ('O', 'X')

#testing in jupiter really quick. 
#Success! you had a spelling error but you figured it out on your own. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        STEP THREE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board,marker,position):
    board[position]=marker #one equals  not two otherwise we reassign the marker variable. 
def place_marker(board, marker, position): #spaces mean everything in python.
    board[position] = marker #board the list [position] the index, marker is the x or o that we add to the list. 
def place_marker(board, marker, position):
    board[position] = marker



#create a function
    # the board
    # marker x or o
    # position. 1-9

def place_marker(board, marker, position): #check spelling
    board[position] = marker #this one you couldnt understand what the directions were saying. but visually its asking for the how the marker is placed on the board. rememebr board works exactly like a list. so indexing is the name of the game here. 

#testing worked. but i need to cram this idea in my head until i get it. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        Step 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 4: Write a function that takes in a board and checks to see if someone has won.

#check the board for three in a row 
    #rows
    #columns
    #diagonals 
    #yes or no (mark)
def win_check(board, mark):
    return ((board[1] == board[2]==board[3]==mark) or 
    (board[4] == board[5]==board[6]==mark) or 
    (board[7] == board[8]==board[9]==mark) or (board[7] == board[4]==board[1]==mark) or 
    (board[8] == board[5]==board[2]==mark) or 
    (board[9] == board[6]==board[3]==mark) or (board[7] == board[5]==board[3]==mark) or 
    (board[1] == board[5]==board[9]==mark) or (board[0]==mark)) 

    #testing works. added a cheat code for fun. pressing zero will mean automatic win for player.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP FIVE 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

#PICK A number between 0 and 1 

#return player 1 or two depending

import random #importing random should look into this

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#random is not defined yet. going to need to learn better on this where it would be applied. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                              STEP 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

#true or false
    #is this space(positon) on this board free(blank)?

def space_check(board, position):
    return board[position] == ' '

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise

#check your board (list) to see if it is full.

def full_board_check(board): 
    for i in range(0,10):# for the index in your list
        if space_check(board, i): #if the space is blank 
            return False #return false
    return True #return true happens here because if we hit true on the board too soon it will false flag it for being a full board. indenting here matters big time. 
\^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|\/|\/|\/|\/|\/ #YOU MADE A LOT OF MISTAKES IN YOUR CODE UP HERE.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        Step 8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use. 

#input('Choose your next position: (1-9) ')
# position = 0 we have to make this something between 1-9 without

#while not statements are helpful for input commands. while not filled in keep bugging the user for a proper input.

def player_choice(board):
    position = 10 # if we start it at zero might trigger accidental win.

    while position not in [0,1,2,3,4,5,6,7,8,9] or not space_check(board,position): #include the 0 for the cheat code. 

        position = int(input('Choose your next position: (1-9) '))# must be an interger not a string. 
    return position

def player_choice(board):
    position = 10 #position must not equal anything on the list we check.

    while position not in [0,1,2,3,4,5,6,7,8,9] or not space_check(board, position): #while the posision is not filled in or a number 0-9 isnt put in.

        position = int(input('Choose your next position: (1-9) '))# must be an interger not a string. # it will ask you to put in an interger.
    #return the position you enter in. 
    return position 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP 9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

#write an input that asks if they want to play again.

#return true if person inputs yes:

def replay():
    return input("Do you want to play again? Yes or No?: ").lower().startswith('y') 

    #if theres no need for an else statement just use return on it's own. 
    # .lower() and .startswith() help idiot proof the answer. startswith should be remembered for any time you need an extra condition. be kin to your future self. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            STEP TEN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

#DONT PANIC. 

#write it out. 

#making mistakes is okay. the code will forgive you.


#welcome to tic tac toe 
print("welcome to tic-tac-toe!")


    #reset the board. 
    board = [' ']*11

    #player 1 is x or o?
    
    #goes first. 
    
    #while the game is running.
        #show the board

        #player 1 turn
    
            #check space
    
                #check win
    
                    #check full
    
                #else player 2 turn
    
        #player 2
    
            #check space
    
            #check win
    
                #check full
    
                #else player 1 turn.
    
    #if not replay() break.


###WHELP still lost. time to follow along.  

print('welcome to tic tac toe!')

while True:
    #play the game

    ###set everything up (board, whos first, choose markers x,o)
    theboard = [' ']*10
    player1_marker,player2_marker = player_input() #see step 2

    turn = choose_first() #step 5
    print(turn + ' will go first')#step 5 
    play_game = input("ready? Y or N") #asking if players are ready 
    if play_game == 'y'.lower(): 
        game_on = True #will let us proceed to next while loop
    else:
        game_on = False 

    ##gameplay 
    while game_on:
        ##player 1 turn
        if turn == 'Player 1':
            #show the board.
            display_board(theboard) #step 1
            #choose position
            position = player_choice(theboard)#step 8
            #place marker on position
            place_marker(theboard,player1_marker,position) #step 3
            #check win
            if win_check(theboard,player1_marker): #step 4
                display_board(theboard) #step 1
                print('Player 1 wins')
                game_on = False

            #check tie
            else:
                if full_board_check(theboard):#step 7
                    display_board(theboard) #step 1
                    print("tie game!")
                    game_on = False
                else:
                    turn = 'Player 2'
            #no tie and no win? then next player's turn. 

        

        else:
        ##player 2 turn
            turn == 'Player 2'
            #show the board.
            display_board(theboard) #step 1
            #choose position
            position = player_choice(theboard)#step 8
            #place marker on position
            place_marker(theboard,player2_marker,position) #step 3
            #check win
            if win_check(theboard,player2_marker): #step 4
                display_board(theboard) #step 1
                print('Player 2 wins')
                game_on = False

            #check tie
            else:
                if full_board_check(theboard):#step 7
                    display_board(theboard) #step 1
                    print("tie game!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

#break out of the  while loop on replay()



# you have a lot of spelling to fix here.  but you are otherwise good. take a small victory for debugging. but lets follow a youtube tutorial on tic tac toe after dinner.