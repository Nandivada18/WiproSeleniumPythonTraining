import re

#check if a string contains only digit
text = "1234899"
if re.match(r"^\d+$",text):
    print("Yes: ",text)
else:
    print("No")

# Pattern match a 10-digit mobile number
text = "1234567898"
if re.match(r"^\d{10}$",text):
    print("Yes: ",text)
else:
    print("No")

#find all lowercase letters
text = "abcDEF"
print(re.findall(r"[a-z]",text))

#find all uppercase letters
text = "abcDEF"
print(re.findall(r"[A-Z]",text))

#match a string at start
text = "Helloworld Hiiworld"
print(re.match(r"^Hello",text))

#match a string at end
text = "Helloworld Hiiworld"
print(re.search(r"world$",text))

#find all words separated by spaces
text = "Helloworld Hiiworld"
print(re.findall(r"\w+",text))

#match exactly 5 characters
text = "111 333 55555 766666676"
print(re.findall(r"\d{5}",text))

#Find all occurrence of word python
text = "pythondd PYTHONcode cat"
print(re.findall(r"python",text))

#replace all spaces in string with underscores
text = "pythondd pythoncode cat"
print(re.sub(r" ","_",  text))