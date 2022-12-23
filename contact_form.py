# contact_form.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
	QTabWidget, QLabel, QRadioButton, QGroupBox, 
	QLineEdit, QHBoxLayout, QVBoxLayout)

class ContactForm(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 300)
		self.setWindowTitle("Contact Form") # 창 캡션
		self.setupTabs()
		self.show()

	def setupTabs(self):

		self.info_tab = QTabWidget(self)

		self.prof_details_tab = QWidget()
		self.background_tab = QWidget()

		self.info_tab.addTab(self.prof_details_tab, "개인 정보")
		self.info_tab.addTab(self.background_tab, "학력 정보")		

		self.profDetailTab()
		self.backgroundTab()

		h_box = QHBoxLayout()
		h_box.addWidget(self.info_tab)

		self.setLayout(h_box)

	def profDetailTab(self):
		name_label = QLabel("이름")
		name_entry = QLineEdit()

		address_label = QLabel("주소")
		address_entry = QLineEdit()

		gender_gb = QGroupBox("성별")
		male_rb = QRadioButton("Male")
		female_rb = QRadioButton("Female")

		h_box_gender = QHBoxLayout()
		h_box_gender.addWidget(male_rb)
		h_box_gender.addWidget(female_rb)
		gender_gb.setLayout(h_box_gender)

		v_box = QVBoxLayout()
		v_box.addWidget(name_label)
		v_box.addWidget(name_entry)
		v_box.addStretch()
		v_box.addWidget(address_label)
		v_box.addWidget(address_entry)
		v_box.addStretch()
		v_box.addWidget(gender_gb)

		self.prof_details_tab.setLayout(v_box)

	def backgroundTab(self):
		self.edu_gb = QGroupBox("학력")

		v_box = QVBoxLayout()

		for edu in ["고졸", "전문학사","학사","석사","박사"]:
			edu_rb = QRadioButton(edu)
			v_box.addWidget(edu_rb)

		self.edu_gb.setLayout(v_box)

		back_v_box = QVBoxLayout()
		back_v_box.addWidget(self.edu_gb)

		self.background_tab.setLayout(back_v_box)

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv

	# print(sys.argv)
	window = ContactForm()
	sys.exit(app.exec_())