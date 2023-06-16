import os
import time
import serial
from Robotiq_manger.crc_math import command_creat
os.system('color')
from termcolor import colored
from Robotiq_manger.GRipper_Controll_F import gri_set,gri_op,gri_full_op,gri_full_close,gri_op_grad,gri_op_dynamic

def Man_F2():
    print(colored('Robotiq F2 85 collaborative gripper manual control panel: \n  ','green'),
          colored('List  of working commands:\n','green'),
          colored('########################################\n','green'),
          colored('P :   Input active port\n','green'),
          colored('O :   Open gripper full (max speed and force)\n','green'),
          colored('C :   Close gripper full (max speed and force)\n','green'),
          colored('S :   Set gripper to start operation\n','green'),
          colored('SE :  Set gripper parameters( closing position limit, max speed , max force , + value , Timer )\n','green'),
          colored('      To set back to default just type DE                             \n','green'),
          colored('OC :  Open costume position\n','green'),
          colored('D :   Display current position.\n','green'),
          colored('+ :   Close gripper (+ value)\n','green'),
          colored('- :   Open gripper (- value)\n','green'),
          colored('G :   Gradual closing of the gripper by 1 point   \n', 'green'),
          colored('GC :   Gradual closing of the gripper by costum point   \n', 'green') ,
          colored('E :   Exit  \n', 'green'),
          colored('##################################\n','green')
          )
    PARAM = []
    PARAMD = [220,250,250,10,0.004]
    P,S,F = 0,0,0
    PORT = ''
    while True:
          print( colored('Please enter the command to input  the active port: ','blue'))
          Command = input("Please enter the requested command :\n")
          if Command != 'P' and Command != 'E':
                print(colored('Command is incorrect please enter the correct command !','yellow'))
          elif Command == 'P':
                PORT = input("Please enter the name of the active port for the gripper :\n")
                print('Gripper PORT is set = ',PORT )
                break
          elif Command == 'E':
                print(colored('Shutting down ','red'))
                break
    if Command != 'E':
        while True:
              print( colored('Please enter the Set command to set up the gripper and start operation: ','blue'))
              Command = input("Please enter the requested command :\n")
              if Command != 'S' and Command != 'E':
                    print(colored('Command is incorrect please enter the correct command !','yellow'))
              elif Command == 'S':
                    ser = gri_set(PORT)
                    print('Gripper set, now set Parameters')
                    break
              elif Command == 'E':
                    print(colored('Shutting down ','red'))
                    break
        if Command != 'E':
              while True:
                    Command = input("Please enter a  command :\n")
                    if Command != 'SE' and Command != 'E':
                          print('Command is incorrect please enter the correct command !')
                    elif Command == 'SE':
                          pos_limi = input("Please enter a  Gripper closing limit 0~~255 :\n")
                          PARAM.append(float(pos_limi))
                          M_S = input("Please enter a  Gripper  max speed 0~~255 :\n")
                          PARAM.append(float(M_S))
                          M_F = input('Please enter a  Gripper  max Force 0~~255 :\n"')
                          PARAM.append(float(M_F))
                          Grd = input('Please enter a  Gripper  Position increase multiplier 0~~255 :\n"')
                          PARAM.append(float(Grd))
                          Tim = input('Please enter a  Gripper  cool down timer 0.004~~1 :\n"')
                          PARAM.append(float(Tim))
                          print('Are these Parameters correct =', PARAM)
                          conf =  input('yes or no\n"')
                          if conf == 'yes':
                                print('Parameters set, now you can start operation enjoy !\n ')
                                break
                          else:
                                print('Please edit again !\n')
                    elif Command == 'E':
                          print(colored('Shutting down ', 'red'))
                          break
              if Command != 'E':
                    while True:
                        print(' welcome to operation mode !\n')
                        Command = input("Please enter a  command :\n")
                        if Command == 'E':
                              print(colored('Shutting down ', 'red'))
                              break
                        elif Command == 'D':
                              print('Current parameters: ', PARAM)
                        elif Command == 'S':
                              ser = gri_set(PORT)
                              print('Gripper set\n')
                        elif Command == 'SE':
                              print('Please enter new parameters\n')
                              pos_limi = input("Please enter a  Gripper closing limit 0~~255 :\n")
                              PARAM.append(float(pos_limi))
                              M_S = input("Please enter a  Gripper  max speed 0~~255 :\n")
                              PARAM.append(float(M_S))
                              M_F = input('Please enter a  Gripper  max Force 0~~255 :\n"')
                              PARAM.append(float(M_F))
                              Grd = input('Please enter a  Gripper  Position increase multiplier 0~~255 :\n"')
                              PARAM.append(float(Grd))
                              Tim = input('Please enter a  Gripper  cool down timer 0.004~~1 :\n"')
                              PARAM.append(float(Tim))
                              print('Are these Parameters correct =', PARAM)
                              conf = input('yes or no\n"')
                              if conf == 'yes':
                                    print('Parameters set, now you can start operation enjoy !\n ')
                              else:
                                    print('Please enter parameter edit command again !\n')
                        elif Command == 'O':
                              P, S, F = 0, 250, 250
                              print('Gripper fully open')
                              gri_full_op(ser)
                        elif Command == 'C':
                              P, S, F = pos_limi, 250, 250
                              print('Gripper fully closed')
                              gri_full_close(ser)
                        elif Command == 'OC':
                              print('Set your costume parameters')
                              P = float(input("Please enter a  Gripper  desired position :\n"))
                              while True:
                                  if P not in range (0,pos_limi):
                                        print('please enter a correct value')
                                  else:
                                    break
                              F = float(input('Please enter a  Gripper  desired speed  :\n"'))
                              while True:
                                  if F not in range (0,M_S):
                                        print('please enter a correct value')
                                  else:
                                    break
                              S = float(input('Please enter a  Gripper  desired force  :\n"'))
                              while True:
                                    if S not in range(0, M_F):
                                          print('please enter a correct value')
                                    else:
                                          break
                              print('Operation finished !')
                              gri_op(ser, P, F, S)
                              PARAM.append(float(P))
                        elif Command == '+':
                              P = P + Grd
                              gri_op(ser, P, F, S)
                              print('position  + ', Grd)
                        elif Command == '-':
                              P = P - Grd
                              gri_op(ser, P, F, S)
                              print('position  - ', Grd)
                        elif Command == 'DE':
                             PARAM = PARAMD
                             print('Parameters set to default  = ', PARAM)
                        elif Command == 'G':
                             gri_op_grad(ser,pos_limi,M_S,M_F,Tim)
                             print('Closing done')
                        elif Command == 'GC':
                             gri_op_dynamic(ser,pos_limi,M_S,M_F,Tim,Grd)
                             print('Closing done')
                        else:
                             print('Please enter a correct command  ')
