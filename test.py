import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the CSV file
data = pd.read_csv("output.csv", names=["Timestamp", "Number"])

# Convert the "Number" column to numeric (in case there are any formatting issues)
data["Number"] = pd.to_numeric(data["Number"], errors="coerce")

# Drop rows with invalid numbers
data.dropna(subset=["Number"], inplace=True)

# Generate an index column as a proxy for time (since the timestamp might not be equally spaced)
data["Index"] = range(len(data))

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(data["Index"], data["Number"])

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.plot(data["Index"], data["Number"], label="Actual Numbers", marker='o')
plt.plot(data["Index"], intercept + slope * data["Index"], label=f"Linear Fit: y={slope:.2f}x+{intercept:.2f}", color="red")
plt.title("Number Growth Analysis")
plt.xlabel("Time (Index)")
plt.ylabel("Number")
plt.legend()
plt.grid()
plt.show()

# Print the regression results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
