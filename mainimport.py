import subfolder.mainsubimport
import subfolder2.mainsubimport2

# OR

#from subfolder.mainsubimport import area
#from subfolder2.mainsubimport2 import volume

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
@@ website: http://brisbanerobotics.club/      @@@@@%%@@@@@@@@@@@%*****+*###**########%@@@%%%#%%@@@@@######*
@@                                             @@@@@@@@@@@@@@@@@@%#******#***@@@@@@@@@@@@@@#******%@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*****#**#@@@@@@@@@@@@@@#*#*#%*#@%%@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%######%@@@@@@@@@@@@@@@@%%@%##%%@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@                                                                                                        @@
@@    For instructions : http://brisbanerobotics.club/using-libraries-with-python3/                       @@
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

AREA = subfolder.mainsubimport.area(l,b)
VOLUME = subfolder2.mainsubimport2.volume(l,b)

# OR

#AREA = area(l,b)
#VOLUME = volume(l,b)

print('Length :',l)
print('Breadth :',b)
print('Area :',AREA)
print('Volume :',VOLUME)