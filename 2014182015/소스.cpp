
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
	uniform_int_distribution<> US(1, 100000);// ���� ������ ���ѹ���
	uniform_int_distribution<> UI(0,25);//���̵𷣴��� ���� ����
	dre.seed(2014182015);
	string UID;
	string ID = "ID:";
	int USC=-1;
	int FB = 0;
	float UR=0;
	int sel=0;
	int sta=0;
	int i = 0;
	//�����͸� �ҷ��´� 
	ifstream SDI("ScoreData.txt");
	//���࿡ �����ÿ� ������ ������ �����ϰ� �����Ѵ�
	using Score = pair < int, string > ;
	set<Score, greater<Score> >SData;
	map<string, int>SData2;
	Score s;
	
	if (SDI.fail()){
		ofstream SDO("ScoreData.txt");//��½� 
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

		//������ ������ �����͸� ���� set�� ������ �����Ѵ�.
		int i = 0;
		while (SDI >> s.first >> s.second){
			SData.insert(make_pair(s.first, s.second));
			SData2[s.second] = s.first;
		}
		SDI.close();
	}

	ofstream SDO("ScoreData.txt", ios::app);//��½� 
	//������� �Է��� �޾Ƽ� ������ ��ġ	
	// �԰ݿ� �Է½� �ٽ��Է��ϰ� ��������.
	while (sta != 2){
		system("cls");
	
			cout << "����� ID�� �Է����ּ���: ";
			cin >> UID;
			
			cout << "����� ������ �Է����ּ���: ";
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
		cout << "�Է��Ͻ� ������:" << UID << "->" << USC << endl;
		SData.insert(make_pair(USC, ID + UID));
	
		SData2[ID+UID] =USC;
		

		
		sta = 0;

		while (sta != 1&&sta!=2){
			auto p1 = SData.begin();
			auto p2 = SData.find(make_pair(USC, ID + UID));
			auto p3 = SData.find(make_pair(USC, ID + UID));
			FB = 0;
			cout << "1. ����ã��" << endl;
			cout << "2. ID �������� �������� ���" << endl;
			cout << "3. ������ �������� �������� ���" << endl;
			cout << "4. �� ������ �������� �յ� 10�����" << endl;
			cout << "5. ���Ͽ� �����ϰ� ������ �Է�" << endl;
			cout << "6. ����" << endl;
			cout << "�Ͻ� �۾��� �������ּ���: ";

			fflush(stdin);
			cin >> sel;
			switch (sel)
			{
			case 1://����ã��
				for (int i = 0; p1 != p2; ++p1, ++i){
					UR = i;
				}
				cout << "����� " << UR+1<< "�� �̸� ����" << ((UR+1) / SData.size() * 100) << "�ۼ�Ʈ �Դϴ�." << endl;
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