#import mainsubimport
from mainsubimport import area

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
@@    To run code      : python3 mainimport.py                                                            @@
@@                                                                                                        @@
@@    NOTE             : Humans were NOT harmed making this robot. This is free and open-source software  @@
@@                       distributed under the terms of the GNU General Public License version 2.         @@
@@                                                                                                        @@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')

l = 4
b = 5

#AREA = mainsubimport.area(l,b)
AREA = area(l,b)

#mainsubimport.demo()

print('Length :',l)
print('Breadth :',b)
print('Area :',AREA)