#from gui import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
try:
    dir=input("enter directory (folder) for images : ")
    os.chdir(dir)

    files=os.listdir()
    imgs=[i for i in files if(i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png') )]
    #print(imgs)
    img_path=[os.path.realpath(i) for i in imgs]
except:
    print('INVALID PATH !!! ')
    sys.exit()
