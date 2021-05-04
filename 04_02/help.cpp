#include <iostream>
using namespace std;

static const int N = 2e5 + 1;
int n, m, volume[N], vessels[N], where[N];
 
int solve (int p, int x){
	int available = volume[p] - vessels[p];
	if (p > n)
		return p;
	if (x <= available)){
		vessels[p] += x;
		return p;
	}
	else{
		x -= available;
		vessels[p] = volume[p];
		return where[p] =  solve(where[p], x);
	}
}
 
int main (){
	cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> volume[i];
		where[i] = i + 1;
	}
	cin >> m;
	for (int i = 0; i < m; i++)
	{
		int k, p, x;
		cin >> k >> p;
		if (k == 1)
		{
			cin >> x;
			solve(p, x);
		}
		else if (k == 2)
			cout << vessels[p] << "\n";
	}
}
