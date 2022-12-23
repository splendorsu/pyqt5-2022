# Regisration
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit, QMessageBox, QCheckBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

class CreateNewUser(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(130, 130, 400, 400)
		self.setWindowTitle("회원가입 창")
		self.displayWidgets()
		self.show()

	def displayWidgets(self) :
		new_user_image = 'images/new_user_icon.png'		
		try:
			with open(new_user_image):
				new_user = QLabel(self)
				pixmap = QPixmap(new_user_image)
				new_user.setPixmap(pixmap)
				new_user.move(180, 60)

		except FileNotFoundError:
			print('Not Found Image')


		# 아이디 입력
		id_label = QLabel(self)
		id_label.setText("아이디 : ") # Label에 문구 작성하기
		id_label.move(50, 180)
		id_label.setFont(QFont('Arial', 12))		

		self.id_entry = QLineEdit(self)
		self.id_entry.move(130, 180)
		self.id_entry.resize(200, 20)

		# 비밀번호 입력
		pw_label  = QLabel("비밀번호 : ", self)
		pw_label.move(50, 240)

		self.pw_entry = QLineEdit(self)
		self.pw_entry.setEchoMode(QLineEdit.Password)
		self.pw_entry.move(130, 240)
		self.pw_entry.resize(200,20)

		pw_confirm_label  = QLabel("비밀번호 확인 : ", self)
		pw_confirm_label.move(50, 270)

		self.pw_confirm_entry = QLineEdit(self)
		self.pw_confirm_entry.setEchoMode(QLineEdit.Password)
		self.pw_confirm_entry.move(130, 270)
		self.pw_confirm_entry.resize(200,20)

		# 회원가입 버튼
		sign_up_button = QPushButton("회원가입", self)
		sign_up_button.move(100,310)
		sign_up_button.resize(200,40)
		sign_up_button.clicked.connect(self.confirmSignUp)

	def confirmSignUp(self):
		username = self.id_entry.text()
		password = self.pw_entry.text()
		password_confirm = self.pw_confirm_entry.text()

		if password != password_confirm : 
			QMessageBox.Warning(self, "에러 메세지", "비밀번호가 일치하지 않습니다." , QMessageBox.Close, QMessageBox.Close)

		else :

			with open('files/users.txt', 'a+', encoding = 'utf-8') as f : 
				f.write(username + " ")
				f.write(password + "\n")
			self.close()

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	window = CreateNewUser()
	sys.exit(app.exec_())
