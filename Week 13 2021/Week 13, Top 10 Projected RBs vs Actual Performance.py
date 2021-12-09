"""
Stats provided by NFL Fantasy
Week 13, Top 10 Projected RBs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([24.30,18.70,26.80,9.40,14.90,19.90,11.10,13.20,18.10,8.50])
proj_points = np.array([19.28,16.42,16.25,16.15,15.32,15.32,15.32,14.00,13.83,13.54])
players = np.array(["J. Taylor\n(IND)","L. Fournette\n(TB)","J. Williams\n(DEN)",
                    "J. Mixon\n(CIN)","A. Ekeler\n(LAC)","A. Mattison\n(MIN)",
                    "C. Patterson\n(ATL)","N. Harris\n(PIT)","J. Conner\n(ARI)",
                    "J. Williams\n(DET)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 13, Top 10 Projected RBs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()
