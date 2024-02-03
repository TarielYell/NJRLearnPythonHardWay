#1.
# Excersise

print("Hello World")
print("Hello Again")
print("I like typing this.')
print "This is fun."
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

# Study Drills
print("This sentence is printed in \ two lines")

#2.
# A comment , this is a comment 

print("This line has a comment but won't get printed") # this is a comment


This is a multi line comment
see
this
wont
be
read
"""

#3.
# Exercise

print("I will now count my chickens:")
print("Hens,25 + 30 / 6)
print("Roosters", 100 - 25 x 3 % 4)
print("Now I will count the eggs:")
print(3 + 2 + 1  5 + 4 % 2 - 1 / 4 - 6)
print("Is it true that 3 + 2 < 5 -7 ")
print(3 + 2 < 5 - 7) # This returns a boolean value...nicee

# This shows that the print function can do mathematical functions in it


#4.
#Exercises

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are",cars,"cars available")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people today")
print("We have",passengers,"to carpool today")
print("We need to put about",average_person_per_car,"in each car")


#5.
my_name = 'mrjoker05'
my_age = 19
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name} . ")
print(f"He's {my_weight} inches tall.")
print(f"Acutally that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
total = my_age + my_height + my_weight
print(f"Total = {total}")

#6.
types_of_people = 10
x = f"There are {types_of_people}"
binary = "binary"
do_not = "don't"
y = f"Thos who know {binary} and those who {do_not}."

print (x)
print(y)
joke_eval = "Isn't that joke so funny ?! {}"
hilarious = False
print(joke_eval.format(hilarious))

#7.
print("Mary had a little lamb.")
print("Its fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print("."*10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6 ,end = ' ')
print(end7 + end8 + end9 +end10 + end11 + end12)

#8.
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    ))

#9.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print(days)
print(months)
print("""
        With three double quotes we can
        type multiline without special formatting
        """)

#10.
tabby = "\tI'm tabbed in."
persian = "I'm split\non a line."
backslash = "I'm \\ a \\ cat."
fat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print(tabby)
print(persian)
print(backslash)
print(fat)


#Escape What it does.
#\\ Backslash (\)
#\' Single-quote (')
#\" Double-quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only)
#\r Carriage return (CR)
#\t Horizontal tab (TAB)
#\uxxxx Character with 16-bit hex value xxxx
#\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
#\v ASCII vertical tab (VT)
#\000 Character with octal value 000
#\xhh Character with hex value hh


#11.
user_name =input("What is your name? ")
prompt = "> "
print(f"Hi {user_name}.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print(f"""
        Alright, so you said {likes} about liking me.
        You live in {lives}. Not sure where that is.
        And you have a {computer} computer. Nice.
        """)

#12.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes!")
    print("Man that's enough for a party!")
    print("Get a blanket\n!")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do maths inside too:")
cheese_and_crackers(5+10,60/3)

print("And we can combine the two, variables and maths:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+10)


#13.
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
