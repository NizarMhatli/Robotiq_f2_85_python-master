import setuptools
setuptools.setup(
                name='Robotiq_manger'          ,
                version='0.6'       ,
                Author ='Nizar mhatli'       ,
                description ='Robotiq f2 85 gripper controll software'    ,
                packages =['Robotiq_manger']       ,
                install_requires=['cython','libscrc','numpy','pandas','pyserial','termcolor']
)