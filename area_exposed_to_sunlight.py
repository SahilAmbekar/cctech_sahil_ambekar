# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:22:39 2020

@author: $AHIL
"""

# CCTech Second Coding Challenge

# Calculate the surface of the building exposed to sunlight ?


import numpy as np
import math
import matplotlib.pyplot as plt
import sys


class AreaExposedToSunlight():
    
    def __init__(self, sun):        
        self.sun = sun
        
    def checks_for_sun(self, x_min, y_max):
        if self.sun[0] > x_min | self.sun[1] < y_max:
            print("Wrong Sun Position")
            sys.exit()
        
    #function to draw buildings
    def draw_polygon(self, building_coordinates):
        
        x_array = np.array(list(x[0] for x in building_coordinates))
        y_array = np.array(list(x[1] for x in building_coordinates))
        plt.figure(figsize=(8, 8))
        plt.axis('equal')
        plt.fill(x_array, y_array, 
                 facecolor='lightblue', 
                 edgecolor='orangered', 
                 linewidth=3)
        plt.grid(color='#999999', linestyle='-', alpha=0.2)
        plt.show()
        
    # calculating the min and max of both axis for starting poit and ending point
    def min_max_points(self, building_coordinates):
        
        x_min = min(x[0] for x in building_coordinates)
        y_min = min(x[1] for x in building_coordinates)
        x_max = max(x[0] for x in building_coordinates)
        y_max = max(x[1] for x in building_coordinates)
        
        # p_min defines point on bottom left i.e. start of building
        p_min = building_coordinates.index([x_min,y_min])
        
        # p_max defines point on top right 
        p_max = building_coordinates.index([x_max,y_max])
        
        # p_mid defines point on top left 
        p_mid = building_coordinates.index([x_min,y_max])
        
        self.checks_for_sun(x_min, y_max)   #check for sun's position
        
        return p_min, p_mid, p_max

    # Function for Distance calculation btn 2 points
    def calculate_distance(self, x1, y1, x2, y2): 
        
         dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
         return dist  
     
    def total_edges_exposed(self, building_coordinates):
        
        p_min,p_mid,p_max = self.min_max_points(building_coordinates)
        
        # Calculating distance of AB
        AB = self.calculate_distance(building_coordinates[p_mid][0],
                                building_coordinates[p_mid][1],
                                building_coordinates[p_min][0],
                                building_coordinates[p_min][1])
        
        # Calculating distance of BC
        BC = self.calculate_distance(building_coordinates[p_mid][0],
                                building_coordinates[p_mid][1],
                                building_coordinates[p_max][0],
                                building_coordinates[p_max][1])
        
        total = AB+BC
        
        print("\nEdges that are Exposed to Sunlight and their Lengths:")
        print("AB =",AB," BC =",BC,"\nAB + BC =",total)
        print("\nTotal length Exposed: ",total)
        
        self.draw_polygon(building_coordinates)
        
        print("\nThank You")
        
#    def user_inputs(self):



if __name__ == "__main__":
    
    print("\n\nQuestion: Calculate the surface of the building exposed to sunlight ?")
    print("Note: Sun position must have height > building and must be on left of the buildings.")
    
    
    building_coordinates = [[4,-2],[4,-5],[7,-5],[7,-2]]
    sun = [1,1]

    AreaExposedToSunlight(sun).total_edges_exposed(building_coordinates)
    





