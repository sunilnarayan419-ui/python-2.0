# STRING METHODS 

txt = " I am Sunil Narayan !!"

print("Original:", txt)

# Case methods
print(txt.capitalize())
print(txt.casefold())
print(txt.lower())
print(txt.upper())
print(txt.swapcase())
print(txt.title())

# Alignment methods
print(txt.center(40, "-"))
print(txt.ljust(40, "-"))
print(txt.rjust(40, "-"))
print("42".zfill(5))

# Search & count
print(txt.count("a"))
print(txt.find("am"))
print(txt.index("am"))
print(txt.rfind("a"))
print(txt.rindex("a"))

# Boolean check methods
print(txt.isalnum())
print(txt.isalpha())
print(txt.isascii())
print(txt.isdecimal())
print(txt.isdigit())
print(txt.isidentifier())
print(txt.islower())
print(txt.isnumeric())
print(txt.isprintable())
print(txt.isspace())
print(txt.istitle())
print(txt.isupper())

# Strip methods
print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())

# Replace & partition
print(txt.replace("Sunil", "SUNIL"))
print(txt.partition("Sunil"))
print(txt.rpartition(" "))

# Split methods
print(txt.split())
print(txt.rsplit())
print(txt.splitlines())

# Startswith / Endswith
print(txt.startswith(" "))
print(txt.endswith("!!"))

# Encoding
print(txt.encode())

# Join (IMPORTANT: join works on iterable)
print("-".join(["I", "am", "Sunil"]))

# Translate
table = str.maketrans("aeiou", "12345")
print(txt.translate(table))

# Format methods
print("My name is {}".format("Sunil"))
print("My name is {name}".format_map({"name": "Sunil"}))
 