def count(sequence,item):
    c = 0
    for char in sequence:
        if char == item:
            c += 1
    return c

print count([4,4,8,5,3,7,'foo','qoo'],5)

'''
The reason why my old function cannot work is:

def count(sequence,item):
    c = 0
    for char in sequence:
        if char == sequence:
            c += 1
    return c

Notice line 15, "if char == sequence:".
In my function, "char" will check "sequence", which means the list.
That means my function will check list exist or not, instead of check "item" in "sequence" list exist or not.
'''