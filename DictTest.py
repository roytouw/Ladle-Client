import re


var = 'This is a simple text !!!!'
# var = re.sub(r'(?<=\!!!!)', 'alib', var)
var = re.sub(r'(\!!!!)', 'ali', var)
print(var)
