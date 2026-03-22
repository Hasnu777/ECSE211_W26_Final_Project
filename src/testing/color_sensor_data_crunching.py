import numpy as np

results = 'data_crunching_results.txt'

file = open(results, 'a')

dataFile = open('calibration_yellow.csv', 'r')

reds = []
greens = []
blues = []

vector_norm_reds = []
vector_norm_greens = []
vector_norm_blues = []

ratio_norm_reds = []
ratio_norm_greens = []
ratio_norm_blues = []

red_mean = 0
green_mean = 0
blue_mean = 0

red_vector_norm_mean = 0
green_vector_norm_mean = 0
blue_vector_norm_mean = 0

red_ratio_norm_mean = 0
green_ratio_norm_mean = 0
blue_ratio_norm_mean = 0

red_sd = 0
green_sd = 0
blue_sd = 0

red_vector_norm_sd =0
green_vector_norm_sd = 0
blue_vector_norm_sd = 0

red_ratio_norm_sd = 0
green_ratio_norm_sd = 0
blue_ratio_norm_sd = 0

dataFile.readline()

for line in dataFile:
    line = line.split(',')
    inted_line = []
    for entry in line:
        inted_line.append(int(entry))
    if '' in inted_line:
        continue
    reds.append(int(inted_line[0]))
    greens.append(int(inted_line[1]))
    blues.append(int(inted_line[2]))

    vector_denominator = (inted_line[0]**2 + inted_line[1]**2 + inted_line[2]**2)**0.5

    ratio_denominator = sum(inted_line)

    vector_norm_reds.append(inted_line[0]/vector_denominator)
    vector_norm_greens.append(inted_line[1]/vector_denominator)
    vector_norm_blues.append(inted_line[2]/vector_denominator)

    ratio_norm_reds.append(inted_line[0]/ratio_denominator)
    ratio_norm_greens.append(inted_line[1]/ratio_denominator)
    ratio_norm_blues.append(inted_line[2]/ratio_denominator)

    red_mean = np.mean(reds)
    green_mean = np.mean(greens)
    blue_mean = np.mean(blues)

    red_vector_norm_mean = np.mean(vector_norm_reds)
    green_vector_norm_mean = np.mean(vector_norm_greens)
    blue_vector_norm_mean = np.mean(vector_norm_blues)

    red_ratio_norm_mean = np.mean(vector_norm_reds)
    green_ratio_norm_mean = np.mean(vector_norm_greens)
    blue_ratio_norm_mean = np.mean(vector_norm_blues)

    red_sd = np.std(reds)
    green_sd = np.std(greens)
    blue_sd = np.std(blues)

    red_vector_norm_sd = np.std(vector_norm_reds)
    green_vector_norm_sd = np.std(vector_norm_greens)
    blue_vector_norm_sd = np.std(vector_norm_blues)

    red_ratio_norm_sd = np.std(vector_norm_reds)
    green_ratio_norm_sd = np.std(vector_norm_greens)
    blue_ratio_norm_sd = np.std(vector_norm_blues)


file.write("Data for yellow:"
           "\n"
           "\n"
           "Means: " + str(red_mean) + ", " + str(green_mean) + ", " + str(blue_mean) + ""
           "\n"
           "SD: " + str(red_sd) + ", " + str(green_sd) + ", " + str(blue_sd) + ""
           "\n"
           "Vector Normalised Means: " + str(red_vector_norm_mean) + ", " + str(green_vector_norm_mean) + ", " + str(blue_vector_norm_mean) + ""
           "\n"
           "Vector Normalised SD: " + str(red_vector_norm_sd) + ", " + str(green_vector_norm_sd) + ", " + str(blue_vector_norm_sd) + ""
           "\n"
           "Ratio Normalised Means: " + str(red_ratio_norm_mean) + ", " + str(green_ratio_norm_mean) + ", " + str(blue_ratio_norm_mean) + ""
           "\n"                                                                                                                                   
           "Ratio Normalised SD: " + str(red_ratio_norm_sd) + ", " + str(green_ratio_norm_sd) + ", " + str(blue_ratio_norm_sd) + ""
           "\n"
           "\n"
           "")