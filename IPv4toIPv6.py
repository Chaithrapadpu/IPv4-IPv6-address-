ip=input("Enter IPv4 address:")
ip1=[int(i) for i in ip.split(".")]
ip2=[]
for i in ip1:
    ip2.append(str(i//16))
    ip2.append(str(i%16))
for i in range(len(ip2)):
    if ip2[i]=='10':
        ip2[i]='a'
    elif ip2[i]=='11':
        ip2[i]='b'
    elif ip2[i]=='12':
        ip2[i]='c'
    elif ip2[i]=='13':
        ip2[i]='d'
    elif ip2[i]=='14':
        ip2[i]='e'
    elif ip2[i]=='15':
        ip2[i]='f'
ip3=''.join(ip2)
s=ip3[0:4]
t=ip3[4:8]
print("IPv6 address is ::ffff:{}:{}".format(s,t))
