# Stats provided by NFL Fantasy
# Week 11, Top 10 WRs vs Projected Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([33.20,27.00,25.60,20.60,20.30,19.60,18.80,18.40,18.20,18.20])
projPoints = np.array([14.15,15.80,5.23,9.90,7.07,13.26,10.76,6.23,11.62,9.71])
players = np.array(["J. Jefferson\n(MIN)","D. Adams\n(GB)","E. Moore\n(NYJ)","D. Mooney\n(CHI)",
                    "M. Valdez-\nScantling\n(GB)","D. Johnson\n(PIT)","T. McLaurin\n(WAS)","M. Goodwin\n(CHI)",
                    "A. Thielen\n(MIN)","M. Williams\n(LAC)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 11, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()