import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the CSV file
data = pd.read_csv("output.csv", names=["Timestamp", "Number"])

# Convert the "Timestamp" column to datetime
data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")

# Drop rows with invalid timestamps or numbers
data["Number"] = pd.to_numeric(data["Number"], errors="coerce")
data.dropna(subset=["Timestamp", "Number"], inplace=True)

# Calculate elapsed time in seconds from the first timestamp
data["Elapsed_Time"] = (data["Timestamp"] - data["Timestamp"].iloc[0]).dt.total_seconds()

# Perform linear regression using elapsed time
slope, intercept, r_value, p_value, std_err = linregress(data["Elapsed_Time"], data["Number"])

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.plot(data["Elapsed_Time"], data["Number"], label="Actual Numbers", marker='o')
plt.plot(data["Elapsed_Time"], intercept + slope * data["Elapsed_Time"],
         label=f"Linear Fit: y={slope:.2f}x+{intercept:.2f}", color="red")
plt.title("Number Growth Analysis (Time-Based)")
plt.xlabel("Elapsed Time (seconds)")
plt.ylabel("Number")
plt.legend()
plt.grid()
plt.show()

# Print the regression results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
