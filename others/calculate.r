# Create a numeric vector
data <- c(12, 15, 21, 20, 16, 14, 19, 18, 20, 21, 23, 22, 17, 15, 20)

# Calculate the median
median_value <- median(data)

# Calculate the mean
mean_value <- mean(data)

# Print the results
print(paste("Median:", median_value))
print(paste("Mean:", mean_value))

# Create a histogram
hist(data, main="Histogram of Data", xlab="Values", col="blue", border="black")
