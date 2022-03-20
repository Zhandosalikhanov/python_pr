import json

long_json = open("sample-data.json")

data = json.load(long_json)

def formalnost():
    print(2 * "\n" + "Interface status")
    print('=' * 80 + "\n" + f"DN{49 * ' '}Description{11 * ' '}Speed{4 * ' '}MTU")
    print(50 * '-' + ' ' + 20 * '-' + ' ' + 6 * '-' + ' ' + 6 * '-')

formalnost()
for dict in data["imdata"]:
    temp = (dict["l1PhysIf"])["attributes"]
    print(temp["dn"] + 30 * ' ' + temp["speed"] + "  ", temp["mtu"])
print()