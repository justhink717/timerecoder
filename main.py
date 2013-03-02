import sys
import time
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)

        self.resize(320,480)
        self.setWindowTitle("Time Record")

        startbutton = QtGui.QPushButton("START",self)
        startbutton.setGeometry(90,100,120,100)
        endbutton = QtGui.QPushButton("END",self)
        endbutton.setGeometry(90,240,120,100)


        self.connect(startbutton,QtCore.SIGNAL('clicked()'),self.kaishi)
        self.connect(startbutton,QtCore.SIGNAL('clicked()'),self.show2)
        self.connect(endbutton,QtCore.SIGNAL('clicked()'),self.jieshu)
        self.connect(endbutton,QtCore.SIGNAL('clicked()'),self.showtime)

    def kaishi(self):
            t1 = time.localtime()
            return t1
    
    def jieshu(self):
            t2 = time.localtime()
            return t2        

    time1=kaishi(self)
    time2=jieshu(self )


    def intervatime(self):
        hour = (self.jieshu()-self.kaishi())/3600
        minute = (self.jieshu()-self.kaishi())%3600/60
        sec =(self.jieshu()-self.kaishi())%3600%60
        #print("%d:%d:%d"%hour,minute,sec)
        return hour,minute,sec
        
    def showtime(self):
        #QtGui.QMessageBox.information(self,"used time",intervatime)
        #print(self.intervatime())
        #t3=time.time()
        print(self.time1,self.time2)

    def show2(self):
        print(time1,time2)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())







