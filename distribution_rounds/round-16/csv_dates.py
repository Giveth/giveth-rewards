import csv
import datetime

def convert_unix_to_iso(unix_timestamp_ms):
    """Converts a Unix timestamp to ISO 8601 format."""
    return datetime.datetime.fromtimestamp(int(unix_timestamp_ms)//1000).isoformat()

input_file = 'praise.csv'
output_file = 'praise_iso8601.csv'

# Open the input and output files
with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
    reader = csv.reader(csv_input)
    writer = csv.writer(csv_output)

    # Read the header row and add a new column for converted timestamps
    header = next(reader)
    # header.append('ISO 8601 Timestamp')
    writer.writerow(header)

    # Process each row
    for row in reader:
        # Get the Unix timestamp from the desired column
        unix_timestamp_ms = row[1]  # Change 2 to the appropriate column index

        # Convert the Unix timestamp to ISO 8601 format
        iso_timestamp = convert_unix_to_iso(unix_timestamp_ms)

        # Append the converted timestamp to the row
        # row.append(iso_timestamp)
        row[1] = iso_timestamp
        # Write the updated row to the output file
        writer.writerow(row)

print(f"Conversion complete. Converted timestamps saved to {output_file}.")
