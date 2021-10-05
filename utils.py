# Utils file for password-strength

# Imports
import os
import platform

# Mapping the clear screen command accordingly to each OSes

os_command_mapper = {'Windows':'cls', 'Linux':'clear', 'Darwin':'clear'}

def clear_screen():
    try:
        cmd = os_command_mapper[platform.system()]
        os.system(cmd)
    except KeyError:
        raise KeyError(f"Your operating system ({platform.system()} was not found in the OS command mapper. Please add your own or open an issue on GitHub.")
