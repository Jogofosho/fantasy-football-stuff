# Stats provided by NFL Fantasy
# Week 12, Top 10 WRs vs Projected Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([24.20,20.70,20.60,20.40,20.30,17.70,17.60,16.90,16.80,16.60])
proj_points = np.array([10.03,11.99,7.39,9.49,15.28,2.22,10.11,15.04,7.92,7.11])
players = np.array(["J. Waddle\n(MIA)","A. Thielen\n(MIN)","K. Bourne\n(NE)","T. Higgins\n(CIN)",
                    "D. Samuel\n(SF)","D. Jackson\n(LV)","H. Renfrow\n(LV)","S. Diggs\n(BUF)",
                    "V. Jefferrson\n(LAR)","O. Beckham Jr.\n(LAR)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 12, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()


