from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys


class PyQtWebCrawler(object):
    def set_up(self, Dialog):
        Dialog.setObjectName("My PyQt WebCrawler")
        Dialog.resize(700, 700)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        # self.lineEdit.setStyleSheet("QLineEdit" #number or RGB)

        self.lineEdit.setObjectName('lineEdit')
        self.verticalLayout.addWidget(self.lineEdit)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        # self.textBrowser.setStylesheet

        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.scrapWeb)
        # self.pushButton.setStyleSheet("QLineEdit {\n"
        #    "background: rgb(51, 102, 255)\n"
        #     "}\n)",)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def scrapWeb(self):
        lineedit = self.lineEdit.text()
        html = urlopen(lineedit)
        bsobj = BeautifulSoup(html, "html")
        self.textBrowser.append(str(bsobj))
        image_tags = bsobj.findAll('img')
        for image_tag in image_tags:
            print(image_tag.get('src'))
        # images = bsobj.findAll("img", src=True)
        # image_src = [x['src'] for x in images]
        # image_src = [x for x in image_src if x.endswith('.jpg')]
        # print('Number of Images', len(images))
        # for image in image_src:
        #     print(image)
        #     break

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Please Enter valid URL"))
        self.pushButton.setText(_translate("Dialog", "Scrap URL"))

stylesheet = """
    QWidget{
    background-color: #cce6ff
    }
    QPushButton{
    background-color: #ffe6ff
    }
    QTextBrowser{
    background-color: #b3ecff
    }
    QLineEdit{
    background-color: #ffcce6
    }
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    Dialog = QtWidgets.QDialog()
    ui = PyQtWebCrawler()
    ui.set_up(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




