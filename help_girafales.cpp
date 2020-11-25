#include <iostream>
#include <map>
#include <cstdlib>
using namespace std;



int main(int argc, char *argv[]) {
	int n, m, nfalsos;
	while(cin>>n && n) {
		map<string, string> mapa;
		for(int i=0;i<n;i++) { 
			string s1, s2;
			cin>>s1>>s2;
			mapa[s1] = s2;
		}
		nfalsos = 0;
		cin>>m;
		for(int i=0;i<m;i++) {
			string s1, s2;
			cin>>s1>>s2;
			s1=mapa[s1];
			int diff = abs(int(s1.size() - s2.size()));
			for(unsigned int j=0;j<min(s1.size(), s2.size());j++) { 
				if(s1[j] != s2[j])
					diff++;
			}
			if(diff>1) nfalsos++;
		}
		cout<<nfalsos<<endl;
	}
	return 0;
}

