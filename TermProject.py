# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:10:12 2016

@author: DH
"""

import urllib.request
import xml.etree.ElementTree as etree
##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None

##### getdata class
class GetData:
    페이지설정="&numOfRows=999&pageSize=999&pageNo=1&startPage=1"
    key = 'peuzoABFl3ew9WDJeae1ap8n5rlnIok9P1zH0%2FzIXXz2LM%2B8qahwkE1WckPkvD%2FET%2BZ5nN3LltIICJNplE0zvA%3D%3D'
    여행경보url = "http://apis.data.go.kr/1262000/TravelWarningService/getTravelWarningList?ServiceKey=" + key + '&numOfRows=999&pageSize=999&pageNo=1&startPage=1'+페이지설정
    국가별공지사항url = "http://openapi.0404.go.kr/openapi/service/CountryNoticeService/getCountryNoticeList?ServiceKey=" + key + 페이지설정
    연락처정보url="http://apis.data.go.kr/1262000/ContactService/getContactList?serviceKey="+key+페이지설정
    def main(self):
        여행경보data = urllib.request.urlopen(self.여행경보url).read()        
        f = open("여행경보제도.xml","wb")
        f.write(여행경보data)
        f.close()
        
        국가별공지사항data = urllib.request.urlopen(self.국가별공지사항url).read()
        f = open("국가별 공지사항 목록조회.xml","wb")
        f.write(국가별공지사항data)
        f.close()
        
        
        연락처정보data = urllib.request.urlopen(self.연락처정보url).read()        
        f = open("연락처정보.xml","wb")
        f.write(연락처정보data)
        f.close()
        print ("XML Document loading complete")
        
#### Menu  implementation
def printMenu():
    print("\n국가정보포털이용프로그램에 오신걸 환영합니다.") 
    print("========Menu==========")
    print("데이터갱신:  d")
    print("1. 여행경보:   p1")
    print("2. 국가별 공지사항 목록조회:   p2")
    print("3. 대사관 지도 url :     s")
    print("4. 비상 연락망 검색 :     c")
    print("Quit program:   q")
    print("==================")
    
def launcherFunction(menu):
    global BooksDoc
    global loopFlag

    if menu ==  'd':
        getData = GetData()
        getData.main()
    elif menu == 'q':
        loopFlag = 0    
    elif menu == 'a':
        title = str(input ('insert 제목 :'))
        fileUrl = str(input ('insert 첨부파일 경로 :'))
        id = str(input ('insert id :'))
        wrtDt = str(input ('insert 작성일 :'))
        AddBook({'제목':title, '첨부파일':fileUrl,'id':id, '작성일':wrtDt})
    elif menu == 'p1':
        Print여행경보()
    elif menu == 'p2':
        Print국가별공지사항()
    elif menu == 's':
       지역이름  = str(input ('대사관을 찾는 지역을 입력해주세요 :'))
    
       지도url(지역이름)
    elif menu == 'c':
        나라이름  = str(input ('연락처를 찾는 지역을 입력해주세요 :'))
        Print찾는나라연락처(나라이름)
    else:
        print ("error : unknow menu key")

def PrintTitle():
    
    tree = etree.parse('국가별 공지사항 목록조회.xml')
    root = tree.getroot()
    
    for a in root.findall('body'):
        for b in a.findall('items'):
            for c in b.findall('item'):
                print('title : ', c.findtext('title'))
              
def Print여행경보():
    
    tree = etree.parse('여행경보제도.xml')
    root = tree.getroot()
    
    print("------------------------------------")
    print("1. 국가명 검색")
    print("2. 여행제한지역 목록")
    print("3. 여행유의지역 목록")
    print("4. 여행자제지역 목록")
    print("종료를 원하시면 아무키나 입력해주세요")
    print("------------------------------------")
    key = str(input ('put :'))
    if key ==  '1':
        국가명  = str(input ('국가명을 입력해주세요 :'))
        
        for a in root.findall('body'):
            for b in a.findall('items'):
                for c in b.findall('item'):
                    if c.findtext('countryName')==국가명:
                        print('여행유의 내용 : ', c.findtext('attentionNote'))
                        print('여행유의(일부) : ', c.findtext('attentionPartial'))
                        print('대륙 : ', c.findtext('continent'))
                        print('여행자제 내용 : ', c.findtext('controlNote'))
                        print('여행자제(일부) : ', c.findtext('controlPartial'))
                        print('영문 국가명 : ', c.findtext('countryEnName'))
                        print('국가명 : ', c.findtext('countryName'))
                        print('id : ', c.findtext('id'))
                        print('국기 이미지 경로 : ', c.findtext('imgUrl'))
                        print('여행위험지도 경로 : ',c.findtext('imgUrl2'))
                        print('여행제한 내용 : ', c.findtext('limitaNote'))
                        print('여행제한(일부) : ', c.findtext('limitaPartial'))
                        print('등록일 : ', c.findtext('wrtDt'))
                        print('')
                        국가명 = None
        if 국가명 != None:
            print("입력한 국가의 정보가 없습니다.")
    elif key ==  '2':
        for a in root.findall('body'):
            for b in a.findall('items'):
                for c in b.findall('item'):
                    if c.findtext('limitaNote')!=None or c.findtext('limitaPartial')!=None:
                        print('대륙 : ', c.findtext('continent'))
                        print('영문 국가명 : ', c.findtext('countryEnName'))
                        print('국가명 : ', c.findtext('countryName'))
                        print('id : ', c.findtext('id'))
                        print('국기 이미지 경로 : ', c.findtext('imgUrl'))
                        print('여행위험지도 경로 : ',c.findtext('imgUrl2'))
                        print('여행제한 내용 : ', c.findtext('limitaNote'))
                        print('여행제한(일부) : ', c.findtext('limitaPartial'))
                        print('등록일 : ', c.findtext('wrtDt'))
                        print('---------------------------------------------------------')
    elif key ==  '3':
        for a in root.findall('body'):
            for b in a.findall('items'):
                for c in b.findall('item'):
                    if c.findtext('attentionNote')!=None or c.findtext('attentionPartial')!=None:
                        print('여행유의 내용 : ', c.findtext('attentionNote'))
                        print('여행유의(일부) : ', c.findtext('attentionPartial'))
                        print('대륙 : ', c.findtext('continent'))
                        print('영문 국가명 : ', c.findtext('countryEnName'))
                        print('국가명 : ', c.findtext('countryName'))
                        print('id : ', c.findtext('id'))
                        print('국기 이미지 경로 : ', c.findtext('imgUrl'))
                        print('여행위험지도 경로 : ',c.findtext('imgUrl2'))
                        print('등록일 : ', c.findtext('wrtDt'))
                        print('---------------------------------------------------------')
    elif key ==  '4':
        for a in root.findall('body'):
            for b in a.findall('items'):
                for c in b.findall('item'):
                    if c.findtext('controlNote')!=None or c.findtext('controlPartial')!=None:
                        print('대륙 : ', c.findtext('continent'))
                        print('여행자제 내용 : ', c.findtext('controlNote'))
                        print('여행자제(일부) : ', c.findtext('controlPartial'))
                        print('영문 국가명 : ', c.findtext('countryEnName'))
                        print('국가명 : ', c.findtext('countryName'))
                        print('id : ', c.findtext('id'))
                        print('국기 이미지 경로 : ', c.findtext('imgUrl'))
                        print('여행위험지도 경로 : ',c.findtext('imgUrl2'))
                        print('등록일 : ', c.findtext('wrtDt'))
                        print('---------------------------------------------------------')
    else:
        print("잘못입력하셨습니다.")
    
                
def Print국가별공지사항():
    tree = etree.parse('국가별 공지사항 목록조회.xml')
    root = tree.getroot()
    
    for a in root.findall('body'):
        for b in a.findall('items'):
            for c in b.findall('item'):
                print("---------------------------------------------------------")
                print('제목 : ', c.findtext('title'))
                print('작성일 : ', c.findtext('wrtDt'))
                
    print("------------------------------------")
    print("제목으로 상세 검색을 원하시면 1을")
    print("종료를 원하시면 아무키나 입력해주세요")
    print("------------------------------------")
    key = str(input ('put :'))
    if key ==  '1':
        제목  = str(input ('제목을 입력해주세요 :'))
        
        for a in root.findall('body'):
            for b in a.findall('items'):
                for c in b.findall('item'):
                    if c.findtext('title')==제목:
                        print('제목 : ', c.findtext('title'))
                        print('첨부파일 경로 : ', c.findtext('fileUrl'))
                        print('id : ', c.findtext('id'))
                        print('작성일 : ', c.findtext('wrtDt'))
                        print('')
                        제목 = None
        if 제목 != None:
            print("제목 입력 오류")
    else:
        print("공지사항 검색 종료")
def Print찾는나라연락처(나라이름):
#   
    tree = etree.parse('연락처정보.xml')
    
    root = tree.getroot()

    for a in root.findall('body'):
        for b in a.findall('items'):
            for c in b.findall('item'):
                if c.findtext('countryName')==나라이름:
                    print(c.findtext('contact'))
                    나라이름 = None
    if 나라이름 != None:
        print("해당 국가의 정보가 없습니다.")
                   

                
def 지도url(지역):
    url= 'https://www.google.co.kr/maps/search/주+'+지역+'+대한민국+대사관'
    print(url)

############### run ###############
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")
