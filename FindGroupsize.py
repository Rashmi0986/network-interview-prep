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


#######Result#######
please enter the prefix in the range between 25 to 30 30
please enter the ip in x.x.x format 192.168.20
number of bits in the last octet is 2
subnet size is 4
number of usable hosts per subnet 2
first and last host IP in the just first subnet is 192.168.20.1 and 192.168.20.2 
total number of subnets 64
subnet number : 192.168.20.0
subnet number : 192.168.20.4
subnet number : 192.168.20.8
subnet number : 192.168.20.12
subnet number : 192.168.20.16
subnet number : 192.168.20.20
subnet number : 192.168.20.24
subnet number : 192.168.20.28
subnet number : 192.168.20.32
subnet number : 192.168.20.36
subnet number : 192.168.20.40
subnet number : 192.168.20.44
subnet number : 192.168.20.48
subnet number : 192.168.20.52
subnet number : 192.168.20.56
subnet number : 192.168.20.60
subnet number : 192.168.20.64
subnet number : 192.168.20.68
subnet number : 192.168.20.72
subnet number : 192.168.20.76
subnet number : 192.168.20.80
subnet number : 192.168.20.84
subnet number : 192.168.20.88
subnet number : 192.168.20.92
subnet number : 192.168.20.96
subnet number : 192.168.20.100
subnet number : 192.168.20.104
subnet number : 192.168.20.108
subnet number : 192.168.20.112
subnet number : 192.168.20.116
subnet number : 192.168.20.120
subnet number : 192.168.20.124
subnet number : 192.168.20.128
subnet number : 192.168.20.132
subnet number : 192.168.20.136
subnet number : 192.168.20.140
subnet number : 192.168.20.144
subnet number : 192.168.20.148
subnet number : 192.168.20.152
subnet number : 192.168.20.156
subnet number : 192.168.20.160
subnet number : 192.168.20.164
subnet number : 192.168.20.168
subnet number : 192.168.20.172
subnet number : 192.168.20.176
subnet number : 192.168.20.180
subnet number : 192.168.20.184
subnet number : 192.168.20.188
subnet number : 192.168.20.192
subnet number : 192.168.20.196
subnet number : 192.168.20.200
subnet number : 192.168.20.204
subnet number : 192.168.20.208
subnet number : 192.168.20.212
subnet number : 192.168.20.216
subnet number : 192.168.20.220
subnet number : 192.168.20.224
subnet number : 192.168.20.228
subnet number : 192.168.20.232
subnet number : 192.168.20.236
subnet number : 192.168.20.240
subnet number : 192.168.20.244
subnet number : 192.168.20.248
subnet number : 192.168.20.252
        
