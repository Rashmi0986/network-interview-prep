# Below code will generate the Network Id , First and Last Host Ip, first and second network ID given the IP and the Prefix.

baseaddress = input("please enter the base address in the x.x.x format \n")
prefix = int(input("please enter the prefix between 25 to 30 \n"))

if prefix > 30 or prefix < 25:
    print("please enter valid number between 25 to 30")
    prefix = int(input())


subnetBits = 32 - prefix
subnet = pow(2,subnetBits)

totalUsableHosts = subnet - 2

firstnwId = baseaddress+".0"
secondnwId = baseaddress+"."+str(subnet)

firsthost = baseaddress+".1"
lasthost = baseaddress+"."+str(totalUsableHosts)



print(f"Total usable hosts per subnet {totalUsableHosts}")
print(f"Network number of the first two subnets are {firstnwId} and {secondnwId}")
print(f"First and lasthost  address in the first subnet are {firsthost} and {lasthost}")
