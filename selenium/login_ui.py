import time
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import  QMessageBox, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import sys
from PyQt5.QtCore import pyqtSignal

driver = None

class LoginWidget(QtWidgets.QDialog):
    loginSuccess = pyqtSignal()
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        self.setupUi(self)
        
        # 로그인 버튼 클릭 시, main UI를 보여줌
        self.pushButton_Login.clicked.connect(self.loginToJobPlanet)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 220)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 341, 160))
        self.groupBox.setObjectName("groupBox")

        # Add labels for ID and password
        self.label_ID = QtWidgets.QLabel(self.groupBox)
        self.label_ID.setGeometry(QtCore.QRect(20, 30, 80, 20))
        self.label_ID.setObjectName("label_ID")
        self.label_ID.setText("아이디:")
        self.label_PW = QtWidgets.QLabel(self.groupBox)
        self.label_PW.setGeometry(QtCore.QRect(20, 70, 80, 20))
        self.label_PW.setObjectName("label_PW")
        self.label_PW.setText("비밀번호:")

        self.lineEdit_ID = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ID.setGeometry(QtCore.QRect(110, 30, 200, 30))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_PW = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_PW.setGeometry(QtCore.QRect(110, 70, 200, 30))
        self.lineEdit_PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PW.setObjectName("lineEdit_PW")
        self.pushButton_Login = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Login.setGeometry(QtCore.QRect(250,120, 80, 30))
        self.pushButton_Login.setObjectName("pushButton_login")
        self.pushButton_Login.clicked.connect(self.loginToJobPlanet)
        
        self.pushButton_SignUp = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_SignUp.setGeometry(QtCore.QRect(140, 120, 100, 30))
        self.pushButton_SignUp.setObjectName("pushButton_SignUp")
        self.pushButton_SignUp.clicked.connect(self.openSignUpPage)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "JobBosst"))
        self.groupBox.setTitle(_translate("Dialog", "잡플래닛 로그인 정보 "))
        self.pushButton_Login.setText(_translate("Dialog", "로그인"))
        self.pushButton_SignUp.setText(_translate("Dialog", "회원가입")) 
        
    def openSignUpPage(self):

        url = "https://www.jobplanet.co.kr/users/sign_up?_nav=gb"
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))
    def show_main_ui(self):
            self.close()  # 로그인 창 닫기

            self.main_ui = QtWidgets.QMainWindow()
            self.ui_main = Ui_MainWindow()
            self.ui_main.setupUi(self.main_ui)
            self.main_ui.show()
    def loginToJobPlanet(self):
        # Get the ID and password from the line edits
        user_id = self.lineEdit_ID.text()
        password = self.lineEdit_PW.text()

        options = Options()
        options.headless = True #창 띄울 땐 꺼야함
        
        global driver
        # Open the login page in a new browser window
        driver = webdriver.Chrome("C:/Users/lke67/Desktop/social/selenium/chromedriver.exe",options=options)
        driver.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")

   # Fill in the login form and submit it
        login_id = driver.find_element("css selector", "input#user_email")
        login_id.send_keys(user_id)

        login_pwd = driver.find_element("css selector", "input#user_password")
        login_pwd.send_keys(password)
        #login_id.send_keys(Keys.RETURN)
        driver.find_element("css selector", "form#new_user").submit()
        time.sleep(1)
        current_url = driver.current_url
        if current_url == "https://www.jobplanet.co.kr/job":
            print("로그인 성공!")
            messagebox = QMessageBox()
            messagebox.setWindowTitle("로그인 성공")
            messagebox.setText("로그인에 성공했습니다.")

                        
            time.sleep(1)
            driver.get("https://www.jobplanet.co.kr/profile/membership")
            if "결제내역이 없습니다." in driver.page_source: #제휴대학 정보 확인
                time.sleep(1)
                driver.get("https://www.jobplanet.co.kr/profile/settings")
                if "제휴대학교 정보" in driver.page_source:
                    print("인증된 회원입니다.")
                    messagebox.setText("인증된 회원입니다. 정상적으로 로그인되었습니다.")
                    messagebox.exec_()
                    self.loginSuccess.emit()

                else:
                    print("인증되지 않은 회원입니다.")
                    messagebox.setWindowTitle("회원 인증 실패")
                    messagebox.setText("인증되지 않은 회원입니다. 결제내역이 없습니다.")

                    
            else:
                print("인증된 회원입니다.")
                messagebox.setWindowTitle("회원 인증 성공")
                messagebox.setText("인증된 회원입니다. 정상적으로 로그인되었습니다.")

                self.loginSuccess.emit()
        else:
            print("로그인 실패!")
            app = QApplication(sys.argv)
            messagebox = QMessageBox()
            messagebox.setWindowTitle("로그인 실패")
            messagebox.setText("로그인에 실패했습니다.")
            messagebox.exec_()

