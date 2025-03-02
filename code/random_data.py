import random

# File pointers to write into file
f1 =  open("code/lane2.txt", "w")
f2 =  open("code/lane3.txt", "w")
f3 =  open("code/lane4.txt", "w")

# Adjacent juntion lanes
r1 =  open("code/t_lane1.txt", "w")
r2 =  open("code/t_lane2.txt", "w")
r3 =  open("code/t_lane3.txt", "w")
r4 =  open("code/t_lane4.txt", "w")

# Vehicle classs to choose from 
vehicles = ['bicycle', 'car', 'motorcycle', 'bus', 'truck']

# Create an empty dictionary to store random vehicle-value pairs
vehicle_dict = {}

# Make a funciton so that it can be called multiple times
def random_count():
    vehicle_dict = {}
    for _ in range(5):
        random_vehicle = random.choice(vehicles)
        random_value = random.randint(1, 21)  # Random value between 1 and 100
        vehicle_dict[random_vehicle] = random_value
    return vehicle_dict
    
# Writing random counts to files --> lane1, lane2, lane3
f1.write(str(random_count()))
f2.write(str(random_count()))
f3.write(str(random_count()))

# Writing random counts to files --> t_lan1, t_lane2, t_lane3, t_lane4 [Adjacent Junction]
r1.write(str(random_count()))
r2.write(str(random_count()))
r3.write(str(random_count()))
r4.write(str(random_count()))

# Clearing all buffers and releasing all resources
f1.close()
f2.close()
f3.close()
r1.close()
r2.close()
r3.close()
r4.close()