# keyword arguments = an arguments precede by an identifier
# help with readability
# order of aurguments doens't matter

def hello(greeting , title , first , last):
    print(f"{greeting} {title} {first} {last}")
    
hello("Hello", title="Mr" , first="sunil",last="narayan")


for x in range(1,11):
    print(x, end=" ")
    
print("1","2","3", sep=" ")

# ex 1 
def get_phone(country , area , first , last ):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=81,first=234,last=2345)

print(phone_num)