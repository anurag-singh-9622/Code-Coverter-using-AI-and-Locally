import numpy as np
import matplotlib.pyplot as plt

# Create a numeric vector
data = np.array([12, 15, 21, 20, 16, 14, 19, 18, 20, 21, 23, 22, 17, 15, 20])

# Calculate the median
median_value = np.median(data)

# Calculate the mean
mean_value = np.mean(data)

# Print the results
print(f"Median: {median_value}")
print(f"Mean: {mean_value}")

# Create a histogram
plt.hist(data, bins=10, color='blue', edgecolor='black')
plt.title("Histogram of Data")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()