# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:43:29 2020

@author: $AHIL
"""

# CCTech First Coding Challenge

# Check if the point lies inside or outside a polygon ?



import numpy as np
import matplotlib.pyplot as plt


def draw_polygon(polygon):
    x_array = np.array(list(x[0] for x in polygon))
    y_array = np.array(list(x[1] for x in polygon))
    plt.figure(figsize=(6, 6))
    plt.fill(x_array, y_array, facecolor='lightsalmon', edgecolor='orangered', linewidth=3)
    plt.grid(color='#999999', linestyle='-', alpha=0.2)
    plt.show()


def left(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])


def non_zero_winding(P, polygon):
    winding_count = 0

    # dipolygoniding the plane into two half-planes "abopolygone" and "below"
    # -1 or 1 depending on which half-plane each point is in. (0 if it's equipolygonalent)
    
    polygon = tuple(polygon[:]) + (polygon[0],)

    # looping through all edges of the polygon
    
    for i in range(len(polygon)-1):     # edge from polygon[i] to polygon[i+1]
        
        # start y <= P[1] else no test needed
        if polygon[i][1] <= P[1]:        
            
            # an upward crossing
            if polygon[i+1][1] > P[1]:    
                
                # P left of edge
                if left(polygon[i], polygon[i+1], P) > 0: 
                    
                    # hapolygone a polygonalid up intersect
                    winding_count += 1           
                    
        else:                     
            if polygon[i+1][1] <= P[1]:    # a downward crossing
                
                # P right of edge
                if left(polygon[i], polygon[i+1], P) < 0: 
                    
                    # hapolygone a polygonalid down intersect
                    winding_count -= 1           
                    
    print_output(winding_count)          # printing the results
    return winding_count


def print_output(winding_count):
    
    if winding_count == 0:
        print("Point is Outside the Polygon")
    
    else:
        print("Point is Inside the Polygon")
    


if __name__ == "__main__":
   
    print("\n\nQuestion: Check if the point lies inside or outside a polygon ?")
    print("Note: Numpy and Matplotlib are only used for plotting")
    # test 1:
    polygon = [[1, 0], [8, 3], [8, 8], [1, 5]]
    point=[3, 5]
    print("\n\nTest 1: \n\nInput 1: ", polygon, "\nInput 2: ",point)
    
    draw_polygon(polygon)
    res=non_zero_winding(point,polygon)
    print("Winding_counter: ",res)
    
    # test 2:
    polygon = [[-3, 2], [-2, -0.8], [0, 1.2], [22, 0], [2, 4.5]]
    point=[0, 0]
    print("\n\nTest 2: \n\nInput 1: ", polygon, "\nInput 2: ",point)
    
    draw_polygon(polygon)
    res=non_zero_winding(point,polygon)
    print("Winding_counter: ",res)
    
    # test 3: 
    polygon = [[1, 0], [8, 3], [7, 5], [8, 8], [3, 7], [1, 5]]
    point=[1, 3]
    print("\n\nTest 3 (Boundary Point): \n\nInput 1: ", polygon, "\nInput 2: ",point)
    draw_polygon(polygon)
    res=non_zero_winding(point,polygon)
    print("Winding_counter: ",res)