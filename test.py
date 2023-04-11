# firstName = input ("Siapa Nama Lengkap Anda ? ")
# nick = input ("Siapa Nama Panggilan Anda ? ")
# live = input ("Dimana alamat Anda ?")
# age = input ("Berapa usia Anda ?")
# print ("Hai, salam kenal " + nick+ " !"+"Nama lengkap Anda adalah"+ firstName+"Saat ini berdomisili di"+ live+"dan usia Anda adalah " + age+ "Terima kasih DevNet")

# nativeVLAN = 100
# dataVLAN = 100
# if nativeVLAN == dataVLAN:
#     print("The native VLAN and the data VLAN are the same.")
# else:
#     print("The native VLAN and the data VLAN are different.")


# aclNum = int(input("What is the IPv4 ACL number? ")) 
# if aclNum >= 1 and aclNum <= 99:
#     print("This is a standard IPv4 ACL.")
# elif aclNum >=100 and aclNum <= 199:
#     print("This is an extended IPv4 ACL.")
# else:
#     print("This is not a standard or extended IPv4 ACL.")

# devices=["R1","R2","R3","S1","S2"] 
# devices=[firstName, nick, live, age] 
# for item in devices:
#     print(item)

# routers=[]
# switches=[]
# devices=[\"RT1\", \"RT2\", \"RT3\", SW1\", \"SW2\", \"SW3\"]
# devices=devices + [\"RT4\", \"SW4\"]
# for i in devices:
#              if \"R\" in i:
#                     routers.append(i)
#              else: switches.append(i)
# switches  

# "duplex {}".format("full")
# 'duplex full'
# "interface {name}, port {port}".format(name="gigabitethernet", port="0/1")
# 'interface gigabitethernet, port 0/1'
# "device hostname ipaddress".split(" ")
# ['device', 'hostname', 'ipaddress']
# ",".join(['device', 'hostname', 'ipaddress'])
# 'device,hostname,ipaddress'

tool = "git clone"
host = "https://github.com/"
org = "arullhrp"
repo = "/netprog_basics"
print({tool},{host},{org},{repo})

nama = input ("Siapa nama lengkap Anda ? \nNama Saya : ")
print("nama Anda adalah : " +nama )
