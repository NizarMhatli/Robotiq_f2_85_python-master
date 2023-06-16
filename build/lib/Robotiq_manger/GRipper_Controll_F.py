import glob
import time
import serial
from Robotiq_manger.crc_math import command_creat
from sys import platform


def grip_check(ser):
    data_raw = list(ser.readline())
    time.sleep(0.001)
    ser.write(b'\x09\x03\x07\xD0\x00\x03\x04\x0E')
    time.sleep(0.001)
    data_raw = list(ser.readline())
    if data_raw[3] == 185:
            grip = 'ok'
    else:
            grip = 'not ok'
    return (grip)



def gri_set(PORT):
    ser = serial.Serial(port=PORT, baudrate=115200, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)
    ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x00\x00\x00\x00\x00\x00\x73\x30')
    data_raw = ser.readline()
    time.sleep(0.01)
    ser.write(b'\x09\x03\x07\xD0\x00\x01\x85\xCF')
    data_raw = ser.readline()
    time.sleep(0.01)
    ####################################
    ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x09\x00\x00\x00\xFF\xFF\x72\x19')
    return(ser)


def gri_op(ser,P,S,F):
    ser.write(command_creat(P, S, F))

def gri_full_op(ser):
    ser.write(command_creat(0, 255, 255))

def gri_full_close(ser):
    ser.write(command_creat(220, 255, 255))

def gri_op_grad(ser,P,S,F,T):
 for i in range(0,P):
    ser.write(command_creat(i, S, F))
    time.sleep(T)

def gri_op_dynamic(ser,P,S,F,T,C):
 for i in range(0,P,C):
    ser.write(command_creat(i, S, F))
    time.sleep(T)


def Port_finder():
    port1 = []
    if platform == 'win32':
        conne = [port.device for port in serial.tools.list_ports.comports()]
        for i in range(0, len(conne)):
            ser = serial.Serial(port=conne[i], baudrate=115200, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS, timeout=1)
            ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x00\x00\x00\x00\x00\x00\x73\x30')
            data_raw = ser.readline()
            if data_raw != b'':
                PORT = conne[i]
            else:
                print('not the needed port')
            time.sleep(0.1)
    else:
        port = glob.glob('/dev/tty[A-Za-z]*')
        for i in range(0, len(port)):
            if 'ttyUSB' in port[i]:
                port1.append(port[i])
        for i in range(0, len(port1)):
            ser = serial.Serial(port=port1[i], baudrate=115200, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS, timeout=1)
            ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x00\x00\x00\x00\x00\x00\x73\x30')
            data_raw = ser.readline()
            if data_raw != b'':
                PORT = port1[i]
            else:
                print('not the needed port')
            time.sleep(0.1)
    return(PORT)

def grip_op_dynamic_w_blocker(ser,P,S,F,T,C,B,BL):
    for i in range(0, P, C):
        if B >= BL:
            break
        else:
            ser.write(command_creat(i, S, F))
        time.sleep(T)