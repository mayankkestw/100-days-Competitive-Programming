#include<iostream>
#include<map>
#include<iterator>

using namespace std;

int main(){

	int n1,n2,n3,temp,nTotal,count=0;
	std::map<int, int> map1;
	std::map<int, int>::iterator it;
	cin>>n1>>n2>>n3;
	nTotal=n1+n2+n3;
	for (int i = 0; i < nTotal; ++i)
	{
		 cin>>temp;
		 map1[temp]++;
		 if(map1[temp]==2)count++;
	}
	cout<<count<<endl;
	for(it=map1.begin();it!= map1.end();++it)
	{
		if(it->second >=2){cout<<it->first<<endl;}
	}


	return 0;
}
