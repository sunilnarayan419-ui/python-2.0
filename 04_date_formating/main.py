# Date formating 

# time between two date times 

from datetime import datetime 

a = datetime(2022 , 10 , 6 , 0 ,0, 0) 
b = datetime(2026 , 10 , 3 , 23 , 45 , 34) 

c = a - b 
print(c.days) 

print(c.total_seconds()) 


# Outputting datetime object to string 

from datetime import datetime 

datetime_for_string = datetime(2026, 10, 1, 0, 0)

datetime_string_format = "%d %m %Y, %H:%M:%S"

sd = datetime_for_string.strftime(datetime_string_format)
print(sd)

# Parsing string to datetime object 

from datetime import datetime 

datetime_string = "oct 1 2026 , 00:00:00" 

datetime_string_format = "%b %d %Y , %H:%M:%S" 

sd = datetime.strptime(datetime_string , datetime_string_format) 
print(sd) 
 
 
