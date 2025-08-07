#define the tuple
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

#create a list of all these employees
employees = [employee1,employee2,employee3]

#iterate through employees list
for emp in employees:
    print("Name: ",emp[0])
    print("Employee_ID: ",emp[1])
    print("Department: ",emp[2])
    print("Salary: ",emp[3])
    print("-"*28)
    
