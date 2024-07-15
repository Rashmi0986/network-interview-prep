import pprint

def expand_interface(interface):
    if '-' in interface:
        start, end = interface.split('-')
        base, start_num = start.rsplit('/', 1)
        _, end_num = end.rsplit('/', 1)
        return [f"{base}/{i}" for i in range(int(start_num), int(end_num) + 1)]
    return [interface]

def vlan_to_interface_mapping():
    data = """
    VLAN  Name                 Status  Reason        Type      Interfaces
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
    """
    
    lines = data.strip().split("\n")
    vlan_dict = {}

    for line in lines[1:]:
        values = line.split(maxsplit=5)  # split into 6 parts
        vlan_id = int(values[0])
        interfaces = values[-1].split(',')
        
        expanded_interfaces = []
        for interface in interfaces:
            if '-' in interface:
                expanded_interfaces.extend(expand_interface(interface))
            else:
                expanded_interfaces.append(interface)
        
        vlan_dict[vlan_id] = expanded_interfaces

    return vlan_dict

# Main function call 
pprint.pprint(vlan_to_interface_mapping())
