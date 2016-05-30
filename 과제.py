
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
 
    print("Print 여행경보:   p1")
    print("Print 국가별 공지사항 목록조회:   p2")
    print("Print 찾는 국가 대사관 지도 url :     s")
    print("Print 찾는 국가 연락처 정보 :     c")
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
    
    for a in root.findall('body'):
        for b in a.findall('items'):
            for c in b.findall('item'):
                print('attentionNote : ', c.findtext('attentionNote'))
                print('attentionPartial : ', c.findtext('attentionPartial'))
                print('continent : ', c.findtext('continent'))
                print('controlNote : ', c.findtext('controlNote'))
                print('controlPartial : ', c.findtext('controlPartial'))
                print('countryEnName : ', c.findtext('countryEnName'))
                print('countryName : ', c.findtext('countryName'))
                print('id : ', c.findtext('id'))
                print('imgUrl1 : ', c.findtext('imgUrl'))
                print('imgUrl2 : ',c.findtext('imgUrl2'))
                print('limitaNote : ', c.findtext('limitaNote'))
                print('limitaPartial : ', c.findtext('limitaPartial'))
                print('wrtDt : ', c.findtext('wrtDt'))
                print('-------------------')
                
def Print국가별공지사항():
    
    tree = etree.parse('국가별 공지사항 목록조회.xml')
    root = tree.getroot()
    
    for a in root.findall('body'):
        for b in a.findall('items'):
            for c in b.findall('item'):
                print('title : ', c.findtext('title'))
                print('fileUrl : ', c.findtext('fileUrl'))
                print('id : ', c.findtext('id'))
                print('wrtDt : ', c.findtext('wrtDt'))
                print('-------------------')
def Print찾는나라연락처(나라이름):
#   
    tree = etree.parse('연락처정보.xml')
    
    root = tree.getroot()

    for a in root.findall('body'):
        for b in a.findall('items'):
            for c in b.findall('item'):
                if c.findtext('countryName')==나라이름:
                    print(c.findtext('contact'))
                   

                
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