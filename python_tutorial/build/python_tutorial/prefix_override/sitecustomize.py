import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/elena/repos/space_robotics/python_tutorial/install/python_tutorial'
