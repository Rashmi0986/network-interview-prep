def expand_interface(interface):
    if '-' in interface:
        start, end = interface.split('-')
        if "/" in start: # to process lag1, lag2 - have added this condition as chatGPT Failed to add this condition 
            base, start_num = start.rsplit('/', 1)
            _, end_num = end.rsplit('/', 1)
            return [f"{base}/{i}" for i in range(int(start_num), int(end_num) + 1)]
        else:
            return start, end # to process lag1, lag2 - have added this condition as chatGPT Failed to add this condition 
    return [interface]

def vlan_to_interface_mapping():
    filename = "show_vlan_ip.txt"
    with open(filename, 'r') as fileObj:
        data = fileObj.read()

    lines = data.strip().split("\n")
    vlan_dict = {}

    for line in lines[1:]:
        values = line.split(maxsplit=5)  # split into 6 parts
        vlan_id = int(values[0])
        interfaces = values[-1].split(',')
       
        expanded_interfaces = []
        for interface in interfaces:
            expanded_interfaces.extend(expand_interface(interface))
       
        vlan_dict[vlan_id] = expanded_interfaces

    return vlan_dict

# Main function call
pprint.pprint(vlan_to_interface_mapping())

"""
show vlan Text contains the data like below 
----------------------------------------------------------------------------------
VLAN  Name                 Status  Reason        Type      Interfaces
-----------------------------------------------------------------------------------
1     DEFAULT_VLAN_1       up      ok            static    1/1/3-1/1/4
2     UserVLAN1            up      ok            static    1/1/1,1/1/3,1/1/5
3     UserVLAN2            up      ok            static    1/1/2-1/1/3,1/1/5-1/1/9
5     UserVLAN3            up      ok            static    1/1/3
10    TestNetwork          up      ok            static    1/1/3,1/1/5
11    VLAN11               up      ok            static    1/1/3
12    VLAN12               up      ok            static    1/1/3,1/1/6,lag1-lag2
13    VLAN13               up      ok            static    1/1/3,1/1/6
14    VLAN14               up      ok            static    1/1/3,1/1/6
20    ManagementVLAN       down    admin_down    static    1/1/3,1/1/10

""""
