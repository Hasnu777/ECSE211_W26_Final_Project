import numpy as np

ninety = "gyro_sensor_90_deg.csv"
eighty = "gyro_sensor_180_deg.csv"
nun = "gyro_sensor_do_nothing.csv"
straight = "gyro_sensor_straight.csv"
rotations = "gyro_sensor_rotations.csv"
base = "gyro_sensor.txt"

ninety_info = ""

with open(ninety,"r") as ninety:
    ninety_header = ninety.readline()
    baseNums = []
    rotedNums = []
    isBase = True
    for line in ninety:
        line = line.split(',')
        if isBase:
            baseNums.append(abs(int(line[0])))
            isBase = not isBase
        else:
            rotedNums.append(abs(int(line[0])))
            isBase = not isBase
    ninety_info += f"Base Mean: {np.mean(baseNums)}\nStandard Deviation: {np.std(baseNums)}\nBase 90'ed: {np.mean(rotedNums)}\nStandard Deviation 90'ed: {np.std(rotedNums)}\n"
    print(baseNums)
    print(rotedNums)

eighty_info = ""

with open(eighty,"r") as eighty:
    eighty_header = eighty.readline()
    baseNums = []
    rotedNums = []
    isBase = True
    for line in eighty:
        line = line.split(',')
        if isBase:
            baseNums.append(abs(int(line[0])))
            isBase = not isBase
        else:
            rotedNums.append(abs(int(line[0])))
            isBase = not isBase
    eighty_info += f"Base Mean: {np.mean(baseNums)}\nStandard Deviation: {np.std(baseNums)}\nBase 180'ed: {np.mean(rotedNums)}\nStandard Deviation 90'ed: {np.std(rotedNums)}\n"
    print(baseNums)
    print(rotedNums)

nun_info = ""

with open(nun,"r") as nun:
    nun_header = nun.readline()
    nums = []
    isBase = True
    for line in nun:
        line = line.split(',')
        nums.append(abs(int(line[0])))
    nun_info += f"Base Mean: {np.mean(nums)}\nStandard Deviation: {np.std(nums)}\n"
    print(baseNums)
    print(rotedNums)

print(ninety_info)
print(eighty_info)
print(nun_info)