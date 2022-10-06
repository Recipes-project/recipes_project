# recipes_project

## 프로젝트 목표 : 마트 영수증 이미지에서 텍스트를 추출해 구매한 상품과 연관 있는 레시피 추천하는 시스템 생성

## 주요 사용 기능
  - 데이터 수집 : selenium.webdriver, BeautifulSoup, request
  - 전처리 : 정규식 활용(특수기호, 숫자 등 제거), konlpy의 Okt(데이터 토큰화, 불용어 제거)
  - OCR : easyOcr(영수증 이미지를 텍스트로 변환)
  - 학습 : Word2Vec(토큰화된 데이터를 학습 시켜 입력값과 유사한 단어 추출)
  - 시각화 : Qt Designer
  
# 주요 코드 및 결과

## 데이터 수집
### 만개의 레시피 웹페이지에서 각 레시피 url 데이터 크롤링
- 파일 : crawling_link.ipynb
#### 주요 코드
![링크 크롤링 코드](https://user-images.githubusercontent.com/108312150/191641441-f312862b-0b73-41ef-99c1-4b30f34b59cf.png)
#### 결과
![링크 크롤링 결과](https://user-images.githubusercontent.com/108312150/191641378-b27e78f4-3e3e-41c6-ac7f-76b984c372ad.png)

### 레시피 이름과 재료 데이터 추출
- 파일 : crawling_all.ipynb
#### 주요 코드
![레시피 이름,재료 크롤링 코드1](https://user-images.githubusercontent.com/108312150/191641626-a4cb8886-8428-4677-bca1-913457cb4760.png)
#### 결과
![레시피 이름,재료 크롤링 결과](https://user-images.githubusercontent.com/108312150/191641639-a7213631-8b97-4e3a-8f20-416880ceabb1.png)

## 전처리
### 학습을 위해 레시피 재료 전처리
- 파일 : lotte_final.ipynb
  - Okt를 이용해 재료 데이터 토큰화
  - 정규식을 이용해 재료 데이터에서 한글을 제외한 숫자, 영어, 특수문자 등을 제거
  - 불용어를 stopword로 직접 지정해 재료와 관련없는 문자 삭제
#### 주요 코드
![image](https://user-images.githubusercontent.com/108312150/194186175-696c6e1e-2dfb-4f05-aef0-76c5c3d07a71.png)
#### 결과
![전처리 결과1](https://user-images.githubusercontent.com/108312150/191641995-27c0edd3-26ca-40b3-803d-82315c45b507.png)

## OCR
### easyOcr을 이용해 영수증 이미지에서 텍스트 추출
- 파일 : lotte_final.ipynb
#### 주요 코드
![전처리 영수증,텍스트 변환 코드](https://user-images.githubusercontent.com/108312150/191643407-e99e56cc-d253-4899-93fb-0ea19843213e.png)
#### 결과
![영수증,텍스트 변환 결과1](https://user-images.githubusercontent.com/108312150/191642231-1deeff79-46a5-40a7-a177-c1e4ea035f90.png)

## 학습
### Word2Vec(토큰화된 재료 데이터를 학습시켜 입력값과 가장 유사한 단어를 추출하도록 학습)
- 파일 : lotte_final.ipynb
#### 주요 코드
![학습 코드1](https://user-images.githubusercontent.com/108312150/191642329-4115343c-9398-4643-82fb-a7a700fc741a.png)
'우유'를 입력했을 때 '우유'와 가장 유사한 단어 10개 추출
#### 결과
![학습 코드2](https://user-images.githubusercontent.com/108312150/191642396-561e447b-391d-4c0a-b356-71179c003f6b.png)
영수증에서 추출한 텍스트를 유사한 단어로 치환해서 '서울우유'를 '우유'로 자동 변환하는 기능을 구현하고 싶었지만, 데이터가 부족해 학습히 원활히 이루어지지 않아 구매한 상품명은 임의로 지정함
  
## 시각화
### Qt Designer를 활용해 시스템 시각화
- 파일 : pyqt_recipes.py, recipes.ui
  - 구매한 상품명을 콤보 박스에 담음
  - 콤보 박스에서 해당 상품을 클릭하면 (해당 상품 + 상품과 가장 유사한 재료)를 자동으로 만개의 레시피에 검색하고, 레시피 제목과 url 추출
  - 목록 클릭 시 레시피 링크 자동 접속 구현
    
# 최종 결과
![홈플러스 깃에 올릴거](https://user-images.githubusercontent.com/108312150/191685290-e0197ea5-fdb9-4bf4-803e-7523199dc319.gif)

  
