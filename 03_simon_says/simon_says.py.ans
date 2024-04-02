# write your code here

def echo(s):
    return s

def shout(s):
    return s.upper()

def repeat(s, count = 2):
    rs = s
    for i in range(count - 1):
        rs += " " + s
    return rs

def start_of_word(s,c):
    return s[0:c]

def first_word(s):
    return s.split(" ")[0]

def titleize(s):
    little_words = ["a", "on", "the", "of", "and", "is"]
    s_split=s.split(" ")
    for i in range(0,len(s_split)):
        if (i == 0):
            s_split[i] = s_split[i].capitalize()
        elif s_split[i] not in little_words:
            s_split[i] = s_split[i].capitalize()
        elif i == len(s_split) - 1:
            s_split[i] = s_split[i].capitalize()
    return " ".join(s_split)

