# Reads coordinates from file and outputs a graph of the coordinates using matplotlib

import matplotlib.pyplot as plt
# Read file 
text = open('route.txt', 'r')

xcoordinates = [];
ycoordinates = [];

# Read each line in the route file as x and y coordinates:
for line in text:
        mylist = line.split(",")
        xcoordinates.append(mylist[4])
        ycoordinates.append(mylist[3])

# Plot the route with red lines between coordinates: 
plt.plot(xcoordinates, ycoordinates, '.r-')
plt.show()