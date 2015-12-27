#Warning: This code will never run.

def anti_vowel(text):
    char = list(text)
    print (char[2])
    vowel = ['a','e','i','o','u','A','E','O','I','U']
    x = 0
    while char[0] == char[len(char)]:
        if char in vowel:
            out = ""
            x += 1
            return out
        else:
            out = char
            x += 1
            return out
    else:
        return out

print (anti_vowel("Hey You!"))
