# Input User Name
userName = input("Enter User Name: ")

# Input Password
password = input("Enter Password: ")

# Password Rules / Metrics
has_lower = False
has_upper = False
has_digit = False
strength  = ""
for c in password:
    if c.isupper():
        has_upper = True
    if c.islower():
        has_lower = True
    if c.isdigit():
        has_digit = True

if len(password) < 8:
    strength = "Weak"
elif has_digit and has_lower and has_upper:
    strength = "Strong"
else:
    strength = "Medium"


print("=======================")
print(" 🔐 User Details ")
print("=======================")
print("User Name         :" ,userName)
print("Has Uppercase     :" ,"Yes" if has_upper else "No")
print("Has Lowercase     :" ,"Yes" if has_lower else "No")
print("Has Digit         :" ,"Yes" if has_digit else "No")
print("Password Length   :" ,len(password))
print("Password Strength :" ,strength)
print("Password          :" ,"*" * len(password))





