
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import main as m
from PIL import Image


class Ui_MainWindow(object):
    def __init__(self):
        self.i=0
        self.imgs=m.img_path
        self.length=len(self.imgs)
        if(self.length==0):
            print('no images found !!')
            self.ext()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #image name label
        self.name=QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(160,500,500,20)
        self.name.setText(self.imgs[self.i])
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)

        #image window
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(170, 100, 400, 300))
        self.img.setText("")
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img_size(self.imgs[0])
        self.img.setPixmap(QtGui.QPixmap(self.imgs[0]))
        self.img.setScaledContents(True)
        self.img.setOpenExternalLinks(False)
        self.img.setObjectName("img")
        #next and prev buttons
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(660, 210, 61, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(60, 210, 61, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.prev.setFont(font)
        self.prev.setObjectName("prev")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.next.clicked.connect(self.next_pic)
        self.prev.clicked.connect(self.prev_pic)

        #code for getting image in center
        self.vbox=QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.img)
        self.vbox.addStretch()

    def next_pic(self):
        self.i=(self.i+1)%self.length
        self.img_size(self.imgs[self.i])
        self.img.setPixmap(QtGui.QPixmap(self.imgs[self.i%self.length]))
        self.name.setText(self.imgs[self.i])

    def  prev_pic(self):
        self.i=(self.i-1)%self.length
        self.img_size(self.imgs[self.i])
        self.img.setPixmap(QtGui.QPixmap(self.imgs[self.i%self.length]))
        self.name.setText(self.imgs[self.i])

    def img_size(self,image):
        img=Image.open(image)
        w,h=img.size
        print(w,h,end=' ')
        #original window size=400,300(w,h)
        if(w<400 and h <300):
            print("converted to w and h",w,h)
            self.img.setGeometry(QtCore.QRect(170, 100, w, h))
        else:
            #code to do
            if(w>h):
                d=w/h
                w=400
                h=400/d
            else:
                d=h/w
                h=400
                w=400/d
            print("converted to w and h",w,h)
            self.img.setGeometry(QtCore.QRect(170, 100, w, h))
    def ext(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer"))
        self.next.setText(_translate("MainWindow", ">"))
        self.prev.setText(_translate("MainWindow", "<"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
