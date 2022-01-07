"""
Stats provided by NFL Fantasy
Week 17, Top 10 Projected RBs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([5.80,17.90,2.80,18.50,28.10,18.70,6.80,19.10,13.10,16.00])
proj_points = np.array([16.76,15.87,15.65,15.52,15.05,14.84,14.71,14.65,13.86,13.85])
players = np.array(["N. Chubb\n(CLE)","J. Taylor\n(IND)","D. Cook\n(MIN)","A. Kamara\n(NO)",
                    "N. Harris\n(PIT)","A. Ekeler\n(LAC)","M. Carter\n(NYJ)","D. Montgomery\n(CHI)",
                    "A. Jones\n(GB)","J. Jacobs\n(LV)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 17, Top 10 Projected RBs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()