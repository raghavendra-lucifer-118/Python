# Basic Menu For Input
print("============================")
print("🎓 STUDENT REPORT SYSTEM")
print("============================")

# Calculate Total
def calculate_total(m1,m2,m3):
    return m1 + m2 + m3

def calculate_avg(total_marks,n=3):
    return total_marks/n

def get_grade(avg):
    if avg < 50:
        return "Fail"
    if avg < 60:
        return "C"
    if avg < 75:
        return "B"
    if avg < 90:
        return "A"
    return "A+"


# Print the Report
def report(name, sci_marks, math_marks, eng_marks, total, average, grade):
    print("============================")
    print(" 📄 REPORT CARD")
    print("============================")
    print("Student Name   : " , name)
    print("Science Marks  : " , sci_marks)
    print("Math Marks     : " , math_marks)
    print("English Marks  : " , eng_marks)
    print("--------------------------")
    print("Total Marks    : ", total)
    print("Average        : ", average)
    print("Grade          : ", grade)
    print("============================")




# Taking Inputs from User
name = input("Enter Name: ")
sci = float(input("Enter Marks in Science: "))
maths = float(input("Enter Marks in Math: "))
eng = float(input("Enter Marks in English: "))



# Calculating total , average and grade
total = calculate_total(sci,maths,eng)
average = calculate_avg(total)
grade = get_grade(average)
report(name, sci, maths, eng, total, average, grade)

