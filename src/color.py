from idlelib.multicall import r


class Color:
    def __init__(self, name, red_mean, green_mean, blue_mean,  red_sd, green_sd, blue_sd):
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
        distance = (delta_red**2 + delta_green**2 + delta_blue**2)**0.5
        return distance



    # Compared the new normalized rgb values (s.d. method)
    def is_match(self, new_r, new_g, new_b):
        # Comparison values are true if the difference is <= 2 s.d.s
        print("R diff: ", abs(self.red_mean - new_r))
        print("G mean: ", self.green_mean)
        print("new_g = ", new_g)
        print(self.green_mean-new_g)
        print("G diff: ", abs(self.green_mean - new_g))
        print("B diff: ", abs(self.blue_mean - new_b))
        red_in_range = abs(self.red_mean - new_r) <= (2 * self.red_sd)
        green_in_range = abs(self.green_mean - new_g) <= (2 * self.green_sd)
        blue_in_range = abs(self.blue_mean - new_b) <= (2 * self.blue_sd)

        print("Red in range:", red_in_range)
        print("Green in range:", green_in_range)
        print("Blue in range:", blue_in_range)

        if (red_in_range and green_in_range and blue_in_range):
            return True

        return False
        


