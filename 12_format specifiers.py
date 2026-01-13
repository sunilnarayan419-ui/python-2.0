# format specifies = {value : flags} format a value based on what flags are inserted

# (number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :< = left justify
# :> = right justify
# :^ = center align 
# :+ = use a plus sign to indicate positive value
# :=  = place sign to leftmost position 
# : = insert sign before positive number
# : , = comma separator 

price1 = 3.145
price2 = 4.345
price3 = 5.678

print(f" Price 1 is ${price1:.2f}")
print(f" Price 2 is ${price2:.2f}")
print(f" Price 3 is ${price3:.2f}") 
