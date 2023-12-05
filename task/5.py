import re
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
def get_str_paras(info):
    paras = ''
    for key in info:
        paras += key + ', '
    if len(paras) > 0:
        paras = paras[0:-2]
    return paras

def item_1():
    device = input('Enter name of device: ')
    if device in london_co:
        info = london_co[device]
        paras=get_str_paras(info)
        para = input(f'Enter parameter name ({paras}): ')
        for key in info:
            if para.lower() == key.lower():
                print(info[key])
                return
        else:
            print('No such parameter')

def item_2_network():
    host = input('Enter network/mask combinations: ')
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})$"

    # Use re.match to check if the combination matches the pattern
    match = re.match(pattern, host)
    if match is None:
        return
    ip0,ip1,ip2,ip3,mask = match.groups()
    ip0_num,ip1_num,ip2_num,ip3_num,mask_num = [int(i) for i in [ip0,ip1,ip2,ip3,mask]] 
    if ((ip0_num >= 0 and ip0_num <=255) and 
       (ip1_num >= 0 and ip1_num <=255) and 
       (ip2_num >= 0 and ip2_num <=255) and
       (ip3_num >= 0 and ip3_num <=255) and
       (mask_num >0 and mask_num <=32)):
       mask_bi = '1'* mask_num + '0' * (32-mask_num)
       mask0_num,mask1_num,mask2_num,mask3_num = [int(mask_bi[8*i:8*i+8],2) for i in [0,1,2,3]] 
       ip0_num = ip0_num & mask0_num
       ip1_num = ip1_num & mask1_num
       ip2_num = ip2_num & mask2_num
       ip3_num = ip3_num & mask3_num
       print('Network:')
       print(f'{ip0_num:<8} {ip1_num:<8} {ip2_num:<8} {ip3_num:<8}')
       print(f'{bin(ip0_num)[2:]:>08} {bin(ip1_num)[2:]:>08} {bin(ip2_num)[2:]:>08} {bin(ip3_num)[2:]:>08}')
       print('Mask:')
       print(f'/{mask_num}')
       print(f'{mask0_num:<8} {mask1_num:<8} {mask2_num:<8} {mask3_num:<8}')
       print(f'{bin(mask0_num)[2:]:>08} {bin(mask1_num)[2:]:>08} {bin(mask2_num)[2:]:>08} {bin(mask3_num)[2:]:>08}')



if __name__ == "__main__":
    # item_1()
    item_2_network()