#!/bin/bash

# Define the output CSV file
OUTPUT_FILE="output.csv"

# Write header to CSV if it doesn't exist
if [[ ! -f $OUTPUT_FILE ]]; then
    echo "Date,Number" > $OUTPUT_FILE
fi

# Loop indefinitely
while true; do
    
    # Make the curl request and extract the "nr" field
    RESPONSE=$(curl -s https://alegerilibere.ro/c.php)
    NUMBER=$(echo "$RESPONSE" | jq -r '.nr')

    CURRENT_DATE=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Append the date and number to the CSV file
    echo "$CURRENT_DATE,$NUMBER" >> $OUTPUT_FILE
    
    # Wait for 2 seconds before the next request
    sleep 30
done
