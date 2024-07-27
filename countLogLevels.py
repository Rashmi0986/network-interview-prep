s = """INFO Starting application
WARNING Deprecated configuration detected
ERROR Failed to connect to database
INFO User logged in
ERROR File not found
INFO User logged out
"""
def count_log_levels(log_lines):
    log_levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in log_lines.strip().splitlines():
        for level in log_levels:
            if line.startswith(level):
                log_levels[level] += 1
    return log_levels



log_counts = count_log_levels(s)
print(log_counts)

