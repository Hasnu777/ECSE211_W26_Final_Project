class Color:
    def __init__(self, name, red_mean, green_mean, blue_mean,  red_sd, green_sd, blue_sd):
        self.name = name
        self.red_mean = red_mean
        self.green_mean = green_mean
        self.blue_mean = blue_mean
        self.red_sd = red_sd
        self.green_sd = green_sd
        self.blue_sd = blue_sd
    
    # Return an array with the cluster's RGB centers
    def get_center(self):
        return [self.red_mean, self.green_mean, self.blue_mean]
    
    # Returns an assray with the cluster's RGB sds
    def get_sd(self):
        return [self.red_sd, self.green_sd, self.blue_sd]
    
    # Compared the new normalized rgb values to the 
    # Return True if it's a match
    # Return False if it isn't a match
    def is_match(self, new_r, new_g, new_b):
        # Comparison values are true if the difference is <= 2 s.d.s
        red_in_range = abs(self.red_mean - new_r) <= (2 * self.red_sd)
        green_in_range = abs(self.green_mean - new_g) <= (2 * self.green_sd)
        blue_in_range = abs(self.blue_mean - new_b) <= (2 * self.blue_sd)

        if (red_in_range and green_in_range, blue_in_range): 
            return True
        
        return False
        
