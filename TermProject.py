import urllib.request
import xml.etree.ElementTree as etree
##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None

##### getdata class
class GetData:
    
    key = 'peuzoABFl3ew9WDJeae1ap8n5rlnIok9P1zH0%2FzIXXz2LM%2B8qahwkE1WckPkvD%2FET%2BZ5nN3LltIICJNplE0zvA%3D%3D'
    여행경보url = "http://apis.data.go.kr/1262000/TravelWarningService/getTravelWarningList?ServiceKey=" + key + '&numOfRows=999&pageSize=999&pageNo=1&startPage=1'
    국가별공지사항url = "http://openapi.0404.go.kr/openapi/service/CountryNoticeService/getCountryNoticeList?ServiceKey=" + key + '&numOfRows=999&pageSize=999&pageNo=1&startPage=1'
    def main(self):
        여행경보data = urllib.request.urlopen(self.여행경보url).read()        
        f = open("여행경보제도.xml","wb")
        f.write(여행경보data)
        f.close()
        
        국가별공지사항data = urllib.request.urlopen(self.국가별공지사항url).read()
        f = open("국가별 공지사항 목록조회.xml","wb")
        f.write(국가별공지사항data)
        f.close()
        
        print ("XML Document loading complete")
        
#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)") 
    print("========Menu==========")
    print("Get data:  g")
    print("Print title:   p")
    print("Print 여행경보:   p1")
    print("Print 국가별 공지사항 목록조회:   p2")
    print("Add 여행경보 Data :   a")
    print("Add 국가별 공지사항 Data :   a1")
    print("Quit program:   q")
    print("==================")
    
def launcherFunction(menu):
    global BooksDoc
    global loopFlag
    if menu ==  'g':
        getData = GetData()
        getData.main()
    elif menu == 'q':
        loopFlag = 0    
    elif menu == 'p':
        PrintTitle()
    elif menu == 'p1':
        Print여행경보()
    elif menu == 'p2':
        Print국가별공지사항()
    elif menu == 'b':
        PrintBookList(["title",])
    elif menu == 'a':
        ISBN = str(input ('insert ISBN :'))
        title = str(input ('insert Title :'))
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == 'a1':
        ISBN = str(input ('insert ISBN :'))
        title = str(input ('insert Title :'))
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == 'e':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    elif menu == 'm':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
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


############### run ###############
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")