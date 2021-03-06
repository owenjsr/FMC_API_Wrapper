from fmc_wrapper_v2 import *
import sys

"""
Set FMC IP, Username, Password.
"""
username = 'apiscript'
password = 'Admin123'
serverIP = '192.168.11.5'
autodeploy = False

# Use passed in username password, if so desired.
if len(sys.argv) > 2:
    username = sys.argv[1]
    password = sys.argv[2]

"""
Create a list of python objects relating to the various API objects.
Set the method for each object (get, post, put, delete, getall) and any data you wish to send.
For now, any 'get' method will just print data to the screen.  The other methods will print a success message
 or a reason for failure.
"""

"""
# Testing 'post' method.
users_objects = [
    Network(method='post', name='A Dax Mickelson', value='1.2.3.4/32'),
    Network(method='post', name='A Nother Host', value='1.2.3.3'),
    Network(method='post', name='A W!@#$T!!@#%#$F', value='3.2.1.0/24'),
    Network(method='post', name='A_Ranger', value='1.1.1.1-2.2.2.2'),
    Network(method='post', name='AB_Ranger', value='1.1.1.1-2.2.2.2'),
]
"""
"""
# Try every combination of 'get' for Network Class.  'get' for Host, Networks, and NetworkGroups.
# 'get' by name, id, and 'getall' as default method.
users_objects = [
    Network(method='get', id='000C2926-64BB-0ed3-0000-012884907880'),
    Network(method='get', name='A Dax Mickelson'),
    Network(method='get', id='000C2926-64BB-0ed3-0000-012884907916'),
    Network(method='get', name='A_W____T_______F'),
    Network(method='get', id='000C2926-64BB-0ed3-0000-012884908007'),
    Network(method='get', name='A_Ranger'),
    Network(),
]
"""
"""
# Testing 'delete' method.  (Haven't tried this yet.)
users_objects = [
    Network(method='post', name='AAABBBCCC', value='9.9.9.0/24'),
    Network(method='delete', name='AAABBBCCC'),
]
"""

"""
Open a connection to FMC.  Optionally choose whether to deploy to FTDs once connection is closed.
"""
with FMC(serverIP, username, password, autodeploy = autodeploy) as fmc1:
    if 'users_objects' in locals():
        fmc1.batch_send(users_objects)

print('Connection to FMC is now exited.  Thank you for playing.')
