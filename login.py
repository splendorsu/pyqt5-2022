import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit, QMessageBox, QCheckBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt
from Registration import CreateNewUser

class LoginWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 350, 400)
		self.setWindowTitle("Login Widget")
		self.displayWidgets()
		self.show()

	def displayWidgets(self):
		author_label = QLabel("아이디와 비밀번호를 입력하세요", self)
		author_label.move(40,50)

		id_label = QLabel("아이디 : " , self)
		id_label.move(50,90)

		self.id_entry = QLineEdit(self)
		self.id_entry.move(110, 90)
		self.id_entry.setPlaceholderText("아이디를 입력하세요")

		pw_label = QLabel("비밀번호 : " , self)
		pw_label.move(50,130)

		self.pw_entry = QLineEdit(self)
		self.pw_entry.move(110, 130)
		self.pw_entry.setPlaceholderText("비밀번호를 입력하세요")		
		self.pw_entry.setEchoMode(QLineEdit.Password) # 비밀번호 가리기 option 1

		cb = QCheckBox("비밀번호 표시", self)
		cb.move(50,170)
		cb.stateChanged.connect(self.ShowPassword)
		# cb.toggle() # 비밀번호 가리기 option 2 toggle로 체크박스 선택했다가
		# cb.setChecked(False) # check 를 해제해서.. 아래 change state에서 echomode 로 만듦

		self.login_button = QPushButton('로그인', self)
		self.login_button.move(90,200)
		self.login_button.resize(80,20)
		self.login_button.clicked.connect(self.clicklogin)

		pw_label = QLabel("회원가입은 이 곳 : " , self)
		pw_label.move(50,250)

		self.join_button = QPushButton('회원가입', self)
		self.join_button.move(180,250)
		self.join_button.resize(80,20)
		self.join_button.clicked.connect(self.CreateNewUser)

	def ShowPassword(self, state):
		if state == Qt.Checked:
			self.pw_entry.setEchoMode(QLineEdit.Normal)
		else :
			self.pw_entry.setEchoMode(QLineEdit.Password)

	def clicklogin(self) :
		users = {} # Dictionary
		try:
			with open('files/users.txt', 'r', encoding = 'utf-8') as f:
				for line in f :
					user_fields = line.split(" ")
					username = user_fields[0]
					password = user_fields[1].rstrip('\n')
					users[username] = password

		except FileNotFoundError:
			print('file not found')
			f = open('files/users.txt', 'w')

		username = self.id_entry.text()
		password = self.pw_entry.text()

		if (username, password) in users.items():
			QMessageBox.information(self, "로그인 성공", "로그인 성공하셨습니다!", QMessageBox.Ok, QMessageBox.Ok)
			self.close()
		else :
			QMessageBox.warning(self, "로그인 실패", "아이디와 패스워드를 확인하세요!", QMessageBox.Close, QMessageBox.Close)
	
	def CreateNewUser(self):
		self.create_new_user = CreateNewUser()
		self.create_new_user.show()

	

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	window = LoginWindow()
	sys.exit(app.exec_())
