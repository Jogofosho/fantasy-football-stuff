# Stats provided by NFL Fantasy
# Week 12, Top 10 Projected RBs vs Actual Performance

# NOTE: NFL Fantasy removed Christian McCaffrey's projection after being placed
# on IR. Projection for his week 12 performance provided by fantasydata.com

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([17.70,3.50,18.90,2.40,11.30,5.20,8.90,40.60,17.50,30.30])
proj_points = np.array([17.65,16.96,16.54,16.46,15.21,14.98,14.60,14.44,14.21,14.15])
players = np.array(["J. Taylor\n(IND)","C. McCaffrey\n(CAR)","A. Ekeler\n(LAC)","D. Swift\n(DET)",
                    "D. Cook\n(MIN)","N. Harris\n(PIT)","D. Montgomery\n(CHI)","L. Fournette\n(TB)",
                    "A. Dillon\n(GB)","J. Mixon\n(CIN)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 12, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()


