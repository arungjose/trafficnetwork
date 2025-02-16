import random

# File pointers to write into file
f1 = open("lane1.txt", "w")
f2 = open("lane2.txt", "w")
f3 = open("lane3.txt", "w")

# Vehicle list
vehicles = ['bicycle', 'car', 'motorcycle', 'bus', 'truck']

# Function to generate random vehicle counts
def random_count():
    # Initialize a new dictionary for each call
    vehicle_dict = {}
    for _ in range(5):
        random_vehicle = random.choice(vehicles)
        random_value = random.randint(1, 21)  # Random value between 1 and 21
        vehicle_dict[random_vehicle] = random_value
    return vehicle_dict

# Generate and write data for each lane
a = random_count()
f1.write(str(a))

b = random_count()
f2.write(str(b))

c = random_count()
f3.write(str(c))

# Close files
f1.close()
f2.close()
f3.close()

