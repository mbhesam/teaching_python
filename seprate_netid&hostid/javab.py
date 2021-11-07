address = input("plz enter ip address with subnetmask to show netid and hostid:\t")
addr_list = address.split("/")
ip = addr_list[0]
mask = addr_list[1]
octet = ip.split(".")
octet_b = []
octet_b.append(format(int(octet[0]),"08b"))
octet_b.append(format(int(octet[1]),"08b"))
octet_b.append(format(int(octet[2]),"08b"))
octet_b.append(format(int(octet[3]),"08b"))
li_index = int(int(mask)/8)
baghi_index = int(mask)%8
netid = (".".join(octet_b[0:li_index]) + "." + octet_b[li_index][0:baghi_index]).strip(".")
hostid = (octet_b[li_index][baghi_index:] + "." + ".".join(octet_b[li_index+1:])).strip(".")
print("count of netid bits is:\t "+mask)
print("netid is equal to:\t"+netid)
print("count of hostid bits is:\t"+str(32-int(mask)))
print("hostid is equal to:\t"+hostid)
