import json


table = '''Interface Status
=======================================================================================
DN                                            Ether type   Speed     MTU  
--------------------------------------------  -----------  --------  ------
'''
print(table)
with open('sample-data.json', 'r') as f:
    d = json.load(f)
    for _ in d['imdata']:
       key = next(iter(_))
       print(f'{_[key]["attributes"]["dn"]: <45} {_[key]["attributes"]["dot1qEtherType"]: <13}{_[key]["attributes"]["speed"]: <10}{_[key]["attributes"]["mtu"]: <11}')
       

