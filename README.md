# GripperPackage



# Discreption:

- This package is created to make controlling Robotiq F2 85 Collabrtive gripper much easier.


![bb0e4c86fdb1e8ebee6795cf452773880729b0fed8981fcc65e1a2a5789491bb](https://user-images.githubusercontent.com/47193436/158507415-9e6fc433-b7e2-41ea-8175-e110ea7451b3.png)



- This package has 2 control methods for the gripper:
1- Manual control:
        Running the Manual control will run script that will turn the Terminal into a control panel,
        You can use the key board to input basic commands :
        
        O :   Open gripper full (max speed and force)
        
        C :   Close gripper full (max speed and force)
        
        S :   Set gripper to start operation
  
        P :   Input active port
        
        SE :  Set gripper parameters( closing position limite)
        
        OC :  Open costum position 
        
        D :   Display current position. 
        
        + :   Open gripper (+ value)
        
        - :   Close gripper (- value)
        
        E :   Exit  
        
 2- Automatic control:
     This package also works as library for controlling the gripper, 
     it contains multiple functions that controll the functionalities of the gripper,
     List of working functions so far: 
     
     - grip_set(): Set up the gripper to start operation 
     
     - gri_op() :  Costum command to open/close gripper at set speed 
     
     - gri_full_op() : Fully open the gripper
     
     - gri_full_close() : Fully close the gripper 
     
     - grip_check() :  Check if there is any object in the gripper 
     
     - gri_op_grad() : Increase Gripper position graduly 

     - gri_op_dynamic() : Increase Gripper position graduly with dynamic multiplier
     
     - grip_op_dynamic_w_blocker() :  Increase Gripper position graduly with  dynamic multiplier , with a limit blocker that will stop the gripper when 
     it is reached. 

     - Port_finder():  Find the active port of the gripper. 
     
     
# TO DO:

1 - Update this package to become a ROS2 package compatible with multpile robots. 

2 - Add more functions for dynamic control of the gripper Manual/Automatic. 

3 - Add the install txt file for easy install. 

4 - Edit the readme file.

5 - Add Dynamic port detection for the gripper. 
