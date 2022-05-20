# print on a new line directly
print("hey this is a string being printed!")

# declare my variable
x = "my variable is printing!"
# print my variable
print(x)

# print an empty line
print()

# declare my variables
myName = "Sasha"
myAge = 32
# print a sentence
print("Hello", myName, "you are", myAge, "years old")
# change the seperator
print("Hello", myName, "you are", myAge, "years old", sep="--")
# remove seperator
print("Hello", myName, "you are", myAge, "years old", sep="")

# empty line
print()

# declare array variable
words = ["dont", "ask", "too", "many", "questions"]
# print my variables
print(words)

# printing the array
print("The sentence is: ")
for i in words:
    print(i, end=' ')
