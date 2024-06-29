import re

def parse_cpu(s):
    data = s.strip().split("\n")
    cpu_info = {}
    cur_processor = None
    for line in data:
        if re.match(r'processor\s+:\s+\d+', line):
            cur_processor = line.split(":")[1].strip()
            cpu_info[cur_processor] = {}
        elif cur_processor is not None:
            if "model name" in line:
                match = re.search(r"model name\s+:\s+(.+)", line)
                if match:
                    cpu_info[cur_processor]['model name'] = match.group(1).strip()
            elif "cpu family" in line:
                match = re.search(r"cpu family\s+:\s+(\d+)", line)
                if match:
                    cpu_info[cur_processor]['cpu family'] = match.group(1).strip()
    
    return cpu_info

s = """
processor   : 0
vendor_id   : GenuineIntel
cpu family  : 6
model       : 142
model name  : Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
stepping    : 10
cpu MHz     : 2000.000
cache size  : 8192 KB

processor   : 1
vendor_id   : GenuineIntel
cpu family  : 6
model       : 142
model name  : Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
stepping    : 10
cpu MHz     : 2000.000
cache size  : 8192 KB
"""

parsed_data = parse_cpu(s)

# Define table headers and format
header = f"{'Processor':<10} {'CPU Family':<10} {'Model Name':<50}"
print(header)
print('-' * len(header))

# Print rows
for processor, info in parsed_data.items():
    print(f"{processor:<10} {info.get('cpu family', ''):<10} {info.get('model name', ''):<50}")
