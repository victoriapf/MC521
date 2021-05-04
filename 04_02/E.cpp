#include <iostream>
using namespace std;
int i,j,n,m;
int main(){
	cin>>n;
   	int volume[n],vessels[n],where[n];
	for(i=0;i<n;i++){
		cin>>volume[i];
		where[i] = i+1;
		vessels[i] = 0;
	}
	cin>>m;
	for(i=0;i<m;i++){
		int s, p, x;     
		cin>>s>>p;
   		p -= 1;
   		int newP = p;
		if (s == 1){
			cin>>x;
			while((x > 0) and (newP < n)){
               	int available = volume[newP]-vessels[newP];
               	if(x <= available){
                   	vessels[newP] += x;
                   	break;
               	}else{
                   	x -= available;
                   	vessels[newP] = volume[newP];
                   	newP = where[newP];
                }
			}
			for(j=p;j<newP;j++){
				where[j] = newP;
			}
			for(j=0;j<n;j++){
				cout << where[j];
			}
			cout << endl;
		}else{
			cout<<vessels[p]<<endl;
		}	
	}
}
