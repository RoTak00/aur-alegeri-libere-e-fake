const express = require("express");
const cors = require("cors");
const app = express();
const fs = require("fs");

// Allow all origins or specify a specific origin
app.use(
  cors({
    origin: "https://alegerilibere.ro", // Replace '*' with the specific origin if needed
  })
);

// Parse JSON payloads
app.use(express.json());

// Variable to store the last logged timestamp and last value
let lastTimestamp = 0;
let lastValue = null;

// CSV file path
const csvFilePath = "../output.csv";

// Function to append data to the CSV file
function appendToCSV(timestamp, valueDifference, currentValue) {
  const data = `${new Date(timestamp).toISOString()},${currentValue}\n`;

  // Append the data to the CSV file
  fs.appendFile(csvFilePath, data, (err) => {
    if (err) {
      console.error("Error writing to CSV file:", err);
    } else {
      console.log("Data appended to CSV:", data.trim());
    }
  });
}

app.post("/update", (req, res) => {
  const currentTimestamp = Date.now(); // Current time in milliseconds
  const receivedValue = parseFloat(req.body.nr); // Convert received value to a number

  // Check if the received value is a valid number
  if (isNaN(receivedValue)) {
    return res.status(400).json({ error: "Invalid value, must be a number" });
  }

  // Calculate the time difference in seconds
  const timeDifference = (currentTimestamp - lastTimestamp) / 1000;

  // Check if more than 10 seconds have passed since the last log
  if (timeDifference > 10) {
    if (lastValue !== null) {
      // Calculate the difference between the current and the last value
      const valueDifference = receivedValue - lastValue;

      // Log the difference to the console
      console.log(
        `[${new Date(
          currentTimestamp
        ).toISOString()}] Difference between values: ${valueDifference}`
      );

      // Write the log to CSV
      appendToCSV(currentTimestamp, valueDifference, receivedValue);
    }

    // Log the new value and update the last timestamp and value
    console.log(
      `[${new Date(currentTimestamp).toISOString()}] Received: ${receivedValue}`
    );
    lastTimestamp = currentTimestamp; // Update the last timestamp
    lastValue = receivedValue; // Store the last value of the current batch
  }

  // Respond to the client
  res.json({ status: "success", receivedValue });
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");

  // Create the CSV file with headers if it doesn't exist
  if (!fs.existsSync(csvFilePath)) {
    const headers = "timestamp,value_difference,current_value\n";
    fs.writeFileSync(csvFilePath, headers);
  }
});
