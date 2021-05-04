#include <iostream>
using namespace std;

static const int N = 2e5 + 1;
int n, m, volume[N], vessels[N], where[N];
 
int solve (int p, int x){
	int available = volume[p] - vessels[p];
	if (p > n){
		return p;
	}else if (x <= available){
		vessels[p] += x;
		return p;
	}else{
		x -= available;
		vessels[p] = volume[p];
		where[p] =  solve(where[p], x);
		return where[p];
	}
}
 
int main (){
	cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> volume[i];
		where[i] = i+1;
		vessels[i] = 0;
	}
	cin >> m;
	for (int i = 0; i < m; i++){
		int s, p, x;
		cin >> s >> p;
		if (s == 1){
			cin >> x;
			solve(p, x);
		}else if (s == 2){
			cout<<vessels[p]<<endl;
        }
	}
}
