# Name: NISHANT KOTADIA
# ID: 20CS029


K = int(input())  # Taking the number for matching the rooms.

rooms = [int(i) for i in input().split(' ')]  # Creating an array for number of rooms entered by user.

sorted_array = list(set(sorted(rooms)))
captions_room = None

for item in sorted_array:                   # use for loop
    yes = 0
    no = 0
    for i in rooms:
        if item == i:
            yes += 1
        else:
            no += 1
    if yes == K:
        continue
    else:
        captions_room = item

print(captions_room)             #Print captions room
