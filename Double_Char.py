#Double Char

#Given a string, you have to return 
#a string in which each character (case-sensitive) is repeated once.

#double_char("String") ==> "SSttrriinngg"
#double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
#double_char("1234!_ ") ==> "11223344!!__  "

def double_char(s):
    once = ""
    for i in range(len(s)):
        once += s[i]*2
    return once
