#!/bin/bash

# Define the output CSV file
OUTPUT_FILE="output.csv"

# Write header to CSV if it doesn't exist
if [[ ! -f $OUTPUT_FILE ]]; then
    echo "Date,Number" > $OUTPUT_FILE
fi

# Loop indefinitely
while true; do
    # Get the current date
    CURRENT_DATE=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Make the curl request and extract the "nr" field
    RESPONSE=$(curl -s https://alegerilibere.ro/c.php)
    NUMBER=$(echo "$RESPONSE" | jq -r '.nr')
    
    # Append the date and number to the CSV file
    echo "$CURRENT_DATE,$NUMBER" >> $OUTPUT_FILE
    
    
done
