import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 700, 700)

        groupBox = QGroupBox("리뷰 요약")
        checkBox1 = QCheckBox("업무와 삶의 균형")
        checkBox2 = QCheckBox("사내 문화")
        checkBox3 = QCheckBox("승진 기회 및 가능성")
        checkBox4 = QCheckBox("복지 및 급여")
        checkBox5 = QCheckBox("경영진")
        checkBox6 = QCheckBox("평균 연봉")
  
        tableWidget = QTableWidget(10, 5)
        tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tableWidget.setHorizontalHeaderLabels(["네이버", "삼성", "쿠팡", "토스", "카카오"])
        tableWidget.setMinimumHeight(500)
        tableWidget.setMinimumWidth(500)

        leftInnerLayOut = QVBoxLayout()
        leftInnerLayOut.addWidget(checkBox1)
        leftInnerLayOut.addWidget(checkBox2)
        leftInnerLayOut.addWidget(checkBox3)
        leftInnerLayOut.addWidget(checkBox4)
        leftInnerLayOut.addWidget(checkBox5)
        leftInnerLayOut.addWidget(checkBox6)

        groupBox.setLayout(leftInnerLayOut)

        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(groupBox)




        # 테이블 위젯과 버튼
        tableButtonLayOut = QVBoxLayout()
        tableButtonLayOut.addWidget(tableWidget)
        tableButtonLayOut.addStretch()




        # 오른쪽 레이아웃
        rightLayOut = QVBoxLayout()
        rightLayOut.addLayout(tableButtonLayOut)

        # 전체 레이아웃
        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(rightLayOut)

        self.setLayout(layout)
                

        tableDescLabel = QLabel("항목이름 사이의 경계선을 통해\n테이블 위젯 크기를 조절할 수 있습니다.")
        tableDescLabel.setStyleSheet("font-size: 5pt;")
        tableDescLabel.setAlignment(Qt.AlignRight)

        tableButtonLayOut.addWidget(tableWidget)
        tableButtonLayOut.addWidget(tableDescLabel)
        tableButtonLayOut.addStretch()

        downloadButton = QPushButton("다운로드")
        prevButton = QPushButton("이전")
        buttonLayOut = QHBoxLayout()
        buttonLayOut.addWidget(downloadButton)
        buttonLayOut.addWidget(prevButton)

        tableButtonLayOut.addLayout(buttonLayOut)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
