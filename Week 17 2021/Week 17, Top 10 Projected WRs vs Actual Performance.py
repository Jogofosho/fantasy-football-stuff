"""
Stats provided by NFL Fantasy
Week 17, Top 10 Projected WRs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([18.50,15.70,25.10,4.10,7.70,13.10,7.70,17.10,6.20,8.80])
proj_points = np.array([17.17,16.75,15.68,15.07,14.46,13.51,13.48,13.13,12.77,12.66])
players = np.array(["C. Kupp\n(LAR)","D. Samuel\n(SF)","D. Adams\n(GB)","A. Brown\n(TB)",
                    "T. Higgins\n(CIN)","D. Johnson\n(PIT)","S. Diggs\n(BUF)","H. Renfrow\n(LV)",
                    "J. Waddle\n(MIA)","J. Jefferson\n(MIN)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 17, Top 10 Projected WRs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()