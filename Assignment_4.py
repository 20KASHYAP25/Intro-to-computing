print("----------------------------------ASSIGNMENT 4-----------------------------")
print("")
print('-------------------------------Question #1----------------------------------')
print("SOL 1. :- Solution the problem of tower of Hanoi with three disks.")
print("")
def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')
print("")

###################################################################################

print("---------------------------------Question #2----------------------------------")
print(" ")
print(" ")
#input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops
print("\nUsing loops:\n")
for line in range(1, n+1):

    #everything else same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")

#####################################################################################

print("---------------------------------Question #3----------------------------------")
print(" ")

print(" ")
a=int(input("Enter the first integer: "))
b=int(input("Enter the first integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

###################################################################################

print("---------------------------------Question #4----------------------------------")
print(" ")
print(" ")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Lakshay Sheokand", 21105046)
print("Object created")

#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

#deleting object
del student1
print("")

#####################################################################################

print("---------------------------------QUESTION #5----------------------------------")
print("Solution to Problem 5:")
#creating class to store details of employees
class Employee:
    def __init__(self, emp_name, emp_salary):
        self.emp_name = emp_name
        self.emp_salary = emp_salary 
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#Part-a
print("part-a")
employee1.emp_salary = 70000
print(f"The Updated Salary Of {employee1.emp_name} Is {employee1.emp_salary} ")

#Part-b
print("part-b")
del employee3
print("Deleting record of employee Viren")
print("\n")
#####################################################################################

print("----------------------------------QUESTION #6---------------------------------")
word =input("Enter the word: ")
word=word.lower()

#inputting a meaningful word with the exact same letters
testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword=testword.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()