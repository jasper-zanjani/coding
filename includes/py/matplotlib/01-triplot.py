import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

# 1. Define the points (vertices) of the triangles
x = np.array([0, 1, 0, 0.5])
y = np.array([0, 0, 1, 0.5])

# 2. Define the triangles by specifying the indices of the vertices
# Each row in 'triangles' represents one triangle, with the numbers
# being the indices of the points in the 'x' and 'y' arrays.
triangles = np.array([[0, 1, 3], [0, 3, 2]])

# 3. Create a Triangulation object
# This object represents the triangulation of the given points.
triang = tri.Triangulation(x, y, triangles)

# 4. Create the plot
fig, ax = plt.subplots()

# 5. Use triplot to plot the triangulation
# 'ax.triplot()' takes the Triangulation object as input.
ax.triplot(triang, color='r', linewidth=0.5)

# Optional: Add the original points for clarity
ax.plot(x, y, 'o', color='r', markersize=8, label='Points')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Triplot Example')
ax.legend()

# Display the plot
plt.show()
