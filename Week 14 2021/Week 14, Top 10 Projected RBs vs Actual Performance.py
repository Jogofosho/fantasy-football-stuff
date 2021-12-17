"""
Stats provided by NFL Fantasy
Week 14, Top 10 Projected RBs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([15.40,34.70,21.20,22.50,23.90,12.90,3.10,20.80,29.00,7.50])
proj_points = np.array([18.20,16.40,16.18,15.49,15.33,15.03,14.80,14.52,14.08,14.08])
players = np.array(["A. Ekeler\n(LAC)","D. Cook\n(MIN)","L. Fournette\n(TB)","A. Kamara\n(NO)",
                    "N. Harris\n(PIT)","C. Patterson\n(ATL)","A. Gibson\n(WFT)","J. Williams\n(DEN)",
                    "J. Conner\n(ARI)","J. Jacobs\n(LV)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 14, Top 10 Projected RBs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()
