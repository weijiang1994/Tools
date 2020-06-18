"""
coding:utf-8
file: main.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/6/17 19:24
@desc:
"""
import hashlib
import time

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon

from ui.mainwindow import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys
import uuid
import threading
import frozen_dir

STYLE = '* {\
    font-family: "Microsoft YaHei";\
}\
\
QWidget:focus{\
    outline: none;\
}\
\
QPushButton[class="Aqua"] {\
    border-radius: 4px;\
    height: 30px;\
    background-color: #3bafda;\
}\
\
QPushButton:hover[class="Aqua"] {\
    background-color: #4fc1e9;\
}\
\
QPushButton:pressed[class="Aqua"] {\
    background: qradialgradient(cx:0.5,\
    cy: 0.5,\
    fx: 0.5,\
    fy: 0.5,\
    radius: 1.5,\
    stop: 0.2 #4fc1e9,\
    stop: 0.8 #3bafda);\
}\
\
QLineEdit {\
    border: 1px solid #aab2bd;\
    border-radius: 4px;\
    font-size: 12px;\
    padding: 5px 8px;\
    selection-background-color: lightgray;\
}\
\
QLineEdit:focus {\
    border: 1px solid #3bafda;\
}'
pre_salt = 'SUNNY-'
nex_salt = ':SHERRY'


class MainForm(Ui_Form, QWidget):
    copy_signal = pyqtSignal(int)

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('测评软件授权码生成器V1.0')
        self.generate_pushButton.clicked.connect(self.generate)
        self.encrypt_lineEdit.setEnabled(False)
        self.setWindowIcon(QIcon(frozen_dir.app_path() + r'/res/app_icon.png'))
        self.copy_pushButton.clicked.connect(self.copy)
        self.mac_lineEdit.textChanged.connect(self.tran_upper)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setStyleSheet(STYLE)
        self.hint_label.setVisible(False)
        self.copy_signal.connect(self.dis_hint)
        self.generate_pushButton.setProperty('class', 'Aqua')
        self.copy_pushButton.setProperty('class', 'Aqua')
        th = threading.Thread(target=self.set_mac)
        th.start()

    def copy(self):
        if self.encrypt_lineEdit.text() == '':
            return
        cb = QApplication.clipboard()
        cb.setText(self.encrypt_lineEdit.text())
        self.hint_label.setVisible(True)
        th = threading.Thread(target=self.dis_hint, args=(1,))
        th.setDaemon(True)
        th.start()

    def dis_hint(self, tag):
        if tag:
            self.hint_label.setText('拷贝成功,宝贝你可以按Crtl+V进行粘贴啦!')
            time.sleep(2)
        else:
            self.hint_label.setText('拷贝失败了,宝贝请重试一下吧~')
            time.sleep(2)
        self.hint_label.setVisible(False)

    def tran_upper(self):
        """
        将输入转换为大写形式
        """
        txt = self.mac_lineEdit.text()
        self.mac_lineEdit.setText(txt.upper())

    def set_mac(self):
        self.mac_lineEdit.setText(self.get_mac_address())

    def generate(self):
        if self.mac_lineEdit.text() == '':
            QMessageBox.warning(self, '提示', '宝贝你还没有输入内容呢!!!')
            return
        self.encrypt_lineEdit.setText(self.get_md5(pre_salt+self.mac_lineEdit.text()+nex_salt))
        print(pre_salt+self.mac_lineEdit.text()+nex_salt)

    @staticmethod
    def get_md5(data):
        """
        获取md5加密密文
        :param data: 明文
        :return: 加密后的密文
        """
        m = hashlib.md5()
        b = data.encode(encoding='utf-8')
        m.update(b)
        return m.hexdigest()

    @staticmethod
    def get_mac_address():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return "-".join([mac[e:e + 2] for e in range(0, 11, 2)]).upper()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
