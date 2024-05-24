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
        if prefix == 8 or prefix == 16 or prefix == 24 or prefix == 32:
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
for i in range(1,33):
    print(f"given prefix:{i} subnetmask:{getSubnetMask(i)}")
