from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Addplaylist(object):

    def __init__(self) :
        self.addplaylist = QtWidgets.QMainWindow()
        self.setupUi()
        # self.addplaylist.show()


    def setupUi(self):
        self.addplaylist.setObjectName("MainWindow")
        self.addplaylist.resize(822, 209)

        self.centralwidget = QtWidgets.QWidget(self.addplaylist)
        self.centralwidget.setObjectName("centralwidget")

        self.PlayListLabel = QtWidgets.QLabel(self.centralwidget)
        self.PlayListLabel.setGeometry(QtCore.QRect(20, 70, 180, 31))
        self.PlayListLabel.setObjectName("PlayListLabel")

        self.InputPlayList = QtWidgets.QLineEdit(self.centralwidget)
        self.InputPlayList.setGeometry(QtCore.QRect(210, 70, 600, 31))
        self.InputPlayList.setObjectName("InputPlayList")

        
        self.CompleteAdd = QtWidgets.QPushButton(self.centralwidget)
        self.CompleteAdd.setGeometry(QtCore.QRect(620, 170, 170 , 31))
        self.CompleteAdd.setObjectName("CompleteAdd")

        self.addplaylist.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.addplaylist)
        QtCore.QMetaObject.connectSlotsByName(self.addplaylist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add PlatList"))
        self.PlayListLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">PlayListName</span></p></body></html>"))
        self.CompleteAdd.setText(_translate("YouTubePlayer", "플레이목록 추가"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     start = Ui_Addplaylist()
    
#     sys.exit(app.exec_())

