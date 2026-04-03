# Structure of Students Data
students =[ {"Name" : "Raghava",
            "Marks": [85 , 67 , 92],
            },

            {"Name" : "Raghu",
            "Marks": [85 , 67 , 92],
            },

            {"Name" : "Raghav",
             "Marks": [85 , 67 , 92],
            }
         ]
# average
def average(studentsList):
   for student in studentsList:
      marks = student['Marks']
      student['Average'] = sum(marks) / len(marks)

# grade
def grade(studentsList):
   for student in studentsList:
      avg = student['Average']
      if avg < 50:
         student['Grade'] = "Fail"
      elif avg < 60:
         student['Grade'] = "C"
      elif avg < 75:
         student['Grade'] = "B"
      elif avg < 90:
         student['Grade'] = "A"
      else:
         student['Grade'] = "A+"


# Details of Specific Student
def find_student(studentsList,name):
    for student in studentsList:
        if student['Name'] == name:
            print(f"Name    : {student['Name']}")
            print(f"Marks   : {student['Marks']}")
            print(f"Average : {student['Average']}")
            print(f"Grade   : {student['Grade']}")
            break
    else:
            print("OOPS! , Sorry no student found 🤷‍♂️")



# Print details of all Students
def students_list(studentsList):
   for student in studentsList:
      print(f"Name    : {student['Name']}")
      print(f"Marks   : {student['Marks']}")
      print(f"Average : {student['Average']}")
      print(f"Grade   : {student['Grade']}")
      print("--------------------")



# Add a Student details to list
def add_student(name , marks):
    dict = {"Name" : name, "Marks" : marks}
    students.append(dict)


# Execution Starts
while True:
# MENU
   print("""==================================
🎓 STUDENT MANAGEMENT SYSTEM
==================================
1. Add Student
2. View All Students
3. Search Student
4. Exit """)
   choice = int(input("Enter Choice: "))

# Matching cases
   match choice:
      case 1:
          new_name = input("Enter Student Name: ")
          user_input = input("Enter Marks separated by space: ")
          new_marks = list(map(int, user_input.split()))
          add_student(new_name,new_marks)
          print("Added Succesfully ✔️")

      case 2:
          average(students)
          grade(students)
          students_list(students)
      case 3:
          std = input("Enter Name: ")
          average(students)
          grade(students)
          find_student(students,std)
      case 4:
           print("Exiting System , Have a nice day! ☺️")
           break
      case _: print("Please enter a valid choice! 😅")


