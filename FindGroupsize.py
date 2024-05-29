def findGroupSize(prefix, IP):
    result = []
    group = 32 - prefix
    
    groupSize = 2 ** group
    usablehosts = groupSize - 2
    
    
    for i in range(0,255,groupSize):
        result.append(i)
    
    hosts = []
    firstIP = ""
    lastIP = ""
    for g in result:
        if firstIP == "":
            firstIP = str(g+1)
            lastIP  = str(groupSize - 2)
        hosts.append(IP+"."+str(g))
    
    firsthostIP = IP+"."+firstIP
    lasthostIP =  IP+"."+lastIP
    totalSubnets = len(hosts)
    
    print(f"number of bits in the last octet is {group}")
    print(f"subnet size is {groupSize}")
    print(f"number of usable hosts per subnet {usablehosts}")
    print(f"first and last host IP in the just first subnet is {firsthostIP} and {lasthostIP} ")
    print(f"total number of subnets {totalSubnets}")
    
    for host in hosts:
        print(f"subnet number : {host}")
    
prefix = int(input("please enter the prefix in the range between 25 to 30 "))
ip = input("please enter the ip in x.x.x format ")
findGroupSize(prefix, ip)
        
