import os
import subprocess
x = "g++ -std=c++11 *.cpp"
# os.system("echo " + x)
subprocess.call("g++ -std=c++11 *.cpp", shell=True)