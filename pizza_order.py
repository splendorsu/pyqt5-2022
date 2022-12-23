# pizza_order.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
	QTabWidget, QLabel, QRadioButton, QGroupBox, 
	QButtonGroup, QPushButton, QGridLayout,QMessageBox,
	QLineEdit, QHBoxLayout, QVBoxLayout)

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import  Qt

style_sheet = """
QWidget {
    background-color: #C92108;
}
QWidget#Tabs {
    background-color: #FCEBCD;
    border-radius: 4px;
}
QWidget#ImageBorder {
    background-color: #FCF9F3;
    border-width: 2px;
    border-style: solid;
    border-radius: 4px;
    border-color: #FABB4C;
}
QWidget#Side {
    background-color: #EFD096;
    border-radius: 4px;
}
QLabel {
    background-color: #EFD096;
    border-width: 2px;
    border-style: solid;
    border-radius: 4px;
    border-color: #EFD096;
}
QLabel#Header {
    background-color: #EFD096;
    border-width: 2px;
    border-style: solid;
    border-radius: 4px;
    border-color: #EFD096;
    padding-left: 10px;
    color: #961A07;
}
QLabel#ImageInfo {
    background-color: #FCF9F3;
    border-radius: 4px;
}
QGroupBox {
    background-color: #FCEBCD;
    color: #961A07;
}
QRadioButton {
    background-color: #FCF9F3;
}
QPushButton {
    background-color: #C92108;
    border-radius: 4px;
    padding: 6px;
    color: #FFFFFF;
}
QPushButton:pressed {
    background-color: #C86354;
    border-radius: 4px;
    padding: 6px;
    color: #DBD8D7;
}

"""


class pizzaOrder(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		# self.setGeometry(100, 100, 400, 300)
		self.setMinimumSize(600,700) # 창 최소 사이즈 지정
		self.setWindowTitle("Pizza Order") # 창 캡션
		
		self.setupTabs()
		self.show()

	def setupTabs(self):
		self.info_tab = QTabWidget(self)

		self.pizza_tab = QWidget()
		self.pizza_tab.setObjectName("Tabs")
		self.sidedish_tab = QWidget()
		self.sidedish_tab.setObjectName("Tabs")

		self.info_tab.addTab(self.pizza_tab, "Pizza")
		self.info_tab.addTab(self.sidedish_tab, "Sidedish")
		
		self.pizzaTab()
		self.sidedishTab()

		# side widget : 피자 선택 후, Side 메뉴 선택 시 기존 선택 내역 확인용
		self.side_widget  = QWidget()
		self.side_widget.setObjectName("Tabs")

		order_label = QLabel("주문 현황")
		order_label.setObjectName("Header")

		item_box = QWidget()
		item_box.setObjectName("Side")
		pizza_label = QLabel("피자 타입 : ")
		self.display_pizza_label = QLabel("")
		topping_label = QLabel("토핑 : ")
		self.display_topping_label = QLabel("")
		side_label = QLabel("기타 메뉴 : ")
		self.display_side_label = QLabel("")

		item_grid = QGridLayout()
		item_grid.addWidget(pizza_label, 0, 0, Qt.AlignRight)
		item_grid.addWidget(self.display_pizza_label, 0, 1)
		item_grid.addWidget(topping_label, 1, 0, Qt.AlignRight)
		item_grid.addWidget(self.display_topping_label, 1, 1)
		item_grid.addWidget(side_label, 2, 0, Qt.AlignRight)
		item_grid.addWidget(self.display_side_label, 2, 1)		

		item_box.setLayout(item_grid)

		v_box_side = QVBoxLayout()
		v_box_side.addWidget(order_label)
		v_box_side.addWidget(item_box)
		v_box_side.addStretch()

		self.side_widget.setLayout(v_box_side)

		h_box = QHBoxLayout()
		h_box.addWidget(self.info_tab)
		h_box.addWidget(self.side_widget)

		self.setLayout(h_box)


	def pizzaTab(self):
		name_label = QLabel("피자를 선택하세요")
		name_label.setObjectName("Header")

		desc_box = QWidget()
		desc_box.setObjectName("ImageBorder")
		pizza_image_path = 'images/pizza.jpg'
		pizza_image = self.loadImage(pizza_image_path)
		pizza_desc = QLabel()
		pizza_desc.setObjectName("ImageInfo")
		pizza_desc.setText("크랩&립 하우스 #스노우 크랩&치즈의 눈꽃 축제와 립 스테이크의 불꽃 축제! #글로벌 축제의 맛이 하프앤하프로 만나다!")
		pizza_desc.setWordWrap(True) # 문장이 길때 맞춰서 다음줄로 넘겨주는 역할

		h_box = QHBoxLayout()
		h_box.addWidget(pizza_image)
		h_box.addWidget(pizza_desc)
		desc_box.setLayout(h_box)

		# crust choices 
		crust_gbox = QGroupBox()
		crust_gbox.setTitle("크러스트 선택")

		self.crust_group = QButtonGroup()
		v_box_gb = QVBoxLayout()
		crust_list = ["트리플 치즈 버스트 엣지", "더블치즈엣지", "기본"]

		for cr in crust_list :
			crust_rb = QRadioButton(cr)
			v_box_gb.addWidget(crust_rb)
			self.crust_group.addButton(crust_rb)
		# self.crust_group.setExclusive(False)
		crust_gbox.setLayout(v_box_gb)

		# topping choices 
		topping_gbox = QGroupBox()
		topping_gbox.setTitle("토핑 선택")

		self.topping_group = QButtonGroup()
		v_box_gb = QVBoxLayout()
		topping_list = ["치즈", "파인애플", "페퍼로니", "올리브","비프","토마토"]

		for top in topping_list :
			topping_rb = QRadioButton(top)
			v_box_gb.addWidget(topping_rb)
			self.topping_group.addButton(topping_rb)
		self.topping_group.setExclusive(False)
		topping_gbox.setLayout(v_box_gb)

		# 주문 추가 버튼
		add_to_order_button1 = QPushButton("주문 추가")
		add_to_order_button1.clicked.connect(self.displayPizzaInOrder)

		page1_v_box = QVBoxLayout()
		page1_v_box.addWidget(name_label)
		page1_v_box.addWidget(desc_box)
		page1_v_box.addWidget(crust_gbox)
		page1_v_box.addWidget(topping_gbox)
		page1_v_box.addStretch()
		page1_v_box.addWidget(add_to_order_button1, alignment = Qt.AlignRight)

		self.pizza_tab.setLayout(page1_v_box)

	def loadImage(self, image_path):
		try:
			with open(image_path):
				image = QLabel(self)
				image.setObjectName("ImageInfo")
				pixmap = QPixmap(image_path)
				image.setPixmap(pixmap.scaled(image.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation ))
			return image
		except FileNotFoundError : 
			print("Image Not Found")


	def sidedishTab(self):
		side_label = QLabel("특가로 제공되는 사이드 디시 선택")
		side_label.setObjectName("Header")

		desc_box = QWidget()
		desc_box.setObjectName("ImageBorder")
		side_image_path = 'images/pasta.jpg'
		side_image = self.loadImage(side_image_path)
		side_desc = QLabel()
		side_desc.setObjectName("ImageInfo")
		side_desc.setText("모든 피자 주문 시 사이드디시 반값")
		side_desc.setWordWrap(True) # 문장이 길때 맞춰서 다음줄로 넘겨주는 역할

		h_box = QHBoxLayout()
		h_box.addWidget(side_image)
		h_box.addWidget(side_desc)
		desc_box.setLayout(h_box)

		# side choices 
		side_gbox = QGroupBox()
		side_gbox.setTitle("사이드 선택")

		self.side_group = QButtonGroup()
		v_box_gb = QVBoxLayout()
		side_list = ["씨푸드 로제 파스타", "웨스턴 핫윙","허니&갈릭 윙스",
		"베이컨 까르보나라 페투치니","치즈 볼로네즈 스파게티"]

		for side in side_list :
			side_rb = QRadioButton(side)
			v_box_gb.addWidget(side_rb)
			self.side_group.addButton(side_rb)
		self.side_group.setExclusive(False)
		side_gbox.setLayout(v_box_gb)

		# 주문 추가 버튼
		add_to_order_button1 = QPushButton("주문 추가")
		add_to_order_button1.clicked.connect(self.displaySideInOrder)

		page2_v_box = QVBoxLayout()
		page2_v_box.addWidget(side_label)
		page2_v_box.addWidget(desc_box)
		page2_v_box.addWidget(side_gbox)
		page2_v_box.addStretch()
		page2_v_box.addWidget(add_to_order_button1, alignment = Qt.AlignRight)

		self.sidedish_tab.setLayout(page2_v_box)

	def displayPizzaInOrder(self):
		try :
			pizza_text = self.crust_group.checkedButton().text()
			self.display_pizza_label.setText(pizza_text)

			toppings = self.collectToppingsInList()
			toppings_str = '\n'.join(toppings)
			self.display_topping_label.setText(toppings_str)

		except:
			print("No value selected")
			pass

	def displaySideInOrder(self):
		try :
			sides = self.collectSidesInList()
			sides_str = '\n'.join(sides)
			self.display_side_label.setText(sides_str)

		except:
			print("No value selected")
			pass

	def KeyPressEvent(self, event):
		if event.key() == Qt.Key_Escape :
			print("App Close!")		
			self.close()

	def closeEvent(self, event):
		quit_msg = QMessageBox.question(self, "프로그램 종료",
			"정말로 종료하시겠습니까?", 
			QMessageBox.Yes | QMessageBox.No,
			QMessageBox.Yes)
		if quit_msg == QMessageBox.Yes :
			event.accept() # 이벤트를 받아들임
		else:
			event.ignore() # 이벤트를 무시함

	def collectToppingsInList(self):
		toppings_list = [button.text() for i, button in enumerate(self.topping_group.buttons()) if button.isChecked()]
		return toppings_list

	def collectSidesInList(self):
		sides_list = [button.text() for i, button in enumerate(self.side_group.buttons()) if button.isChecked()]
		return sides_list



# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	app.setStyleSheet(style_sheet)
	# print(sys.argv)
	window = pizzaOrder()
	sys.exit(app.exec_())