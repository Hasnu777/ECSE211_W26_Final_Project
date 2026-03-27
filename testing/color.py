"""
Purpose of this files: Color class used in the color_identification files (for both unit vector and ratio)
How to test with this code?:

"""


from idlelib.multicall import r

THRESHOLD = 5


class Color:

    def __init__(self, name, red_mean, green_mean, blue_mean, red_sd, green_sd, blue_sd):
        self.name = name
        self.red_mean = red_mean
        self.green_mean = green_mean
        self.blue_mean = blue_mean
        self.red_sd = red_sd
        self.green_sd = green_sd
        self.blue_sd = blue_sd

    def get_name(self):
        return self.name

    # Return an array with the cluster's RGB centers
    def get_center(self):
        return [self.red_mean, self.green_mean, self.blue_mean]

    # Return an array with the cluster's RGB sds
    def get_sd(self):
        return [self.red_sd, self.green_sd, self.blue_sd]

    # Return the distance between unknown color and this one
    def find_distance(self, new_r, new_g, new_b):
        delta_red = new_r - self.red_mean
        delta_green = new_g - self.green_mean
        delta_blue = new_b - self.blue_mean
        distance = (delta_red ** 2 + delta_green ** 2 + delta_blue ** 2) ** 0.5
        return distance
