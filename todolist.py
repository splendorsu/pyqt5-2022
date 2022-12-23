# todolist.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit,
	QPushButton, QButtonGroup, QCheckBox, QLineEdit, QMessageBox, 
	QComboBox, QSpinBox, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

# QLineEdit : 1줄만 입력 가능
# QTextEdit : 여러줄 입력 가능

class AppForm(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 600, 400) # 창 위치 지정
		self.setWindowTitle("Todo List") # 창 캡션
		self.todoWidgets()
		self.show() 

	def todoWidgets(self):
		main_grid = QGridLayout()

		title = QLabel("Todo List")
		title.setFont(QFont("Arial", 24))
		title.setAlignment(Qt.AlignCenter)
		
		close_button = QPushButton("Close")
		close_button.clicked.connect(self.close)

		mustdo_lable = QLabel("할일")
		mustdo_lable.setFont(QFont("Arial", 20))
		mustdo_lable.setAlignment(Qt.AlignCenter)
		appts_label = QLabel("약속")
		appts_label.setFont(QFont("Arial", 20))
		appts_label.setAlignment(Qt.AlignCenter)

		# 할일 섹션
		mustdo_grid = QGridLayout()
		mustdo_grid.setContentsMargins(5,5,5,5)
		mustdo_grid.addWidget(mustdo_lable, 0,0,1,2)
		for position in range(1, 15):
			cb = QCheckBox()
			lineedit = QLineEdit()
			lineedit.setMinimumWidth(200)
			mustdo_grid.addWidget(cb, position, 0)
			mustdo_grid.addWidget(lineedit, position, 1)

		# 약속 섹션
		morning_label = QLabel("오전")
		morning_label.setFont(QFont("Arial", 16))
		morning_entry = QTextEdit()
		afternoon_label = QLabel("오후")
		afternoon_label.setFont(QFont("Arial", 16))
		afternoon_entry = QTextEdit()
		evening_label = QLabel("저녁")
		evening_label.setFont(QFont("Arial", 16))
		evening_entry = QTextEdit()

		v_box_appts = QVBoxLayout()
		v_box_appts.setSpacing(10)		
		v_box_appts.addWidget(appts_label)
		v_box_appts.addWidget(morning_label)
		v_box_appts.addWidget(morning_entry)
		v_box_appts.addWidget(afternoon_label)
		v_box_appts.addWidget(afternoon_entry)
		v_box_appts.addWidget(evening_label)
		v_box_appts.addWidget(evening_entry)
		
		main_grid.addWidget(title, 0, 0, 1, 2)
		main_grid.addLayout(mustdo_grid, 1, 0)
		main_grid.addLayout(v_box_appts, 1, 1)
		main_grid.addWidget(close_button, 2, 0, 1, 2)

		self.setLayout(main_grid)


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = AppForm()
	sys.exit(app.exec_())
