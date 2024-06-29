filename = "show_ip_int_brief.txt"
with open(filename, 'r') as file_object:
    data = file_object.read()

#initialize the final outer dictionary out_dict = {}
out_dict = {}

#iterate each line using splitlines and unpack items to variables
for line in data.splitlines():
    intf, ip, ok, method, status, protocol, *_ = line.split()
    if "IP-Address" in ip:
        continue
        
    #create an inner_dict with key (int_name) = {values}
    inner_dict = { intf : {'ip_addr': ip, 'line_status': status, 'line_protocol': protocol}}
    
    #add the inner dict to the out_dict
    out_dict.update(inner_dict)

#print out_dict
out_dict
