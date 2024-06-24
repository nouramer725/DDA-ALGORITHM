import matplotlib.pyplot as plt

def dda_algorithm(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = max(dx, dy)
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    points = [(round(x), round(y))]

    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points, steps

# Example usage
x1, y1 = 1, 2
x2, y2 = 8, 5

points, num_steps = dda_algorithm(x1, y1, x2, y2)
print("Number of steps:", num_steps)
print("Points:", points)

# Plotting the line
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
plt.plot(x_values, y_values, 'bo-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('DDA Algorithm')
plt.show()


