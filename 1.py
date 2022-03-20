import math

course = input("Enter your course ")
print("Your " + course + " grades")
a = input("First grade ")
b = input("Second grade ")
c = input("Third grade ")
d = input("Fourth grade ")

course1 = input("Enter your course ")
print("Your " + course1 + " grades")
a1 = input("First grade ")
b1 = input("Second grade ")
c1 = input("Third grade ")
d1 = input("Fourth grade ")

course2 = input("Enter your course ")
print("Your " + course2 + " grades")
a2 = input("First grade ")
b2 = input("Second grade ")
c2 = input("Third grade ")
d2 = input("Fourth grade ")

n1_gpa = (float(a) + float(b) + float(c) + float(d)) / 4
print("Your " + course + " GPA is " + str(n1_gpa))

n2_gpa = (float(a1) + float(b1) + float(c1) + float(d1)) / 4
print("Your " + course1 + " GPA is " + str(n2_gpa))

n3_gpa = (float(a2) + float(b2) + float(c2) + float(d2)) / 4
print("Your " + course2 + " GPA is " + str(n3_gpa))

total_gpa = (n1_gpa + n2_gpa + n3_gpa) / 3
print("Your total GPA's average " + str(round(total_gpa)))

grades = ["A", "B", "C", "D", "F"]
index = 5 - math.floor(n1_gpa)
print("Your " + course + " GPA is " + grades[index])

index = 5 - math.floor(n2_gpa)
print("Your " + course1 + " GPA is " + grades[index])

index = 5 - math.floor(n3_gpa)
print("Your " + course2 + " GPA is " + grades[index])

if total_gpa > 3:
    print("You are getting your schoolarship ")
else:
    print("You are not getting your schoolarship ")