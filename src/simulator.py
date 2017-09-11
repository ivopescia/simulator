# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:45:51 2017

@author: pescia
"""

import numpy.random as random
import csv

segments =  {'young': 
         {"age": (15.0,4.0),
          "toys": {"A": 0.7, "B": 0.1, "C": 0.2}, 
         "read": {"A": 0.1, "B": 0.1, "C": 0.1, "D": 0.7},
         "pay": {"A": 0.1, "B": 0.2, "C": 0.5, "D": 0.2},
         "evening": {"A": 0.3, "B": 0.01, "C": 0.19, "D": 0.5},
         "move": {"A": 0.2, "B": 0.1, "C": 0.0, "D": 0.7},
         "music": {"A": 0.6, "B": 0.2, "C": 0.2},
         "office": {"A": 0.2, "B": 0.1, "C": 0.1, "D": 0.6}
         },
       'marry': 
          {"age": (30.0,5.0), 
          "toys": {"A": 0.5, "B": 0.4, "C": 0.1}, 
         "read": {"A": 0.4, "B": 0.3, "C": 0.2, "D": 0.1},
         "pay": {"A": 0.2, "B": 0.8, "C": 0.1, "D": 0.1},
         "evening": {"A": 0.6, "B": 0.1, "C": 0.2, "D": 0.1},
         "move": {"A": 0.4, "B": 0.4, "C": 0.1, "D": 0.1},
         "music": {"A": 0.2, "B": 0.5, "C": 0.3},
         "office": {"A": 0.1, "B": 0.1, "C": 0.7, "D": 0.1}
         },
       'career': 
          {"age": (35.0,10.0),
         "toys": {"A": 0.1, "B": 0.85, "C": 0.05}, 
         "read": {"A": 0.6, "B": 0.1, "C": 0.2, "D": 0.1},
         "pay": {"A": 0.3, "B": 0.5, "C": 0.05, "D": 0.15},
         "evening": {"A": 0.2, "B": 0.2, "C": 0.55, "D": 0.05},
         "move": {"A": 0.1, "B": 0.6, "C": 0.1, "D": 0.2},
         "music": {"A": 0.2, "B": 0.7, "C": 0.1},
         "office": {"A": 0.1, "B": 0.1, "C": 0.75, "D": 0.05}
         }, 
       'family': 
         {"age": (33.0,8.0),
         "toys": {"A": 0.2, "B": 0.05, "C": 0.75}, 
         "read": {"A": 0.2, "B": 0.65, "C": 0.1, "D": 0.05},
         "pay": {"A": 0.1, "B": 0.15, "C": 0.05, "D": 0.7},
         "evening": {"A": 0.05, "B": 0.9, "C": 0.05, "D": 0.0},
         "move": {"A": 0.05, "B": 0.15, "C": 0.75, "D": 0.05},
         "music": {"A": 0.3, "B": 0.6, "C": 0.1},
         "office": {"A": 0.5, "B": 0.3, "C": 0.15, "D": 0.05}
         },
       'forty': 
         {"age": (45.0,7.0),
         "toys": {"A": 0.3, "B": 0.2, "C": 0.5}, 
         "read": {"A": 0.25, "B": 0.1, "C": 0.6, "D": 0.05},
         "pay": {"A": 0.6, "B": 0.3, "C": 0.05, "D": 0.05},
         "evening": {"A": 0.2, "B": 0.4, "C": 0.3, "D": 0.1},
         "move": {"A": 0.05, "B": 0.2, "C": 0.6, "D": 0.15},
         "music": {"A": 0.1, "B": 0.4, "C": 0.5},
         "office": {"A": 0.05, "B": 0.6, "C": 0.2, "D": 0.15}
         }, 
       'retirement': 
         {"age": (67.0,12.0),
         "toys": {"A": 0.05, "B": 0.9, "C": 0.05}, 
         "read": {"A": 0.1, "B": 0.3, "C": 0.5, "D": 0.1},
         "pay": {"A": 0.8, "B": 0.1, "C": 0.0, "D": 0.1},
         "evening": {"A": 0.05, "B": 0.2, "C": 0.1, "D": 0.65},
         "move": {"A": 0.05, "B": 0.1, "C": 0.3, "D": 0.55},
         "music": {"A": 0.4, "B": 0.1, "C": 0.5},
         "office": {"A": 0.2, "B": 0.05, "C": 0.05, "D": 0.7}
         }}

samples = []
# start loop
for x in range(10000):
    sample = []
    
# determine segment
    sample.append(list(segments.keys())[random.randint(0,len(segments.keys()))])
    # determine age
    for j in segments[sample[0]].keys():
        if j == "age":
            sample.append(round(random.normal(segments[sample[0]]["age"][0], segments[sample[0]]["age"][1]),0))
        else:
            # determine a1-a7
            r = random.uniform()
            tmp = 0.0
            for y in segments[sample[0]][j].keys():
                if r < segments[sample[0]][j][y] + tmp:
                    sample.append(y)
                    break
                else:
                    tmp = segments[sample[0]][j][y] + tmp
    samples.append(sample)
    print(str(x) + " " + str(samples[x]))
    
with open('C:/Users/pescia/Downloads/samples.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples)
   
        