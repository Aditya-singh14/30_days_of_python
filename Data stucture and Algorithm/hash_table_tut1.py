def get_hash(key):
    h=0
    for char in key:
        h+=ord(char)                    #ord('a')--->returns ascii value of any character
    return h%10
print(get_hash("March 28"))