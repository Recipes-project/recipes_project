
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import requests
from bs4 import BeautifulSoup
import webbrowser
# from lotte_final import *

# 커널 충돌로 lotte.ipynb에서 만든 리스트가 불려오지 않아 임의로 리스트 정의함
list_d = [{'main_key': '치즈', 'sub_key': ('슈', 0.7635844945907593)},
 {'main_key': '닭갈비', 'sub_key': ('해파리', 0.9521470665931702)},
 {'main_key': '부대찌개', 'sub_key': ('고기만', 0.9328819513320923)},
 {'main_key': '돼지', 'sub_key': ('찌개', 0.7788151502609253)},
 {'main_key': '앞다리', 'sub_key': ('목살', 0.821096658706665)},
 {'main_key': '냉동', 'sub_key': ('쌀국수', 0.7521064877510071)},
 {'main_key': '현미', 'sub_key': ('잡곡', 0.6692217588424683)},
 {'main_key': '미나리', 'sub_key': ('데친', 0.8159814476966858)},
 {'main_key': '바지락', 'sub_key': ('조개', 0.7604948878288269)},
 {'main_key': '돼지', 'sub_key': ('찌개', 0.7788151502609253)}]

# qtpy에서 사용하기 위한 key 저장
list_A = []

for A in range(len(list_d)):
    ori_A = list_d[A]['main_key']
    list_A.append(ori_A)

list_A = list(set(list_A))
list_A


recipes_ui = 'C:/localRepository/recipes_oraganization/recipes.ui'


class MyWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        uic.loadUi(recipes_ui, self)

        self.pushButton.clicked.connect(self.pushButtonClicked)
        # self.lineEdit.textChanged.connect(self.line_changed)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)

        self.comboBox.addItems(list_A)
        self.comboBox.activated[str].connect(lambda :self.selectedComboItem(self.comboBox))
        self.pushButton.clicked.connect(self.selectedComboItem)

        self.show()

 
    def line_changed(self):
        # self.label_end.setText('')
        pass
 
    def pushButtonClicked(self):

        url = f'https://www.10000recipe.com/recipe/list.html?q='
        keyword = self.comboBox.currentText()
        url_b = '&query=&order=date'
        
        result = requests.get(url + keyword + url_b)
        bs_obj = BeautifulSoup(result.content, 'html.parser')
        

        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(10) 
        self.tblResult.setHorizontalHeaderLabels(['레시피 이름', '레시피 링크'])
        self.tblResult.setColumnWidth(0,350)
        self.tblResult.setColumnWidth(1,250)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # read only

        ul = bs_obj.find('ul', class_='common_sp_list_ul ea4')
        lis = ul.find_all('li', class_='common_sp_list_li')

        list_title = []
        list_url = []

        for li in lis:
            title = li.find('div',class_= 'common_sp_caption_tit line2').get_text()
            list_title.append(title)

            url = li.find('div', class_='common_sp_thumb')
            url = url.find('a')['href']
            url = f'https://www.10000recipe.com/{url}'
            list_url.append(url)
  

        for i in range(len(list_title)):
            self.tblResult.setItem(i,0,QTableWidgetItem(list_title[i]))
            self.tblResult.setItem(i,1,QTableWidgetItem(list_url[i]))

    def tblResultSelected(self) -> None:
        selected = self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected, 1).text()
        webbrowser.open(link)


    ### 콤보박스 관련 함수
    def selectedComboItem(self,text):
        # print(self.comboBox.currentText())
        pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Dialog = MyWindow()
    Dialog.show()
    app.exec_()