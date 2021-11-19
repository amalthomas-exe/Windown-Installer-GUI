## Windows-Installer-GUI


![platforms](https://img.shields.io/badge/Platforms-Windows%20|%20Linux%20|%20Mac-blue)
![python version](https://img.shields.io/badge/Python%20Version-Python%203-yellow)
![GitHub repo size](https://img.shields.io/github/repo-size/amalthomas-exe/Windows-Installer-GUI)
![issues](https://img.shields.io/github/issues/amalthomas-exe/Wall-E)

A Qt5 based implementation of a typical Windows installer. If the required logic can be added, it can be a successful cross-platform alternative to the default Windows installer.

This is a community project to accomplish installaing Windows OS on other systems without having to clean install the PC. 

Current OS version specified : Windows 11<br>

### Dependencies
This project requires atleast [Python](https://www.python.org) version 3.5. Also pip must be added to PATH (in case of Windows)

The required dependencies can be installed using <br>
```pip install requirements.txt``` (For Windows)<br>
```pip3 install requirements.txt``` (For Linux/OSX)<br>

### Usage
Just type in the following command inside the project folder<br>
```python main.py```

### Executables
Now this is the tricky part :). As of now , there is no good tool to create binaries from python scripts. The best tool so far ([Pyinstaller](https://pypi.org/project/pyinstaller)), bundles a full blown python interpreted along with the executable. As a result, for a project size of just 22 kb, the resulting binary is about 300-400 MB. 

So for now, we are not planning to ship the executables for these programs. You will have to download the python interpreter yourself. You may skip the trouble if you own a Linux powered system, because they come with python3 by default. 

### Issues
Please report any bugs to the issues tab.

### Ending note:
This is not a final project and work is yet to be done. This section will be updated as per the status of the project

