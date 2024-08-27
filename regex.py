import re


txt ="the cat sat on a mat with another cat"

pattern=r"cat"

matched =re.findall(pattern,txt)

print(matched)


#starting 

pattern =r"^the"

matched =re.findall(pattern,txt)

print(matched)

if matched: 
	print("match found")


#closing

pattern =r"cat$"

matched =re.findall(pattern,txt)

print(matched)

if matched: 
	print("match found")