#Answer 1
x=int(input('Enter number 1:'))
y=int(input('Enter number 2:'))
z=int(input('Enter number 3:'))
result=(x+y+z)/3
print('The average of number is:',result)

print()
print()

#Answer 2
income=int(input('Enter your gross income:'))
dep=int(input('Enter number of dependents:'))
t= income-10000-(dep*3000)
print('Your annual tax is:', t*0.2)

print()
print()

#Answer 3
Name=input('Enter your name: ')
SID=int(input('Enter your sid: '))
Gender=input('Enter your gender: ')
Course=input('Enter your course name: ')
CGPA=input('Enter your CGPA: ')
Student=[SID,Name,Gender,Course,CGPA]
print(Student)

print()
print()

  #Answer 4
Marks1=int(input('Enter marks of 1st student '))
Marks2=int(input('Enter marks of 2nd student '))
Marks3=int(input('Enter marks of 3rd student '))
Marks4=int(input('Enter marks of 4th student '))
Marks5=int(input('Enter marks of 5th student '))
Marks=[Marks1,Marks2,Marks3,Marks4,Marks5]
Marks.sort()
print(Marks)

print()
print()

 #Answer 5
color=['Red', 'Green', 'White','Black', 'Pink', 'Yellow']
print(color)

#Part A
del color[3]
print('After Deleting 4th item,new list is:', color)

#Part B
color=['Red', 'Green', 'White','Black', 'Pink', 'Yellow']
color[3]=color[4]='purple'
print('Answer for part B:', color[0:4]+color[5:])
