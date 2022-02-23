# Name: NISHANT KOTADIA
# ID: 20CS029


inputEnter = input()     #input from user

A = []            #createArray

for item in inputEnter:
    if item.islower():
        A.append(item.upper())
    elif item.isupper():
        A.append(item.lower())
    else:
        A.append(item)

print(''.join(A))           #print Result
