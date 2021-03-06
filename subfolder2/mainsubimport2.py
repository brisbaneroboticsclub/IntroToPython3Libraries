import random

def volume(l,b):
    rectangle_volume = l * b * 1
    return rectangle_volume

def demo():

    print('-------------------')
    print('This is the demo loop.')
    print('-------------------')
    print('This demo Calculates the Volume of a rectangle.')
    print('-------------------')

    l = random.randint(1000,100000) #2

    #print('The Length of the rectangle is :',l,'units')

    l = l / 10

    '''
    https://mkaz.blog/code/python-string-format-cookbook/

    repeat for area
    '''

    print('The Length of the rectangle is :',l,'units')
    print('The Length of the rectangle is :','%2.0f' % l,'units')
    print('The Length of the rectangle is :','%2.1f' % l,'units')
    print('The Length of the rectangle is :','%2.2f' % l,'units')
    print("The Length of the rectangle is : {:,.2f} units".format(l))
    print('The Length of the rectangle is :','%3.2f' % l,'units')

    print('-------------------')

    b = random.randint(0,100) #3
    print('The Breadth of the rectangle is :',b,'units')
    print('-------------------')

    V = volume(l,b)
    print('Therefore the Volume of the rectangle is : ',V,'units^3')
    print('-------------------')

if __name__ == "__main__":

    print('''

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##*###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##*####%%%*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@                                             @@@@@@@@@@@@@@####*##%@##*%@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@  This program was brought to you by the:    @@@@@@@@@@@@@%%#%@@@@@@@@*#%#*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
    @@                                             @@@@@@@@@@@@@@%######%*+**+#%%%#*#**%@@@@@@@@@%@@@@@@@@@@@@@#
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@@@@@@@@@@@@@@@@%###%##***+*++*%###***@@@@@@@@#%*=+*++==*+*#
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@@@@@@@@@@@@@@@@@@@%%#*******++%+%##+#@@@@@@@@%#*=-***=-++@%
    @@    _.~"                             "~._    @@@%%%%@@@@@@@@@@@@@@@%##*******%+###*%@@@@@@@@%#%##*#**++%@%
    @@    _.~"   Brisbane Robotics Club.   "~._    @@%####%@@@@@@@@@@@@@@%##****###%+####@@@@@@@@@%######:-:+=@%
    @@    _.~"                             "~._    @@#***##@@@@@@@@@@@%##%%%%######%*#%%%%##**#%@@@%####**+++#@%
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@#*****@@%%%####%%%%%%%%%%%%%%%%%%##%%######@@@@@%%%####%@@%
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@@####*#########%%######%#%%%%%#***#@@%%%##**#@@@@@%@%%@@@@%
    @@                                             @@@#**###%%%%@%@@@%#########%%###%%@@@@@@%##***#@@@@@@@@@@@@%
    @@ website: http://brisbaneroboticsclub.id.au/ @@@@@%%@@@@@@@@@@@%*****+*###**########%@@@%%%#%%@@@@@######*
    @@                                             @@@@@@@@@@@@@@@@@@%#******#***@@@@@@@@@@@@@@#******%@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*****#**#@@@@@@@@@@@@@@#*#*#%*#@%%@@@@@@@       
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%######%@@@@@@@@@@@@@@@@%%@%##%%@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@                                                                                                        @@                               
    @@    For instructions : http://brisbaneroboticsclub.id.au/using-libraries-with-python3/                  @@
    @@                                                                                                        @@
    @@    To run code      : python3 mainsubimport2.py                                                        @@
    @@                                                                                                        @@
    @@    NOTE             : Humans were NOT harmed making this robot. This is free and open-source software  @@
    @@                       distributed under the terms of the GNU General Public License version 2.         @@
    @@                                                                                                        @@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ''')

    print('-------------------')
    print('Starting Main Menu loop.')
    print('-------------------')

    while 1:

        print('-------------------')
        print('Main Menu.')
        print('-------------------')

        inp = int(input('\n1. Run Demo.\
        \n2. Exit. \
        \n\nhttp://BrisbaneRoboticsClub.id.au >>> '))

        if inp == 1:
            demo()
        elif inp == 2:
            break

    print('----------------')
    print('Program End.')
    print('----------------')