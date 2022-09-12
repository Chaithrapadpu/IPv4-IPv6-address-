ip=input("Enter IPv6 address:")
ip1=ip.split(":")
print(ip1)
s=ip1[3]+ip1[4]
t=list(s)
for i in range(len(t)):
    if t[i]=='a':
        t[i]='10'
    if t[i]=='b':
        t[i]='11'
    if t[i]=='c':
        t[i]='12'
    if t[i]=='d':
        t[i]='13'
    if t[i]=='e':
        t[i]='14'
    if t[i]=='f':
        t[i]='15'
u=[int(x) for x in t ]
x=(u[0]*16)+u[1]
y=(u[2]*16)+u[3]
z=(u[4]*16)+u[5]
a=(u[6]*16)+u[7]
print("IPv4 address is:{}.{}.{}.{}".format(x,y,z,a))
