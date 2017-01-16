import string

a = string.ascii_letters
vowels = 'aeiou'
i = int(len(a)/2) - 1
alfa = int(len(a)/2)
z = ''
while i > -1:
    if a[i] in vowels:
        z += (a[i+alfa])
    else:
        z += (a[i])
    i -= 1
print(z)

