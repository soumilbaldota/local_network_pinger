from os import system as s
print(s(f'fing -n {input("enter the default gateway : ")}/24 -o table,text'))
ip=input('enter the ip do you want to ping from the above table ? ')
s(f'ping {ip}')
