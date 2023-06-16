import cython
import libscrc
def  command_creat (Pos,speed,force):
    crc_cal, command, li_s  = [9,16,3,232,0,3,6,9,00,00,00,255,255], [9,16,3,232,0,3,6,9,00,00,00,255,255,114,41],['0','0','0','0']
    command[10], command[11], command[12] = Pos, speed,force
    for j in range(0,len(crc_cal)):
        crc_cal[j] = command[j]
    crc_cal = bytes(crc_cal)
    crc = libscrc.modbus(crc_cal)
    crc = str(hex(crc))
    crc = crc.replace('0x','')
    li = [char for char in  crc ]
    if len(li) == 3:
        li_s[1] = li[0]
        li_s[2] = li[1]
        li_s[3] = li[2]
        li1 = [li_s[0], li_s[1]]
        li2 = [li_s[2], li_s[3]]
    elif len(li) == 2:
        li_s[2] = li[0]
        li_s[3] = li[1]
        li1 = [li_s[0], li_s[1]]
        li2 = [li_s[2], li_s[3]]
    elif len(li) == 1:
        li_s[3] = li[0]
        li1 = [li_s[0], li_s[1]]
        li2 = [li_s[2], li_s[3]]
    else:
       li1 =[li[0],li[1]]
       li2 =[li[2],li[3]]
    hex1 = ''
    hex1 = bytes(hex1.join(li1),'utf-8')
    hex2 = ''
    hex2 = bytes(hex2.join(li2),'utf-8')
    hex1 = int(hex1,16)
    hex2 = int(hex2,16)
    command[13] = hex2
    command[14] = hex1
    final_command = bytes(command)
    return(final_command)


