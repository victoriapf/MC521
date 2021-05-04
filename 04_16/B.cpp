#include <iostream>
using namespace std;

int n, m, l, r;
 
int main (){
    int ones = 0;
    int c;
	cin >> n >> m;
	for (int i = 0; i < n; i++){
        cin >> c;
        ones +=(c==1);
	}
    ones=min(ones,n-ones);
	for (int i = 0; i < m; i++){
		cin >> l >> r;
		c = (((r - l) + 1)%2) && ((r-l)/2< ones);
        cout<<c<<endl;
	}
}