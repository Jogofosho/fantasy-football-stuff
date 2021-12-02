# Stats provided by NFL Fantasy
# Week 12, Top 10 RBs vs Projected Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([40.60,30.30,26.50,25.30,20.10,20.10,18.90,18.60,18.20,18.20])
proj_points = np.array([14.44,14.15,12.34,10.68,11.20,7.76,16.54,10.87,12.13,11.98])
players = np.array(["L. Fournette\n(TB)","J. Mixon\n(CIN)","C. Patterson\n(ATL)","E. Mitchell\n(SF)",
                    "A. Gibson\n(WAS)","J.D. McKissic\n(WAS)","A. Ekeler\n(LAC)","J. Williams\n(DEN)",
                    "M. Gaskin\n(MIA)","J. Jacobs\n(LV)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 12, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()






