weights = {
    "car": 3,
    "bus": 5, 
    "truck": 5,
    "bike": 2
}

alpha = 0.4
beta = 0.2
gamma = 0.4
time_factor = 60
internode_congestion = 70

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            try:
                vehicle_counts = eval(content)
                if not isinstance(vehicle_counts, dict):
                    raise ValueError("File doesn't contain a valid dictionary")
                return vehicle_counts
            except (SyntaxError, NameError) as e:
                print(f"Error parsing dictionary: {e}")
                return {}
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return {}

def calculate_intranode_congestion(filename, weights):
    vehicle_counts = read_file(filename)
    
    if not vehicle_counts:
        return 0
    
    total_congestion = 0
    
    for vehicle_type, weight in weights.items():
        count = vehicle_counts.get(vehicle_type, 0)
        congestion_contribution = count * weight
        total_congestion += congestion_contribution
    
    return total_congestion

def calculate_delta_value(filename):
    intranode_congestion = calculate_intranode_congestion(filename, weights)
    
    weighted_intranode = intranode_congestion * alpha
    weighted_internode = internode_congestion * beta
    weighted_time = time_factor * gamma
    
    delta_value = weighted_intranode + weighted_internode + weighted_time
    
    return delta_value

del_dict = {}

for i in range(4):
    fnum = i + 1

    filename = "code/lane" + str(fnum) + ".txt"
    key_lane = "lane" + str(fnum)
    
    delta_value = calculate_delta_value(filename)
    
    del_dict.update({key_lane : delta_value})


with open('code/junc_a.txt', 'w') as f:
    f.write(str(del_dict))

print("Delta values of Junction A calculated and stored in --junc_a.txt--")

del_dict = {}

for i in range(4):
    fnum = i + 1

    filename = "code/t_lane" + str(fnum) + ".txt"
    key_lane = "lane" + str(fnum)
    
    delta_value = calculate_delta_value(filename)
    
    del_dict.update({key_lane : delta_value})


with open('code/junc_b.txt', 'w') as f:
    f.write(str(del_dict))

print("Delta values of Junction B calculated and stored in --junc_b.txt--")