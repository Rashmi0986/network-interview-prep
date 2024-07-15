#Given the subnetmask generate the Prefix for the same 
   #- constraints: validate and generate only for valid subnets 

"""
Algorithm 
1. first generate all subnets 
2. Validate if the given Ip is in the subnet list 
3. if valid convert each octet to binary 
4. return the prefix 
"""

def getSubnetMask(prefix):
    value = ""
    if prefix >= 25 and prefix <= 32: #4th octet
          value = getSubnetValue(prefix)
          res = "255.255.255."+value
     
    elif prefix >= 17 and prefix <= 24: #3rd octet
          value = getSubnetValue(prefix)
          res = "255.255."+value+".0"
         
    elif prefix >= 9 and prefix <= 16: # 2nd octet
           value = getSubnetValue(prefix)
           res = "255."+value+".0.0"
    else:
          value = getSubnetValue(prefix)
          res = value+".0.0.0"
    return res
 

def getSubnetValue(prefix):
        if prefix == 8 or prefix ==16 or prefix ==24 or prefix == 32:
            res = 255
        else:
            subnetbits = prefix % 8
            n = 7
            res = 0
            while subnetbits:
                res += 2 ** n
                n-=1
                subnetbits-=1
        return str(res)

#Generating the subnet mask for all the prefix .
def getallSubnets():
    subnetMaskSet = set()
    for i in range(1,33):
        subnetMaskSet.add(getSubnetMask(i))
    return subnetMaskSet

def trans(octet): # this method converts each octet to binary  
    bits = []
    octet = int(octet)
    while octet:
        bits.append(octet%2)
        octet = octet>>1
    return bits

# Latest Code with the validation added 
def getPrefix(subnetMask):
    allSubnets = getallSubnets()
    res = ""
    total = 0
    if subnetMask in allSubnets: # check if it is valid subnetmask first 
        values = subnetMask.split(".") # split IP by dot to get the exact values
        for val in values:
            res = trans(val) # convert to binary
            total += res.count(1) # count the number of 1's 
        return total
    else:
        return f"invalid Subnetmask!! can't convert"

s= "128.0.0.0" # valid case
#s = "255.255.255.256" invalid case
print(f"{getPrefix(s)}")
