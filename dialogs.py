import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

class AuthorWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 250)
		self.setWindowTitle("QMessageBox Widget")
		self.displayWidgets()
		self.show()

	def displayWidgets(self):
		author_label = QLabel("검색하실 저자 이름을 입력하세요", self)
		author_label.move(40,60)

		author_name = QLabel("이름 : " , self)
		author_name.move(50,90)

		self.name_entry = QLineEdit(self)
		self.name_entry.move(95, 90)
		self.name_entry.setPlaceholderText("이름 성")

		self.search_button = QPushButton('검색', self)
		self.search_button.move(90,130)
		self.search_button.resize(80,20)
		self.search_button.clicked.connect(self.searchAuthor)

		self.clear_button = QPushButton('Clear', self)
		self.clear_button.clicked.connect(self.clearEntries)
		self.clear_button.move(200,130)
		self.clear_button.resize(80,20)

	def searchAuthor(self) :
		try:
			with open('files/authors.txt', 'r',encoding = 'utf-8') as f:
				authors = [line.rstrip('\n') for line in f]
		except FileNotFoundError:
			print('file not found')
	
		not_found = QMessageBox()
		if self.name_entry.text() in authors :
			QMessageBox().information(self, "저자 검색", "저자가 검색되었어요", QMessageBox.Ok,  QMessageBox.Ok)
		else :
			not_found = QMessageBox().question(self, "저자 검색", "그런 저자는 없는데요\n 계속 검색하시겠습니까?", QMessageBox.Yes | QMessageBox.No,  QMessageBox.No)

		if not_found == QMessageBox.No :
			print('Program end')
			self.close()
		
		else :
			pass
		# sender = self.sender()
		# if sender.text() == '검색':		
		# 	self.bmi_label.setText(f"Your BMI : {bmi} ")
	
	def clearEntries(self) :
		self.name_entry.clear()
		

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	window = AuthorWindow()
	sys.exit(app.exec_())
