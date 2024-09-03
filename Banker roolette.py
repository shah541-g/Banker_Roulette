import random
import time

# seeding current second
random.seed(int(time.strftime('%S')))
selected_one = random.randint(0,5)

# provide names comma seperated
names = input("Provide names of your friends, seperated by comma: ").strip()

# converting to a list by splitting at the comma
friends = names.split(',')

# removing empty and vacant spaces
if "" in friends:
    friends.remove("")
if " " in friends:
    friends.remove(" ")

# getting length of list
total_names=len(friends)


selected_one = random.randint(0,total_names-1)
print(f"{friends[selected_one]} is the one who will Pay the bill.")