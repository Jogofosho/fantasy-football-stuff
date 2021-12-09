"""
Stats provided by NFL Fantasy
Week 13, Top 10 WRs vs. Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([30.10,26.50,24.30,22.90,22.70,19.90,19.80,17.90,17.60,16.90])
proj_points = np.array([17.50,13.30,10.45,18.49,12.70,13.72,6.87,6.10,11.66,3.14])
players = np.array(["J. Jefferson\n(MIN)","D. Johnson\n(PIT)","T. Higgins\n(CIN)",
                    "C. Kupp\n(LAR)","C. Godwin\n(TB)","K. Allen\n(LAC)",
                    "A. St. Brown\n(DET)","D. Harris\n(NO)","E. Moore\n(NYJ)",
                    "J. Guyton\n(LAC)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 13, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()

