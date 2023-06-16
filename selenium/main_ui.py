from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QLineEdit,QGridLayout,QGroupBox
from login_ui import LoginWidget
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from login_ui import driver
from selenium.webdriver.common.by import By
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.login_widget = LoginWidget(self)  # 로그인 위젯 생성
        self.main_widget = QMainWindow()
        self.ui.setupUi(self.main_widget)

        self.stacked_widget.addWidget(self.login_widget)  # 로그인 위젯 추가
        self.stacked_widget.addWidget(self.main_widget)

        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.login_widget)
        self.resize(self.login_widget.size())
        
        self.login_widget.loginSuccess.connect(self.loggedIn)  # loginSuccess signal에 loggedIn 메소드를 연결
        
    def loggedIn(self):
        self.stacked_widget.setCurrentWidget(self.main_widget)
        self.resize(600,700)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 360, 270, 250))  #그룹박스 1 
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 120, 16)) #복지 및 급여
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(16, 12))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 150, 16)) #업무
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setIconSize(QtCore.QSize(16, 15))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 90, 120, 16)) #사내문화
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 120, 150, 16)) #승진 기회
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 150, 111, 16)) #리뷰 작성일 
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_11.setGeometry(QtCore.QRect(160, 30, 91, 16)) #경영진
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_12.setGeometry(QtCore.QRect(160, 60, 110, 16)) #평균연봉 
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 360, 280, 250)) #그룹박스2
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_13.setGeometry(QtCore.QRect(10, 30, 150, 16)) #면접리뷰 제목
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_14.setGeometry(QtCore.QRect(10, 60, 111, 16)) #면접 결과
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_2) #면접 질문
        self.checkBox_15.setGeometry(QtCore.QRect(10, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_16.setGeometry(QtCore.QRect(10, 120, 150, 16)) #면접답변,느낌
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_17.setGeometry(QtCore.QRect(10, 150, 170, 16)) #면접 리뷰 작성일자
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_17.setFont(font)
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_18.setGeometry(QtCore.QRect(150, 30, 120, 16)) #난이도
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_18.setFont(font)
        self.checkBox_18.setObjectName("checkBox_18")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 310, 121, 40)) #리뷰요약
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 310, 121, 40))#면접요약
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 40, 561, 261)) #회사명 그룹박스
        self.groupBox_3.setObjectName("groupBox_3")

        self.gridLayout = QGridLayout(self.groupBox_3)  # Changed to grid layout

        self.pushButton_5 = QtWidgets.QPushButton("추가하기", self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 10, 120, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton("Following", self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 10, 101, 30))
        self.pushButton_4.setObjectName("pushButton_4")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_5.clicked.connect(self.add_line_edit)
        self.line_edits = []
        self.counter = 0

        # 기존의 입력 창 추가
        self.add_line_edit() #lineEdit_1

        
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        
    def on_pushButton_2_clicked(self):
    
        review_crawl = reviewCrawlOne(self)
        review_crawl.reviewCrawlOne()
    def add_line_edit(self):
        if self.counter < 12:  # (3*4) line edits
            column = self.counter // 4
            row = self.counter % 4
            line_edit = QLineEdit(self.groupBox_3)
            line_edit.setObjectName("lineEdit_" + str(self.counter + 1))
            self.line_edits.append(line_edit)
            self.gridLayout.addWidget(line_edit, row, column)  # add widget to grid layout
            self.counter += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JobBoost"))
  
        self.groupBox.setTitle(_translate("MainWindow", "<리뷰 요약 항목>"))
        self.checkBox.setText(_translate("MainWindow", "복지 및 급여"))
        self.checkBox_2.setText(_translate("MainWindow", "업무와 삶의 균형"))
        self.checkBox_3.setText(_translate("MainWindow", "사내 문화"))
        self.checkBox_4.setText(_translate("MainWindow", "승진 기회 및 가능성"))
        self.checkBox_5.setText(_translate("MainWindow", "리뷰 작성일자"))
        self.checkBox_11.setText(_translate("MainWindow", "경영진"))
        self.checkBox_12.setText(_translate("MainWindow", "평균 연봉"))
        self.groupBox_2.setTitle(_translate("MainWindow", "<면접 리뷰 요약 항목>"))
        self.checkBox_13.setText(_translate("MainWindow", "면접 리뷰 제목"))
        self.checkBox_14.setText(_translate("MainWindow", "면접 결과"))
        self.checkBox_15.setText(_translate("MainWindow", "면접 질문"))
        self.checkBox_16.setText(_translate("MainWindow", "면접 답변, 느낌"))
        self.checkBox_17.setText(_translate("MainWindow", "면접 리뷰 작성 일자"))
        self.checkBox_18.setText(_translate("MainWindow", "면접 난이도"))
        self.pushButton_2.setText(_translate("MainWindow", "리뷰요약"))
        self.pushButton_3.setText(_translate("MainWindow", "면접요약"))
        self.groupBox_3.setTitle(_translate("MainWindow", "회사명"))
        self.pushButton_5.setText(_translate("MainWindow", "입력창 추가"))
        self.pushButton_4.setText(_translate("MainWindow", "Following"))

class reviewCrawlOne():
    def __init__(self, main_window):
        self.main_window = main_window


    def reviewCrawlOne(self):

        #원하는 회사의 리뷰 페이지까지 이동
        company = driver.find_element_by_css_selector("input#search_bar_search_query")
        company.send_keys("네이버")
        company.send_keys(Keys.RETURN)
        driver.implicitly_wait(15)

        driver.find_element_by_css_selector("a.tit").click()
        driver.implicitly_wait(15)

        driver.find_element_by_css_selector("button.btn_close_x_ty1 ").click()
        driver.implicitly_wait(15)

        review_cnt_raw = driver.find_elements_by_css_selector("span.num.notranslate")[1]
        review_cnt = int(review_cnt_raw.text)
        review_page = int(review_cnt/5) + 1
        

        #크롤링한 정보를 담을 리스트명 정의
        list_div = []
        list_cur = []
        list_date =[]
        list_stars = []
        list_summery = []
        list_merit = []
        list_disadvantages = []
        list_managers =[]


        #원하는 회사의 직무/근속여부/일시/요약/평점/장점/단점/경영진에게 바라는 점 크롤링 (for문으로 반복)
        for i in range(review_page): 

            #직무, 근속여부, 지역 ,일시
            user_info = driver.find_elements_by_css_selector("span.txt1")

            #한 페이지 안의 리뷰 갯수
            #한 페이지에 정보 5set씩 나옴. 마지막 페이지는 5개 미만일 수 있으므로 count 변수를 반복횟수로 넣어줌.
            count = int(len(user_info)/4)

            list_user_info = []

            for j in user_info:
                list_user_info.append(j.text)

            for j in range(count):            
                a = list_user_info[4*j]
                list_div.append(a)
                
                b = list_user_info[4*j+1]
                list_cur.append(b)

                c = list_user_info[4*j+3]
                list_date.append(c)

            #별점
            stars = driver.find_elements_by_css_selector("div.star_score")
            for j in stars:
                a = j.get_attribute('style')
                if a[7:9] == '20':
                    list_stars.append("1점")
                elif a[7:9] == '40':
                    list_stars.append("2점")
                elif a[7:9] == '60':
                    list_stars.append("3점")
                elif a[7:9] == '80':
                    list_stars.append("4점")
                else:
                    list_stars.append("5점")
                
            #요약 정보
            summery = driver.find_elements_by_css_selector("h2.us_label")

            for j in summery:
                list_summery.append(j.text)
            
            #장점, 단점, 경영진에게 바라는 점
            list_review = []

            review = driver.find_elements_by_css_selector("dd.df1")

            for j in review:
                list_review.append(j.text)

            for j in range(count):            #한 페이지에 정보 5set씩 나옴. 마지막 페이지는 5개 미만일 수 있으므로 count 변수를 반복횟수로 넣어줌.
                a = list_review[3*j]
                list_merit.append(a)
                
                b = list_review[3*j+1]
                list_disadvantages.append(b)

                c = list_review[3*j+2]
                list_managers.append(c)

            # 다음 페이지 클릭 후 for문 진행, 끝 페이지에서 다음 페이지 클릭 안되는 것 대비해서 예외처리 구문 추가
            try:
                driver.find_element_by_css_selector("a.btn_pgnext").click()
                driver.implicitly_wait(15)
                time.sleep(2) #implicityly_wait로 잘 작동하지 않아서 추가함
            except:
                pass


        # step8.pandas 라이브러리로 표 만들기
        total_data = pd.DataFrame()
        total_data['날짜'] = pd.Series(list_date)
        total_data['직무'] = pd.Series(list_div)
        total_data['재직여부'] = pd.Series(list_cur)
        total_data['별점'] = pd.Series(list_stars)
        total_data['요약'] = pd.Series(list_summery)
        total_data['장점'] = pd.Series(list_merit)
        total_data['단점'] = pd.Series(list_disadvantages)
        total_data['경영진에게 바라는 점'] = pd.Series(list_managers)

        # step9.엑셀 형태로 저장하기
        total_data.to_excel(self.lineEdit_CN.text() + "_잡플래닛 리뷰.xls" ,index=True)

        # step10.크롬 드라이버 종료
        driver.quit()
    
class reviewCrawlMore():
    query = []
    # lineEdit_1부터 lineEdit_12까지 반복하여 값 저장
    
    #for i in range(1, 13):
        #line_edit_value = locals()["lineEdit_" + str(i)].text()  # lineEdit 값 가져오기
        #query.append(line_edit_value)  # usr 배열에 값 추가

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())