
#Question: What does "for ahci in text" mean?

def anti_vowel(text):
    vowels = ['a','e','i','o','u','A','E','O','I','U']
    out = ''
    for ahci in text:
        if ahci not in vowels:
            out += ahci
    return out

print (anti_vowel("heeeoooojbcxzaaa!"))
