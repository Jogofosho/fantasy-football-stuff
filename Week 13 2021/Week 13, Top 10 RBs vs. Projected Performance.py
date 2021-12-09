"""
Stats provided by NFL Fantasy
Week 13, Top 10 RBs vs. Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([26.80,24.30,24.10,20.40,19.90,19.60,19.50,18.70,18.20,18.10])
proj_points = np.array([16.25,19.28,13.49,12.59,15.32,12.85,11.14,16.42,10.91,13.83])
players = np.array(["J. Williams\n(DEN)","J. Taylor\n(IND)","D. Montgomery\n(CHI)",
                    "S. Michel\n(LAR)","A. Mattison\n(MIN)","A. Gibson\n(WFT)",
                    "J. Jacobs\n(LV)","L. Fournette\n(TB)","D. Freeman\n(BAL)",
                    "J. Conner\n(ARI)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 13, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()
