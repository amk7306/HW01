# Author: Abbey Kato amk7306@psu.edu

grade = input("Enter your course 1 letter grade: ")
credit = input("Enter your course 1 credit: ")
grade_average = str(grade)
credit_average = float(credit)

if grade == "A" or grade == "a":
  grade_point = float(4.0)
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "A-" or grade == "a-":
  grade_point = float(3.67)
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "B+" or grade == "b+":
  grade_point = float(3.33)
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "B" or grade == "b":
  grade_point = float(3.0)
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "B-" or grade == "b-":
  grade_point = float(2.67)
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "C+" or grade == "c+":
  grade_point = float(2.33)
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "C" or grade == "c":
  grade_point = float(2.0)
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "D" or grade == "d":
  grade_apoint = float(1.0)
  print(f"Grade point for course 1 is: {grade_point}")
else:
  grade_point = float(0.0)
  print(f"Grade point for course 1 is: {grade_point}")

grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
grade2_average = str(grade2)
credit2_average = float(credit2)

if grade2 =="A" or grade2 == "A":
  grade_point2 = float(4.0)
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="A-" or grade2 == "a-":
  grade_point2 = float(3.67)
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="B+" or grade2 == "b+":
  grade_point2 = float(3.33)
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 == "B" or grade2 == "b":
  grade_point2 = float(3.0)
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="B-" or grade2 == "b-":
  grade_point2 = float(2.67)
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="C+" or grade2 == "c+":
  grade_point2 = float(2.33)
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 == "C" or grade2 == "c":
  grade_point2 = float(2.0)
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 == "D" or grade2 == "d":
  grade_point2 = float(1.0)
  print(f"Grade point for course 1 is: {grade_point2}")
else:
  grade_point2 = float(0.0)

grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
grade3_average = str(grade3)
credit3_average = float(credit3)

if grade3 == "A" or grade3 == "a":
  grade_point3 = float(4.0)
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "A-" or grade3 == "a-":
  grade_point3 = float(3.67)
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "B+" or grade3 == "b-" :
  grade_point3 = float(3.33)
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "B" or grade3 == "b":
  grade_point3 = float(3.0)
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "B-" or grade3 == "b-":
  grade_point3 = float(2.67)
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "C+" or grade3 == "c+":
  grade_point3 = float(2.33)
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "C" or grade3 =="c":
  grade_point3 = float(2.0)
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "D" or grade3 == "d":
  grade_point3 = float(1.0)
  print(f"Grade point for course 1 is: {grade_point3}")
else:
  grade_point3 = float(0.0)
  print(f"Grade point for course 1 is: {grade_point3}")

print(f"Your GPA is: {(grade_point * credit_average + grade_point2 * credit2_average + grade_point3 * credit3_average )/ (credit_average + credit2_average + credit3_average)}")