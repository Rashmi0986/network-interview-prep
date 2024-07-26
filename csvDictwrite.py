import re
import csv
from collections import defaultdict
from datetime import datetime

# Log contents as a string
log_contents = """
2024-07-25 14:23:45 INFO This is an info message
2024-07-25 14:45:12 ERROR This is an error message
2024-07-25 15:01:30 WARN This is a warning message
2024-07-25 15:30:20 INFO Another info message
2024-07-25 16:12:00 ERROR Another error message
"""

# Path to the output CSV file
output_csv_path = 'log_summary.csv'

# Function to process log contents from a string
def process_log_contents(log_contents):
    log_counts = defaultdict(lambda: defaultdict(int))

    # Regex pattern to match log entries
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)')

    for line in log_contents.strip().split('\n'):
        match = log_pattern.match(line)
        if match:
            timestamp_str, log_type, _ = match.groups()
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            time_period = timestamp.strftime('%Y-%m-%d %H:00:00')  # Group by hour
            log_counts[time_period][log_type] += 1

    return log_counts

# Process the log contents
log_counts = process_log_contents(log_contents)

# Write the summary report to a CSV file
with open(output_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['Time Period', 'INFO', 'ERROR', 'WARN']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for time_period in sorted(log_counts.keys()):
        counts = log_counts[time_period]
        row = {
            'Time Period': time_period,
            'INFO': counts.get('INFO', 0),
            'ERROR': counts.get('ERROR', 0),
            'WARN': counts.get('WARN', 0)
        }
        writer.writerow(row)

print(f"Summary report saved to {output_csv_path}")
