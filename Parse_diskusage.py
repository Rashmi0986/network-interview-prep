disk_usage = """
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   30G   20G  60% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
/dev/sdb1       100G   90G   10G  90% /data
"""

# Split the data into lines
lines = disk_usage.strip().split('\n')

# Extract the header and rows
header = lines[0].split()
rows = [line.split() for line in lines[1:]]

# Print the table
print(f"{'Filesystem':<15} {'Size':<8} {'Used':<8} {'Avail':<8} {'Use%':<6} {'Mounted on':<10}")
print('-' * 61)

for row in rows:
    print(f"{row[0]:<15} {row[1]:<8} {row[2]:<8} {row[3]:<8} {row[4]:<6} {row[5]:<10}")
