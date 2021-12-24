"""
Stats provided by NFL Fantasy
Week 15, Top 10 Projected RBs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([10.10,23.00,15.80,10.20,4.10,16.20,16.30,3.60,15.50,10.90])
proj_points = np.array([17.22,16.84,16.57,16.20,15.82,15.48,15.10,15.04,14.62,14.58])
players = np.array(["D. Cook\n(MIN)","J. Taylor\n(IND)","N. Chubb\n(CLE)","L. Fournette\n(TB)",
                    "A. Kamara\n(NO)","A. Ekeler\n(LAC)","J. Robinson\n(JAX)","N. Harris\n(PIT)",
                    "A. Gibson\n(WAS)","J. Jacobs\n(LV)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 15, Top 10 Projected RBs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()