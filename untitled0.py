# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:49:52 2018

@author: Enoch Appiah
"""
'''
from pylab import figure, show, legend, ylabel
 
# create the general figure
fig1 = figure()
 
# and the first axes using subplot populated with data 
ax1 = fig1.add_subplot(111)
line1 = ax1.plot([1,3,4,5,2], 'o-')
ylabel("Left Y-Axis Data")
 
# now, the second axes that shares the x-axis with the ax1
ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
line2 = ax2.plot([10,40,20,30,50], 'xr-')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ylabel("Right Y-Axis Data")
 
# for the legend, remember that we used two different axes so, we need 
# to build the legend manually
legend((line1, line2), ("1", "2"))
show()
'''

import matplotlib.pyplot as plt
fig2 = plt.figure()
ax1 = fig2.add_subplot(111)
line1 = ax1.plot([1,3,4,5,2], 'o-')
plt.ylabel("Left Y-Axis Data")
plt.legend()


ax2=fig2.add_subplot(111, sharex=ax1, frameon=False)
line2 = ax2.plot([10,40,20,30,50], 'xr-')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
plt.ylabel("Right Y-Axis Data")
plt.legend()
plt.show()