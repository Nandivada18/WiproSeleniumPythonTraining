# match - match the exact sequence

import re
#o/p match object - matched sequence and span() - start and end index
text = "hello world"
result = re.match("hello",text)
print(result)

#using pattern
test_str ="12356778abckjnbdkkdABCabc"
pattern = re.compile("abc")
#re.finditer() finds all no-overlapping matches of a pattern in a string and
# returns an iterator of match objects (not a list)
matches = pattern.finditer(test_str)

for match in matches:
    print(match)

#Search operation searches the entire string
# returns teh first occurrence
text = "python of powerful maths powerful"
result = re.search("powerful",text)
print(result)

#serach - search the entire string - find the occurrence
#match - beginning only - validate the formates
# raw string for including the special character
a = r"\tHello"
print(a)

##finditer() - Find all substring where the RE matches, and returns them as an iterator.
#findall() -  find all the strings where the re matches return as list
#findall()
my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

#methods on match
#group() - Return the string matched by the RE
#start() - Return  the starting position of the match
#end() - Return the ending position of the match
#span() - Return the spam position of the match

test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    print(match.span(), match.start(),match.end())
    print(match.group())#return the substring that was matched by the RE

#special characters
#meta characters
#regular expressions
#pattern meaning
# abc Matches exact text
# [abc] a or b or c
# [a-z] lower letters
# [0-9] digits a-b
# any single character

text = 'I like abc and abcde'
result = re.findall("abc",text)
print(result)

#match exact abc where ever it is appearing
#match single characters: a or b or c
text = 'apple banana cat'
result = re.findall("[abc]",text)
print(result)

#[a-z] lower case letters
text = 'I like abc and ABCDEF'
result = re.findall("[a-z]",text)
print(result)

#[0-9] digits
text = 'I like abc and 123456ABCDEF'
result = re.findall("[0-9]",text)
print(result)

#'a b'
text = 'cab bat rat'
result = re.findall(".b",text)
print(result)

#special characters
'''
Special sequences begin with a backslash \
Sequence    Meaning    Example
\d  Digit (0–9)    \d\d
\D  Non-digit  \D
\w  Word char (a-z, A-Z, 0-9, _)   \w+
\W  Non-word char  \W
\s  Whitespace \s
\S  Non-whitespace \S
\b  Word boundary  \bcat\b
\B  Not a word boundary    \Bcat
'''
#\d Digit (0-9) \d\d
print(re.findall(r"\d","Order 123 costa 450"))

#\D Non-digit
print(re.findall(r"\D","Order 123 costa 450"))

#\w word char (a-z, A-Z, 0-9, _)
text = 'Python_3 version'
result = re.findall(r"\w",text)
print(result)

#\W Non-word char \W
# #matches anything that is NOT a word cahracter
text = 'Hello@123'
result = re.findall(r"\W",text)
print(result)

#\s Whitespace spaces, tabs and newline
text = "Hello world\nPython"
result = re.findall(r"\s",text)
print(result)

#\S Non-Whitespace \S - Matches anything that is not space, tab, newline
text = "Hi There"
result = re.findall(r"\S",text)
print(result)

#\b word boundary - Matches position at start or end of a word
text = 'cat scatter catalog'
result = re.findall(r"\bcat\b",text)
print(result)
# matches only full word cat

#\B not a  word boundary \B cat - Matches when pattern is a NOT at word boundary
text = 'cat scatter catalog'
result = re.findall(r"cat\B",text)
print(result)
'''
Meta-characters have special meaning in regex.

Meta-character  Meaning
.   Any character
^   Start of string
$   End of string
*   0 or more
+   1 or more
?   0 or 1
{n} Exactly n times
{n,}    n or more
{n,m}   Between n and m
[]  Character set
()  Grouping
'''

#^ Start of string
text  = "Python is easy"
print(re.findall(r"^Python",text))

#$ End of string
text  = "Python is easy"
print(re.findall(r"easy$",text))

#+ 1 or more
text  = "ab abb abbbb a"
print(re.findall(r"ab+",text))

#* 0 or more
text  = "ab abb abbbb a"
print(re.findall(r"ab*",text))

#? 0 0r 1
text  = "color colour colr"
print(re.findall(r"colour?",text))

#{n} Exactly
text  = "111 22 3333 68799"
print(re.findall(r"\d{3}",text))

#{n,} n or more
text  = "111 22 3333 68799"
print(re.findall(r"\d{3,}",text))

#{n,m} between n and m
text  = "111 22 3333 68799"
print(re.findall(r"\d{2,3}",text))

#[] character set
text  = "apple banana cat"
print(re.findall(r"[abc]",text))

#() Graphing
text  = "2026-02-11"
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})",text))

#Regular expression modifiers
'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''
#re.IGNORECASE re.I case - insesitive matching
text = "Python"
print(re.search("python",text,re.I))

#re.MULTILINE re.M - ^ and $ match each line\
text = "Hello\nPython"
print(re.findall("^Python",text,re.M))

#re.DOTALL re.S  matches newline
text = "Hello\nWorld"
print(re.search("Hello.*World",text,re.S))

#re.VERBOSE re.X write readable regex with comments - make it more readable
pattern = re.compile(r"""
     7879hbjockjsnjc..%%^^&&9
     """,re.X)
print(pattern)

#re.ASCII re.A ASCII - only matching
print(re.findall(r"\w+",text,re.A))

#re.DEBUG - Debug patterns
pattern = re.compile(r"""
     7879hbjockjsnjc..%%^^&&9
     """,re.DEBUG)
print(pattern)

#assertitions - validating the output or checking certain condition
"""
^ → Start of string
$ → End of string
\b → Word boundary
\B → Not word boundary
(?=...) → Positive Lookahead
(?!...) → Negative Lookahead
(?<=...) → Positive Lookbehind
(?<!...) → Negative Lookbehind
"""
#(?=...) Positive Lookahead= match only if followed by something
text = "user1 admin2 test"
print(re.findall(r"\w+(?=\d)", text))

#(?!...) Negative Lookahead
text = "user1 admin test2"
print(re.findall( r"\w+(?!\d)", text))

#(?<=...) Positive Lookbehind match pnly if preceeeded by something
text = "Price ₹500"
print(re.findall(r"(?<=₹)\d+", text))

#(?<!...) Negative Lookbehind
text = "500 ₹300"
print(re.findall(r"(?<!₹)\d+", text))

