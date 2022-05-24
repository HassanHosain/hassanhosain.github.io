#https://www.youtube.com/watch?v=8ext9G7xspg&t=100s

#string concatenation (aka how to put strings together)
#example we want to create a string that says "subscribe to _____"

someVar = "test" #some string variable

#several methods
#print("subscribe to " + someVar)
#print("subscribe to {}".format(someVar))
#print(f"subscribe to {someVar}")

#using madlib

adj = input("Adjective:")
verb1 = input("Verb:")
verb2 = input("Verb:")
famous_person=input("Famous person:")

madlib = f"Computer programming  is so {adj}! It makes me so excited all the time becase \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)