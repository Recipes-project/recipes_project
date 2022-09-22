
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
list_d = [{'key': '우유', 'sub_key': [('생크림', 0.7950142025947571), ('무염', 0.761357307434082), ('노른자', 0.7127785682678223), ('연유', 0.702159583568573), ('이스트', 0.6995631456375122), 
            ('버터', 0.6953340768814087), ('파우더', 0.6717946529388428), ('베이킹파우더', 0.6663267612457275), ('빵가루', 0.6544387340545654), ('흰자', 0.6529161334037781)]}, 
            {'key': '양지', 'sub_key': [('사태', 0.8905509114265442), ('샤브샤브', 0.8868820071220398), ('쇠고기', 0.8584051132202148), ('자른', 0.8546854257583618), ('미역국', 0.8422269225120544), 
            ('갈비살', 0.8276513814926147), ('염장', 0.8213863372802734), ('토란', 0.8185833692550659), ('용소', 0.8079002499580383), ('방', 0.7932040095329285)]}, 
            {'key': '토종닭', 'sub_key': [('라자냐', 0.9339334964752197), ('꼬리', 0.933007538318634), ('강정', 0.932475745677948), ('점', 0.9290907979011536), ('사진', 0.9290493726730347), 
            ('삶기', 0.9243596792221069), ('민물', 0.9243115782737732), ('광어', 0.9209685325622559), ('랍스터', 0.9207404851913452), ('찰옥수수', 0.9197703003883362)]}, 
            {'key': '갈비', 'sub_key': [('등뼈', 0.8643282055854797), ('등', 0.853766143321991), ('근', 0.808203935623169), ('돼지', 0.8056599497795105), ('돼지갈비', 0.7501478791236877), 
            ('콜라', 0.7415348887443542), ('사태', 0.731940507888794), ('돈', 0.7301970720291138), ('찜', 0.7254461050033569), ('수육', 0.7155761122703552)]}]

list_A = []

for A in range(len(list_d)):
    ori_A = list_d[A]['key']
    ori_B = list_d[A]['sub_key']

    list_A.append(ori_A)


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