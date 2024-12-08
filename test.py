import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from scipy.stats import linregress

filename = "output.csv"
max_samples = None
sample_offset = None

#get args 
if len(sys.argv) > 1:
    filename = sys.argv[1]

if len(sys.argv) > 2:
    max_samples = int(sys.argv[2])

if len(sys.argv) > 3:
    sample_offset = int(sys.argv[3])



#check the file actually exists 

if not os.path.exists(filename):
    print(f"File {filename} does not exist")
    sys.exit(1)

if max_samples is not None and max_samples <= 0:
    print("Max samples must be a positive integer") 

if sample_offset is not None and sample_offset < 0:
    print("Sample offset must be a non-negative integer")

# Load the CSV file
data = pd.read_csv(filename, names=["Timestamp", "Number"])

# Convert the "Timestamp" column to datetime
data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")

# Drop rows with invalid timestamps or numbers
data["Number"] = pd.to_numeric(data["Number"], errors="coerce")
data.dropna(subset=["Timestamp", "Number"], inplace=True)

# Calculate elapsed time in seconds from the first timestamp
data["Elapsed_Time"] = (data["Timestamp"] - data["Timestamp"].iloc[0]).dt.total_seconds()

no_values = data["Number"].count()

# if max_rows is set, take the first max_rows rows with offset 
if max_samples is not None: 
    if sample_offset is not None:
        data = data.iloc[sample_offset:sample_offset+max_samples]
    else:
        data = data.head(max_samples)

no_reduced_values = data["Number"].count()
# Perform linear regression using elapsed time
slope, intercept, r_value, p_value, std_err = linregress(data["Elapsed_Time"], data["Number"])

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.plot(data["Elapsed_Time"], data["Number"], label="Actual Numbers", marker='o')
plt.plot(data["Elapsed_Time"], intercept + slope * data["Elapsed_Time"],
         label=f"Linear Fit: y={slope:.2f}x+{intercept:.2f}", color="red")
plt.title(f"From {data['Timestamp'].iloc[0]} to {data['Timestamp'].iloc[-1]} ({no_reduced_values}/{no_values} values)")
plt.xlabel("Elapsed Time (seconds)")
plt.ylabel("Signatures")
plt.legend()
plt.grid()
plt.show()

# Print the regression results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
