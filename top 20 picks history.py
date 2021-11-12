# Historical fantasy football data provided by fantasydata.com
# Record for TFFE 2016-2020

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

picks = []
for i in range(1,21):
    picks.append(str(i))

np.picks = np.array(picks)

# Outliers on the lower end of points scored are very likely due to injury
points2016 = np.array([254.3,246.1,218.4,158.4,176.7,367.8,7.5,257.1,155.0,153.4,
                       84.5,256.2,162.8,309.4,124,175.6,9.3,120.1,126.3,256.1])
points2017 = np.array([10.0,259.8,207.9,61.5,167.6,189.3,190.2,182.2,110.7,123.1,
                       151.9,192.9,134.4,175.5,351.3,261.8,212.2,188.6,188.7,154.2])
points2018 = np.array([342.6,290.7,221.6,340.3,271.7,191.84,276,109.4,269.4,126.4,
                       107.7,247.4,332.0,11.6,116.8,243.1,151.18,312.58,221.9,177.9])
points2019 = np.array([218.1,413.2,123.5,216.54,284.7,224.6,164.3,207.9,205.8,203.9,
                       14.1,199.2,168.1,221.4,214.1,207,174.3,132.0,146.6,126.1])
points2020 = np.array([81.9,12.4,197.7,63.9,323.6,158.0,260.26,315.8,120.6,89.1,
                       230.3,114.0,214.8,213.6,150.7,169.3,163.0,182.4,66.6,211.9])

plt.plot(np.picks, points2016, 'o', c = 'g', label = '2016', ms = 6)
plt.plot(points2017,  'o', c = 'r', label = '2017', ms = 6)
plt.plot(points2018, 'o', c='b', label = '2018', ms = 6)
plt.plot(points2019, 'o', c='black', label = '2019', ms = 6)
plt.plot(points2020, 'o', c='orange', label = '2020', ms = 6)
plt.title("Top 20 Draft Picks vs. Season Total Points")
plt.xlabel("Pick #")
plt.ylabel("Points scored")
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
plt.grid()
plt.show()

