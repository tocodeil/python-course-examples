"""
ex3.py
DB

"""
import sys

#sys.argv

IP_List = []
IP_Dic = {}
with open('hosts','r') as f:
    IP_List = f.read().split()
for comp_name_n_IP in IP_List:
    IP_Dic[comp_name_n_IP.split("=")[0]] = comp_name_n_IP.split("=")[1]

for comp_name in sys.argv[1:]:
    if comp_name in IP_Dic:
        print comp_name + " = " + IP_Dic[comp_name]
    else:
        print  comp_name + " - IP unknown "


