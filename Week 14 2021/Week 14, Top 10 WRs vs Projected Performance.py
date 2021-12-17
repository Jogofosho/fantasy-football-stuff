"""
Stats provided by NFL Fantasy
Week 14, Top 10 WRs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([29.10,24.80,24.70,22.80,22.20,18.10,17.90,17.90,17.00,16.70])
proj_points = np.array([15.97,17.15,10.68,10.67,13.79,11.01,5.52,5.80,19.09,7.59])
players = np.array(["D. Adams\n(GB)","C. Kupp\n(LAR)","T. Lockett\n(SEA)","J. Chase\n(CIN)",
                    "H. Renfrow\n(LV)","M. Evans\n(TB)","R. Anderson\n(CAR)","A. Lazard\n(GB)",
                    "J. Jefferson\n(MIN)","O. Beckham Jr.\n(LAR)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 14, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()

