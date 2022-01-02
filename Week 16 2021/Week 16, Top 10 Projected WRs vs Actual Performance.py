"""
Stats provided by NFL Fantasy
Week 16, Top 10 Projected WRs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([16.30,23.60,28.40,15.10,37.40,12.10,18.00,11.50,20.20,15.60])
proj_points = np.array([17.17,16.75,15.68,15.63,14.46,13.80,13.48,13.13,12.77,12.66])
players = np.array(["C. Kupp\n(LAR)","D. Samuel\n(SF)","D. Adams\n(GB)","A. Brown\n(TB)",
                    "T. Higgins\n(CIN)","D. Johnson\n(PIT)","S. Diggs\n(BUF)","H. Renfrow\n(LV)",
                    "J. Waddle\n(MIA)","J. Jefferson\n(MIN)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 16, Top 10 Projected WRs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()