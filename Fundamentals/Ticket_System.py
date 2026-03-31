movieName = input("Enter Movie Name: ")
basePrice = float(input("Enter Base Price: "))
age = int(input("Enter Your Age: "))
student = input("Are You Student?: ")
total_tickets = int(input("Total Number of Tickets: "))
price = basePrice


if age < 12:
    price = price - (price * 0.3)
elif age > 60:
    price = price - (price * 0.25)
if student.lower() == "yes":
    price = price - (price * 0.1)
if  total_tickets >= 5:
    price = price - (price * 0.15)


price = total_tickets * price

print("=============================================")
print(" 🎫 MOVIE TICKET INVOICE")
print("==============================================")
print("Movie Name                   :" , movieName)
print("Base Price                   :" , basePrice)
print("Age                          :" , age)
print("Student                      :" ,student)
print("Number Of Tickets            :" ,total_tickets)
print()
print("Final Price per Ticket       :" ,price / total_tickets)
print("Total Price                  :" ,price)
print("===============================================")
print("Thank You for Booking , Enjoy Your Movie 🍿")

