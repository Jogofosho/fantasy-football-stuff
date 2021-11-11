import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

figure(figsize=(12, 6), dpi=80)

pointsFor = np.array([1116.68, 834.52, 986.86, 991.28, 1061.82,
                      1101.76,955.50,985.58,876.60,970.36])
wins = np.array([7,5,5,5,2,6,5,5,3,2])
colours = np.array(["red","green","yellow","cyan","magenta","black","orange",
                   "purple","grey","brown"])
teams = np.array(["YAF", "TBB", "TJ4U", "FDF", "HN-HF", "SMYT",
                  "ABS", "LKA", "CP", "GoJ"])

plt.scatter(pointsFor, wins, c=colours)
plt.axis([800,1200,0,8])
plt.title("Week 9, Points Scored vs. Wins")
plt.xlabel("Points scored")
plt.ylabel("Wins")
plt.grid()
plt.show


