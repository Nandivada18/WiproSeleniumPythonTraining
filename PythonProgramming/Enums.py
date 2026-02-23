#enumerate with list
fruits = ["orange" , "cherry" , "kiwi"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

#enumerate with start value changed
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# enumerate with strings
word = "python"
for i , ch in enumerate(word, start=2):
    print(i, ch)

#enumerate with tuple
fruits = ("orange" , "cherry" , "kiwi")
for index, fruit in enumerate(fruits):
    print(index, fruit)

# real time scenario
test_cases = ["Login", "Signup", "Checkout"]
for case_no, test in enumerate(test_cases, start = 1):
    print(f"Executing Testcase {case_no}: {test}")

# accessing of the enumerate values
a = ['God', 'is', 'Great']
b = enumerate(a)
next(b)
nxt_val = next(b)
print(nxt_val)

#duplicate detection using enumeration
characters = ["krillin", "Goku",  "Goku", "Gohan", "Piccolo",
              "krillin", "Goku", "vegeta","Gohan", "Piccolo",
              "piccolo", "Goku", "vegeta", "Goku", "piccolo"]
character_map = {character : [] for character in set(characters)}
for index, character in enumerate(characters):
    character_map[character].append(index)
print(character_map)
