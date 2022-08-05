from random import choice

class RandomWalk():
    #Class created to generate random walking
    def __init__(self, num_points=5000):
        #Initialing random walking atributes
        self.num_points = num_points
        
        #Starting point has a value (0,0)
        self.x_values = [0]
        self.y_values = [0]