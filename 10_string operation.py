name = input("Enter you FULL name : ")
phone_num = int(input(f" Enter you phone number : "))
result = len(name) 
result = name.find("u")
result = name.rfind("n")
name = name.capitalize()
name = name.lower()
name = name.isdigit()
result = name.imag

phone_num = phone_num.bit_count( )
phone_num = phone_num.bit_length()
phone_num = phone_num.__abs__()


print(phone_num)

# ✅ Rules for Naming String Variables in Python

# Must start with a letter (a–z, A–Z) or underscore (_)
# ✔ name, _msg
# ❌ 1name

# Cannot start with a number
# ❌ 2value
# ✔ value2

# Can contain only letters, numbers, and underscores
# ✔ user_name1
# ❌ user-name, user@name

# No spaces allowed
# ❌ first name
# ✔ first_name

# Case-sensitive
# Name, name, and NAME are different variables

# Cannot be a Python keyword (reserved word)
# ❌ if, else, for, while, class, str
# ✔ condition, loop_var, text

# Should not override built-in names (good practice)
# ❌ str = "Hello"
# ✔ message = "Hello"

# Use meaningful and readable names
# ✔ student_name, email_id
# ❌ x, a1

# No special characters allowed
# ❌ name!, price$, @data

# Unlimited length (but keep it readable)
# ✔ this_is_a_long_variable_name_for_message 

username = input("Enter a username : ")

if len(username) > 12:
    print(f"Your username can't be more than 12 charactor")
elif not username.find(" ") == -1 :
    print(f"Your username can't contain space")
elif not username.isalpha():
    print(f"username must not contain digits")
else:
    print(f" Welcome {username}")