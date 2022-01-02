"""
Stats provided by NFL Fantasy
Week 16, Top 10 Projected RBs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([10.80,1.00,25.90,6.90,13.50,7.80,9.00,14.50,10.90,12.80])
proj_points = np.array([17.07,16.14,15.21,14.61,14.57,14.44,13.70,13.52,13.48,13.41])
players = np.array(["J. Taylor\n(IND)","J. Robinson\n(JAX)","N. Chubb\n(CLE)","A. Kamara\n(NO)",
                    "N. Harris\n(PIT)","C. Patterson\n(ATL)","J. Williams\n(DEN)","A. Mattison\n(MIN)",
                    "J. Jacobs\n(LV)","A. Gibson\n(WFT)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 16, Top 10 Projected RBs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()