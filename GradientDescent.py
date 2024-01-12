import numpy as np

class GradientDescent:
    def __init__(self, w, b, a, data, error_range):
        self.w = w
        self.b = b
        self.a = a
        self.x_values = data[0]
        self.y_values = data[1]
        self.data_size = len(data[0])
        self.error_range = 0.1
    
    def step_descent(self):
        f = self.w*self.x_values + self.b
        temp_w = self.w - self.a*(1/self.m)*(np.sum(f*self.x_values))
        temp_b = self.b - self.a*(1/self.m)*(np.sum(f))

        # stores whether minimum reached
        ret = np.abs(temp_w-self.w) <= self.error_range and np.abs(temp_b-self.b) <= self.error_range

        self.w = temp_w
        self.b = temp_b
        
        # returns whether minimum reached
        return ret
    
    def complete_descent(self):
        while not self.step_descent():
            pass

    



        
