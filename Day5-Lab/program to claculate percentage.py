#Program to accept student name , roll no ,marks of 5 subje t and calculate percentage and grade

#accept the data from the user
name = input("Enter your name: ")
roll_number = input("Enter your roll number: ")
print("Enter marks for the 5 subjects (out of 100):")

#initialize marks
marks = []

for i in range(1,6):
    subject_marks = float(input(f"Subject {i}:"))
    marks.append(subject_marks)

#Calculate total marks and percentage

total_marks = sum(marks)
percentage = total_marks/5

#determine the grade based on percentage
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C+'
elif percentage >= 40:
    grade = 'C'
else:
    grade = 'F'


#display the results
print("Student Report")
print("Student Name: ",name)
print("Student Roll Number: ",roll_number)
print("Total Marks Obtained: ",total_marks)
print(f"Percentage: {percentage:.2f}%")
print("Grade: ",grade)




