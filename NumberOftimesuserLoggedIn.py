import re
from collections import defaultdict
from datetime import datetime

# Example log content as a string
log_content = """
2023-07-26 10:00:00 INFO User logged in: user1
2023-07-26 10:05:00 ERROR Failed to load resource: resource1
2023-07-26 10:10:00 INFO User logged out: user1
2023-07-26 10:15:00 WARN Disk space low on server: server1
2023-07-26 10:20:00 INFO User logged in: user2
2023-07-26 10:25:00 ERROR Failed to load resource: resource2
2023-07-26 10:30:00 INFO User logged out: user2
"""

# Function to process the log string
def process_log_string(log_string):
    # Initialize storage
    user_sessions = defaultdict(list)
    error_messages = defaultdict(list)

    # Regex pattern to match log entries
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)')

    # Split the log string into lines
    lines = log_string.strip().split('\n')
    for line in lines:
        match = log_pattern.match(line)
        if match:
            timestamp_str, log_type, message = match.groups()
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            
            if log_type == 'INFO' and 'User logged in' in message:
                user = message.split(': ')[1]
                user_sessions[user].append({'login': timestamp, 'logout': None})
            elif log_type == 'INFO' and 'User logged out' in message:
                user = message.split(': ')[1]
                if user in user_sessions and user_sessions[user][-1]['logout'] is None:
                    user_sessions[user][-1]['logout'] = timestamp
            elif log_type == 'ERROR':
                # Assuming the last user in user_sessions is the current user
                if user_sessions:
                    current_user = list(user_sessions.keys())[-1]
                    error_messages[current_user].append(f'{timestamp_str} - {message}')

    return user_sessions, error_messages

# Process the log string
user_sessions, error_messages = process_log_string(log_content)

# Calculate total login time for each user
user_login_times = defaultdict(int)
for user, sessions in user_sessions.items():
    for session in sessions:
        if session['logout']:
            duration = session['logout'] - session['login']
            user_login_times[user] += duration.total_seconds()

# Output the results
print("User Login Times (in seconds):")
for user, total_time in user_login_times.items():
    print(f'{user}: {total_time} seconds')

print("\nError Messages:")
for user, errors in error_messages.items():
    print(f'Errors for {user}:')
    for error in errors:
        print(f'  {error}')
