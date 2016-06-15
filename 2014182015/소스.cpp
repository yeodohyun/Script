
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<random>
#include<iostream>
#include<fstream>
#include<functional>
using namespace std;

int main(){
	default_random_engine dre;
	uniform_int_distribution<> US(1, 100000);// 점수 랜덤을 위한범위
	uniform_int_distribution<> UI(0,25);//아이디랜덤을 위한 범위
	dre.seed(2014182015);
	string UID;
	string ID = "ID:";
	int USC=-1;
	int FB = 0;
	float UR=0;
	int sel=0;
	int sta=0;
	int i = 0;
	//데이터를 불러온다 
	ifstream SDI("ScoreData.txt");
	//만약에 없을시에 데이터 만개를 생성하고 저장한다
	using Score = pair < int, string > ;
	set<Score, greater<Score> >SData;
	map<string, int>SData2;
	Score s;
	
	if (SDI.fail()){
		ofstream SDO("ScoreData.txt");//출력시 
		while (i < 10000){
			SData.insert(make_pair(US(dre), ID + char(UI(dre) + 65) + char(UI(dre) + 65) + char(UI(dre) + 65)));

			++i;

		}
		for (auto d : SData){
			SData2[d.second] = d.first;
			SDO << d.first << " ";
			SDO << d.second << " ";
		}
		SDO.close();
		SDI.close();

	}
	else{

		//파일이 있으면 데이터를 각각 set과 맵으로 저장한다.
		int i = 0;
		while (SDI >> s.first >> s.second){
			SData.insert(make_pair(s.first, s.second));
			SData2[s.second] = s.first;
		}
		SDI.close();
	}

	ofstream SDO("ScoreData.txt", ios::app);//출력시 
	//사용자의 입력을 받아서 현재의 위치	
	// 규격외 입력시 다시입력하게 만들어야함.
	while (sta != 2){
		system("cls");
	
			cout << "당신의 ID를 입력해주세요: ";
			cin >> UID;
			
			cout << "당신의 점수를 입력해주세요: ";
			cin >> USC;
		/*	try{
				if (USC > 10000 || USC < 0)
					throw 10;
				else
					throw "eror";
			}
			catch(int exp){
				goto base;
			}
			catch(string exp){
				goto base;
			}*/
		cout << "입력하신 정보는:" << UID << "->" << USC << endl;
		SData.insert(make_pair(USC, ID + UID));
	
		SData2[ID+UID] =USC;
		

		
		sta = 0;

		while (sta != 1&&sta!=2){
			auto p1 = SData.begin();
			auto p2 = SData.find(make_pair(USC, ID + UID));
			auto p3 = SData.find(make_pair(USC, ID + UID));
			FB = 0;
			cout << "1. 순위찾기" << endl;
			cout << "2. ID 기준정렬 오름차순 출력" << endl;
			cout << "3. 점수를 기준으로 내림차순 출력" << endl;
			cout << "4. 내 점수를 기준으로 앞뒤 10개출력" << endl;
			cout << "5. 파일에 저장하고 새점수 입력" << endl;
			cout << "6. 종료" << endl;
			cout << "하실 작업을 선택해주세요: ";

			fflush(stdin);
			cin >> sel;
			switch (sel)
			{
			case 1://순위찾기
				for (int i = 0; p1 != p2; ++p1, ++i){
					UR = i;
				}
				cout << "당신은 " << UR+1<< "등 이며 상위" << ((UR+1) / SData.size() * 100) << "퍼센트 입니다." << endl;
				break;
			case 2:
				for (auto d : SData2)
					cout << d.first << "-->" << d.second << endl;
				break;
			case 3:
				for (auto d : SData)
					cout << d.second << "-->" << d.first << endl;
				break;
			case 4:
				
				for (; FB < 10&&p3!=SData.begin(); ){
					++FB;
					--p3;
				}
				cout << FB << endl;
				for (int c=0; c < FB+10&&p3!=SData.end(); ++c,++p3){
					
					cout << p3->second << "-->" << p3->first << endl;
				}
				cout << FB << endl;
				break;
			case 5:
				
				SDO << p2->first<< " ";
				SDO << p2->second << " ";
				sta = 1;
				break;
			case 6:

				SDO << p2->first << " ";
				SDO << p2->second << " ";
				sta = 2;
				break;
			


			}
		}

	}
	//

}